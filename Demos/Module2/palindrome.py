import re

def is_palindrome(s: str) -> bool:
    # Remove non-alphanumeric characters and convert to lowercase
    cleaned = re.sub(r'[^a-zA-Z0-9]', '', s.lower())
    # Compare the cleaned string with its reverse
    return cleaned == cleaned[::-1]

# Test cases
palindromes = ["madam", "eve", "bob", "33"]
non_palindromes = ["owl", "case", "teacher"]

print("Test cases:")
for word in palindromes:
    print(f"'{word}': {is_palindrome(word)}")
for word in non_palindromes:
    print(f"'{word}': {is_palindrome(word)}")

# User input
user_input = input("\nEnter a string to check if it's a palindrome: ")
result = is_palindrome(user_input)
print(f"The input '{user_input}' is {'a palindrome' if result else 'not a palindrome'}.")
