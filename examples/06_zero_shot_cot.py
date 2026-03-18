import sys
from pathlib import Path

# allow importing from project root
sys.path.append(str(Path(__file__).resolve().parent.parent))

from helper import get_completion

# prompt = """
# A freelancer earns ₹80,000 per month.
# Fixed monthly expenses are ₹35,000.
# He wants to save enough money to buy a laptop costing ₹1,20,000.

# Solve this step by step and tell:
# 1. Monthly savings
# 2. How many months it will take
# 3. One practical suggestion to reach the goal faster
# """

prompt = """
If a train travels 60km/h for 2.5 hours, then 80km/h for 1.5 hours, what is the total distance?
Let's think step by step and solve it.
"""

response = get_completion(prompt)

print("Prompt:")
print("-" * 50)
print(prompt)

print("\nResponse:")
print("-" * 50)
print(response)