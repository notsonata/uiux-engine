---
name: design-system
description: Discover the design system already encoded in a product, consolidate it into DESIGN.md, define genuine gaps, and flag off-system values instead of silently inventing them. Internal reasoning skill used by ux-design, ux-review, and restyle.
license: MIT
metadata:
  version: "2.0.0"
  category: ui-ux
  visibility: internal
---

# Design System

## Purpose

Create one source of truth for visual and interaction decisions while respecting the system the product already has.

## Inspect before inventing

Before proposing tokens or components, inspect available evidence:
- CSS variables and theme files;
- Tailwind or framework configuration;
- typography definitions;
- spacing values and layout/grid rules;
- recurring component variants;
- icon library and sizing;
- motion/easing values;
- dark/light themes;
- the most reused components;
- existing design documentation.

Repeated values are evidence, not automatically good design. Separate intentional patterns from accidental drift.

## Foundation model

Consolidate the system from the bottom up:

1. **Foundations:** semantic color roles, typography, spacing/grid, radius/elevation, iconography, motion.
2. **Components:** variants and behavior built from those foundations.
3. **Patterns:** recurring composition such as forms, navigation, tables, dialogs, and empty states.
4. **Product surfaces:** screens composed from the same system.

### Color
Prefer semantic tokens such as background, surface, text, border, brand, and status roles over scattered raw values. Themes should change token values rather than component intent.

### Typography
Document named roles and a coherent scale, including weight and line-height. Avoid arbitrary one-off sizes.

### Spacing and grid
Use a consistent base rhythm. A 4 px or 8 px family is a useful default when the existing product does not already establish one. Define container, column, gutter, and breakpoint behavior only as needed by the product.

### Components
Every reusable interactive component must define relevant states such as default, hover, active/pressed, focus, disabled, selected, loading, and error.

### Iconography
Use a consistent icon family, optical weight, and sizing scheme. The visible glyph may be small while the interaction target remains comfortably usable.

### Motion
Define a small duration/easing vocabulary. Motion should communicate relationship or feedback, remain interruptible, and respect reduced-motion preferences.

## Accessibility and responsive rules

DESIGN.md must include:
- focus treatment;
- non-color status cues;
- contrast expectations;
- minimum practical target sizing;
- responsive transformation principles;
- keyboard interaction rules for custom controls where applicable.

## DESIGN.md

Write or update `DESIGN.md` at the project root with:
1. product/design principles;
2. visual character;
3. color tokens;
4. typography roles;
5. spacing/layout/grid;
6. radius, borders, elevation;
7. iconography;
8. component variants and states;
9. motion;
10. responsive and accessibility rules;
11. voice/copy conventions where established;
12. extension policy and known exceptions.

Each important value should have a reason, not merely a number.

## Gap questions

If the existing codebase leaves genuine ambiguity, ask at most five high-leverage questions. Do not interrogate the user about decisions already encoded in the product.

## Enforcement

After DESIGN.md exists:
- reuse system values;
- flag off-system values;
- either replace them with an existing token or record a deliberate extension;
- never create silent one-off tokens merely to make one screen look good.
