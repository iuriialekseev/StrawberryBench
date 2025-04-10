import asyncio
import json

from tqdm import tqdm

from client import get_client
from config import ADDITIONAL_RS, ITERATIONS, MODELS
from utils import evaluate_response, generate_prompt, generate_word


async def run_single_iteration(model_info: dict, additional_rs: int, word: str, pbar) -> tuple:
    prompt = generate_prompt(word, model_info["type"])
    client = get_client(model_info)
    response = await client.query_model(prompt)
    correct = evaluate_response(word, response)
    pbar.update(1)
    return model_info["name"], additional_rs, 1 if correct else 0, model_info["type"]


async def main():
    tasks = []
    total = len(ADDITIONAL_RS) * len(MODELS) * ITERATIONS

    with tqdm(total=total, desc="Benchmarking", unit="iteration") as pbar:
        for model_info in MODELS:
            for additional_rs in ADDITIONAL_RS:
                modified_word = generate_word(additional_rs)
                for _ in range(ITERATIONS):
                    tasks.append(run_single_iteration(model_info, additional_rs, modified_word, pbar))

        results = await asyncio.gather(*tasks)

    summary = {}
    for model, additional_rs, correct, type in results:
        key = (model, additional_rs, type)
        summary.setdefault(key, []).append(correct)

    final_results = []
    for (model, additional_rs, type), correctness in summary.items():
        accuracy = (sum(correctness) / len(correctness)) * 100
        final_results.append(
            {
                "model": model,
                "additional_rs": additional_rs,
                "accuracy": int(accuracy),
                "type": type,
            }
        )

    formatted_json = ",\n".join(json.dumps(result, separators=(", ", ": ")) for result in final_results)
    print(formatted_json)


if __name__ == "__main__":
    asyncio.run(main())
