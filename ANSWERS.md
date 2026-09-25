# Evaluation report

Answer concisely in your own words. Refer to concrete evidence from the project
and its tools.

## 1. Initial assessment

What was incomplete, incorrectly configured, or failing when you first examined
the repository? Explain how you discovered each item.

- `uv run mypy` failed with: `Failed to spawn: mypy` → `mypy` was configured in `[tool.mypy]` but missing from the dev dependency group and from `uv.lock`.
- `ruff format --check` reported that `metrics.py` would be reformatted (leading blank lines).
- `pytest`: **3 failed**, **6 passed**.
    - CTR returned **0.05** instead of **5.0**.
    - Tag count returned **2** instead of **3**.
    - `normalize_campaign_name(None)` raised `AttributeError`.
- Running the app failed with: `CAMPAIGN_ACCESS_TOKEN is required` → no local `.env` and no documentation for the variable.
- `ls -a` showed no `README`, `LICENSE` or `.env.example`.

## 2. Toolchain evidence

What did the quality chain tools contribute to
your investigation? Give relevant examples and distinguish the kinds of
problems they can detect.

- **Ruff formatter**: layout only (the blank lines at the top of `metrics.py`).
- **Ruff linter**: code-quality rules (E, F, I); initially clean, it later caught the naming issue once **N803** was enabled (bonus).
- **mypy (strict)**: found `union-attr` on `CampaignName.strip()` because the parameter can be `None`, without running the code.
- **pytest**: checks behavior against the contract; it found the percentage and off-by-one bugs, which are well typed and well formatted, so no static tool saw them. The `None` bug was found by both mypy (statically) and pytest (at runtime).

## 3. Corrections

Describe the implementation and configuration corrections you made. For each
important correction, connect the original problem, the evidence, and the
resulting behavior.

- Added `mypy` with `uv add --dev mypy` → `pyproject.toml` and `uv.lock` updated → mypy runs.
- Formatted `metrics.py` with `ruff` after reviewing the diff (whitespace only).
- CTR: `100 * clicks / impressions` → test expects `5.0` → passes; app prints `5.00%`.
- None name: return `""` when the name is `None` → test passes and mypy’s `union-attr` disappears.
- Added `.gitignore` for `.env`

## 4. Reproducibility and local configuration

Explain how the completed repository lets another developer reconstruct,
configure, run, and verify the project safely.

- `pyproject.toml` separates **runtime** dependencies (`python-dotenv`) from **dev** tools (`ruff`, `mypy`, `pytest`).
- `uv.lock` pins versions, so `uv sync --locked` recreates the same environment.
- The token is stored only in a local `.env` file (ignored by Git), created from `.env.example`.
- The `README` provides the setup, run, and verification commands.
- I verified this by deleting `.venv`, then re-syncing and re-running the full toolchain.

## 5. Git workflow

Explain how your branches and commits divide the work into reviewable changes.
Mention how the completed work was integrated.

## 6. Limits of verification

Why does a completely passing quality toolchain provide useful evidence but not
proof that the program contains no defects?

## 7. Bonus question

Document the investigation trail for the bonus question:

1. How did you decide which project tool was responsible for this type of
   policy?
2. What documentation or repository evidence did you consult?
3. Which rule or rule family did you identify, and what behavior does it check?
4. What configuration did you change, and how did you verify that every existing
   rule remained enabled?
5. What new diagnostic appeared after the configuration change?
