import os

# Debug switch
DEBUG = False


# Generic internet settings
TIMEOUT = 60
N_RETRIES = 3
COOLDOWN = 2
BACKOFF = 1.5


# Settings for OpenAI NLP models. Here, NLP tokens are not to be confused with user chat or image generation tokens

INITIAL_PROMPT = "In the style of Bad character, not married. You can respond with wit and irony in the same language in which you are addressed. You should always take on the image of the Glass family from Salinger's work. Use the language in which you are addressed. You respond in the language in which you are addressed'"

PRE_SUMMARY_PROMPT = "The above represents a conversation between you, an erudite and experienced MIT professor, and a human user. Please summarize the discussion for reference in the next post. Don't write a reply to the user or create a hint, just write a summary."

PRE_SUMMARY_NOTE = "Before the most recent messages, here's a summary of the conversation so far:"
POST_SUMMARY_NOTE = "The summary ends. And here are the most recent two messages from the conversation. You should generate the next response based on the conversation so far."

NLP_MODEL_NAME = "gpt-3.5-turbo-0125"                    # If Azure OpenAI, make sure this aligns with engine (deployment)
NLP_MODEL_ENGINE = os.getenv("OPENAI_ENGINE", None) # If Azure OpenAI, make sure this aligns with model (of deployment)
NLP_MODEL_MAX_TOKENS = 4000
NLP_MODEL_REPLY_MAX_TOKENS = 1000
NLP_MODEL_TEMPERATURE = 0.8
NLP_MODEL_FREQUENCY_PENALTY = 1
NLP_MODEL_PRESENCE_PENALTY = 1
NLP_MODEL_STOP_WORDS = ["Human:", "AI:"]