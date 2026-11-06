# Research 04: agents (retrieved 2026-11-06; Microsoft Learn / Support / microsoft.com only)

Style as 01-03: URL + date shown + what was claimed. "Not stated" means I read the page and it does not say. Copilot Studio is out of scope beyond one line (see end).
Several fetches were summarised by the fetch tool rather than read raw; where a number matters (limits, prices) re-check on the page before publishing.

## Sources (letters continue the site's reference list; date = date shown on page)
- o  Learn, What is Microsoft Copilot? ms.date 2026-11-05 https://learn.microsoft.com/en-us/microsoft-365/copilot/microsoft-365-copilot-overview
- ac Learn, Set up your development environment for a Microsoft 365 Copilot plugin (holds "Agent capabilities and licensing models" table) ms.date 2026-09-30 https://learn.microsoft.com/en-us/microsoft-365/copilot/extensibility/prerequisites
- y  Learn, Agent Builder overview, ms.date 2026-10-26 https://learn.microsoft.com/en-us/microsoft-365/copilot/extensibility/agent-builder
- z  Learn, Build agents in Agent Builder, ms.date 2026-10-26 https://learn.microsoft.com/en-us/microsoft-365/copilot/extensibility/agent-builder-build-agents
- aa Learn, Add knowledge sources to an agent in Agent Builder, ms.date 2026-09-30 https://learn.microsoft.com/en-us/microsoft-365/copilot/extensibility/agent-builder-add-knowledge
- ab Learn, Share and manage agents built in Agent Builder, ms.date 2026-11-06 https://learn.microsoft.com/en-us/microsoft-365/copilot/extensibility/agent-builder-share-manage-agents
- ai Support, Create an agent in SharePoint, no date (c. 2026) https://support.microsoft.com/en-us/sharepoint/copilot-in-sharepoint/create-an-agent-in-sharepoint
- aj Support, Get started with agents in SharePoint, no date https://support.microsoft.com/en-us/office/get-started-with-sharepoint-agents-69e2faf9-2c1e-4baa-8305-23e625021bcf
- ak Support, Manage agents in SharePoint, no date https://support.microsoft.com/en-us/office/manage-agents-in-sharepoint-bcab837a-835c-4a1a-8ad4-d53a353c369f
- al Support, Use an agent created in SharePoint in Microsoft Copilot app, no date https://support.microsoft.com/en-us/sharepoint/copilot-in-sharepoint/use-an-agent-created-in-sharepoint-in-microsoft-365-copilot-chat
- am Support, Get started with agents in the Microsoft Copilot app, no date https://support.microsoft.com/en-us/microsoft-365-copilot/get-started-with-agents-in-the-microsoft-365-copilot-app
- an Support, Get more agents in the Microsoft Copilot app, no date https://support.microsoft.com/en-us/Microsoft-365-Copilot/get-more-agents-in-the-microsoft-365-copilot-app
- ao Support, Build your own agent with Microsoft Copilot, no date https://support.microsoft.com/en-us/microsoft-365-copilot/build-your-own-agent-with-microsoft-365-copilot
- ag Learn, Agent Store in Microsoft Copilot, ms.date 2026-04-17 https://learn.microsoft.com/en-us/copilot/manage/copilot-agent-store
- ah Learn, Agents admin guide for Microsoft 365, ms.date 2026-04-07 (updated 2026-10-31) https://learn.microsoft.com/en-us/microsoft-365/copilot/agent-essentials/m365-agents-admin-guide
- ad Learn, Manage agents in the Microsoft 365 admin center, ms.date 2026-07-09 https://learn.microsoft.com/en-us/microsoft-agent-365/admin/manage-copilot-agents-integrated-apps
- ae Learn, Set up Microsoft Copilot pay-as-you-go services, ms.date 2026-07-17 https://learn.microsoft.com/en-us/microsoft-365/copilot/pay-as-you-go/setup
- af Learn, Use capacity packs vs pay-as-you-go billing for Copilot Chat, ms.date 2026-04-29 https://learn.microsoft.com/en-us/microsoft-365/copilot/pay-as-you-go/copilot-capacity-packs
- u  Learn, Researcher agent, ms.date 2026-02-19 (updated 2026-11-04) https://learn.microsoft.com/en-us/microsoft-365/copilot/researcher-agent
- v  Support, Get started with Researcher, no date https://support.microsoft.com/en-us/microsoft-365-copilot/get-started-with-researcher-in-microsoft-365-copilot
- x  Support, Agents built by Microsoft, no date https://support.microsoft.com/en-us/microsoft-365-copilot/agents-built-by-microsoft
- ar Support, How Copilot Chat works with and without a Microsoft Copilot license, no date https://support.microsoft.com/en-us/microsoft-365-copilot/how-copilot-chat-works-with-and-without-a-microsoft-365-copilot-license
- ap Learn, Data, privacy and security for Microsoft Copilot, ms.date 2026-07-09 (updated 2026-11-04) https://learn.microsoft.com/en-us/microsoft-365/copilot/microsoft-365-copilot-privacy
- w  Learn, Release notes for Microsoft 365 Copilot, latest entry 2026-11-04 https://learn.microsoft.com/en-us/microsoft-365/copilot/release-notes

