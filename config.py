MODELS = [
    # { "name": "anthropic/claude-3.5-haiku", "provider": "openrouter", "cot": False, "rate_limit": 1000 },
    # { "name": "anthropic/claude-3.5-haiku", "provider": "openrouter", "cot": True, "rate_limit": 1000 },

    # { "name": "anthropic/claude-3.5-sonnet", "provider": "openrouter", "cot": False, "rate_limit": 1000 },
    # { "name": "anthropic/claude-3.5-sonnet", "provider": "openrouter", "cot": True, "rate_limit": 1000 },

    # { "name": "mistralai/mistral-large", "provider": "openrouter", "cot": False, "rate_limit": 1000 },
    # { "name": "mistralai/mistral-large", "provider": "openrouter", "cot": True, "rate_limit": 1000 },

    # { "name": "mistralai/mistral-small-24b-instruct-2501", "provider": "openrouter", "cot": False, "rate_limit": 1000 },
    # { "name": "mistralai/mistral-small-24b-instruct-2501", "provider": "openrouter", "cot": True, "rate_limit": 1000 },

    # { "name": "x-ai/grok-2-1212", "provider": "openrouter", "cot": False, "rate_limit": 1000 },
    # { "name": "x-ai/grok-2-1212", "provider": "openrouter", "cot": True, "rate_limit": 1000 },

    # { "name": "deepseek/deepseek-r1", "provider": "openrouter", "cot": False, "rate_limit": 1000 },
    # { "name": "deepseek/deepseek-r1", "provider": "openrouter", "cot": True, "rate_limit": 1000 },

    # { "name": "deepseek/deepseek-r1-distill-llama-70b", "provider": "openrouter", "cot": False, "rate_limit": 1000 },
    # { "name": "deepseek/deepseek-r1-distill-llama-70b", "provider": "openrouter", "cot": True, "rate_limit": 1000 },

    # { "name": "meta-llama/llama-3.3-70b-instruct", "provider": "openrouter", "cot": False, "rate_limit": 1000 },
    # { "name": "meta-llama/llama-3.3-70b-instruct", "provider": "openrouter", "cot": True, "rate_limit": 1000 },

    # { "name": "qwen/qwen-2.5-72b-instruct", "provider": "openrouter", "cot": False, "rate_limit": 1000 },
    # { "name": "qwen/qwen-2.5-72b-instruct", "provider": "openrouter", "cot": True, "rate_limit": 1000 },

    # { "name": "openai/gpt-3.5-turbo", "provider": "openai", "cot": False, "rate_limit": 1000 },
    # { "name": "openai/gpt-3.5-turbo", "provider": "openai", "cot": True, "rate_limit": 1000 },

    # { "name": "openai/gpt-4o-mini", "provider": "openai", "cot": False, "rate_limit": 1000 },
    # { "name": "openai/gpt-4o-mini", "provider": "openai", "cot": True, "rate_limit": 1000 },

    # { "name": "openai/gpt-4o", "provider": "openai", "cot": False, "rate_limit": 1000 },
    # { "name": "openai/gpt-4o", "provider": "openai", "cot": True, "rate_limit": 1000 },

    # { "name": "openai/chatgpt-4o-latest", "provider": "openai", "cot": False, "rate_limit": 1000 },
    # { "name": "openai/chatgpt-4o-latest", "provider": "openai", "cot": True, "rate_limit": 1000 },

    # { "name": "openai/chatgpt-o1-mini", "provider": "openai", "cot": False, "rate_limit": 1000 },
    # { "name": "openai/chatgpt-o1-mini", "provider": "openai", "cot": True, "rate_limit": 1000 },

    # { "name": "openai/chatgpt-o1", "provider": "openai", "cot": False, "rate_limit": 1000 },
    # { "name": "openai/chatgpt-o1", "provider": "openai", "cot": True, "rate_limit": 1000 },

    # { "name": "openai/chatgpt-o3-mini", "provider": "openai", "cot": False, "rate_limit": 1000 },
    # { "name": "openai/chatgpt-o3-mini", "provider": "openai", "cot": True, "rate_limit": 1000 },

    # { "name": "google/gemini-1.5-flash-001", "provider": "google_vertex", "cot": False, "rate_limit": 1000 },
    # { "name": "google/gemini-1.5-flash-001", "provider": "google_vertex", "cot": True, "rate_limit": 1000 },

    # { "name": "google/gemini-1.5-flash-002", "provider": "google_vertex", "cot": False, "rate_limit": 1000 },
    # { "name": "google/gemini-1.5-flash-002", "provider": "google_vertex", "cot": True, "rate_limit": 1000 },

    # { "name": "google/gemini-1.5-pro-001", "provider": "google_vertex", "cot": False, "rate_limit": 30 },
    # { "name": "google/gemini-1.5-pro-001", "provider": "google_vertex", "cot": True, "rate_limit": 30 },

    # { "name": "google/gemini-2.0-flash-001", "provider": "google_vertex", "cot": False, "rate_limit": 500 },
    # { "name": "google/gemini-2.0-flash-001", "provider": "google_vertex", "cot": True, "rate_limit": 500 },

    # { "name": "google/gemini-2.0-flash-thinking-exp-01-21", "provider": "google_vertex", "cot": False, "rate_limit": 5 },
    # { "name": "google/gemini-2.0-flash-thinking-exp-01-21", "provider": "google_vertex", "cot": True, "rate_limit": 5 },

    # { "name": "google/gemini-2.0-flash-lite-preview-02-05", "provider": "google_vertex", "cot": False, "rate_limit": 5 },
    # { "name": "google/gemini-2.0-flash-lite-preview-02-05", "provider": "google_vertex", "cot": True, "rate_limit": 5 },

    # { "name": "google/gemini-2.0-pro-exp-02-05", "provider": "google_vertex", "cot": False, "rate_limit": 5 },
    # { "name": "google/gemini-2.0-pro-exp-02-05", "provider": "google_vertex", "cot": True, "rate_limit": 5 },
]

# The additional characters to insert in the word
ADDITIONAL_RS = range(0, 10)

ITERATIONS = 20
TEMPERATURE = 1.0
