# Research 01: product map and privacy (primary sources, retrieved 2026-10-16)

## Sources
- S1 Microsoft Learn, "What is Microsoft Copilot?" (ms.date 2026-10-14) https://learn.microsoft.com/en-us/microsoft-365/copilot/microsoft-365-copilot-overview
- S2 Microsoft Learn, "Data, Privacy, and Security for Microsoft Copilot" (ms.date 2026-07-09, updated 2026-10-08) https://learn.microsoft.com/en-us/microsoft-365/copilot/microsoft-365-copilot-privacy

## IMPORTANT: naming has changed (S1, S2)
- "Microsoft 365 Copilot" is now named **Microsoft Copilot**; "Microsoft 365 Copilot Chat" is now **Microsoft Copilot Chat**. Docs still use old names during the transition. Guide must explain both names.
- Main URL: `copilot.cloud.microsoft`; also Copilot app (web/desktop/mobile), Copilot Chat in Edge, Outlook, Teams.

## Four tiers (S1 comparison table)
1. **Copilot Chat (Basic)**: included with eligible M365 licences. Web data only. Org content only if you paste/upload/select it, or Copilot Chat in Outlook/Teams with content open, or pay-as-you-go agent. NO Copilot in Word/Excel/PowerPoint/OneNote.
2. **Microsoft 365 Copilot (Basic)**: no add-on licence, but *standard access* to Copilot in Word, Excel, PowerPoint, OneNote. Web data only (no Graph). Standard access "subject to service capacity and might vary throughout the day". In-app: Word draft/rewrite/summarise; Excel analyse/formulas/visuals; PowerPoint create from prompts/edit; Outlook draft/summarise/coaching; OneNote drafts; Teams summarise (up to 30 days)/transcribe/action items; Forms drafts.
3. **Microsoft 365 Copilot (Premium)**: the add-on licence. Priority access; grounding in web + org data automatically via Microsoft Graph and **Work IQ** (Work IQ can be turned on/off); Copilot Search; semantic indexing; agents using web and work data; admin tools (SharePoint Advanced Management, Purview, usage reports).
4. **Usage-based billing capabilities**: requires Premium licence; adds **Copilot Cowork** (carries out tasks across M365 on your behalf) and **Copilot Code** (Frontier preview) billed on consumption (Copilot credits).
- Model selector: Auto / Quick response / Think deeper (S1). Anthropic and OpenAI models can be used as subprocessors, admin-controlled; Anthropic models excluded from EU Data Boundary (S2).
- Other independently licensed products: Security Copilot, GitHub Copilot, Copilot Studio (S1).
- Sign in with **Entra (work) account** for work protections; personal MSA sign-in is a different experience (S1).

## Privacy and data (S2)
- Copilot = LLMs + Microsoft Graph content you can access + M365 apps.
- Shows only org data the user has **at least view permission** to access; permissions in SharePoint etc. are the safety net, incl. shared channels/external collaborators.
- Prompts, responses and data accessed via Graph are **not used to train foundation LLMs**.
- Prompt + response + citations stored as "Copilot activity history", encrypted, retained per M365 commitments; admins can search via Content search/Purview and set retention; **users can delete their own history** via My Account portal https://myaccount.microsoft.com/.
- Honors Purview sensitivity labels / IRM usage rights.
- Web search: Copilot builds a search query sent to Bing; admin policy "Allow web search in Copilot".
- Agents: check agent's privacy statement; admins control which agents allowed.
- Abuse monitoring with human review: Copilot has opted out.
- EU Data Boundary: EU traffic stays in EU; Anthropic models excluded.
- Responses "aren't guaranteed to be 100% factual"; review before sending. Microsoft doesn't claim ownership of output. Copilot Copyright Commitment for commercial customers.
- Workplace-harm filter: Copilot restricted from inferences/judgments about employee performance, attitude, emotional state.
- If admin turns off "connected experiences that analyze your content", Copilot is unavailable in Word/Excel/OneNote/Outlook/PowerPoint.

## Still to verify (primary source)
- Current prices (only third-party blogs so far: ~$30/user/month Premium list; Copilot Business $21, promo $18; E7 $99). microsoft.com fetch timed out. NOT to be published until confirmed on a Microsoft page.
