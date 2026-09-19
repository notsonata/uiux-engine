---
name: interaction-design
description: Define UI behavior, controls, transitions, affordances, selection, editing, navigation, destructive actions, and interaction feedback. Use when specifying how an interface behaves rather than only how it looks.
license: MIT
metadata:
  version: "1.0.0"
  category: ui-ux
---

# Interaction Design

## Objective

Make available actions discoverable, predictable, safe, and efficient.

## Action hierarchy

For each surface identify:
- one primary action when possible;
- secondary actions;
- destructive or exceptional actions;
- contextual actions;
- unavailable actions and why.

Visual emphasis should track task importance, not implementation convenience.

## Affordance

Users should be able to distinguish:
- interactive from static elements;
- selected from unselected;
- editable from read-only;
- enabled from disabled;
- expanded from collapsed;
- saved from unsaved.

Do not rely on hover alone to reveal essential functionality.

## Feedback timing

Feedback should match the action:
- immediate local feedback for toggles, selection, typing, drag, and direct manipulation;
- progress for noticeable asynchronous work;
- clear completion for consequential operations;
- persistent status when the state matters after a transient toast disappears.

## Destructive actions

Choose protection proportional to consequence:
- undo for quickly reversible actions;
- confirmation for high-cost or irreversible actions;
- typed confirmation only for exceptional destructive operations;
- soft delete or recovery windows where practical.

Avoid confirmation dialogs for routine, low-risk actions.

## Selection vs navigation

In rows, cards, lists, and tables, define whether clicking the container:
- opens details;
- selects the item;
- toggles a state;
- does nothing.

Do not overload the same click target with conflicting meanings.

## Focus and input

Define:
- logical tab order;
- visible focus;
- Enter/Space behavior for controls;
- Escape behavior for temporary layers;
- focus destination when dialogs open and close;
- touch target and pointer affordance;
- keyboard alternatives to drag or gesture-only actions where needed.

## Modal decision

Use modal surfaces for bounded tasks that require temporary focus. Avoid them for deep navigation, large multi-step work, content users may need to compare with the underlying page, or workflows requiring browser navigation/history.

## Output

Specify behavior as rules, not animation descriptions alone. Include triggers, response, feedback, failure handling, and recovery.
