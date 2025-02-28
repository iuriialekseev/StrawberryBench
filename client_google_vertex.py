import os
import vertexai
from vertexai.generative_models import GenerativeModel, GenerationConfig
from retry import retry
from config import TEMPERATURE


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

    @retry(tries=5, delay=10, exceptions=(Exception, TypeError))
    async def query_model(self, prompt: str) -> str:
        await self.rate_limiter.acquire()
        response = await self.vertex_model.generate_content_async(prompt)
        text = response.candidates[0].content.text
        return text or ""
