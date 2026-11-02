---
name: decide
description: "Turn evidence and comparisons into a reasoned recommendation with explicit uncertainty."
metadata:
  version: "1.0.0"
---

# decide

## Activation and scope
Use for `$decide`, the conversational alias `/DECIDE`, or requests clearly matching the description. A slash alias is text, not a registered native slash command. A term appearing only in quoted material does not select this workflow.

## Inputs
Decision, alternatives and evidence; optionally criteria and constraints. Natural-language parameters are supported.

## Workflow
Recommend the option supported by the evidence and objective. Explain why it is preferable, its tradeoffs, remaining risks and what new information could change the recommendation. When evidence is insufficient, make a conditional recommendation or identify the decisive missing information. Do not present uncertainty as certainty or treat a recommendation as permission to execute.

## Output
A supported recommendation or conditional decision with tradeoffs and limits. Follow the requested format and language; use English when no language preference is available.

## Missing information and composition
Ask only for missing information that materially changes the result; continue independent work and label assumptions. Do not claim actions, access, checks or results that did not occur. Combine relevant skills in a logical order, reuse evidence and avoid loops. Research externally only when needed or requested. Activating a skill does not itself authorize sending, publishing, installing or modifying external resources; follow the scope authorized by the user.

## Example
`$decide A costs 100, B costs 150 and the budget is 120. Recommend an option.`

## Acceptance
Meet the workflow and requested output, preserve constraints, and distinguish facts, interpretations, estimates and recommendations where relevant. Verify the result, not merely the existence of a file.
