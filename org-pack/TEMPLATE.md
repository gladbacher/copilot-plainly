# Organisation pack

An organisation pack lets one organisation add its own policy, support route and rules to the public guide without changing the public text. The public site shows nothing for these slots. An org build fills them with "At <name>" boxes.

## File format

A JSON file kept **outside the repository** (or in `org-pack/`, where `*.json` is ignored by git except `example.json`).

```json
{
  "name": "Contoso",
  "answers": {
    "policy": { "html": "<p>Short answer in HTML.</p>", "links": [{ "text": "Link text", "url": "https://..." }] }
  }
}
```

- `name` appears in the top bar badge and in each box ("At Contoso").
- Every key under `answers` is optional. A key you leave out shows nothing.
- `html` is inserted as it is. Keep it short: two or three sentences.
- `links` is an optional list of `{ "text", "url" }`.
- Any `html` containing the word `TODO` gets a dashed border so unfinished boxes stand out.
- The `feedback` answer may carry a `url`. If it does, every page's "Report a problem" link goes there instead of GitHub.

## Keys

| Key | What to write | Example |
|---|---|---|
| `policy` | Your AI or Copilot use policy, and where to read it | "Read the AI use policy before you paste anything." |
| `support` | Where to get help | "Raise a Service Desk ticket titled Copilot." |
| `tiers` | Who gets which licence and how to request one | "Everyone has Chat. Request Premium through your manager." |
| `agents` | Approved or recommended agents | "Approved: HR helper, Policy explainer." |
| `agent-sharing` | Rules for building and sharing agents | "Team agents are fine; company-wide needs review." |
| `retention` | How long chats are kept | "180 days." |
| `data-rules` | Classification, customer data and personal data rules | "Nothing Confidential or above. No customer personal data." |
| `report-oversharing` | How to report something you shouldn't see | "Do not use it. Email security@..." |
| `feedback` | Where to send feedback on the guide (use `url`) | A form or mailbox link |
| `training` | Internal training and champions network | "Monthly clinic; local champions list." |

## Building

```bash
python3 tools/build.py --org /abs/path/org.json --out /abs/path/outside-repo
```

- `--out` must be outside the repository. It is emptied on each build, so use a dedicated folder. The build refuses to empty a non-empty folder it did not create.
- It writes the full site, and `org-summary.html`: one standalone page with every answer, ready to paste into an intranet page. SharePoint will not render a static HTML site, so use this page.
- `example.json` in this folder is a fictional Contoso pack to copy from.
