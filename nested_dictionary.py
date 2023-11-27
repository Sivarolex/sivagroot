student_info = {
    'Alice': {
        'age': 20,
        'grade': 'A',
        'courses': ['Math', 'English', 'History']
    },
    'Bob': {
        'age': 22,
        'grade': 'B',
        'courses': ['Physics', 'Chemistry', 'Biology']
    },
    'Charlie': {
        'age': 21,
        'grade': 'A-',
        'courses': ['Computer Science', 'Statistics', 'Psychology']
    }
}

# Accessing information in the nested dictionary
print("Alice's age:", student_info['Alice']['age'])
print("Bob's courses:", student_info['Bob']['courses'])
print("Charlie's grade:", student_info['Charlie']['grade'])