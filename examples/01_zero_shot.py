"""
Module 01 — Prompting Guidelines
Example: Zero-shot prompting
"""

import sys
from pathlib import Path

# allow importing from project root
sys.path.append(str(Path(__file__).resolve().parent.parent))

from helper import get_completion

# prompt = """
# Translate the following text to French:

# The stock market closed higher today, driven by strong earnings reports from major technology companies.
# """

# prompt = """
# Classify the sentiment of this review as POSITIVE, NEGATIVE OR NEUTRAL:

# The product arrived on time, but the packaging was damaged and the instructions were confusing.
# """

# prompt = """
# Write a function that takes a list of numbers and returns the average of the numbers.
# """

prompt = """
You are a professional financial analyst.
Explain what 'P/E ratio' means to a beginner investor in simple terms in one paragraph.
"""

response = get_completion(prompt)

print("Prompt:")
print("-" * 50)
print(prompt)

print("\nResponse:")
print("-" * 50)
print(response)