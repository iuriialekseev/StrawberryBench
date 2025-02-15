MODELS = [
    # 'openai/gpt-3.5-turbo',
    # 'openai/gpt-4o-mini',
    # 'openai/gpt-4o',
    # 'openai/chatgpt-4o-latest',
    # 'openai/o1-mini',
    # 'openai/o1',
    # 'openai/o3-mini',
    # 'openai/o3-mini-high',
    # 'google/gemini-flash-1.5',
    # 'google/gemini-2.0-flash-001',
    # 'google/gemini-pro-1.5',
    # 'anthropic/claude-3.5-haiku',
    # 'anthropic/claude-3.5-sonnet',
    # 'meta-llama/llama-3.3-70b-instruct',
    # 'mistralai/mistral-large',
    # 'x-ai/grok-2-1212',
    # 'deepseek/deepseek-r1',
    # 'qwen/qwen-2.5-72b-instruct',
]

# The additional `r` characters to insert in the word
ADDITIONAL_RS_RANGE = range(0, 11)

# Number of query iterations for statistical significance
ITERATIONS = 20

# Whether to include a chain-of-thought prompt in the queries
COT = True
