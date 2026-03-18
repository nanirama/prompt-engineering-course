import sys
from pathlib import Path

# allow importing from project root
sys.path.append(str(Path(__file__).resolve().parent.parent))

from helper import get_completion

# prompt = """
# Tag each message with one label only:
# Billing, Technical Issue, Delivery, Account Access

# Message: I was charged twice for the same subscription.
# Label: Billing

# Message: My order still has not arrived.
# Label: Delivery

# Message: I cannot reset my password.
# Label: Account Access

# Message: The application freezes after login.
# Label: Technical Issue

# Message: I am unable to download the invoice.
# Label: Billing

# Now tag this:
# Message: The website keeps showing an error when I try to sign in.
# Label:
# """

prompt = """
Assign priority P1/P2/P3 to support tickets.

Message: 'Website is completely down for all users'
Label: P1 (Critical)

Message: 'Wrong invoice sent to customer'
Label: P2 (High)

Message: 'Profile picture won't upload'
Label: P3 (Low)

Message: 'Payment gateway failing for 30% of transactions'
Label: P1 (Critical)

Message: 'Dark mode toggle not working on iPad'
Label: P3 (Low)

4. 'Payment gateway failing for 30% of transactions' → P1 (Critical)
5. 'Dark mode toggle not working on iPad' → P3 (Low)

Now assign priority:
'Bulk email notifications sending to wrong customer IDs'

"""

response = get_completion(prompt)

print("Prompt:")
print("-" * 50)
print(prompt)

print("\nResponse:")
print("-" * 50)
print(response)