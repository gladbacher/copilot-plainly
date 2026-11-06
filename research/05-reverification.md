# Research 05: re-verification of earlier claims (retrieved 2026-11-06)

Compared against notes 01-03 (retrieved 2026-10-16). Verdicts: CONFIRMED / CHANGED / STILL UNCLEAR. Source letters continue from 04-agents.md (o..ap etc. defined there); new ones below.

## New/extra sources
- p  Learn, License options for Microsoft Copilot, ms.date 2026-10-19 (updated 2026-11-04) https://learn.microsoft.com/en-us/microsoft-365/copilot/microsoft-365-copilot-licensing
- q  microsoft.com, Copilot business pricing, undated, fetched 2026-11-06 https://www.microsoft.com/en-us/copilot/pricing/business
- r  Learn, Manage Copilot Chat, ms.date 2026-10-28 https://learn.microsoft.com/en-us/copilot/manage/manage-copilot-chat
- s  Support, What Copilot license do I have, "Last updated: April 2026" https://support.microsoft.com/en-us/microsoft-365-copilot/what-copilot-license-do-i-have
- t  Support, Microsoft Copilot Chat, your AI assistant for work, undated https://support.microsoft.com/copilot-microsoft365-chat
- aq Learn, Microsoft Copilot requirements, ms.date 2026-11-04 https://learn.microsoft.com/en-us/microsoft-365/copilot/microsoft-copilot-requirements
- as Support, Copilot in Excel, undated https://support.microsoft.com/en-us/copilot-excel
- at Support, Copilot in PowerPoint, "Last updated: October 2026" https://support.microsoft.com/en-us/copilot-powerpoint
- au Support, Get started with Copilot in Teams meetings, undated https://support.microsoft.com/en-us/office/get-started-with-copilot-in-microsoft-teams-meetings-0bf9dd3c-96f7-44e2-8bb8-790bedf066b1
- av Support, Copilot in Outlook, undated https://support.microsoft.com/en-us/copilot-outlook
- aw Support, Copilot in Word, undated https://support.microsoft.com/en-us/copilot-word
- ax Support, Copilot app updates for personal, work and school accounts, undated https://support.microsoft.com/en-us/microsoft-365-copilot/learning/changes-microsoft-copilot-app
- ay Support, Understand changes to Microsoft Copilot mobile app, undated https://support.microsoft.com/en-us/microsoft-365-copilot/understand-changes-to-microsoft-365-copilot-mobile-app
- az Support, Standard versus priority access, undated https://support.microsoft.com/topic/standard-versus-priority-access-to-features-in-microsoft-365-copilot-chat-12c8d9f8-db32-4f99-8ebe-d8d85879137f
- (Not on the allowed domains, so NOT fetched or relied on: a Tech Community thread "Removal of Copilot Chat Availability in M365 Apps" quoting Message Center notice MC1253863. It only appeared in a search result; see item 1.)

## 1. Do "Basic" users still get in-app Copilot in Word/Excel/PowerPoint/OneNote? The April 2026 change
**Verdict: CONFIRMED as to the current Microsoft wording; the April 2026 change itself is only partly confirmed.**
- o (Learn overview, ms.date 2026-11-05) still says Copilot Chat (Basic) users "don't have access to Copilot in Word, Excel, PowerPoint, and OneNote", whereas Microsoft 365 Copilot (Basic) users "have standard access" to Copilot in those four apps, "subject to service capacity and might vary throughout the day".
- s (Support, last updated April 2026) says the same for the three labels.
- aq (2026-11-04): "Chat experiences in Word, Excel, and PowerPoint vary depending on the user's license and tenant configuration."
- So there are TWO unpaid states, not one. A user with the Copilot Chat (Basic) label has NO Copilot inside Word/Excel/PowerPoint/OneNote. A user with the M365 Copilot (Basic) label has "standard access". Which one a given person gets is not explained on any page I read (what decides Chat-Basic vs M365-Basic: licence, tenant setting or rollout?). STILL UNCLEAR. The site must not say "Basic users get Copilot in Word"; say it depends on the label under your name.
- The reported April 2026 change: I could NOT find Microsoft's own notice on learn/support. A search surfaced a community post quoting Message Center MC1253863: from 15 April 2026 the Copilot Chat pane in Word, Excel, PowerPoint and OneNote ends for Copilot Chat (unlicensed) users, who keep web chat, the Word/Excel/PowerPoint agents inside the Copilot app, Outlook and Teams chat. That is consistent with o and s but is secondary and unfetched. Phrase: "Microsoft's documentation now says... ; I couldn't find the original announcement on a Microsoft docs page, only a reference to it."
- Still available for unlicensed users, confirmed: Copilot in Outlook ("Included" in both columns, ar/av), Copilot Chat in Edge, Teams, Outlook with open content (o).
- Related: Copilot mobile app no longer edits Word/Excel/PowerPoint files; non-subscribers are redirected to the Office apps (ay, undated).
- Standard vs priority access page (az) gives no numeric limits ("Microsoft doesn't publish specific numeric limits") and says fair-use limits apply to some Copilot Chat features and may change.
- An unlicensed user may still SEE a Copilot button in the apps; Microsoft says a missing/present button depends on subscription and org settings (as, at, aw: "If you don't see Copilot in Word, Excel, PowerPoint, or OneNote, it might not be included with your Microsoft 365 subscription or available based on your organization's settings").

