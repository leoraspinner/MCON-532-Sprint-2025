from src.open_api_client import get_openai_client
from pprint import pprint

client = get_openai_client()
pprint(vars(client))

def prompt1():
    prompt = ("Create a Python dictionary where each student ID maps to another dictionary containing: "
              "\"name\": Student's name (string)"
              " \"grades\": A list of grades (integers). "
              "\"gpa\": The GPA, calculated as (sum of grades / number of grades) / 25, rounded to two decimal places.")
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": prompt}]
    )
    return response.choices[0].message.content

def prompt2():
    prompt = """Create a Python dictionary where each student ID maps to another dictionary containing:
    "name": Student's name (string)
    "grades": A list of grades (integers).
    "gpa": The GPA, calculated as (sum of grades / number of grades) / 25, rounded to two decimal places.
    Use dictionary comprehension to construct the dictionary."""

    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": prompt}]
    )
    return response.choices[0].message.content

def prompt3():
    prompt = """Create a Python dictionary where each student ID maps to another dictionary containing:
    "name": Student's name (string)
    "grades": A list of grades (integers).
    "gpa": The GPA, calculated as (sum of grades / number of grades) / 25, rounded to two decimal places.
    Use dictionary comprehension, and then format the output using print() so that the student data is displayed in a well-structured format."""

    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": prompt}]
    )
    return response.choices[0].message.content

def prompt4():
    prompt = """Create a Python dictionary where each student ID maps to another dictionary containing:
    "name": Student's name (string)
    "grades": A list of grades (integers).
    "gpa": The GPA, calculated as (sum of grades / number of grades) / 25, rounded to two decimal places.
    Use dictionary comprehension to create it.
    Then, write unit tests using unittest to verify that:
    The dictionary contains the correct number of students.
    Each student has a "name", "grades", and "gpa".
    The "grades" list contains only integers.
    Ensure test coverage using IntelliJ's built-in coverage tool."""

    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": prompt}]
    )
    return response.choices[0].message.content

def main():
    print("Prompt 1 Output:")
    output1 = prompt1()
    pprint(output1)

    print("\nPrompt 2 Output:")
    output2 = prompt2()
    pprint(output2)

    print("\nPrompt 3 Output:")
    output3 = prompt3()
    print(output3)

    print("\nPrompt 4 Output:")
    output4 = prompt4()
    print(output4)

    # Generate generated_students.py
    with open('generated_students.py', 'w') as f:
        f.write(output2)

    # Generate test_students.py
    with open('test_students.py', 'w') as f:
        f.write(output4)

    # Saves prompt4 output to output.txt
    with open('output.txt', 'w') as f:
        f.write(output4)

if __name__ == "__main__":
    main()