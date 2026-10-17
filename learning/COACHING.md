# Coaching guide

Use this guide when a learner asks to study Universal Entanglement Readout. The [milestone map](MILESTONES.md) fixes the project's 30 understanding targets. The [Watrous bridge](WATROUS_BRIDGE.md) supplies the source connections and local explanations. The [model](../science/model.md) and linked proofs remain authoritative for scientific claims.

The map is common to all readers, including LLMs. Adapt explanations, examples, and targeted learning within a milestone. Keep its target, phase, and place in the map fixed. A request to furnish or review the repository prepares these materials; a request to begin or resume study starts coaching.

## Start or resume

Read the current milestone, its dependencies, the relevant bridge section, and the canonical scientific source before preparing a round. Begin at M01 when no prior learning record exists. When resuming, recover the actual milestone and unfinished attempt from the learner's private record. Distinguish demonstrated passes from self-assessment, earlier unrelated tutorials, and statements such as “continue.”

A useful starting request is: “Start M01 using this coaching guide.” A continuation can name the current milestone or ask to resume its saved attempt. Supplying the repository revision with a handoff keeps the explanation tied to the same claims and map.

## Every round: Revise → Learn → Test

**Revise** supplies the definitions, notation, assumptions, and earlier results needed for the present target. Revision is mandatory on the initial attempt, each learning round, and every challenge retry.

**Learn** explains the relevant mechanism or addresses the exposed misconception. Before a challenge, keep Revise and Learn compact while supplying enough context for an inference. During targeted learning, develop the explanation and a small example as needed. Neither preparation should reveal the challenge's answer key.

**Test** uses selection-only questions. Every question has exactly four options and exactly one correct answer. Ask for conceptual understanding, an operational consequence, a changed-condition prediction, or a justified distinction. Require at most minimal mental calculation. Supplying a definition makes the question self-contained; copying the correct answer verbatim from the preceding paragraph makes it uninformative.

A challenge is one complete Test set within one round. Displaying its questions one at a time does not create a new Revise → Learn → Test round for each question.

## Challenge and learning rules

Each milestone has one challenge, with as many attempts as needed. Its first attempt contains **two questions** after the compact Revise → Learn introduction. Passing requires **every answer in that attempt to be correct**.

| Current event | Feedback and next step |
|---|---|
| A challenge question is answered | Record the selection and present the next question. Withhold correctness and explanations until the complete set has been answered. |
| The complete challenge is all correct | Report the result, mark this milestone passed, and continue to the next target with a fresh two-question initial challenge, or declare completion after M30. |
| The complete challenge contains an incorrect answer | Report and explain the result, increment this milestone's failed-challenge count once, and begin a targeted learning phase. Complete the whole challenge before this transition. |
| A learning-test question is answered | Give correctness feedback and an explanation immediately, including after an incorrect answer. Use it to guide the next teaching step. |
| The planned learning phase ends | Prepare a fresh challenge attempt, including Revise → Learn. Carry any remaining misconception into this preparation. |
| A challenge is interrupted | Preserve its answers and pending question and resume the same attempt. An interruption is not a failed challenge. |
| A question is ambiguous, malformed, or unreadable | Repair or replace the item without charging a conceptual error to the learner. Keep the attempt's valid answers and intended size. |

After a failed challenge, choose **1–3 learning rounds**, guided by the milestone's suggested intensity and the actual errors. Each contains Revise, Learn, and a **one-question Test**. This is a bounded teaching phase, not a second passing gate. Correct the final learning error immediately even if it occurs in the last planned round, then address it in the next challenge's preparation. Repeated learning-test errors do not extend this phase indefinitely.

Only a **completed failed challenge** increases the next challenge size. If that count in the current milestone is `f`, use `min(2 + f, 6)` questions:

| Completed failed challenges | Next challenge size | Passing requirement |
|---|---:|---|
| 0 | 2 | All 2 correct |
| 1 | 3 | All 3 correct |
| 2 | 4 | All 4 correct |
| 3 | 5 | All 5 correct |
| 4 or more | 6 | All 6 correct |

A learning-test error does not change `f`. Failure at the six-question cap leads to another 1–3-round learning phase and a fresh six-question challenge. A pass resets the count for the next milestone. Correct answers from separate failed attempts are not combined into a pass, and learning-test success does not itself pass a milestone.

## Question design and delivery

Choose the question set and its single-answer keys before displaying a challenge. Keep those keys private until the full-set feedback. During the set, acknowledge a received selection neutrally without hints about its correctness. Finish the set even when one recorded answer is incorrect.

