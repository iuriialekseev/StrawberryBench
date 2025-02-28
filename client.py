from aiolimiter import AsyncLimiter
from client_anthropic import AnthropicClient
from client_openai import OpenAIClient
from client_openrouter import OpenRouterClient
from client_google_vertex import GoogleVertexClient

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
    elif client == "anthropic":
        client = AnthropicClient(name, limiter)
    else:
        raise ValueError(f"Unknown client: {client}")

    cache[key] = client
    return client
