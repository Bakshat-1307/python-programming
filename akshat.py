data = {'name': ['parker', 'smith', 'john', 'william'], 'percentage': [82, 98, 91, 87, 88], 'course': ['bsc', 'bed', 'mphill', 'ba', 'ba']}

# Create an empty dictionary to store the grouped data
grouped_data = {}

# Use zip() to combine the 'course' and 'percentage' lists
for course, percentage in zip(data['course'], data['percentage']):
    # If the course is not already a key in the dictionary, add it and initialize the list
    if course not in grouped_data:
        grouped_data[course] = [percentage]
    # If the course is already a key in the dictionary, append the percentage to the list
    else:
        grouped_data[course].append(percentage)

# Use a dictionary comprehension to calculate the average percentage for each course
average_percentage = {course: sum(percentages)/len(percentages) for course, percentages in grouped_data.items()}

# Print the result
print(average_percentage)

