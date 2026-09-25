# Campaign Validator quality-toolchain evaluation

**Time:** 75 minutes  
**Conditions:** individual work.

## Permitted resources

You may:

- use the internet to research technical questions;
- consult official documentation, including documentation for the tools used by
  the project; and
- consult the course guide and other materials shared by the professor.

You may not use generative AI assistance. This includes AI chatbots, AI coding
assistants, and AI-generated answers or summaries embedded in search tools. A
traditional search engine may be used to locate documentation or troubleshoot
specific errors, but the analysis, code, and written report must be your own
work.

## Scenario

You have received an incomplete Python application used to inspect advertising
campaign data. Treat the repository as a project that must be handed to another
developer: it must be reproducible, understandable, secure, and correct.

Assess the repository before changing it. Use the quality toolchain studied in
class to find problems, understand what each tool is reporting, and make the
project ready for handoff.

## Required outcome

At submission time:

- another developer can reconstruct the project environment from the versioned
  repository;
- every tool needed for the required quality checks is declared in the
  appropriate project dependency category and recorded in the lockfile;
- the application can be configured locally and executed successfully;
- the repository contains the project information and supporting files expected
  for a professional handoff;
- local configuration is documented safely;
- formatting, linting, static type checking, and automated tests all pass;
- running the verification tools does not produce additional file changes;
- the implementation satisfies the behavior described by the supplied tests;
- your repository documentation explains how to set up, configure, run, and
  verify the project;
- the project includes the MIT license with
  `Copyright (c) 2026 Campaign Validator Authors`; and
- `ANSWERS.md` contains your own concise account of the investigation and fixes.

The instructor will provide a synthetic value for `CAMPAIGN_ACCESS_TOKEN`.
Configure it locally so that you can run the application. The value is for this
evaluation only.



## README starting context

Your README should briefly explain what the project is before giving setup
instructions. You may copy or adapt the following context paragraph:

> Campaign Validator is a small Python command-line application for checking
> advertising campaign data. It normalizes a campaign name, calculates a
> click-through-rate percentage, counts campaign tags, and verifies that the
> local campaign access token is configured correctly.

To receive full README credit, add your own concise instructions explaining how
another developer should reconstruct the environment with `uv`, create and
configure the local `.env`, run the application, and execute the quality checks.
The explanation matters more than perfect wording or elaborate presentation.

## Working rules

- The supplied tests are part of the application contract. Do not modify,
  rename, or delete them.
- Correct failures by changing application code, project configuration, or
  missing project-supporting files as appropriate.
- Do not weaken the existing quality policy or hide findings with broad
  exclusions or suppressions.
- Inspect the result of every automated change before committing it.
- Ensure all completed work is integrated into `main` before submission.

## Git workflow

Git history is part of the evaluation. Use appropriately scoped task branches
and focused commits so that another developer can follow how the repository was
assessed and repaired. Integrate completed work into `main`.

Do not delete branches used during the evaluation. They must remain available
to the evaluator together with the complete history. Each student works in an
individual repository: branch protection, pull requests, reviews, and approval
workflows are not part of this evaluation.

Use the branch-naming and commit-message conventions practiced in class. Commit
boundaries should represent coherent changes; the number of commits by itself
is not evidence of atomic work.

Submit the complete Git repository using the mechanism specified by the
instructor. A copy containing only the final working tree is not sufficient.

## Investigation report

Complete `ANSWERS.md` as you work. Base the report on evidence from the
repository, tool output, tests, and Git history. Do not merely list commands:
explain what you learned from them and why each correction was appropriate.

## Bonus question

Configure the project's automated quality policy so that function parameters
which do not follow Python's `snake_case` naming convention are identified as
quality violations. Preserve every quality rule already enforced by the
project. Correct any resulting finding without suppressing the rule.

Determine which tool already included in the project is responsible for this
policy, identify the appropriate rule or rule family, and configure it correctly
using the investigation techniques covered in class. Document your complete
investigation trail in point 7 of `ANSWERS.md`.
