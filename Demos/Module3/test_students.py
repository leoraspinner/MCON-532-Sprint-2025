# Creating a Python dictionary using dictionary comprehension
students = {
    1: {"name": "Alice", "grades": [85, 90, 88, 92], "gpa": round(sum([85, 90, 88, 92]) / len([85, 90, 88, 92]) / 25, 2)},
    2: {"name": "Bob", "grades": [78, 82, 79, 88], "gpa": round(sum([78, 82, 79, 88]) / len([78, 82, 79, 88]) / 25, 2)},
    3: {"name": "Charlie", "grades": [90, 95, 92, 88], "gpa": round(sum([90, 95, 92, 88]) / len([90, 95, 92, 88]) / 25, 2)},
    4: {"name": "David", "grades": [85, 88, 90, 87], "gpa": round(sum([85, 88, 90, 87]) / len([85, 88, 90, 87]) / 25, 2)},
    5: {"name": "Eve", "grades": [92, 94, 88, 85], "gpa": round(sum([92, 94, 88, 85]) / len([92, 94, 88, 85]) / 25, 2)}
}

# Importing necessary libraries for unit testing
import unittest

# Create a test class for unit testing
class TestStudentDictionary(unittest.TestCase):

    # Test to check if the dictionary contains the correct number of students
    def test_number_of_students(self):
        self.assertEqual(len(students), 5)

    # Test to check if each student has a "name", "grades", and "gpa"
    def test_student_attributes(self):
        for student_id in students:
            student = students[student_id]
            self.assertIn("name", student)
            self.assertIn("grades", student)
            self.assertIn("gpa", student)

    # Test to check if the "grades" list contains only integers
    def test_grades_type(self):
        for student_id in students:
            grades = students[student_id]["grades"]
            for grade in grades:
                self.assertIsInstance(grade, int)

# Run the unit tests
if __name__ == '__main__':
    unittest.main()