def numDuplicates(name, price, weight):
    # Write your code here
    items = dict()
    for i in range(len(name)):
        item_name = name[i]
        item_price = price[i]
        item_weight = weight[i]
        composite = (item_name, item_price, item_weight)
        if composite in items:
            items[composite] += 1
        else:
            items[composite] = 1

    duplicate_sum = 0
    for key in items:
        if items[key] >= 2:
            duplicate_sum += items[key] - 1

    return duplicate_sum


if __name__ == '__main__':
    with open('test_input.txt') as input_file:
        test_case = int(input_file.readline())
        for _ in range(test_case):
            size = int(input_file.readline())
            names, prices, weights = [], [], []
            for _ in range(size):
                names.append(input_file.readline().strip())
            for _ in range(size):
                prices.append(int(input_file.readline()))
            for _ in range(size):
                weights.append(int(input_file.readline()))

            print(numDuplicates(names, prices, weights))

