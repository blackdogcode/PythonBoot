# https://algospot.com/judge/problem/read/ALLERGY
# 재귀 호출 로는 2^50 이라는 시간 복잡도내에 수행할 수 없다
# 알고리즘 수행 속도를 개선하는 방법을 고안이 필요하다
def can_everyone_eat(menu, food_table, n, m):
    ret = [0] * n
    for food in menu:
        for friend in range(n):
            if food_table[friend][food] == 1:
                ret[friend] = 1

    if all(ret):
        return True
    else:
        return False


def min_select_menu(menu, food, food_table, n, m):
    # 모든 음식에 대해 만들지 여부를 결정 했을 때
    if food == m:
        if can_everyone_eat(menu, food_table, n, m):
            return len(menu)
        else:
            return float('inf')
    # 이 음식을 만들지 않는 겨우의 답을 계산
    ret = min_select_menu(menu, food + 1, food_table, n, m)
    # 이 음식을 만드는 경우을 계산 후 더 메뉴 개수가 적을 것을 구한다
    menu.append(food)
    ret = min(ret, min_select_menu(menu, food + 1, food_table, n, m))
    menu.pop(-1)
    return ret


test_case = int(input())
for _ in range(test_case):
    n, m = map(int, input().split())
    # 0: 먹을 수 없음, 1: 먹을 수 있음
    food_table = [[0 for _ in range(m)] for _ in range(n)]

    friends = input().split()

    # 각 친구 들이 먹을 수 있는 음식 정보 업데이트
    for food_idx in range(m):
        eat_info = input().split()[1:]
        for friend in eat_info:
            friend_idx = friends.index(friend)
            food_table[friend_idx][food_idx] = 1

    menu = []
    print(min_select_menu(menu, 0, food_table, n, m))
