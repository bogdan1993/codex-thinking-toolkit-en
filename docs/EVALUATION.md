# Evaluation scenarios and release checks

## Checks performed for v1.0.0

- All 20 SKILL.md files passed the bundled Codex skill validator during preparation.
- Installer tests passed locally (16 cases). They do not test model reasoning.
- The instructions were reviewed for preserving evidence, scope and optional profile inputs across editions.
- No separate Codex sessions were run for the scenarios below. Treat them as evaluation cases, not a completed benchmark or a promise of model behavior.

## Behavior to evaluate in a real session

Run a scenario with the indicated skill and raw material, then assess the observable result. Add a missing-input variant and a boundary variant; ask for clarification or a qualified result where the missing information changes the outcome.

| Skill | Scenario | Observable acceptance |
|---|---|---|
| `master` | Coordinate comparison and a recommendation from two supplied quotes. | Uses only relevant stages and respects a request for analysis only. |
| `research` | Two reports disagree; only one has underlying data. | Reads accessible evidence and identifies unresolved disagreement. |
| `fresh` | An updated article discusses an older event. | Distinguishes publication/update dates from the event; reports access limits. |
| `verify` | 80 grows to 100; a second claim has no source. | Confirms 25% growth and marks the second claim unconfirmed, not false. |
| `source-check` | Three articles copy one press release. | Counts one origin rather than three independent confirmations. |
| `expert-lens` | A proposed AI rollout faces adoption and reliability issues. | Applies relevant perspectives without claiming real expert consultation. |
| `analyze` | Retention and training rise together without controls. | Identifies association without declaring causation. |
| `assumptions` | A budget assumes 100 paid registrations. | Separates the assumption from confirmed revenue and explains sensitivity. |
| `compare` | A costs 100 and B 150; budget 120, reliability unknown. | Uses common criteria, flags unknown reliability and budget constraint. |
| `critique` | A plan has a clear goal but no owner for a dependency. | Preserves the useful goal and prioritizes the concrete missing ownership. |
| `red-team` | A launch depends on one supplier. | Explains plausible failure mechanisms and mitigations; takes no intrusive action. |
| `decide` | A fits the budget; B exceeds it; neither has quality evidence. | Makes a conditional recommendation and identifies missing decisive evidence. |
| `plan` | Plan a workshop; no attendee availability is given. | Provides dependencies and acceptance without inventing schedules or sending invites. |
| `next` | Venue booked; agenda and invitations missing. | Prioritizes concrete feasible steps and dependencies. |
| `checklist` | A report needs selectable text and accurate tables. | Defines observable evidence and leaves completion unchecked without proof. |
| `optimize` | Improve a supplied process with one useful approval step. | Preserves effective steps and distinguishes expected from measured benefits. |
| `audience` | Explain two-factor authentication to beginners. | Adapts depth without distorting facts; asks or labels assumptions for undefined audiences. |
| `rewrite` | Make an email warmer without adding commitments. | Preserves qualifications and commitments; requests the original if absent. |
| `content-suite` | Turn one supported idea into LinkedIn and video copy. | Adapts structure by channel without inventing experiences or statistics. |
| `brand` | Only a logo is provided; brand tokens are absent. | Does not label guessed colors/fonts as official and uses optional supplied profiles. |
