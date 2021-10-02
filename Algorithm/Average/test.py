with open('test.txt') as input_file:
    test_case = int(input_file.readline())
    for _ in range(test_case):
        N = int(input_file.readline())
        scores = list(map(int, input_file.readline().split()))
        scores.sort()
        max_grade = scores[-1]
        sum_grade = sum(scores) / max_grade * 100
        avg_grade = sum_grade / N
        print(avg_grade)
