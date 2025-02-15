import os
from retry import retry
from openai import AsyncOpenAI


client = AsyncOpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key=os.environ.get("OPENROUTER_API_KEY")
)


@retry(tries=3, backoff=2)
async def query_model(model: str, prompt: str) -> str:
    response = await client.chat.completions.create(
        messages=[
            {
                "role": "user",
                "content": prompt,
            }
        ],
        model=model,
        temperature=1,
    )
    content = response.choices[0].message.content
    return content or ""
