---
name: information-hierarchy
description: Rank information and actions by user intent, establish scanning order and density, and keep primary tasks from competing with secondary or destructive actions. Internal reasoning skill used by the public UX commands.
license: MIT
metadata:
  version: "2.0.0"
  category: ui-ux
  visibility: internal
---

# Information Hierarchy

## Purpose

Make the interface reflect task priority rather than schema shape.

## Rank everything

Classify visible information and actions as:

- **Primary:** required to understand or complete the current task.
- **Secondary:** useful supporting context or common follow-up.
- **Tertiary:** infrequent, advanced, administrative, or contextual.
- **Deferred:** shown only after explicit disclosure or a later step.

A destructive action is rarely primary simply because the backend exposes it next to Edit.

## Scan path

Define the order a user should perceive:
1. current scope and page purpose;
2. primary information;
3. primary action;
4. supporting context;
5. secondary and exceptional actions.

Use position, grouping, contrast, type, spacing, persistence, and disclosure together. Do not solve hierarchy with font size alone.

## Density

Choose density from the task:
- comparison and repeated operational work may justify compact layouts;
- reading and explanation need more breathing room;
- mobile should preserve priority, not mechanically stack the desktop UI.

For tables, expose only columns that support identification, comparison, status, or action. Move low-value metadata into details or disclosure.

## Navigation and labels

Use user language rather than implementation terms. Keep frequent destinations and actions visible. Overflow menus are for lower-frequency actions, not the main task.

## Accessibility and responsive behavior

Hierarchy must survive zoom, narrow viewports, keyboard navigation, and non-color perception. Do not make meaning depend on color or hover alone.

## Handoff

Return:
- primary / secondary / tertiary / deferred map;
- intended scan path;
- density choice;
- navigation/grouping decisions;
- items to remove, hide, or disclose.
