# tebb Skills

English · [简体中文](README.zh-CN.md)

Official, versioned instructions for [tebb](https://github.com/lkun-lea/tebb) AI companions. These are skills, not executable plugins or permission grants.

| Skill | Purpose |
| --- | --- |
| workflow-builder | Discover adapters, create reusable declarative capabilities, and save visual workflow drafts. |
| github-repo-summary | Summarize repository activity using real GitHub evidence. |
| feishu-doc-writing | Prepare a daily work summary from actual calendar, tasks and conversation. |
| weekly-retro | Review the week using GitHub and Feishu work evidence. |

tebb pins a full commit and file digests in its `skills-source.json`. Developers explicitly prepare that snapshot; release packages include it for offline use. Starting the app does not fetch the latest branch. See tebb's development guide for the preparation command.

Each `skills/<name>/SKILL.md` has `name` and `description` frontmatter and a nonempty body. Keep names stable, describe prerequisites and actual tools, preserve failure/unknown states, and never embed credentials, personal data, implicit external sends, or executable installation hooks. Skills cannot expand the companion's tools or workspace permissions.

Run `python scripts/validate.py` before contributing. Contributions use pull requests in this content repository. Product tools, UI, authentication and scheduling belong to tebb. The first three skills were extracted from tebb commit `4937138a0c2a5ed371433c8cbba48149a16e9926` without changing their instructions.

MIT; see [LICENSE](LICENSE). Preserve original copyright and third-party notices when redistributing.
