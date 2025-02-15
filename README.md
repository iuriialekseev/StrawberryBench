# StrawberryBench

StrawberryBench is a benchmarking tool for evaluating language models on a simple reasoning task: counting the number of `r` characters in a modified version of `strawberry`.

Despite AI models excelling at complex tasks, this benchmark exposes gaps in fundamental processing, showing that there is still room for improvement even as models reach saturation in other benchmarks.

## Rationale

- Trivial for humans but surprisingly hard for LLMs.
- Highlights qualitative differences between human and AI language processing.
- Touches on key concepts: tokenization, attention, syntax vs. semantics, chain-of-thought, etc.
- Binary evaluation: answers are either correct or incorrect.
- Easily extendable, scalable, and modifiable.
- Simple implementation.

## Methodology

- Task prompt: `How many r's are in '[word]'?`.
- Required output format: `<answer>[number]</answer>`.
- Optional CoT prompt: `Think step by step`.
- Additional `r` characters are inserted to increase difficulty.
- Each variant is queried 20 times for statistical significance.
- Incorrect formatting counts as incorrect answer.
- Temperature set to 1.0

## Observations

- "Reasoner" models dominate the benchmark.
- Chain-of-thought improves performance in non-reasoner models.
- Most models (GPT-4o+, Gemini 2.0 Flash, Claude, Mistral, Llama) used CoT without explicit instructions.
- Models giving direct answers without CoT performed worst (Gemini 1.5 Flash/Pro, Grok 2, Qwen 2.5).
- StrawberryBench results correlate with other public benchmark results.

---

- OpenAI's o1 leads by a large margin.
- DeepSeek results are impressive, given its open-source nature and price.
- Google made major gains from Gemini 1.5 Flash to 2.0 Flash.
- Grok 2 and Claude 3.5 Sonnet showed the biggest CoT improvements.
- Grok 2 occasionally hallucinated absurdly long reasoning chains with a high numbers of `r`'s (200–300).

## Criticism

- _"This doesn't test real intelligence"_
  - It reveals how models process information, reason, and follow instructions - core aspects of intelligence.
- _"Just prompt better or use tools"_
  - A strong model should generalize well and get it right without hand-holding.
- _"This is just a tokenization issue"_
  - Large-scale character-level models are impractical.
- _"Strict formatting rules are unfair"_
    - A model that can't follow formatting risks failure elsewhere.
- _"Every model fails, so why test?"_
  - New models are improving. Benchmarks track progress and validate reasoning improvements.
- _"This distracts from bigger AI progress"_
  - Progress in science and engineering often comes from obsessing over what's not working.

## Prerequisites

- Python 3.x
- OpenRouter API key

## Installation

1. **Clone the repository:**

```bash
git clone https://github.com/iuriialekseev/StrawberryBench.git
cd StrawberryBench
```

2. **Install dependencies:**

```bash
python -m venv venv

# source ./venv/bin/activate

pip install -r requirements.txt
```

3. **Set your API key:**

StrawberryBench uses the OpenRouter API. Set your API key as an environment variable:
```bash
export OPENROUTER_API_KEY="your_openrouter_api_key_here"
```

## Configuration

Edit the `config.py` file to customize your benchmark settings.

## Usage

1. **Run the benchmark:**

```bash
python benchmark.py
```
This script generates prompts, queries the models asynchronously, aggregates the results, and outputs them.

2. **Generate plots:**

```bash
python plot.py
```

## Contributing

Contributions, bug reports, and feature requests are welcome!

Feel free to open an issue or submit a pull request.
