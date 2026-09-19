---
name: design-system
description: Discover, document, extend, or define a product design system including tokens, typography, spacing, color roles, components, variants, interaction states, and usage rules. Use before restyling an existing product or when repeated UI patterns are becoming inconsistent.
license: MIT
metadata:
  version: "1.0.0"
  category: ui-ux
---

# Design System

## Objective

Increase consistency without forcing every problem into the same component.

## Existing product discovery

Before creating new tokens or components, inspect available evidence such as:
- CSS variables or theme files;
- design tokens;
- Tailwind/theme configuration;
- component libraries;
- recurring spacing and typography values;
- button/input/table/dialog variants;
- focus, hover, selected, disabled, loading, and error states;
- icon sets;
- dark/light themes;
- existing documentation.

Separate intentional patterns from accidental repetition.

## Token model

Prefer semantic tokens over raw values for reusable decisions:
- foreground/background roles;
- surfaces;
- interactive/accent roles;
- status roles;
- borders/focus;
- typography roles;
- spacing/radius/elevation scales where useful.

Do not create a token for every isolated value.

## Components

A shared component is justified when multiple instances share meaning and behavior, not merely appearance.

Document:
- purpose;
- variants;
- states;
- content rules;
- accessibility behavior;
- responsive behavior;
- anti-patterns.

## Extension rule

When a new UI need appears:
1. reuse an existing pattern if semantics match;
2. add a variant if behavior is fundamentally the same;
3. create a new component when semantics or interaction materially differ;
4. avoid one-off overrides that silently fork the system.

## Output

Produce a concise system inventory and any proposed additions. If documenting from scratch, include principles, tokens, typography, components, interaction states, and examples of when not to use each pattern.
