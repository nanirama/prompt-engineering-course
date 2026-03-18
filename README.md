# Prompt Engineering Techniques Practice

This repo is a beginner-friendly site/collection for practicing common prompt-engineering techniques using the Gemini API.

## What’s inside

- `examples/`: Ready-to-run Python examples that demonstrate each prompting technique.
- `prompts/`: Prompt templates/guides for the same techniques (for copying/modifying).
- `assignments/`: Short practice tasks where you write your own prompt(s) and test locally.
- `practice.py`: A minimal “try it quickly” script.
- `helper.py`: Small utility for calling the Gemini model.

## Included techniques

- Zero-shot prompting
- One-shot prompting
- Few-shot prompting
- Multi-shot prompting
- Chain-of-Thought (CoT) prompting
- Zero-shot Chain-of-Thought prompting

## Prerequisites

- Python 3.x
- A Gemini API key (used by this project via `GEMINI_API_KEY`)

## Setup

1. Install dependencies:
   - `pip install -r requirements.txt`
2. Create a `.env` file in the repo root:
   - `GEMINI_API_KEY=your_api_key_here`

> Note: `.env` is intentionally ignored by git (see `.gitignore`).

## Run the examples

From the repo root (`F:\python\pe-practice`), run any of:

- `python examples\01_zero_shot.py`
- `python examples\02_one_shot.py`
- `python examples\03_few_shot.py`
- `python examples\04_multi_shot.py`
- `python examples\05_chain_of_thought.py`
- `python examples\06_zero_shot_cot.py`

Each script prints the prompt and the model response.

## Do the assignments

Each assignment file in `assignments/` includes:

- the task you must write (your own prompt)
- the rules for how that prompt should be structured
- what will be checked

Start with `assignments/01_zero_shot.md` and work through to `assignments/06_zero_shot_cot.md`.

## Tech notes

- The helper in `helper.py` uses `google-genai` and calls `client.models.generate_content(...)`.
- Prompts/exercises are designed to be small and easy to iterate on.

## License

See `LICENSE`.