## 2. Researcher availability for work accounts
**Verdict: CONFIRMED (licensed only, per Microsoft's wording) with a wording caveat.**
- No Microsoft page I read says unlicensed work users get Researcher. ar: without a licence agents are "Limited (no advanced agents)"; with a licence "advanced agents like Researcher, Analyst, and custom agents". ah (Learn admin guide): a Copilot licence gives "additional capabilities, such as Researcher and Analyst". q (pricing FAQ): organisations with Copilot licences, including the Business add-on, get Researcher, Analyst, Facilitator.
- v (Support Researcher page): "currently available to Microsoft 365 Premium and Pro subscribers and to Microsoft 365 business and enterprise users with a Microsoft 365 Copilot add-on license." Only Learn's Researcher page (u, ms.date 2026-02-19, updated 2026-11-04) states no licence at all.
- The earlier note said sources conflicted ("default for licensed users" vs "Premium/Pro"). Re-reading: they do not truly conflict for WORK accounts; Premium/Pro are personal plans. Admin may also need to enable it (v). Claude in Researcher needs admin to allow Anthropic models (v).
- Admin page ad (2026-07-09): Researcher and Analyst sit in Copilot Chat under "Tools" and "will not fall under any agent-related settings", so an admin's agent-blocking may not switch them off. I couldn't confirm what does.

## 3. Names and labels
**Verdict: CONFIRMED, with extra detail.**
- Rename confirmed again (o, aq, r): "Microsoft 365 Copilot is now named Microsoft Copilot, and Microsoft 365 Copilot Chat is now named Microsoft Copilot Chat"; URL copilot.cloud.microsoft. aq's table header: "Microsoft Copilot (formerly Microsoft 365 Copilot)" and "Microsoft Copilot Chat (formerly Microsoft 365 Copilot Chat)".
- The labels in the docs are not all renamed: o's table still says "Copilot Chat (Basic) license", "Microsoft 365 Copilot (Basic) license", "Microsoft 365 Copilot (Premium) license" (long forms). s and t (Support) give the in-product short forms "Copilot Chat (Basic)", "M365 Copilot (Basic)", "M365 Copilot (Premium)", shown "under your name" / in the apps ("In-product labels are displayed in Microsoft 365 apps ... and in the Microsoft Copilot app", o). I couldn't confirm whether the in-product text will change to "Microsoft Copilot". Keep all three on the site with a note.
- Other naming: o now has a "Home" tab with Chat and Cowork; "Cowork and Code require a Microsoft 365 Copilot license and an assigned usage-based billing policy". The overview page was re-dated 2026-11-05 (was 2026-10-14 in note 01) and its canonical URL is now learn.microsoft.com/en-us/copilot/plan/copilot-overview. License options page canonical is /copilot/plan/copilot-license-options (p). Old URLs still work. Page names changed to "Manage Copilot Chat" etc.
- Fourth column in o is "Usage-based billing capabilities" (not a licence), as before.
- Pay-as-you-go note: o says Copilot Chat (Basic) and M365 (Basic) both get "Access to agents that use web data" and "Pay-as-you-go work data agents".

## 4. Copilot Business prices
**Verdict: CONFIRMED, all figures identical on q (fetched 2026-11-06).**
- Add-on: $18.00 yearly (promo; "originally starting from $21.00"), $25.20 monthly. Promo window 1 Jul 2026 to 31 Dec 2026, existing Microsoft 365 customers with an eligible Business plan, annual commitment, first year only, not on trials, can't be combined with other offers, "Microsoft can change or cancel it at any time". The page shows no promo for monthly.
- Bundles: Business Standard with Copilot $23.50 yearly / $28.20 monthly; Business Premium with Copilot $32.00 / $38.40.
- Also on q: one-month free trial (card required); 7-day prorated refund window on paid subscriptions; yearly plans auto-renew; up to 300 users; Copilot Cowork, Autopilot and Work IQ APIs are billed separately by usage via Copilot Credits.
- p (licensing, ms.date 2026-10-19): Copilot Business is an add-on for organisations with up to 300 users, annual commitment, eligible plans: Business Premium, Standard, Basic, Apps for Business, Teams Essentials. Microsoft 365 E7 "includes Microsoft Copilot". Note p says "Microsoft Copilot Business" and q says "Microsoft 365 Copilot Business"; both names appear.
- Prices are US dollars, no tax; I did not check a UK (GBP) page, and the user is UK-spelling. STILL UNCLEAR: GBP prices. Say "US list prices; UK prices differ".

## 5. Excel modes/platforms, PowerPoint limits, Teams meeting limits
- Excel (as): CONFIRMED. Three modes Allow editing (default), Plan, Chat only; no "Agent mode" wording on the page (a linked blog title mentions it). Windows/Mac/web: edit + chat + plan. iPad: chat + plan, edit "rolling out to production". iPhone: chat, edit rolling out. Android: chat only. Note: iPhone is now described as edit "rolling out" (my earlier note said chat only); minor CHANGE. Still not stated: table requirement, size limits, functions. New release note 4 Nov (w): clickable links in chat to changed sheets/ranges.
- PowerPoint (at, now dated "Last updated: October 2026"): the 24 MB figure is CHANGED/NARROWED. Page says Copilot "works best with Word documents that are smaller than 24 MB" (a tip about Word files used as the source, not a PowerPoint file limit or a hard cap). Languages: my earlier note had "one output language at a time"; the fetch summary this time said the page names no supported languages, so I could NOT re-confirm it; re-check the page by eye before keeping that line. New release notes (w): attach a deck to copy its style (27 Oct/4 Nov), attach an image (27 Oct), custom skills (6 Oct).
- Teams meetings (au, undated): licence = Teams Premium (intelligent recap) or Copilot licence; the organiser controls Copilot for their meetings even if unlicensed; transcription required if "During and after the meeting" is chosen; doesn't work in meetings hosted outside your organisation; chat context up to 24 hours before the meeting; catch-up if you join more than 5 minutes late; recurring-meeting history lost if a later meeting is transcribed. NOT stated on this page: meeting length limit, language list, 30-day retention. The "summarise up to 30 days" figure for Basic Teams is from o. STILL UNCLEAR: any meeting length limit.
- Word (aw): licence wording "eligible Microsoft 365 subscription and/or Microsoft 365 Copilot license"; custom model selection only for eligible premium subscriptions; others get Auto, Instant, Think deeper.

## 6. Outlook, incl. classic Outlook for Windows
**Verdict: CHANGED (better than before): classic Outlook IS supported per Learn; the Support page still doesn't say so.**
- av (Support) "Applies to": Outlook for Microsoft 365, Outlook for Microsoft 365 for Mac, New Outlook for Windows; classic Outlook, web and mobile not named.
- aq (Learn, 2026-11-04): "Microsoft Copilot works with supported versions of classic Outlook and new Outlook for Windows and Mac." Needs an Exchange Online mailbox; "Microsoft Copilot isn't available in group mailboxes."
- w (27 Oct 2026): "Copilot Settings in classic Outlook for Windows" (File menu); 4 Nov: account selector in the Calendar Copilot pane (web).
- Unlicensed vs licensed split in Outlook CONFIRMED (av): without add-on, Copilot Chat in Outlook handles inbox/calendar/meetings and "other limited data" and can act in Outlook (schedule meetings, flag, auto-replies); with add-on adds chats and enterprise data. "Supported versions" of classic Outlook are not defined on the pages I read; STILL UNCLEAR which builds.
- Mailbox must be Exchange Online (aq).

## 7. Other notable changes since 16 Oct 2026
- Page re-dates: o (11-05), p (11-04 updated), aq (11-04), r (10-28), ab (11-06). No contradiction with the notes, but o and aq now say "Microsoft Copilot" more consistently.
- Release notes (w): 27 Oct and 4 Nov entries: Learning Agent in Microsoft 365 Copilot (Windows); SharePoint list agent; Agents usage report in admin centre; custom MCP connectors for admins; Copilot Search authoritative sites (up to 100); HubSpot and Canva connectors in Researcher; Edge new tab page with Copilot; Cowork can use local Edge sessions; Teams AI Workflows (off by default); Excel and PowerPoint items above.
- SharePoint: "Upgrades to agents in SharePoint are coming in mid-November 2026" (aj, ak). Not live yet at 2026-11-06; the site should say "rolling out from mid-November".
- Agent Builder share page (ab) updated 2026-11-06 with the Can edit / Can chat roles, org-wide sharing toggle, About this agent fields and org-catalogue submission. If the site text on sharing was written from older pages, re-check it.
- Copilot app (personal accounts mostly, ax): sign in to the updated app by 31 Dec 2026 or unmigrated content is deleted; Deep Research and Podcasts retired 18 Aug 2026; "Work or school users: changes are mostly limited to the Copilot icon and name". Not relevant to work accounts except the icon/name change.
- Pay-as-you-go/capacity packs for Copilot Chat: details in 04 sections 8 (ae 2026-07-17, af 2026-04-29). Learn says to use the "Copilot Credit Guide" for the latest. Pages fetched but unverified for price per credit.
- Not checked: Microsoft 365 roadmap, Message Center, Tech Community (outside allowed domains).

## Gaps to flag on the site ("I couldn't confirm ...")
1. What decides whether an unlicensed work user is Chat-Basic or M365-Basic.
2. The original April 2026 announcement on a Microsoft docs page.
3. Whether Agent Builder is open to unlicensed Copilot Chat users in a tenant with no pay-as-you-go.
4. Whether the Learning/Writing/Career Coaches are metered under pay-as-you-go.
5. GBP prices; Teams meeting length limits; PowerPoint language limits; which classic Outlook builds.
6. Third-party agent data being covered by Microsoft's training/EU boundary commitments.
