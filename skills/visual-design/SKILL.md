---
name: visual-design
description: Define or improve visual hierarchy, typography, spacing, color roles, density, surfaces, iconography, imagery, and motion after product structure is understood. Use for visual refinement, restyling, art direction, or improving a UI that is functionally sound but visually weak or inconsistent.
license: MIT
metadata:
  version: "1.0.0"
  category: ui-ux
---

# Visual Design

## Objective

Create a coherent visual language that reinforces hierarchy, comprehension, product character, and interaction state.

## Prerequisite

Do not use visual polish to conceal unresolved information architecture or interaction problems. If the primary action, hierarchy, or state behavior is unclear, resolve those first.

## Visual hierarchy

Establish clear differences among:
- page/screen title;
- section title;
- primary content;
- supporting metadata;
- actions;
- status;
- secondary or de-emphasized content.

Avoid giving every region a card, border, background, or heading when spacing and grouping are sufficient.

## Typography

Define roles, not arbitrary one-off sizes. Consider:
- display/title;
- heading levels;
- body;
- label/control;
- metadata/caption;
- numeric or tabular data where relevant.

Use line length, line height, weight, and spacing to support reading and scanning.

## Spacing and density

Use a consistent spacing rhythm. Density should reflect task type:
- exploratory/marketing interfaces can tolerate more breathing room;
- professional tools may benefit from compact, comparison-friendly layouts;
- touch interfaces need enough target space even when visually dense.

## Color

Define color by role:
- canvas/surface;
- text hierarchy;
- border/separator;
- accent/brand;
- interactive;
- success/warning/error/info;
- selection/focus.

Do not introduce multiple decorative accents without semantic purpose.

## Surface treatment

Use elevation, border, radius, blur, and shadow consistently. Avoid nesting multiple card surfaces by default.

## Product character

Choose 2-4 explicit traits, such as precise, editorial, utilitarian, calm, technical, playful, premium, dense, or expressive. Translate traits into concrete decisions rather than adding fashionable effects.

Avoid defaulting to generic AI-product tropes such as gratuitous purple gradients, glow, glassmorphism, excessive rounded cards, or decorative sparkles unless they genuinely fit the product.

## Motion

Use motion to explain spatial or state change, preserve continuity, or provide feedback. Keep it brief and interruptible. Respect reduced-motion preferences.

## Output

Provide visual principles and token-level direction precise enough to implement, while allowing the existing design system to override generic defaults.
