import os

from google import genai
from google.genai.types import GenerateContentConfig, ThinkingConfig
from tenacity import (
    retry,
    retry_if_exception_type,
    stop_after_attempt,
    wait_exponential,
)

from src.config import TEMPERATURE

class GoogleVertexClient:
    MAX_THINKING_BUDGET = 24_000

    def __init__(self, model: str, rate_limiter):
        if model.startswith("google/"):
            model = model.replace("google/", "")

        self.rate_limiter = rate_limiter
        self.model = model

        self.client = genai.Client(
            vertexai=True,
            project=os.getenv("VERTEX_PROJECT_ID"),
            location=os.getenv("VERTEX_LOCATION"),
        )

        self.generation_config = GenerateContentConfig(
            temperature=TEMPERATURE,
            thinking_config=ThinkingConfig(
                thinking_budget=self.MAX_THINKING_BUDGET
            ),
        )


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
            config=self.generation_config,
        )

        return response.text or ""
