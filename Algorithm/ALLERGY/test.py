def show_food_table(food_table):
    for row in food_table:
        print(row)


with open('test.txt', 'r') as input_file:
    test_case = int(input_file.readline())
    for _ in range(test_case):
        n, m = map(int, input_file.readline().split())
        # 0: 먹을 수 없음, 1: 먹을 수 있음
        food_table = [[0 for _ in range(m)] for _ in range(n)]

        friends = input_file.readline().split()

        # 각 친구 들이 먹을 수 있는 음식 정보 업데이트
        for food_idx in range(m):
            eat_info = input_file.readline().split()[1:]
            for friend in eat_info:
                friend_idx = friends.index(friend)
                food_table[friend_idx][food_idx] = 1

        show_food_table(food_table)
