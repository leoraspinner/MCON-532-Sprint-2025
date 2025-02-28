from palindrome import is_palindrome

def test_palindrome():
    """Run test cases for the palindrome checker."""
    palindromes = ["madam", "eve", "bob", "33"]
    non_palindromes = ["owl", "case", "teacher"]

    print("Test cases:")
    for word in palindromes:
        print(f"'{word}': {is_palindrome(word)}")
    for word in non_palindromes:
        print(f"'{word}': {is_palindrome(word)}")

#  test cases
if __name__ == "__main__":
    test_palindrome()

    # User input
    user_input = input("\nEnter a string to check if it's a palindrome: ")
    result = is_palindrome(user_input)
    print(f"The input '{user_input}' is {'a palindrome' if result else 'not a palindrome'}.")