---
name: ux-intent-discovery
description: Establish who a UI is for, what they are trying to accomplish, what context they have, and what mistake matters most before interface decisions are made. Internal reasoning skill used by the public UX commands.
license: MIT
metadata:
  version: "2.0.0"
  category: ui-ux
  visibility: internal
---

# UX Intent Discovery

## Purpose

Prevent implementation from mirroring the database or ticket wording when the user's actual task requires a different interface.

## Required questions

Before designing, resolve four things:

1. **Who** uses this surface in practice?
2. **What** are they trying to accomplish here?
3. **What do they need to know** before acting?
4. **What is the worst plausible mistake** they could make?

Ask only for information that materially changes the design. If the request already answers these questions, do not repeat them.

If the user says to skip questions, proceed with explicit assumptions and mark them as provisional.

## Intent brief

Produce a compact internal brief:

- User:
- Trigger/context:
- Primary job:
- Decision or information needed:
- Most costly mistake:
- Frequency:
- Constraints:
- Known evidence:
- Assumptions:

Translate feature language into user-outcome language. "Add an account table" is not an outcome. "Support staff can find the correct account and act without deleting the wrong one" is.

## Risk handling

The greater the consequence of a mistake, the stronger the need for:
- clearer hierarchy;
- safer defaults;
- confirmation or undo;
- persistent status;
- recovery;
- explicit copy.

Do not invent research findings, personas, or user preferences.

## Handoff

Pass the intent brief to `information-hierarchy` and the invoking command or agent.
