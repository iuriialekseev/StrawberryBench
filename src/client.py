from aiolimiter import AsyncLimiter

from clients.anthropic import AnthropicClient
from clients.google_studio import GoogleStudioClient
from clients.google_vertex import GoogleVertexClient
from clients.openai import OpenAIClient
from clients.openrouter import OpenRouterClient

cache = {}


def get_client(model: dict):
    name = model["name"]
    client = model["client"]
    rate_limit = model.get("settings", {}).get("rate_limit", 100)
    key = (name, client)

    if key in cache:
        return cache[key]

    limiter = AsyncLimiter(rate_limit, time_period=60)

    if client == "openrouter":
        client = OpenRouterClient(name, limiter)
    elif client == "openai":
        client = OpenAIClient(name, limiter)
    elif client == "google_vertex":
        client = GoogleVertexClient(name, limiter)
    elif client == "google_studio":
        client = GoogleStudioClient(name, limiter)
    elif client == "anthropic":
        client = AnthropicClient(name, limiter)
    else:
        raise ValueError(f"Unknown client: {client}")

    cache[key] = client
    return client