## 1. Who gets what: the tier split (ac, o, ah, ar)
Source ac has the clearest table ("Agent capabilities and licensing models"). Three columns:
| Capability | Copilot Chat, no usage billing | Copilot Chat + usage billing (pay-as-you-go) | Licensed |
| Custom instructions, code interpreter, image generator, custom actions, web search, scoped web search | yes | yes | yes |
| Knowledge: Copilot connectors, SharePoint, embedded files, Dataverse | NO | yes | yes |
| Knowledge: Email, People, Teams messages, Teams meetings | NO | NO | yes |
- Footnote: usage limits apply to all included features; no cost for knowledge sources already available without usage billing.
- Licensed includes Copilot Business and E7 "where applicable" (ac).
- Copilot Chat users "have access to agents ... grounded on instructions or the web" (ac); o says "Declarative agents that are grounded in instructions and public websites are included with Copilot Chat. Access to custom or other agents is pay-as-you-go only."
- Support comparison (ar): without a licence agents are "Limited (no advanced agents)"; with one "Extensive use (including advanced agents like Researcher, Analyst, and custom agents)". Copilot Studio: "Pay-as-you-go" vs "Included".
- ah: "Agents utilizing metered consumption are off by default for users in Microsoft Copilot Chat." Agents on shared tenant data (SharePoint, Graph connector content) are metered. No-cost agents still need the admin to enable them.
- Gov clouds (GCC/GCCH/DoD): usage-based billing and agents grounded in shared tenant work data not available (ac).
- Basic, M365 Basic, Premium split for the apps themselves: see 05-reverification.md.

