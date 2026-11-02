---
name: next
description: "Identify and prioritize concrete next actions from the current state."
metadata:
  version: "1.0.0"
---

# next

## Activation and scope
Use for `$next`, the conversational alias `/NEXT`, or requests clearly matching the description. A slash alias is text, not a registered native slash command. A term appearing only in quoted material does not select this workflow.

## Inputs
Goal and current state; optionally blockers, deadline and resources. Natural-language parameters are supported.

## Workflow
Choose feasible actions prioritized by impact, urgency, dependencies and effort. Give each action a concrete object and observable outcome. If context is missing, ask only for information that changes the first action or state the assumption used. Avoid generic advice and unnecessarily rebuilding a complete plan.

## Output
Prioritized next actions and the outcome each should produce. Follow the requested format and language; use English when no language preference is available.

## Missing information and composition
Ask only for missing information that materially changes the result; continue independent work and label assumptions. Do not claim actions, access, checks or results that did not occur. Combine relevant skills in a logical order, reuse evidence and avoid loops. Research externally only when needed or requested. Activating a skill does not itself authorize sending, publishing, installing or modifying external resources; follow the scope authorized by the user.

## Example
`$next We have the venue but no agenda or invitations. What comes next?`

## Acceptance
Meet the workflow and requested output, preserve constraints, and distinguish facts, interpretations, estimates and recommendations where relevant. Verify the result, not merely the existence of a file.
