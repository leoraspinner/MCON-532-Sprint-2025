import re

def is_palindrome(s: str) -> bool:
    # Remove non-alphanumeric characters and convert to lowercase
    cleaned = re.sub(r'[^a-zA-Z0-9]', '', s.lower())
    # Compare the cleaned string with its reverse
    return cleaned == cleaned[::-1]
