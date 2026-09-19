---
name: feedback-and-affordance
description: Make actions look actionable, states legible, feedback immediate, and destructive behavior proportionally protected. Internal reasoning skill used by the public UX commands.
license: MIT
metadata:
  version: "2.0.0"
  category: ui-ux
  visibility: internal
---

# Feedback and Affordance

## Purpose

Users should understand what they can do, what just happened, and what the system is doing next.

## Affordance

A user should be able to distinguish:
- interactive from static;
- selected from unselected;
- editable from read-only;
- enabled from disabled;
- expanded from collapsed;
- saved from unsaved.

Do not depend on hover alone for essential actions. Icon-only actions need understandable labels or accessible names.

## Feedback timing

Direct manipulation should react immediately. For common local interactions, visible response should begin within roughly 100 ms whenever technically feasible.

For longer work:
- show progress when delay is noticeable;
- keep status persistent for background jobs;
- separate queued, running, completed, failed, and cancelled outcomes when those distinctions matter.

## Destructive actions

Use protection proportional to consequence:
- undo for quick reversible operations;
- confirmation for high-cost or irreversible operations;
- typed confirmation only for exceptional destructive risk;
- recovery windows or soft deletion when feasible.

Do not burden routine low-risk actions with confirmation dialogs.

## Status communication

Use more than color for meaningful state. Combine label, shape, icon, position, or other cues as appropriate.

## Motion

Motion should explain change, relationship, or feedback. It must not block the user. Respect reduced-motion preferences.

## Handoff

Return affordance issues, feedback rules, destructive-action protection, and status/motion requirements.

## Pattern references

For destructive actions, bulk/row actions, overlays, or feedback behavior, consult `../../references/patterns/INDEX.md` and load only the relevant action, feedback, or overlay patterns.
