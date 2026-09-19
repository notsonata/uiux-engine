# UX Specification

## 1. Intent brief
- User:
- Trigger/context:
- Primary job:
- Information/decision needed:
- Worst plausible mistake:
- Constraints:
- Assumptions:

## 2. Primary flow
1.
2.
3.

## 3. Wireframe

Use a low-fidelity structural representation. Show hierarchy, regions, controls, and states, not final decoration.

```text
┌────────────────────────────────────────────┐
│ Screen title                         Action │
├────────────────────────────────────────────┤
│ Primary task/content                       │
│                                            │
├────────────────────────────────────────────┤
│ Supporting / secondary content             │
└────────────────────────────────────────────┘
```

## 4. Information hierarchy
- Primary:
- Secondary:
- Tertiary:
- Deferred/advanced:
- Intended scan path:
- Density:

## 5. Screen/component inventory
| Surface | Purpose | Primary action | Key information |
|---|---|---|---|

## 6. Six-state coverage
- Loading:
- Empty:
- Partial:
- Error:
- Success:
- Offline:

### Conditional states
- Initial:
- Validation:
- Disabled/unavailable:
- Permission/session:
- Destructive pending:
- Stale/conflict:
- Background-job states:

## 7. Interaction and affordance
- Navigation:
- Selection:
- Editing:
- Destructive actions:
- Confirmation/undo:
- Feedback:
- Keyboard/focus:
- Touch/pointer behavior:

## 8. Form UX
- Fields/grouping:
- Defaults:
- Validation timing:
- Error/recovery:
- Progressive disclosure:

## 9. Design system + visual character
- DESIGN.md constraints:
- Type:
- Color:
- Space/density:
- Finish:
- Off-system extensions, if any:

## 10. Responsive + accessibility requirements
- Narrow layout transformation:
- Spacious layout behavior:
- Semantic/keyboard requirements:
- Focus:
- Contrast/non-color cues:
- Motion alternatives:
- Target sizing:

## 11. Acceptance criteria
- [ ] Primary task is obvious
- [ ] Worst-case action is proportionally protected
- [ ] Six required states were considered
- [ ] Error recovery preserves work where practical
- [ ] Keyboard/focus paths are viable
- [ ] Responsive behavior preserves task priority
- [ ] Components follow DESIGN.md or record a deliberate extension
