import os

from google import genai
from google.genai.types import GenerateContentConfig
from tenacity import (
    retry,
    retry_if_exception_type,
    stop_after_attempt,
    wait_exponential,
)

from src.config import TEMPERATURE


class GoogleStudioClient:
    def __init__(self, model, rate_limiter):
        if model.startswith("google/"):
            model = model.replace("google/", "")

        self.rate_limiter = rate_limiter
        self.client = genai.Client(api_key=os.getenv("GENAI_API_KEY"))
        self.model = model

    @retry(
        stop=stop_after_attempt(5),
        wait=wait_exponential(multiplier=2, min=2),
        retry=retry_if_exception_type((Exception, TypeError)),
    )
    async def query_model(self, prompt: str) -> str:
        await self.rate_limiter.acquire()
        response = await self.client.aio.models.generate_content(
            model=self.model,
            contents=prompt,
            config=GenerateContentConfig(
                temperature=TEMPERATURE,
            ),
        )

        print(response)
        return response.text or ""
