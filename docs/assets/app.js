(function(){
  var root=document.documentElement;
  root.classList.add('js');
  function get(k){try{return localStorage.getItem(k)}catch(e){return null}}
  function set(k,v){try{localStorage.setItem(k,v)}catch(e){}}
  function esc(t){return t.replace(/&/g,'&amp;').replace(/</g,'&lt;').replace(/>/g,'&gt;')}
  function each(sel,fn,ctx){[].slice.call((ctx||document).querySelectorAll(sel)).forEach(fn)}

  // ---- Theme ----
  var btn=document.getElementById('theme');
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
      root.setAttribute('data-theme',n);set('theme',n);label();
    });
  }

  // ---- Licence switch: remembers Chat / Premium and hides the other track ----
  var sw=document.getElementById('tierswitch');
  function applyTier(t){
    if(t==='chat'||t==='premium')root.setAttribute('data-tier',t);else root.removeAttribute('data-tier');
    if(sw)each('button',function(b){b.setAttribute('aria-pressed',String(b.getAttribute('data-t')===(t||'both')))},sw);
    if(window.__recount)window.__recount();
  }
  function setTier(t){set('tier',t);applyTier(t)}
  if(sw){
    sw.hidden=false;
    sw.addEventListener('click',function(e){
      var b=e.target.closest('button[data-t]');if(!b)return;
      setTier(b.getAttribute('data-t'));
      var n=document.getElementById('tiernote');if(n)n.remove();
    });
  }
  applyTier(get('tier'));
  // A link into the other licence's section still has to land somewhere.
  function reveal(){
    var id=decodeURIComponent(location.hash.slice(1));if(!id)return;
    var el=document.getElementById(id);if(!el)return;
    var sec=el.closest('[data-tier]');
    var t=root.getAttribute('data-tier');
    if(sec&&t&&sec.getAttribute('data-tier')!==t){
      applyTier('both');
      if(!document.getElementById('tiernote')){
        var n=document.createElement('p');n.id='tiernote';n.className='tiernote';
        n.textContent='This link goes to the '+(sec.getAttribute('data-tier')==='chat'?'Chat':'Premium')+' section, so both licences are showing on this page. Your saved choice has not changed.';
        var art=document.querySelector('article');if(art)art.insertBefore(n,art.firstChild);
      }
      el.scrollIntoView();
    }
  }
  reveal();window.addEventListener('hashchange',reveal);

  // ---- Prompt boxes: fill in the blanks, then copy ----
  var n=0;
  each('.promptbox',function(box){
    var pre=box.querySelector('pre');if(!pre)return;
    var tpl=pre.textContent,re=/\[([^\]\n]{1,90})\]/g,names=[],m,vals={};
    while((m=re.exec(tpl))){if(names.indexOf(m[1])<0)names.push(m[1])}
    function render(){
      var out='',last=0;
      tpl.replace(re,function(all,name,idx){
        out+=esc(tpl.slice(last,idx));
        out+=vals[name]?'<mark class="filled">'+esc(vals[name])+'</mark>':'<span class="ph">['+esc(name)+']</span>';
        last=idx+all.length;return all;
      });
      pre.innerHTML=out+esc(tpl.slice(last));
    }
    if(names.length){
      render();
      var det=document.createElement('details');det.className='fill';
      var sum=document.createElement('summary');sum.textContent='Fill in the blanks ('+names.length+')';det.appendChild(sum);
      var f=document.createElement('div');f.className='fields';
      names.forEach(function(name){
        var id='f'+(++n),big=/^paste|^describe|^attach/i.test(name);
        var wrap=document.createElement('div');if(big)wrap.className='wide';
        var lab=document.createElement('label');lab.setAttribute('for',id);lab.textContent=name;
        var inp=document.createElement(big?'textarea':'input');inp.id=id;
        if(!big){
          inp.type='text';
          var opts=name.split(' / ');
          if(opts.length>1){
            var dl=document.createElement('datalist');dl.id=id+'l';
            opts.forEach(function(o){var op=document.createElement('option');op.value=o.replace(/^(who|e\.g\.): /,'');dl.appendChild(op)});
            wrap.appendChild(dl);inp.setAttribute('list',dl.id);inp.placeholder='Pick or type your own';
          }else if(/^\d+$/.test(name)){inp.placeholder=name;inp.inputMode='numeric'}
        }
        inp.addEventListener('input',function(){vals[name]=inp.value.trim();render()});
        wrap.appendChild(lab);wrap.appendChild(inp);f.appendChild(wrap);
      });
      det.appendChild(f);box.appendChild(det);
    }
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

  // ---- Filters: any <input class="filter" data-target="selector"> ----
  each('input.filter',function(inp){
    var sel=inp.getAttribute('data-target'),cat='';
    var count=document.getElementById('libcount'),chips=document.getElementById('libcats');
    function run(){
      var q=inp.value.toLowerCase().trim().split(/\s+/),shown=0;
      each(sel,function(el){
        var t=el.textContent.toLowerCase();
        var ok=q.every(function(w){return t.indexOf(w)>-1})&&(!cat||el.getAttribute('data-cat')===cat);
        el.hidden=!ok;
        if(ok&&el.offsetParent!==null)shown++;
      });
      if(count&&sel==='.pitem')count.textContent=shown+' prompt'+(shown===1?'':'s');
    }
    if(chips&&sel==='.pitem'){
      var cats=[];each(sel,function(el){var c=el.getAttribute('data-cat');if(c&&cats.indexOf(c)<0)cats.push(c)});
      ['All'].concat(cats).forEach(function(c){
        var b=document.createElement('button');b.type='button';b.textContent=c;
        b.setAttribute('aria-pressed',String(c==='All'));
        b.addEventListener('click',function(){
          cat=c==='All'?'':c;
          each('button',function(x){x.setAttribute('aria-pressed',String(x===b))},chips);run();
        });
        chips.appendChild(b);
      });
      chips.hidden=false;window.__recount=run;
    }
    inp.addEventListener('input',run);run();
  });

  // ---- Checklists that remember (5-day challenge) ----
  var boxes=[].slice.call(document.querySelectorAll('input[type=checkbox][data-save]'));
  if(boxes.length){
    var done={};try{done=JSON.parse(get('done')||'{}')}catch(e){}
    var prog=document.getElementById('progress');
    function tally(){
      var c=boxes.filter(function(b){return b.checked}).length;
      if(prog)prog.textContent=c+' of '+boxes.length+' done'+(c===boxes.length?'. You have finished the challenge.':'');
    }
    boxes.forEach(function(b){
      b.checked=!!done[b.getAttribute('data-save')];
      b.addEventListener('change',function(){done[b.getAttribute('data-save')]=b.checked;set('done',JSON.stringify(done));tally()});
    });
    tally();
  }

  // ---- TOC highlight ----
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

  // ---- Licence picker: reads the label, sets the switch ----
  var tree=document.getElementById('tree');
  if(tree){
    var base=tree.getAttribute('data-base')||'';
    var nodes={
      start:{q:'What does the label under your name say at copilot.cloud.microsoft?',o:[
        ['Copilot Chat (Basic)','basic'],
        ['M365 Copilot (Basic)','m365basic'],
        ['M365 Copilot (Premium)','premium'],
        ['I can’t tell, or I don’t see a label','unknown']]},
      basic:{t:'chat',r:'<p><strong>You are on the Chat track.</strong> This site now shows you the Chat routes only. Copilot answers from the web and from whatever you paste, upload or have open. That is more than it sounds.</p><p><a class="btn" href="playbooks/">Pick a job to do</a> <a class="btn ghost" href="what-is-copilot/">What my licence can do</a></p>'},
      m365basic:{t:'chat',r:'<p><strong>You are on the Chat track.</strong> This site now shows you the Chat routes only. Microsoft says your label also has standard access to Copilot inside Word, Excel, PowerPoint and OneNote, so look for the Copilot button there.</p><p><a class="btn" href="playbooks/">Pick a job to do</a> <a class="btn ghost" href="what-is-copilot/">What my licence can do</a></p>'},
      premium:{t:'premium',r:'<p><strong>You are on the Premium track.</strong> This site now shows you the Premium routes only. Copilot can reach your emails, files, meetings and chats, within what you can already open.</p><p><a class="btn" href="playbooks/">Pick a job to do</a> <a class="btn ghost" href="what-is-copilot/">What my licence can do</a></p>'},
      unknown:{r:'<p><strong>Check your sign-in first.</strong> Go to <code>copilot.cloud.microsoft</code> and sign in with your <em>work</em> account. Look for the word “Work” under your name and the green shield. Still no label? Open <a href="https://aka.ms/CopilotLicenseDetails">Microsoft’s licence details page</a>, or see <a href="troubleshooting/#account">Fix it</a>.</p>'}
    };
    function show(id){
      var nd=nodes[id],h='';
      if(nd.q){
        h='<h2 id="tree-q" tabindex="-1">'+nd.q+'</h2><div class="opts">';
        nd.o.forEach(function(o){h+='<button type="button" data-n="'+o[1]+'">'+o[0]+'</button>'});
        h+='</div>';
      }else{
        if(nd.t)setTier(nd.t);
        h='<div class="result" id="tree-q" tabindex="-1">'+nd.r.replace(/href="(?!http)/g,'href="'+base)+'</div><button type="button" class="restart" data-n="start">Change my answer</button>';
      }
      tree.innerHTML=h;
      if(tree.getAttribute('data-moved')){var f=document.getElementById('tree-q');if(f)f.focus()}
    }
    tree.addEventListener('click',function(e){
      var b=e.target.closest('button[data-n]');if(!b)return;
      tree.setAttribute('data-moved','1');show(b.getAttribute('data-n'));
    });
    var saved=get('tier');
    if(saved==='chat'||saved==='premium'){
      tree.innerHTML='<div class="result"><p><strong>You are on the '+(saved==='chat'?'Chat':'Premium')+' track.</strong> Change it any time with the <em>My licence</em> switch at the top.</p></div><button type="button" class="restart" data-n="start">Check my label again</button>';
    }else show('start');
  }
})();
