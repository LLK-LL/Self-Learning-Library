# Security and Publishing

Self-Learning Library is built around local Markdown notes. That makes the vault easy to inspect, but it also means you should review the vault before publishing it.

## Do Not Publish Accidentally

Review for:

- private manuscripts;
- unpublished research details;
- private project names;
- customer names;
- credentials;
- API keys;
- local machine paths;
- raw chat logs;
- mentor or collaborator comments that were not meant to be public;
- personal data.

## Suggested Review Commands

Search for sensitive-looking keywords:

```powershell
Select-String -Path .\paper_writing_obsidian_vault\**\* -Pattern "token","password","secret","api_key","credential","cookie","session" -CaseSensitive:$false
```

Search for private project or collaborator names manually. Automated checks will not catch everything.

## Safer Public Template Pattern

For a public template, prefer:

1. a synthetic demo vault;
2. fake task history;
3. fake corrections;
4. fake stable rules;
5. no raw chat logs;
6. no private drafts;
7. no private reviewer or mentor feedback.

## Included Vault Note

The current repository includes a real exported manuscript-assistance vault. Treat it as an example of the layered harness structure, not as a recommendation to publish private work without review.

## Reporting Security Issues

If you find unsafe publishing behavior, redaction gaps, or a file that should not be public, open a minimal issue that describes the class of problem without pasting secrets or private content.
