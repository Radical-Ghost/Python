import itertools

def contain_subset(trs, support_item_set):
    return set(support_item_set).issubset(set(trs))

def combination(Trs, unique_items, support, set_len, min_support):
    support_item_set = set(itertools.combinations(unique_items, set_len))
    
    new_support = {}
    for trs in Trs:
        for item_set in support_item_set:
            if contain_subset(trs, item_set):
                if item_set in new_support:
                    new_support[item_set] += 1
                else:
                    new_support[item_set] = 1

    rm_list = []
    for item_set in new_support:
        if new_support[item_set] < min_support:
            rm_list.append(item_set)

    for item_set in rm_list:
        new_support.pop(item_set)

    if new_support == {}:
        return support

    return combination(Trs, unique_items, new_support, set_len + 1, min_support)

def main():
    Trs = []
    n = int(input("Enter the number of transactions: "))
    for i in range(n):
        trs = input(f"Enter the transaction {i+1} (items separated by spaces): ").split()
        Trs.append(trs)

    min_support = int(input("Enter the minimum support: "))
    
    unique_items = set(itertools.chain(*Trs))

    frequent_set = combination(Trs, unique_items, {}, 2, min_support)
    print(f"Frequent item sets: {frequent_set}")

main()