## 2. Agent Builder (y, z, aa, ab, ao)
**Where:** "New agent" in the Microsoft Copilot app (Agents area); builds from microsoft365.com/chat, office.com/chat and the Teams desktop/web client. Available on Work and Web options. Not on mobile (y).
**Licence:** y says access "and the capabilities you can add ... depend on the licenses assigned in your tenant". ah (2026-04-07) says: "Agent Builder is available to users with a Microsoft 365 Copilot license or in tenants with pay-as-you-go enabled for Copilot Studio." ac says Copilot Chat (no usage billing) users can have declarative agents with instructions + web only. I COULDN'T CONFIRM from one page whether an unlicensed Copilot Chat user in a tenant WITHOUT pay-as-you-go can open Agent Builder at all. ac says "build and test agents for Microsoft 365 Copilot Chat, with limited capabilities" with a plain M365 Business Basic subscription, which points to yes (web/instructions only), but ah reads the other way. Write it as "depends on your organisation; check".
**Three ways to start (z):** (1) Describe (natural language, "recommended"), (2) "Skip to configure" (manual Configure tab), (3) templates.
- Describe: you chat; name, description, instructions, knowledge, suggested prompts are filled in for you and visible on Configure. Adds sources for you (e.g. "My emails"); code interpreter/image generator on automatically. Plus (+) in chat box: add work content, upload, attach cloud files. Natural-language only works in listed languages; otherwise use Configure (z).
- Configure fields and limits (z): Name 30 characters; Description 1,000 characters (also what the LLM uses to decide when to use the agent, and shown to users); Instructions 8,000 characters; Icon (generate/library/upload; PNG, 192x192 px, 1 MB); Model = default response mode Auto / Quick response / Think deeper (users can override); Knowledge; Starter prompts (name + description each; "no minimum number"; I did not see a maximum).
- Capabilities toggles: "Create documents, charts, and code" (code interpreter), "Create images" (image generator). Skills can be added (separate page, not read).
- No external actions in Agent Builder: copy to Copilot Studio for that (y, z).
**Knowledge sources and limits (aa), per agent:** public website URLs 4 (max two path levels, no query strings); SharePoint files/folders/sites 100 files; SharePoint lists 1 (list max 20,000 rows / 50 MB text, attachments column not used; selecting a site does NOT include its lists); OneDrive files 50; Teams chats and meetings 5 chats + 5 meetings (or "My Teams chats and meetings" for all); uploaded files from device 20 (docx/pdf/pptx/txt etc. 512 MB each, xlsx/xls 30 MB; folders not allowed; no password-protected, double-key-encrypted or user-defined-permission labelled files; not in GCC); Copilot connectors no documented limit, admin must enable; Dynamics/Power Apps needs admin to enable "Business Applications in Work IQ". "Search all websites" toggle for general web. "Only use specified sources" prioritises your sources but does NOT block general AI knowledge. Email knowledge is your whole mailbox, can't be scoped, and people you share with don't get your email. People data on by default for licensed creators. New SharePoint/OneDrive files show "Preparing" for up to several minutes. Excel works best with data on one sheet. Restricted SharePoint Search on => SharePoint can't be a source.
**Test/preview (z):** the "Try it" tab (not called "preview"). Enabled once the agent has a name, description and instructions. Updates as you edit. Can't share prompts, give feedback or @mention other agents inside Try it; those work after creation.
**Create / sharing (ab):** select Create; agent starts private. Share dialog: roles "Can edit" (owner: edit, share, manage) and "Can chat". Groups can only be "Can chat"; owners must be individuals. Copy chat link / edit link. "Org-wide sharing for chat access" toggle; when on, others in the tenant "can see the agent in the Agent Store". Admin can set who may share: All users (default) / Specific users or groups / No users. Policy changes apply to new sharing only. If sharing is restricted, an admin must approve and deploy the agent. Shared users need the licence type the agent's capabilities need, otherwise "attempts to use the agent might result in an error".
**SharePoint knowledge and sharing (ab, y):** agent respects each user's own permissions and sensitivity labels; if the user can't see a file the agent leaves it out. Auto-sharing of files to people you share with only works for specific security groups, not "everyone in the organization" (y). Removing someone from the agent doesn't remove their file access.
**Edit / versioning / delete (ab):** any owner can edit (pencil in the "..." menu, via All agents or New agent > View all agents). "Changes made to agents are saved automatically. However, your changes aren't visible to users until you ... choose Update". Updates may take minutes. I found NO version history / rollback described. Re-share after updating if SharePoint sources changed. Delete: any owner; "permanent and can't be reversed"; gone for other owners and shared users. Admins can reassign ownership (also PowerShell).
**About this agent (ab):** short description (required, 80 chars), creator website, privacy statement and terms links (HTTPS, 2,048 chars each).
**Org catalogue (ab):** owner can "Submit to your org catalog"; an admin reviews in the admin centre and, if approved, deploys it to "Built by your org" in the Agent Store. The shared version and the Store version are managed separately.
**Known limitations (y):** can't use Agent Builder agents in Teams group or 1:1 chats; no customer-managed keys; if admin turns off "Allow web search in Copilot", web is blocked even though the Web content toggle still looks on; sharing doesn't give org-wide deployment or other channels (that is Copilot Studio).
**Data (y):** processed by Copilot Studio services; doesn't use the tenant's Dataverse storage entitlement. Embedded uploaded files are stored in the tenant's default geography, not the user's preferred data location (aa). Anyone who can use the agent can see answers grounded in embedded files; Purview Information Barriers not supported on embedded files (aa).
**Support page (ao):** simple walkthrough: Agents > New Agent > describe > Send, or pick a template > Configure > Create. "Feature availability can vary by account type and license."

