MODELS = [
    # { "name": "anthropic/claude-3.5-haiku", "client": "openrouter", "type": "nocot" },
    # { "name": "anthropic/claude-3.5-sonnet", "client": "openrouter", "type": "nocot" },
    # { "name": "anthropic/claude-3.7-sonnet", "client": "openrouter", "type": "nocot", "settings": { "rate_limit": 25 } },
    # { "name": "google/gemini-1.5-flash-002", "client": "google_vertex", "type": "nocot" },
    # { "name": "google/gemini-1.5-pro-001", "client": "google_vertex", "type": "nocot" },
    # { "name": "google/gemini-2.0-flash-001", "client": "google_vertex", "type": "nocot" },
    # { "name": "google/gemini-2.0-flash-lite-001", "client": "google_vertex", "type": "nocot" },
    # { "name": "google/gemini-2.0-pro-exp-02-05", "client": "google_vertex", "type": "nocot", "settings": { "rate_limit": 10 } },
    # { "name": "meta-llama/llama-3.1-405b-instruct", "client": "openrouter", "type": "nocot" },
    # { "name": "meta-llama/llama-3.3-70b-instruct", "client": "openrouter", "type": "nocot" },
    # { "name": "mistralai/mistral-large-2411", "client": "openrouter", "type": "nocot" },
    # { "name": "openai/chatgpt-4o-latest", "client": "openai", "type": "nocot" },
    # { "name": "openai/gpt-3.5-turbo", "client": "openai", "type": "nocot" },
    # { "name": "openai/gpt-4.5-preview", "client": "openai", "type": "nocot" },
    # { "name": "openai/gpt-4o", "client": "openai", "type": "nocot" },
    # { "name": "openai/gpt-4o-mini", "client": "openai", "type": "nocot" },
    # { "name": "qwen/qwen-max", "client": "openrouter", "type": "nocot", "settings": { "rate_limit": 30 } },
    # { "name": "x-ai/grok-2-1212", "client": "openrouter", "type": "nocot" },

    # { "name": "anthropic/claude-3.5-haiku", "client": "openrouter", "type": "cot" },
    # { "name": "anthropic/claude-3.5-sonnet", "client": "openrouter", "type": "cot" },
    # { "name": "anthropic/claude-3.7-sonnet", "client": "openrouter", "type": "cot", "settings": { "rate_limit": 25 } },
    # { "name": "google/gemini-1.5-flash-002", "client": "google_vertex", "type": "cot" },
    # { "name": "google/gemini-1.5-pro-001", "client": "google_vertex", "type": "cot" },
    # { "name": "google/gemini-2.0-flash-001", "client": "google_vertex", "type": "cot" },
    # { "name": "google/gemini-2.0-flash-lite-001", "client": "google_vertex", "type": "cot" },
    # { "name": "google/gemini-2.0-pro-exp-02-05", "client": "google_vertex", "type": "cot", "settings": { "rate_limit": 10 } },
    # { "name": "meta-llama/llama-3.1-405b-instruct", "client": "openrouter", "type": "cot" },
    # { "name": "meta-llama/llama-3.3-70b-instruct", "client": "openrouter", "type": "cot" },
    # { "name": "mistralai/mistral-large-2411", "client": "openrouter", "type": "cot" },
    # { "name": "openai/chatgpt-4o-latest", "client": "openai", "type": "cot" },
    # { "name": "openai/gpt-3.5-turbo", "client": "openai", "type": "cot" },
    # { "name": "openai/gpt-4.5-preview", "client": "openai", "type": "cot" },
    # { "name": "openai/gpt-4o", "client": "openai", "type": "cot" },
    # { "name": "openai/gpt-4o-mini", "client": "openai", "type": "cot" },
    # { "name": "qwen/qwen-max", "client": "openrouter", "type": "cot", "settings": { "rate_limit": 30 } },
    # { "name": "x-ai/grok-2-1212", "client": "openrouter", "type": "cot" },

    # { "name": "anthropic/claude-3-7-sonnet-20250219", "client": "anthropic", "type": "reasoning", "settings": {"rate_limit": 4} },
    # { "name": "deepseek/deepseek-r1", "client": "openrouter", "type": "reasoning" },
    # { "name": "deepseek/deepseek-r1-distill-llama-70b", "client": "openrouter", "type": "reasoning" },
    # { "name": "google/gemini-2.0-flash-thinking-exp-01-21", "client": "google_vertex", "type": "reasoning", "settings": { "rate_limit": 10 } },
    # { "name": "openai/o1", "client": "openai", "type": "reasoning" },
    # { "name": "openai/o1-mini", "client": "openai", "type": "reasoning" },
    # { "name": "openai/o3-mini", "client": "openai", "type": "reasoning" },
    # { "name": "openai/o3-mini-high", "client": "openai", "type": "reasoning" },
]

# The additional characters to insert in the word
ADDITIONAL_RS = range(0, 10)

ITERATIONS = 20
TEMPERATURE = 1.0
