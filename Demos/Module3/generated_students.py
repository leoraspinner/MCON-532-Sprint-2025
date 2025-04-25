student_data = {
    101: {"name": "Alice", "grades": [85, 90, 88], "gpa": round((sum([85, 90, 88]) / len([85, 90, 88])) / 25, 2)},
    102: {"name": "Bob", "grades": [75, 80, 82], "gpa": round((sum([75, 80, 82]) / len([75, 80, 82])) / 25, 2)},
    103: {"name": "Charlie", "grades": [90, 92, 95], "gpa": round((sum([90, 92, 95]) / len([90, 92, 95])) / 25, 2)}
}

print(student_data)