## 3. SharePoint agents (ai, aj, ak, al, ae, w)
- Create: open a library or list > Copilot > "Create an agent" (scope starts as that library/list), or select files/folders > right-click "Create an agent". Needs a Microsoft Copilot licence OR a tenant with pay-as-you-go for agents in SharePoint, PLUS edit permission on the site (ai, aj). Agent only uses content you already have access to.
- Editors can change scope (add other sites), branding/identity, prompts (aj).
- Default site agent: aj says "Every site comes with Copilot in SharePoint ... the upgrade to the ready-made site agent"; users need a Copilot licence for it; "Upgrades to agents in SharePoint are coming in mid-November 2026" (i.e. not yet). ak: site owners pick the site's "main agent" in Settings (gear) > Site AI; if unchanged, Copilot is the default; it opens from the Agent icon in the site header. The site's own Copilot in SharePoint can't be shared; only custom-built agents can (copy link from the chat pane) (aj).
- Permissions (ak): "All site members can create agents. Members with edit permissions can use, edit, or share them ... and delete agent files." Approval not required; agents are not auto-published. Agents are `.agent` files in the site's document libraries; delete = delete the file (ellipsis > Delete). Copilot Studio-published agents appear under Documents > Copilot Studio Agents.
- Using in the Copilot app (al): after you use a SharePoint agent (in SharePoint, a Teams group chat/meeting, or via link) it appears under Agents in the left nav; only recently used ones, no browse-all. Pin icon pins to top. Edit via ellipsis (disabled without permission). Share/Get link uses the file sharing dialog. Past SharePoint chat context doesn't carry over.
- Billing: SharePoint agents are a separate pay-as-you-go service from Copilot Chat (ae). Copilot credit policies/capacity packs are Copilot Chat only; SharePoint agents still need pay-as-you-go (af). The Agent Builder-style licence table (ac) says for SharePoint knowledge the billing policy must be connected to the SharePoint agents service and users must be in the assigned security group.
- New 2026-11-04 (w): "SharePoint list agent" (creates Microsoft Lists from prompts). After 1 Nov 2026 the old PowerShell opt-in/out is going; availability is managed with Site AI settings (from a search summary, not verified on the fetched pages: treat as unclear).
- Q&A forum threads disagree on whether approval is needed for a default agent; not used here.

