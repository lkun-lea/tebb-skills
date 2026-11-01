# tebb Skills

[English](README.md) · 简体中文

[tebb](https://github.com/lkun-lea/tebb) AI 伙伴的官方版本化技能规程。技能是任务指引，不是可执行插件，也不授予权限。

| 技能 | 用途 |
| --- | --- |
| workflow-builder | 发现适配器、创建可复用声明式能力、保存可视化工作流草稿。 |
| github-repo-summary | 依据真实 GitHub 证据整理仓库动态。 |
| feishu-doc-writing | 依据实际日程、待办和对话整理工作总结。 |
| weekly-retro | 依据 GitHub 与飞书工作证据整理周复盘。 |

tebb 在 `skills-source.json` 固定完整提交和文件摘要。开发者明确准备固定快照，发布包离线携带；应用启动不会跟随最新分支。准备命令见 tebb 开发指南。

每项技能位于 `skills/<名称>/SKILL.md`，包含 name、description 前置元数据及非空正文。保留稳定名称，写明前置条件和实际工具，保留失败/未知状态，不包含凭据、个人资料、隐式外部发送或可执行安装钩子。技能不能扩大伙伴工具或工作区权限。

贡献前运行 `python scripts/validate.py`；本内容仓库通过 PR 评审。产品工具、界面、认证、调度归 tebb。原有三份技能从 tebb 提交 `4937138a0c2a5ed371433c8cbba48149a16e9926` 原样提取。

MIT，见 [LICENSE](LICENSE)。再分发需保留原版权及第三方声明。
