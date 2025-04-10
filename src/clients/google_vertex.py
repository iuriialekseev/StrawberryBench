import os

import vertexai
from tenacity import (
    retry,
    retry_if_exception_type,
    stop_after_attempt,
    wait_exponential,
)
from vertexai.generative_models import GenerationConfig, GenerativeModel

from src.config import TEMPERATURE


class GoogleVertexClient:
    def __init__(self, model, rate_limiter):
        if model.startswith("google/"):
            model = model.replace("google/", "")

        vertexai.init(
            project=os.getenv("VERTEX_PROJECT_ID"),
            location=os.getenv("VERTEX_LOCATION"),
        )

        self.rate_limiter = rate_limiter
        self.vertex_model = GenerativeModel(
            model,
            generation_config=GenerationConfig(
                temperature=TEMPERATURE,
            ),
        )

    @retry(
        stop=stop_after_attempt(5),
        wait=wait_exponential(multiplier=2, min=2),
        retry=retry_if_exception_type((Exception, TypeError)),
    )
    async def query_model(self, prompt: str) -> str:
        await self.rate_limiter.acquire()
        response = await self.vertex_model.generate_content_async(prompt)
        text = response.candidates[0].content.text
        return text or ""
