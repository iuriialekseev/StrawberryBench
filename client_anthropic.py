import os
from anthropic import AsyncAnthropic, InternalServerError
from tenacity import retry, stop_after_attempt, wait_exponential, retry_if_exception_type
from config import TEMPERATURE


class AnthropicClient:
    def __init__(self, model, rate_limiter):
        if model.startswith("anthropic/"):
            model = model.replace("anthropic/", "")

        self.rate_limiter = rate_limiter
        self.model = model
        self.client = AsyncAnthropic(api_key=os.environ.get("ANTHROPIC_API_KEY"))

    @retry(
        stop=stop_after_attempt(5),
        wait=wait_exponential(multiplier=2, min=2),
        retry=retry_if_exception_type((Exception, TypeError, InternalServerError))
    )
    async def query_model(self, prompt: str) -> str:
        await self.rate_limiter.acquire()

        response = await self.client.messages.create(
            model=self.model,
            max_tokens=8000,
            temperature=TEMPERATURE,
            messages=[{"role": "user", "content": prompt}],
        )

        # print(response)
        for block in response.content:
            if (
                hasattr(block, "type")
                and block.type == "text"
                and hasattr(block, "text")
            ):
                # print(block.text)
                return block.text

        return ""
