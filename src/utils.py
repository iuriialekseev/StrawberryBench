import re


def generate_word(additional_rs: int) -> str:
    base_word = "strawberry"
    new_r_sequence = "r" * (2 + additional_rs)
    return base_word[:7] + new_r_sequence + base_word[9:]


def generate_prompt(word: str, type: bool) -> str:
    prompt = f"How many r's are in '{word}'?\n"
    if type == "cot":
        prompt += "Think step by step.\n"
    prompt += "Provide the final answer in the format: <answer>number</answer>"
    return prompt


def evaluate_response(word: str, response: str) -> int:
    correct_count = word.lower().count("r")
    match = re.search(r"<answer>(\d+)</answer>", response, re.IGNORECASE)
    if match:
        try:
            return int(match.group(1)) == correct_count
        except ValueError:
            return False
    return False
