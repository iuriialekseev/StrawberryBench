import asyncio
from config import MODELS, ADDITIONAL_RS_RANGE, ITERATIONS, COT
from utils import generate_word, generate_prompt, evaluate_response
from client import query_model
from tqdm import tqdm
import json


async def run_single_iteration(model: str, additional_rs: int, word: str, pbar) -> tuple:
    prompt = generate_prompt(word)
    response = await query_model(model, prompt)
    correct = evaluate_response(word, response)
    pbar.update(1)
    return model, additional_rs, 1 if correct else 0


async def main():
    tasks = []
    total = len(ADDITIONAL_RS_RANGE) * len(MODELS) * ITERATIONS

    with tqdm(total=total, desc="Benchmarking", unit="iteration") as pbar:
        for additional_rs in ADDITIONAL_RS_RANGE:
            word = generate_word(additional_rs)
            for model in MODELS:
                for _ in range(ITERATIONS):
                    tasks.append(run_single_iteration(model, additional_rs, word, pbar))
        results = await asyncio.gather(*tasks)

    summary = {}
    for model, additional_rs, correct in results:
        key = (model, additional_rs)
        summary.setdefault(key, []).append(correct)

    final_results = []
    for (model, additional_rs), correctness in summary.items():
        accuracy = (sum(correctness) / len(correctness)) * 100
        final_results.append({
            "model": model,
            "additional_rs": additional_rs,
            "accuracy": int(accuracy),
            "cot": COT
        })

    formatted_json = ',\n'.join(json.dumps(result, separators=(', ', ': ')) for result in final_results)
    print(formatted_json)

if __name__ == "__main__":
    asyncio.run(main())
