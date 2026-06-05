---
title: Layered graph overview
tags:
  - layer/output
  - paper-iteration
  - vault-graph
---

# Layered Graph Overview

## Layer Flow

```mermaid
flowchart LR
  A["10_Project_Change_Log<br/>project edit evidence"] --> B["20_Paper_Memories<br/>reusable writing evidence"]
  B --> C["30_Writing_Rules<br/>intermediate paper-writing rules"]
  B --> H["35_Workflow_Governance<br/>workflow and process rules"]
  B --> J["45_Supervision<br/>user-triggered supervision corrections"]
  C --> D["40_Final_Generalized_Rules<br/>final paper-writing rules"]
  C --> E["50_Conflicts<br/>priority and contradiction checks"]
  C --> F["60_Limited_Rules<br/>not-yet-generalizable paper rules"]
  D --> G["70_Iterative_Thinking<br/>current conclusions and graph analysis"]
  H --> G
  J --> G
  E --> G
  F --> G
  G --> I["00_Index<br/>entry and navigation"]

  classDef evidence fill:#0f766e,stroke:#115e59,color:#ffffff;
  classDef reasoning fill:#2563eb,stroke:#1d4ed8,color:#ffffff;
  classDef output fill:#d97706,stroke:#b45309,color:#ffffff;
  class A,B evidence;
  class C,D,E,F,H,J reasoning;
  class G,I output;
```

## Layer Counts

- Evidence: `144` notes
- Reasoning: `30` notes
- Output: `7` notes

## Obsidian Graph Filters

- All layers: `tag:#layer/evidence OR tag:#layer/reasoning OR tag:#layer/output`
- Evidence only: `tag:#layer/evidence`
- Evidence and reasoning: `tag:#layer/evidence OR tag:#layer/reasoning`
- Hide output layer: `tag:#layer/evidence OR tag:#layer/reasoning`

## Rule

Only the Evidence Graph contributes to conclusion support scores. Reasoning and output layers are shown for navigation and audit.
