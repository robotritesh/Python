import re

# Find all email addresses in a text
text = "Contact us at info@example.com or support@domain.com"
emails = re.findall(r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b', text)
print("Found Emails:", emails)
