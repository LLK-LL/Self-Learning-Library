---
title: SCI-memory auto-record conversation changes and user suggestions
created: 2026-06-03 14:40
tags:
  - SCI-memory
  - layer/evidence
  - paper-memory
  - revision-process
  - workflow-convention
---

# SCI-memory auto-record conversation changes and user suggestions

## Source Metadata

- Memory ID: `sci-memory-auto-record-dialogue-2026-06-03`
- Type: `convention`
- Status: `active`
- Project: `Ti-Al explosive welding SPH-FEM analysis`
- Created: `2026-06-03T14:40:00+08:00`
- Importance: `high`
- Source: `user-instruction`

## Memory Content

用户要求：当启用 `SCI-memory` 后，应自动记录每次对话中的论文修改过程和用户提出的建议。该记录不应只在用户明确要求“存入论文知识库”时才执行。

## Potential Generalized Rule

在本项目中，只要用户启用 `SCI-memory` 并围绕论文写作、修改、导师意见、摘要、引言、正文、参考文献或写作规则展开对话，就应在完成任务后自动记录本轮对话中的关键信息。记录内容应包括：修改对象、修改原因、导师意见、用户补充建议、最终采用的写作规则，以及后续可复用的边界条件。

## Applicability

- 适用于用户显式启用 `SCI-memory` 的论文写作和修改任务。
- 适用于导师意见、用户写作偏好、段落修改过程、摘要或引言主线调整、参考文献替换原则等内容。
- 适用于需要把一次具体修改沉淀为后续可复用写作规则的情形。

## Boundary

- 不自动运行 `run_paper_iteration.ps1`，除非用户明确要求启动知识库迭代。
- 不把非论文相关的工具配置、代码调试或系统操作记录进论文知识库。
- 若对话内容只是临时询问且没有形成论文修改、导师意见或可复用建议，可不记录或仅在最终回复中说明未记录原因。
