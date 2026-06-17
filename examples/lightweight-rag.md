# Lightweight RAG Before a Task

Use lightweight retrieval when the assistant needs only a few relevant rules before doing work.

## When to Use

Use this for ordinary content or coding tasks:

- revise a paragraph;
- apply project-specific writing rules;
- check a known formatting constraint;
- retrieve the most relevant correction before answering;
- avoid repeating a past mistake.

## Command

```powershell
py tools\kb_rag.py --query "revise introduction with mentor feedback" --limit 3
```

For ordinary tasks, keep retrieval narrow:

- do not add `--include-workflow`;
- do not add `--include-evidence`;
- do not add `--include-related`;
- do not load `70_Iterative_Thinking/` as normal context.

## Expected Agent Behavior

The assistant should:

1. Run the retrieval command.
2. Convert retrieved notes into a short checklist.
3. Do the requested work.
4. Check against high-priority corrections.
5. Record a reusable lesson only when the task produced one.

## Why This Matters

The point is not to make the model read the whole vault. The point is to give it just enough local memory to avoid predictable regressions.
