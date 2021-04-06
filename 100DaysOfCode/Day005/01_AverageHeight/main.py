# Python infinity: https://www.geeksforgeeks.org/python-infinity/

if __name__ == "__main__":
    student_heights = [180, 124, 165, 173, 189, 169, 146]
    print(f'Student heights info: {student_heights}')

    min_height = float('+inf')
    max_height = float('-inf')
    sum_height = 0.0
    for height in student_heights:
        if height < min_height:
            min_height = height
        if height > max_height:
            max_height = height
        sum_height += height
    print(f'Minimum height: {min_height}')
    print(f'Maximum height: {max_height}')
    print(f'Summation of heights: {sum_height}')

    avg_height = round(sum_height / len(student_heights))
    print(f'Average of heights: {avg_height}')
