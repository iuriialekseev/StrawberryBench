import os
import json
import aiohttp
from retry import retry
from config import TEMPERATURE


class OpenRouterClient:
    def __init__(self, model, rate_limiter):
        self.rate_limiter = rate_limiter
        self.model = model
        self.base_url = "https://openrouter.ai/api/v1/chat/completions"
        self.api_key = os.environ.get("OPENROUTER_API_KEY")
        self.headers = {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json",
        }

    @retry(tries=5, delay=10, exceptions=(Exception, TypeError))
    async def query_model(self, prompt: str) -> str:
        await self.rate_limiter.acquire()

        payload = {
            "model": self.model,
            "temperature": TEMPERATURE,
            "messages": [{"role": "user", "content": prompt}],
            "include_reasoning": True,
        }

        async with aiohttp.ClientSession() as session:
            async with session.post(
                self.base_url, headers=self.headers, data=json.dumps(payload)
            ) as response:
                response.raise_for_status()
                result = await response.json()
                # print(result)
        return result["choices"][0]["message"]["content"] or ""
