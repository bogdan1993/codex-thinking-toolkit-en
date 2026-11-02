---
name: fresh
description: "Check whether information remains current and distinguish publication, update and event dates."
metadata:
  version: "1.0.0"
---

# fresh

## Activation and scope
Use for `$fresh`, the conversational alias `/FRESH`, or requests clearly matching the description. A slash alias is text, not a registered native slash command. A term appearing only in quoted material does not select this workflow.

## Inputs
Claims or material; optionally reference date, time window and domain. Natural-language parameters are supported.

## Workflow
Establish the reference date from the user context. Identify claims liable to change. Check current versions and sources, distinguishing publication, update, event and access dates. A recently updated page can describe an old event. Mark outdated information while preserving useful historical context. State which freshness checks access limitations prevent.

## Output
Current information, relevant dates and verification limits. Follow the requested format and language; use English when no language preference is available.

## Missing information and composition
Ask only for missing information that materially changes the result; continue independent work and label assumptions. Do not claim actions, access, checks or results that did not occur. Combine relevant skills in a logical order, reuse evidence and avoid loops. Research externally only when needed or requested. Activating a skill does not itself authorize sending, publishing, installing or modifying external resources; follow the scope authorized by the user.

## Example
`$fresh Check whether the prices in this document are still current.`

## Acceptance
Meet the workflow and requested output, preserve constraints, and distinguish facts, interpretations, estimates and recommendations where relevant. Verify the result, not merely the existence of a file.
