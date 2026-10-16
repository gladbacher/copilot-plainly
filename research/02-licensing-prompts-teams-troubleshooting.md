# Research 02: licensing, prices, prompts, Teams, troubleshooting (retrieved 2026-10-16)

## Sources
- S3 Learn, "License Options for Microsoft Copilot" (ms.date 2026-09-25) https://learn.microsoft.com/en-us/microsoft-365/copilot/microsoft-365-copilot-licensing
- S4 Learn, "Manage Microsoft Copilot Chat" (ms.date 2026-10-12) https://learn.microsoft.com/en-us/copilot/manage
- S5 microsoft.com, Copilot business pricing https://www.microsoft.com/en-us/copilot/pricing/business (fetched 2026-10-16)
- S6 Microsoft Support, "Get started writing prompts in Microsoft Copilot" (updated Sept 2026) https://support.microsoft.com/en-us/topic/learn-about-copilot-prompts-f6c3b467-f07c-4db1-ae54-ffac96184dd5
- S7 Microsoft Support, "Get started with Copilot in Microsoft Teams meetings" (no page date) https://support.microsoft.com/en-us/office/get-started-with-copilot-in-microsoft-teams-meetings-0bf9dd3c-96f7-44e2-8bb8-790bedf066b1
- S8 Microsoft Support, Copilot Chat page (license comparison; no date) https://support.microsoft.com/copilot-microsoft365-chat

## Eligibility and licences
- Copilot Chat: no extra cost for users signing in with Entra work/school account on an eligible M365 plan (E3/E5/E7, F1/F3, Business Basic/Standard/Premium, Teams Essentials/Enterprise, Office 365 E1/E3/E5/F3, A/G plans) (S4).
- Paid Copilot is an add-on to those plans (S3). Check an account with Microsoft's "Copilot License Details" diagnostic https://aka.ms/CopilotLicenseDetails (S3).
- To see your tier: label under your name at copilot.cloud.microsoft: "Copilot Chat (Basic)", "M365 Copilot (Basic)", "M365 Copilot (Premium)" (S8).
- Sign-in cues: work account shows "Work" label under profile + green data protection shield; personal account looks different and has different protections (S4).
- Users can use Copilot Chat in Edge sidebar with work account (enterprise data protection) (S4).

## Prices (S5, USD, per user per month, excl. tax; verify before buying)
- Copilot Business add-on (needs qualifying M365 Business plan, up to 300 users): list $21.00; promo $18.00 yearly (first year only, 1 Jul 2026 to 31 Dec 2026, existing customers only, not on trials); $25.20 monthly. Annual commitment; 7-day prorated refund window.
- Business Standard with Copilot $23.50 yearly / $28.20 monthly. Business Premium with Copilot $32.00 yearly / $38.40 monthly.
- Business add-on includes: Copilot in M365 apps and Teams, Researcher, Analyst, Facilitator agents, Work IQ chat, usage analytics.
- Enterprise Copilot add-on price (reported ~$30) and E7 ($99) NOT yet confirmed on a Microsoft page: do not publish; link to Microsoft pricing instead.

## Conflict to flag (do not resolve silently)
- S1 says Microsoft 365 Copilot (Basic) users have *standard access* to Copilot in Word/Excel/PowerPoint/OneNote. Third-party university IT pages (e.g. Drake, Drexel KBs) say embedded Copilot in those apps ended for unlicensed users in April 2026. Guide wording: "what you get depends on the label under your name and your tenant; check yours, ask IT". Mark as "check with your IT".

## Prompting (S6)
- Four parts: Goal (only required), Context, Source, Expectations. Refine with follow-ups; verify answers; same prompt can give different results.

## Teams meetings (S7)
- Organizer chooses Online meeting options > Copilot and other AI: during and after (transcription required) / only during / off.
- After-meeting questions need a transcript. Late joiner (>5 min) catch-up summary. Doesn't work in meetings hosted outside your org. Intelligent recap requires Teams Premium or a Copilot licence. Export long answers to Word, tables to Excel (unless blocked by sensitivity label or copy/forward restriction).

## Troubleshooting leads (third-party, lower confidence; verify before publishing as fact)
- Wrong account (personal vs work), licence not assigned/refreshed (File > Account > Update License), update channel (Semi-Annual Enterprise Channel lacks some features), New vs classic Outlook, sign out/in of Teams.
- Admin side: connected experiences policy off => no Copilot in Office apps (S2, primary). Web search policy "Allow web search in Copilot" (S4, primary). Network must allow *.cloud.microsoft (S4, primary).

## Not yet researched (v1.1)
Per-app deep dives (Excel Agent mode limits, PowerPoint, Word), Copilot Notebooks/Pages, Researcher/Analyst, Cowork, credits billing.
