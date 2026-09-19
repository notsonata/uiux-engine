---
name: visual-character
description: Force deliberate visual choices across type, color, space, and finish so an interface reflects the product rather than an agent's default aesthetic. Internal reasoning skill used by ux-design and restyle.
user-invocable: false
license: MIT
metadata:
  version: "2.0.0"
  category: ui-ux
  visibility: internal
---
# Visual Character

## Purpose

Make visual direction an explicit product decision, not the statistically safest UI an agent happens to generate.

## Four axes

Make one coherent decision on each axis.

### Type
Define type roles, hierarchy, weight contrast, line-height, and reading density. Reuse the project's existing scale when it is coherent.

### Color
Use semantic roles rather than scattered raw values. Limit accents to what the product needs. Status meaning must not depend on color alone.

### Space
Choose a spacing rhythm and density appropriate to the task. Operational tools may be compact; editorial or exploratory screens may breathe more. Consistency matters more than maximizing whitespace.

### Finish
Decide border, radius, elevation, icon, illustration, texture, and motion treatment. Do not stack decorative effects without purpose.

## Existing system first

Read `DESIGN.md` and the actual component/theme implementation before proposing visual changes. If they conflict, identify the conflict instead of silently choosing a third style.

## Anti-default check

Do not default to:
- generic purple/blue gradients;
- glassmorphism;
- glow;
- excessive rounded cards;
- card-inside-card layouts;
- decorative sparkles or "AI" motifs;
- oversized whitespace unrelated to task needs.

These are allowed only when they are deliberate and product-appropriate.

## Lineup test

Ask: if this screen appeared beside ten competent AI-generated versions of the same prompt, what makes it recognizably this product?

If the answer is "nothing", strengthen the four axes without sacrificing usability.

## Restyle boundary

When invoked by `/restyle`, visual changes must preserve logic, component responsibility, information meaning, and copy meaning unless the user explicitly expands scope.
