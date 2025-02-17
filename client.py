from aiolimiter import AsyncLimiter
from client_openai import OpenAIClient
from client_openrouter import OpenRouterClient
from client_google_vertex import GoogleVertexClient

cache = {}

def get_client(model: dict):
    name = model["name"]
    provider = model["provider"]
    rate_limit = model["rate_limit"]
    key = (name, provider, rate_limit)

    if key in cache:
        return cache[key]

    limiter = AsyncLimiter(rate_limit, time_period=60)

    if provider == "openrouter":
        client = OpenRouterClient(name, limiter)
    elif provider == "openai":
        client = OpenAIClient(name, limiter)
    elif provider == "google_vertex":
        client = GoogleVertexClient(name, limiter)
    else:
        raise ValueError(f"Unknown provider: {provider}")

    cache[key] = client
    return client
