with open('test.txt', 'r') as input_file:
    N = int(input_file.readline())
    numbers = list(map(int, input_file.readline().split()))
    M = int(input_file.readline())
    targets = list(map(int, input_file.readline().split()))
    results = [0] * M

    numbers.sort()
    for idx, target in enumerate(targets):
        lo, hi = (0, N - 1)
        while lo <= hi:
            mid = int((lo + hi) / 2)
            if numbers[mid] == target:
                results[idx] = 1
                break

            if target < numbers[mid]:
                hi = mid - 1
            else:
                lo = mid + 1

    for ret in results:
        print(ret)