Use plausible conceptual distractors. Retry questions should test fresh applications of the target, not repeat an earlier item with shuffled option labels. Larger attempts broaden the evidence within the same milestone; they do not require longer calculations. Keep question identifiers distinct across milestones, attempts, and learning rounds so a submitted answer is consumed only once.

Prefer genuine native answer-selection controls that submit the learner's choice to the conversation and support the required feedback timing. A challenge needs delayed full-set feedback; a learning round needs immediate feedback. Do not promise that decorative buttons, ordinary links, or Markdown option lists submit an answer. If a compatible native control is unavailable, explain that limitation briefly and accept a single option letter, A–D. Free-text questions and corrections remain welcome, but a conceptual explanation is not compulsory in place of an answer selection.

When a question is challenged, inspect its wording, assumptions, display, and answer key before scoring. If an ambiguity affects earlier feedback, correct the record and resume from the repaired assessment. A technical presentation failure does not demonstrate a misunderstanding of the science.

## Teaching this particular project

Use the local-to-global order in [M01–M30](MILESTONES.md). The background phase ends by assembling the state domain, apparatus, retained record, and resource count. The narrative phase ends by explaining how the geometric obstruction and statistical penalty fit into that same task.

Keep the following ideas visible when selecting examples:

| Conceptual target | What a useful question should distinguish |
|---|---|
| Retained measurement data | One fixed setting, one outcome label, and the complete probability vector; retained randomized-setting labels also count. |
| Physical and algebraic operations | A fixed positive POVM effect, a partial transpose used in a proof, and whitening by an unknown marginal used only in the analysis. |
| Rank and dimension | The promise that the qutrit marginal is invertible, the unrestricted qubit–qutrit domain, and the larger-dimensional lower bound. |
| Geometry and continuation | A physical neighborhood where positivity is controlled, the diagonal normal slice, and a polynomial identity extended to a rank variety. |
| Binary rigidity and statistics | A determinant factor, at least fourth-order flatness on the hard pure-state path, and the effect-uniform argument required for the best fixed-block minimax rate. |
| The promise-gap result | Copies per binary block, the behavior allowed inside the excluded gap, exact probability resolution, and the uncontrolled statistical margin. |
| Scientific evidence | A proof step, an imported theorem, an exact finite check, and an interpretation supported by those results. |

For example, a question can change which classical labels are retained and ask how the resource description changes. Another can change the domain from all mixed states to a nonzero distance promise and ask which theorem still applies. These are question-design targets; the actual items should be written for the active milestone after reading its sources.

The textbook supplies foundations, the bridge develops the route into the project, and the scientific pages establish the claims. Follow the [attribution record](../references/RELATED_WORK.md) for imported results. In particular, preserve the prior status of the four-copy two-qubit determinant construction. The six-copy qubit–qutrit constructions establish sufficiency, and the fixed-block statistical theorem requires exact universality on all two-qubit mixed states.

## Private learning record

Keep individual attempts separate from the public common map. The repository contains instructions and scientific material, not a presumed score for its author or another reader. Preserve the following state privately when a coaching session actually occurs:

| Field | Purpose |
|---|---|
| Repository revision and map identity | Identify the exact scientific claims and understanding targets used. |
| Learner, current milestone, and phase | Distinguish challenge preparation, an active challenge, targeted learning, and a completed milestone. |
| Passed milestone IDs and evidence | Record actual complete successful attempts. |
| Failed-challenge count in the current milestone | Determine the next challenge's size. |
| Current attempt ID, question set, private keys, and selections | Resume a partial challenge without early feedback, repeating a scored selection, or changing the intended questions. |
| Planned learning-round count, active round, pending item, and feedback | Keep the one-question item's ID, options, private key, and any received selection; enforce the 1–3-round bound and preserve immediate correction of learning errors. |
| Question repairs and the exact next action | Resume correctly after a display error, clarification, or interruption. |

Do not manufacture missing answers after an interruption. A missing or inconsistent record calls for a focused clarification about the current attempt. Existing documented passes should not be silently erased. A substantive change to the science may require updating a target and identifying the affected prior evidence; ordinary misconceptions do not change the map.

## Completion

Passing all **30 milestones** completes this project-understanding tutorial. State that completion explicitly. M30 is the integrative endpoint; an additional final examination or new curriculum is not required.

The shortest route contains **60 challenge questions**, with all initial attempts passed. Learning rounds and retries increase the total; repeated failures give no fixed maximum course length. The six-question cap applies to one challenge attempt.

Completion records the conceptual evidence gathered by this tutorial. It does not certify every technical calculation, independently validate the research, or imply that every possible specialist question can be answered. Repository completion and tutorial completion are separate outcomes.