## 4. Finding agents: Agent Store, All agents, Agents pane, @-mention, pinning (am, an, ag, ah, ad)
- Agents pane: left navigation > Agents; chevron expands pre-installed agents. "All agents" opens the Agent Store. In the store: Add or Open. Agents work in both Work and Web tabs (am). A colleague can also send a link.
- Some agents need IT approval: you see "Request approval" instead of Add (an).
- Agent Store (ag): hub for agents from Microsoft, trusted partners and your org. Admin deploys prebuilt agents (Agents > All agents in the admin centre; assign to Just me / Entire organization / Specific users or groups; Block/Remove). Org-built agents appear under "Built by your org" only after admin approval. Agent 365-enabled agents show in "Agents for your team". Store accessible across Teams, Outlook, Word, Excel, PowerPoint. ag's prerequisites list "A Microsoft Copilot license assigned to your organization" (for admins doing deployment; wording is about the org, not each user).
- Pinning (ah): "agents pinned by Microsoft, admins, and users." Researcher and Analyst are preinstalled and pinned. Admins pin via Copilot controls. Users pin their own. Pin icon works for SharePoint agents (al).
- @-mention: Agent Builder page confirms @mentioning agents exists in the Copilot app (z, in the Try it note). I did not find a Support page that explains @-mention step by step; a search snippet said type @, choose the agent (Copilot Studio docs, not fetched). Write as "type @ and pick the agent" with that caveat.
- Admin view (ad): agent types = published by your org, shared by creator (incl. Agent Builder, Copilot Studio), Microsoft agents, external partner agents, Frontier agents (e.g. App Builder, Workflows). Admins can view shared agents in the registry and block unsafe ones. Researcher and Analyst "are part of the core Copilot chat experience and will not fall under any agent-related settings" (ad, 2026-07-09).
- New 2026-11-04 (w): admin "Agents usage report" splits active users by licensed/unlicensed.

## 5. Researcher (u, v, ah, ad, w)
- Multi-step research over the web and your work content (files, emails, meetings, chats you can access); cited report, headings, visuals. Slower by design; for quick answers use ordinary chat. Find it under Agents in the Copilot app (u); admin page ad says it appears in Chat under "Tools". Be specific, define scope (work/web/both), answer its clarifying questions (u).
- Licence: u does not state one. v: "currently available to Microsoft 365 Premium and Pro subscribers and to Microsoft 365 business and enterprise users with a Microsoft 365 Copilot add-on license" (that sentence mixes personal and work plans). ah: "when you purchase a license for Microsoft Copilot, your organization has access to ... Researcher and Analyst". ar: advanced agents like Researcher are in the licensed column. Business add-on FAQ lists Researcher, Analyst, Facilitator (microsoft.com pricing, see 05). No Microsoft page I read says unlicensed work users get Researcher.
- Admin: v says if it isn't available "your administrator may not have enabled it". Claude in Researcher needs an admin to allow Anthropic models first (v).
- Connectors in Researcher (w): HubSpot (4 Nov), Canva (27 Oct). "Researcher with Computer Use (Frontier)" and Critique exist as separate support pages; not read.
- Deep Research (personal Copilot) retired 18 Aug 2026, separate from this (ax in 05).

## 6. Analyst
- Description only: "Turns raw data into insights and clear visualizations for metrics, trends, and forecasts" (x). The Learn page for Analyst at /microsoft-365/copilot/analyst-agent returned 404; I did not find a dated Analyst page. Licensing same as Researcher (ah, ar). Pinned by default (ah).

## 7. Other Microsoft-built agents (x, ah, w)
- Shown by default (x): Analyst, Researcher, Visual Creator ("turns descriptions into visuals, prototypes, videos, and interactive scenarios"). Add from All agents (x): Idea Coach (ideas to action plans), Writing Coach (tone, grammar, style), Prompt Coach (how to structure prompts), Learning Coach (study plans, skills), Career Coach (goals, career paths; page says "students and institutions"). "More agents are coming soon". Facilitator is not on that page.
- x gives no per-agent licence; says "With your Microsoft Copilot subscription, you have access to multiple agents ... Feature availability varies by subscription type" and a missing agent may mean no licence "or your administrator has not enabled the agent".
- ah: Writing Coach, Idea Coach, Prompt Coach, Career Coach, Learning Coach are "available at no additional cost and are included with Microsoft Copilot Chat".
- UNCLEAR: the pay-as-you-go setup FAQ (ae) suggests testing PAYG by asking Learning Coach, Writing Coach or Career Coach "What can you do?" and says that "consumes about 12 credits". That implies at least some coaches are metered in a PAYG tenant, which sits oddly with "no additional cost" (ah, 2026-04-07). I couldn't reconcile. Say coaches are "included, but the admin must enable them and usage rules may apply".
- New (w, 27 Oct 2026, Windows): "Learning Agent in Microsoft 365 Copilot" (microlearning, structured learning paths). Unclear if same as Learning Coach. Also Facilitator (Teams meetings) appears in Business pricing FAQ.

