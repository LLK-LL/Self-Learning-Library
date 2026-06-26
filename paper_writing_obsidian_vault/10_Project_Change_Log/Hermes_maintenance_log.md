---
title: Hermes maintenance log
tags:
  - codex-maintenance
  - hermes-maintenance
  - layer/evidence
  - workflow-governance
source: hermes_template
status: template
scope: knowledge-base-governance
---

# Hermes Maintenance Log

This file is now a historical Hermes maintenance log plus the transition record
for Codex-owned knowledge-base maintenance. Add new maintenance summaries to the
Codex-owned project change log unless the entry specifically explains historical
Hermes/Jarvis behavior.

## 2026-06-12 Hermes routing retired; Codex ownership restored

### 本次新增

- Added the governance decision that Codex now owns all project knowledge-base
  maintenance, including RAG health checks, orphan-note checks, index checks,
  iteration, conflict monitoring, and skill-promotion review.

### 本次修订

- Retired the active Hermes/Jarvis routing surface.
- Changed the skill-promotion candidate queue from Hermes-maintained to
  Codex-maintained.
- Updated root routing so Codex does not ask the user to summon Hermes for
  knowledge-base maintenance.

### 本次删除

- Removed the active `@HERMES_TEAM.md` include from root `AGENTS.md`.

### 影响层级

- `AGENTS.md`
- `HERMES_TEAM.md`
- `20_Paper_Memories`
- `35_Workflow_Governance`
- `tools/paper_iteration.py`

### 是否需要运行 harness

- Yes. Codex should run the project harness after this governance update so
  generated workflow-governance outputs reflect the new ownership.

### 是否有 skill 候选

- No. This is a governance ownership change, not a new executable workflow
  candidate.

### 备注

- Historical Hermes maintenance entries below remain as provenance only.

## 2026-06-08 Codex-Jarvis coordination setup

### 本次新增

- Added `20_Paper_Memories/Skill Promotion Candidates.md` as the Hermes-facing
  skill-candidate queue.
- Added this `10_Project_Change_Log/Hermes_maintenance_log.md` maintenance log.

### 本次修订

- Updated `tools/paper_iteration.py` so `35_Workflow_Governance/Skill promotion
  registry.md` reads Hermes-maintained rows from `Skill Promotion Candidates.md`
  and renders them under `Hermes Candidate Queue`.

### 本次删除

- None.

### 影响层级

- `10_Project_Change_Log`
- `20_Paper_Memories`
- `35_Workflow_Governance`
- `70_Iterative_Thinking`
- `tools/paper_iteration.py`

### 是否需要运行 harness

- Yes. Codex ran `run_paper_iteration.ps1`; latest verified output:
  `70_Iterative_Thinking/Iteration 20260608_164431.md`.

### 是否有 skill 候选

- No Hermes-maintained candidates yet. The table is ready for Hermes to fill.

### 备注

- Jarvis accepted the Hermes/Codex division of labor.
- Jarvis verified that both new templates are readable.
- Jarvis attempted to update its `paper-kb-maintenance` skill to v1.1.0, but
  Hermes-side `skill_manage(action='patch')` could not find the skill path in
  the active `jarvis` profile. This remains a Hermes-side follow-up.
- Until that update lands, Codex-side templates and harness integration are
  ready, but Hermes-side automated post-maintenance logging depends on the
  pending `paper-kb-maintenance` update.

## 2026-06-08 Hermes skill path fix completed by Codex

### 本次新增

- Added巡检项 6 to Hermes `paper-kb-maintenance`: check
  `20_Paper_Memories/Skill Promotion Candidates.md` and flag candidates with
  `重复次数 >= 3`.
- Added巡检项 7: check
  `10_Project_Change_Log/Hermes_maintenance_log.md` for required maintenance
  summary fields.
- Added Hermes maintenance post-step guidance.
- Added note-writing tag guidance for 20/30-layer notes.

### 本次修订

- Updated `D:/Hermes/profiles/jarvis/skills/note-taking/paper-kb-maintenance/SKILL.md`
  to v1.1.0.
- Replaced the old 5-check overview with a 7-check overview.

### 本次删除

- None.

### 影响层级

- Hermes profile skill: `paper-kb-maintenance`
- `10_Project_Change_Log`
- `20_Paper_Memories`
- `35_Workflow_Governance`

### 是否需要运行 harness

- Yes. Codex should run the project harness after this log update.

### 是否有 skill 候选

- No new Hermes-maintained candidate rows yet.

### 备注

- Root cause: Hermes `skill_view` accepted `note-taking/paper-kb-maintenance`,
  but `skill_manage(action='patch')` required the bare skill name
  `paper-kb-maintenance`. Jarvis successfully changed the version to 1.1.0 but
  did not complete the body patch before tool-iteration limits. Codex located
  the actual file and patched it directly.

