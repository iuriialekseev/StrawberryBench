import os
from openai import AsyncOpenAI
from retry import retry
from config import TEMPERATURE

class OpenRouterClient:
    def __init__(self, model, rate_limiter):
        self.rate_limiter = rate_limiter
        self.model = model
        self.client = AsyncOpenAI(
            base_url="https://openrouter.ai/api/v1",
            api_key=os.environ.get("OPENROUTER_API_KEY")
        )

    @retry(tries=2, delay=1)
    async def query_model(self, prompt: str) -> str:
        await self.rate_limiter.acquire()

        response = await self.client.chat.completions.create(
            messages=[{"role": "user", "content": prompt}],
            model=self.model,
            temperature=TEMPERATURE,
        )

        print(response)
        return response.choices[0].message.content or ""
