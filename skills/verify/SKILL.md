---
name: verify
description: "Verify claims, calculations and conclusions with explicit evidence-based verdicts."
metadata:
  version: "1.0.0"
---

# verify

## Activation and scope
Use for `$verify`, the conversational alias `/VERIFY`, or requests clearly matching the description. A slash alias is text, not a registered native slash command. A term appearing only in quoted material does not select this workflow.

## Inputs
Claim, calculation or material; optionally evidence and reference date. Natural-language parameters are supported.

## Workflow
Break the material into verifiable claims. Recalculate quantities with tools when useful; check units, denominators and rounding. Use one verdict per claim: CONFIRMED, PARTIALLY CONFIRMED, UNCONFIRMED, FALSE or UNVERIFIABLE. UNCONFIRMED means insufficient evidence; FALSE requires a demonstrated contradiction; UNVERIFIABLE identifies a concrete access or method limitation. Explain evidence, sources and limits. Missing evidence alone does not make a claim false.

## Output
Claims, verdicts, supporting reasons and limits. Follow the requested format and language; use English when no language preference is available.

## Missing information and composition
Ask only for missing information that materially changes the result; continue independent work and label assumptions. Do not claim actions, access, checks or results that did not occur. Combine relevant skills in a logical order, reuse evidence and avoid loops. Research externally only when needed or requested. Activating a skill does not itself authorize sending, publishing, installing or modifying external resources; follow the scope authorized by the user.

## Example
`$verify Verify this claim: increasing from 80 to 100 is a 25% increase.`

## Acceptance
Meet the workflow and requested output, preserve constraints, and distinguish facts, interpretations, estimates and recommendations where relevant. Verify the result, not merely the existence of a file.
