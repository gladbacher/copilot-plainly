(function(){
  var root=document.documentElement;
  root.classList.add('js');

  // Theme toggle (remembered per browser; works without storage)
  var btn=document.getElementById('theme');
  function stored(){try{return localStorage.getItem('theme')}catch(e){return null}}
  function save(v){try{localStorage.setItem('theme',v)}catch(e){}}
  var t=stored();
  if(t==='light'||t==='dark'){root.setAttribute('data-theme',t)}
  function current(){
    var a=root.getAttribute('data-theme');
    if(a)return a;
    return window.matchMedia&&matchMedia('(prefers-color-scheme: dark)').matches?'dark':'light';
  }
  function label(){if(btn)btn.textContent=current()==='dark'?'Light mode':'Dark mode'}
  if(btn){
    label();
    btn.addEventListener('click',function(){
      var n=current()==='dark'?'light':'dark';
      root.setAttribute('data-theme',n);save(n);label();
    });
  }

  // Copy buttons on prompt boxes
  document.querySelectorAll('.promptbox').forEach(function(box){
    var pre=box.querySelector('pre');if(!pre)return;
    var b=document.createElement('button');
    b.type='button';b.className='copy';b.textContent='Copy';
    b.setAttribute('aria-label','Copy this prompt');
    b.addEventListener('click',function(){
      var text=pre.innerText;
      function ok(){b.textContent='Copied';setTimeout(function(){b.textContent='Copy'},1600)}
      function fallback(){
        var ta=document.createElement('textarea');ta.value=text;ta.style.position='fixed';ta.style.opacity='0';
        document.body.appendChild(ta);ta.select();
        try{document.execCommand('copy');ok()}catch(e){b.textContent='Press Ctrl/Cmd+C'}
        document.body.removeChild(ta);
      }
      if(navigator.clipboard&&navigator.clipboard.writeText){navigator.clipboard.writeText(text).then(ok,fallback)}else{fallback()}
    });
    box.appendChild(b);
  });

  // TOC highlight
  var links=[].slice.call(document.querySelectorAll('.toc a'));
  if(links.length&&'IntersectionObserver' in window){
    var map={};links.forEach(function(a){map[a.getAttribute('href').slice(1)]=a});
    var io=new IntersectionObserver(function(es){
      es.forEach(function(e){
        if(e.isIntersecting){links.forEach(function(l){l.classList.remove('on')});var a=map[e.target.id];if(a)a.classList.add('on')}
      });
    },{rootMargin:'-20% 0px -70% 0px'});
    Object.keys(map).forEach(function(id){var el=document.getElementById(id);if(el)io.observe(el)});
  }

  // Decision tree (data-tree on a container; the no-JS fallback is the list inside .nojs)
  var tree=document.getElementById('tree');
  if(tree){
    var nodes={
      start:{q:'What shows under your name at copilot.cloud.microsoft?',o:[
        ['Copilot Chat (Basic)','basic'],
        ['M365 Copilot (Basic)','m365basic'],
        ['M365 Copilot (Premium)','premium'],
        ['I can’t tell, or I don’t see a label','unknown']]},
      basic:{r:'<p><strong>You have the free chat.</strong> It answers from the web. It can use a work file only if you upload or paste it, or if you open it alongside Outlook or Teams.</p><p>Read <a href="copilot-chat/">Copilot Chat</a> next, then <a href="prompts/">the prompt library</a>.</p>'},
      m365basic:{r:'<p><strong>You have standard access inside some apps.</strong> That covers Word, Excel, PowerPoint and OneNote, but not automatic access to your emails, meetings and files. Capacity can vary through the day.</p><p>Read <a href="what-is-copilot/">what each tier gives you</a>, then <a href="copilot-chat/">Copilot Chat</a>.</p>'},
      premium:{r:'<p><strong>You have the full add-on.</strong> Copilot can reach your work data automatically through Microsoft Graph, within what you are already allowed to see.</p><p>Read <a href="safety/">Safety</a> first, then <a href="prompts/">the prompt library</a>.</p>'},
      unknown:{r:'<p><strong>Check your sign-in first.</strong> Go to <code>copilot.cloud.microsoft</code> and sign in with your <em>work</em> account. Look for the word “Work” under your name and the green shield. If you still see no label, ask IT which licence you have.</p><p>See <a href="start/">Start here</a> or <a href="troubleshooting/">Troubleshooting</a>.</p>'}
    };
    var base=tree.getAttribute('data-base')||'';
    function show(id){
      var n=nodes[id];var h='';
      if(n.q){
        h='<h2 id="tree-q" tabindex="-1">'+n.q+'</h2><div class="opts">';
        n.o.forEach(function(o){h+='<button type="button" data-n="'+o[1]+'">'+o[0]+'</button>'});
        h+='</div>';
      }else{
        h='<div class="result" id="tree-q" tabindex="-1">'+n.r.replace(/href="/g,'href="'+base)+'</div><button type="button" class="restart" data-n="start">Start again</button>';
      }
      tree.innerHTML=h;
      if(id!=='start'||tree.getAttribute('data-moved')){var f=document.getElementById('tree-q');if(f)f.focus()}
    }
    tree.addEventListener('click',function(e){
      var b=e.target.closest('button[data-n]');if(!b)return;
      tree.setAttribute('data-moved','1');show(b.getAttribute('data-n'));
    });
    show('start');
  }
})();
