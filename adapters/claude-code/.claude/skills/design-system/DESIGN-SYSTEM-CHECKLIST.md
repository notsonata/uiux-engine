# Design System Checklist

Use this as a compact reference when `design-system` creates or audits DESIGN.md.

## Foundations
- Define semantic color roles rather than scattering raw color values.
- Establish named typography roles with a coherent size, weight, and line-height hierarchy.
- Use a consistent spacing rhythm. Prefer the product's existing rhythm; if none exists, a small base unit such as 4 px with larger steps built from it is a practical starting point.
- Define container/grid behavior only to the level the product needs.
- Use one coherent icon family and sizing language.
- Define a small motion vocabulary with purposeful easing/durations.

## Components
For each reusable interactive component, document:
- purpose;
- variants;
- default;
- hover where applicable;
- active/pressed;
- focus;
- disabled;
- selected;
- loading/error when applicable;
- responsive behavior;
- keyboard and touch behavior.

## Accessibility
- Do not communicate status with color alone.
- Preserve visible focus.
- Keep interaction targets comfortably usable even when glyphs are visually small.
- Respect reduced-motion preferences.
- Treat contrast and readable type as system constraints.

## System maintenance
- Prefer semantic tokens over one-off values.
- Document why a new token or variant exists.
- Reuse before extending.
- Extend before forking.
- Record intentional exceptions.
- Support theme switching through semantic roles rather than component-specific colors.

## Product-state polish
Verify that the system accounts for loading and empty states, not only ideal populated screens.
