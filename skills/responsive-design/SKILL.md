---
name: responsive-design
description: Adapt layouts, navigation, tables, controls, content priority, and interaction patterns across viewport sizes, devices, pointer types, and orientations. Use whenever an interface must work beyond one fixed screen size.
license: MIT
metadata:
  version: "1.0.0"
  category: ui-ux
---

# Responsive Design

## Objective

Preserve the user's task and information priority as space and input capability change.

## Start from constraints, not device labels

Consider:
- available width and height;
- touch vs fine pointer;
- keyboard presence;
- orientation;
- content length/localization;
- safe areas and browser chrome;
- persistent vs transient navigation.

Breakpoints should occur when the design stops working, not because a specific phone model exists.

## Transformation strategies

For each major region decide whether it should:
- remain;
- reflow;
- stack;
- wrap;
- scroll;
- collapse;
- move to another surface;
- become a different control;
- become sticky;
- be deferred behind explicit disclosure.

## Navigation

Preserve access to core destinations. Do not hide the primary task merely because the desktop navigation no longer fits.

## Tables and dense data

Choose based on user task:
- horizontal scrolling when column comparison matters;
- prioritized columns with disclosure when only a subset is essential;
- card/list transformation when row-level scanning matters more than cross-column comparison;
- separate detail view when the dataset cannot remain comprehensible in one compact surface.

Avoid converting every table to cards automatically.

## Forms

On small screens, preserve labels and validation context, use appropriate input modes, and avoid multi-column layouts that create confusing reading order.

## Output

For each major surface describe behavior at constrained, intermediate, and spacious widths. Specify transformations rather than vague breakpoint labels.
