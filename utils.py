import re

def generate_word(additional_rs: int) -> str:
    base_word = "strawberry"
    new_r_sequence = "r" * (2 + additional_rs)
    return base_word[:7] + new_r_sequence + base_word[9:]


def generate_prompt(word: str, cot: bool) -> str:
    prompt = f"How many r's are in '{word}'?\n"
    if cot:
        prompt += "Think step by step.\n"
    prompt += "Please provide the final answer in the format: <answer>[number]</answer>"
    return prompt


def evaluate_response(word: str, response: str) -> int:
    correct_count = word.lower().count('r')
    match = re.search(r"<answer>\s*(\d+)\s*</answer>", response, re.IGNORECASE)
    if match:
        try:
            return int(match.group(1)) == correct_count
        except ValueError:
            return False
    return False
