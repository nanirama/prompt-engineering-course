import sys
from pathlib import Path

# allow importing from project root
sys.path.append(str(Path(__file__).resolve().parent.parent))

from helper import get_completion

# prompt = """
# Convert the sentence into a more professional business tone.

# Example:
# Input: send me the file fast
# Output: Could you please share the file at your earliest convenience?

# Now do the same for:
# Input: I need this work today only
# Output:
# """


# prompt = """
# Input: 'I've been waiting 3 weeks for my order!'
# Output: CATEGORY: Complaint | URGENCY: High | DEPT: Logistics

# Now do this:
# Input: 'Do you offer student discounts?'

# """

# prompt = """
# Extract company name, industry, and revenue from the text.

# Example:
# Input: 'Infosys, a global IT giant, reported revenues of $18B in FY2024.'
# Output: { name: 'Infosys', industry: 'IT Services', revenue: '$18B' }

# Now do this:
# Input: 'Tata Motors, a leading automaker, posted revenues of ₹4.4 lakh crore in FY2024.'
# Output:
# """

prompt = """
Write a product description in a punchy, benefit-first style.

Example:
Input: Running shoes, lightweight, cushioned sole
Output: Run further. Hurt less. Our ultra-light runners with cloud cushioning keep you going when others stop.

Now do this:
Input: Noise-cancelling headphones, 30hr battery, foldable
Output:
"""

response = get_completion(prompt)

print("Prompt:")
print("-" * 50)
print(prompt)

print("\nResponse:")
print("-" * 50)
print(response)