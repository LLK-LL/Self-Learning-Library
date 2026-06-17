# No-Regression Guard

The no-regression guard prevents the assistant from repeating mistakes that were already corrected by the user, mentor feedback, or a confirmed successful baseline.

## What Counts as a Regression?

A regression happens when a new answer violates a known correction, for example:

- reintroducing wording the user explicitly rejected;
- applying an old preference after a newer preference replaced it;
- mixing workflow notes into final content;
- changing a confirmed formatting baseline;
- ignoring high-priority supervision notes;
- applying a rule outside its intended scope.

## Priority Order

When notes conflict, resolve by source priority and scope:

1. explicit mentor feedback;
2. active user-triggered supervision corrections;
3. user-confirmed successful output baselines and explicit user corrections;
4. ordinary memories;
5. change-log facts;
6. generated rules without newer correction evidence.

## Task Checklist

Before finalizing a task:

1. Retrieve relevant high-priority corrections.
2. Identify the scope: abstract, introduction, formula, file-processing, governance, etc.
3. Apply only rules that match the current scope.
4. Check that workflow/audit language did not enter final output content.
5. Report any unresolved conflict instead of forcing a false rule.

## Example Prompt

```text
Use the no-regression guard before finalizing this change. Check high-priority corrections first and tell me if any rule conflicts with the requested edit.
```