## 8. Pay-as-you-go agents in Copilot Chat and the admin step (ae, af, ah, ac)
- What it is: usage-based billing for Copilot Chat and SharePoint agents; units are Copilot Credits. Agents grounded in public data or instructions are free; agents grounded in tenant data are billed (ac, ah).
- Admin does it, not users. Roles: Billing Administrator, AI Administrator or Global Administrator (ae). Needs an Azure subscription and resource group in the same tenant (can be created during setup; needs MCA billing account and Owner/Contributor rights). Steps: create billing policy (up to 50 per tenant), add users/groups, optional budget; then Admin centre > Copilot > Billing & usage > Pay-as-you-go services tab > pick "Microsoft Copilot Chat" or "SharePoint agents" and the policy (ae). Budget sends email alerts but is NOT enforced ("Usage can continue ... even after the budget is surpassed").
- Turning it off: users can keep using agents for up to two hours (ae).
- Capacity packs (af): prepaid, 25,000 Copilot Credits per month per pack (bought as "Microsoft Copilot Studio" in Marketplace); Global Admin enables; "Copilot credit policies" (up to 10 per tenant) scope them to groups; only for Copilot Chat, not SharePoint agents. Standalone credit policy: when credits run out Copilot Chat is unavailable until the next monthly cycle; pair with PAYG for overage. Learn tells readers to use the "Copilot Credit Guide" for current details. Per-credit prices: not on pages I read; I couldn't confirm.
- Tell users: if an agent isn't there or says you can't use it, it is probably an admin/billing setting.

## 9. Sharing and admin controls summary (ab, ad, ah, ag, ap)
- Agent sharing for Agent Builder agents: tenant setting All / Specific / No users (ab). Direct sharing vs org-wide is distinguished; "No users" blocks org-wide only per a SharePoint-side description (from search summary, unverified).
- Admin centre: Agents > All agents / Requests / Settings (ag, ad). Enable, disable, assign, block, remove. Agent Builder can be switched off tenant-wide (y). Web search policy overrides agent web toggle (y). Copilot controls in admin centre manage how users create and use agents (o).
- Researcher/Analyst sit outside agent-specific settings (ad).

## 10. Privacy and third-party agents (ap, ad, ah)
- ap: "When you're using agents ... check the privacy statement and terms of use of the agent to determine how it will handle your organization's data."
- ap: when an agent is needed, Copilot "generates a search query to send to the agent on the user's behalf", based on your prompt, your Copilot activity history, and data you can access in Microsoft 365. So third-party agents can receive that.
- ap: admins see an agent's permissions, data access, terms of use and privacy statement in Integrated apps; "Admins have full control to select which agents are allowed"; users only get agents the admin allows AND that they installed/are assigned. Copilot uses only agents the user has turned on.
- ap: encrypted content can exclude programmatic access, which can stop an agent reading it.
- ad: external partner agents' availability and permissions are admin-controlled. Agent Builder agents let the creator add their own privacy/terms links (ab); defaults are placeholders, so don't assume they've been filled in.
- I did not find any Microsoft statement that third-party agents are covered by Microsoft's "no training" or EU Data Boundary commitments; say "I couldn't confirm".

## 11. Copilot Studio (one line)
Copilot Studio is the separate, more powerful tool for agents with actions/connectors and wider publishing; Agent Builder agents can be copied into it (y); it is outside this guide.