## 2026-06-08 Template

### 本次新增

- None.

### 本次修订

- None.

### 本次删除

- None.

### 影响层级

- `10_Project_Change_Log`
- `20_Paper_Memories`
- `30_Writing_Rules`

### 是否需要运行 harness

- No.

### 是否有 skill 候选

- No.

### 备注

- Hermes should not directly maintain generated layers such as
  `35_Workflow_Governance` or `40_Final_Generalized_Rules`.

## 2026-06-08 v1.1.0 全流程巡检

### 本次新增

- None.

### 本次修订

- None.

### 本次删除

- None.

### 影响层级

- 巡检覆盖全部层级（10/20/30/35/40/50/70），未做任何写入。

### 是否需要运行 harness

- No. 所有 7 项巡检通过，未对知识库内容做任何修改。

### 是否有 skill 候选

- No. `Skill Promotion Candidates.md` 仅有占位模板行。

### 备注

- RAG 可用 (exit_code=0, 96.95% token savings)。
- Isolated notes: 7 / Evidence-layer: 121（均在阈值内）。
- 00_Index.md 完整 (270 行，非空)。
- SCI-memory AUTO-GENERATED 规则数 (8) == 40_Final_Generalized_Rules/*.md (8)，同步正常。
- 50_Conflicts：仅 No unresolved conflicts.md，无待解决冲突。
- Codex harness 已于 2026-06-08 21:28 完成自动迭代 (Iteration 20260608_212814)，更新了 30/35/40/50/70 层。
- 10 层和 20 层在上次 Hermes 维护后无新增变更，无孤儿笔记需要处理。

## 2026-06-08 v1.1.0 全流程巡检 (Cron #3 — 团队化执行)

### 分工记录

- **Jarvis (总控)**: 读取 vault 状态、Skill Promotion Candidates.md、graph_analysis_latest.md、SCI-memory SKILL.md；汇总子任务结果；更新维护日志。
- **小牛马-A (deepseek-v4-pro)**: RAG 可用性 + 00_Index.md 完整性。→ `exit_code=0 / 270行 ✓`
- **小牛马-B (deepseek-v4-pro)**: 孤儿笔记 + 50_Conflicts。→ `Isolated=7 / Evidence=121 / 仅 No unresolved conflicts.md ✓`
- **小牛马-C (deepseek-v4-pro)**: SCI-memory 同步。→ `N_auto=8 == N_files=8 ✓`
- **中牛马 (gpt-5.4)**: 未调动 — 无机检异常。
- **大牛马 (gpt-5.5)**: 未调动 — Skill Promotion Candidates.md 仅占位模板行，无 `重复次数≥3` 候选。
- **模型限制**: `delegate_task` 不支持 per-subagent model/provider/base_url 覆盖；三匹小牛马均以父 agent 的 deepseek-v4-pro 执行。已确认不影响巡检结果。

### 本次新增

- None.

### 本次修订

- None.

### 本次删除

- None.

### 影响层级

- 巡检覆盖全部层级（10/20/30/35/40/50/70），未做任何写入。

### 是否需要运行 harness

- No. 所有 7 项巡检通过，知识库状态与上次 Cron #2 相同。

### 是否有 skill 候选

- No. `Skill Promotion Candidates.md` 仅有占位模板行（重复次数=0）。

### 备注

- graph_analysis_latest.md 时间戳 `2026-06-08 21:28`，上次 Harness 迭代 (Iteration 20260608_212814) 后未再更新。
- Vault notes 总数 212，与上次巡检一致。知识库稳定。
- 本次为 Cron 首次团队化执行，验证了 delegate_task 三并行 + condition 跳过中/大牛马的流程。

## 2026-06-08 v1.1.0 全流程巡检 (Cron #2)

### 本次新增

- None.

### 本次修订

- None.

### 本次删除

- None.

### 影响层级

- 巡检覆盖全部层级（10/20/30/35/40/50/70），未做任何写入。

### 是否需要运行 harness

- No. 所有 7 项巡检通过，自上次 Harness 迭代 (Iteration 20260608_212814) 后 vault 无新变更。

### 是否有 skill 候选

- No. `Skill Promotion Candidates.md` 仅有占位模板行。

### 备注

- RAG: exit_code=0, baseline 29 files/11689 tokens, 96.95% savings ✓
- Orphan: Isolated=7 (≤10 ✓), Evidence-layer=121 (≤150 ✓)
- Index: 00_Index.md present, non-empty ✓
- SCI-memory sync: N_auto=8 == N_files=8 ✓
- Conflicts: Only `No unresolved conflicts.md` ✓
- Vault notes: 212, unchanged from Harness run on same date
- No new evidence, no new rules, no new conflicts — knowledge base stable
