import os
from openai import AsyncOpenAI
from tenacity import retry, stop_after_attempt, wait_exponential, retry_if_exception_type
from config import TEMPERATURE


class OpenAIClient:
    def __init__(self, model, rate_limiter):
        if model.startswith("openai/"):
            model = model.replace("openai/", "")

        self.rate_limiter = rate_limiter
        self.model = model
        self.client = AsyncOpenAI(api_key=os.environ.get("OPENAI_API_KEY"))

    @retry(
        stop=stop_after_attempt(5),
        wait=wait_exponential(multiplier=2, min=2),
        retry=retry_if_exception_type((Exception, TypeError))
    )
    async def query_model(self, prompt: str) -> str:
        await self.rate_limiter.acquire()

        response = await self.client.chat.completions.create(
            messages=[{"role": "user", "content": prompt}],
            model=self.model,
            temperature=TEMPERATURE,
        )

        # print(response)
        return response.choices[0].message.content or ""
