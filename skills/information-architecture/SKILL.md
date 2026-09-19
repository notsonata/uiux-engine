---
name: information-architecture
description: Organize content, navigation, labels, hierarchy, page structure, and task flows. Use for dashboards, settings, navigation, complex screens, content-heavy interfaces, or whenever users need to find, compare, understand, or prioritize information.
license: MIT
metadata:
  version: "1.0.0"
  category: ui-ux
---

# Information Architecture

## Objective

Make the product's structure match the user's mental model and task priority.

## Hierarchy pass

Classify content and actions as:
- **Primary:** necessary to understand or complete the current task.
- **Secondary:** useful supporting context or common follow-up actions.
- **Tertiary:** infrequent, advanced, contextual, or administrative detail.
- **Deferred:** should appear only after another decision or explicit request.

Do not solve hierarchy only with font size. Use order, grouping, spacing, position, contrast, persistence, and disclosure.

## Navigation

Choose navigation based on scope and frequency:
- persistent global navigation for major product areas;
- local navigation for sibling views within a section;
- tabs when users switch among peer views of the same object or scope;
- breadcrumbs for hierarchical location, not as a replacement for primary navigation;
- menus for lower-frequency actions, not the core task.

Do not hide a frequently used primary action in an overflow menu solely to simplify the screen.

## Labels

Use labels that describe the user's object or action. Prefer concrete verbs and nouns. Avoid internal implementation terms, ambiguous icons, clever wording, and unexplained abbreviations.

## Grouping

Group by user task, semantic relationship, lifecycle, or decision. Do not group solely because fields share a database model or API endpoint.

## Dense interfaces

For dashboards, tables, and administrative tools:
- prioritize scan paths;
- keep row actions predictable;
- distinguish selection from navigation;
- expose filters and scope clearly;
- preserve context while drilling down;
- allow density when users benefit from comparison and repeated work.

Do not equate whitespace with usability.

## Output

Provide:
- navigation model;
- hierarchy map;
- content groups;
- primary/secondary/tertiary actions;
- labels that need clarification;
- progressive disclosure decisions;
- proposed task flow or screen sequence.
