from helper import get_completion

prompt = """
Summarize the following and explain below with 4 points:

Prompt engineering helps us write clear instructions for AI models.
"""

response = get_completion(prompt)
print(response)