import csv
from itertools import combinations, chain

def generate_combinations(unique_items, set_len):
    return set(combinations(unique_items, set_len))

def apriori(Trs, unique_items, min_support):
    support = {}
    set_len = 1
    
    current_itemsets = generate_combinations(unique_items, set_len)
    
    while current_itemsets:
        new_support = {}
        for trs in Trs:
            for item_set in current_itemsets:
                if set(item_set).issubset(set(trs)):
                    item_set = tuple(sorted(item_set))
                    if item_set in new_support:
                        new_support[item_set] += 1
                    else:
                        new_support[item_set] = 1

        current_itemsets = {item_set for item_set, count in new_support.items() if count >= min_support}
        if not current_itemsets:
            break

        support.update(new_support)
        set_len += 1
        current_itemsets = generate_combinations(unique_items, set_len)

    frequent_item_sets = [set(item_set) for item_set, count in support.items() if count >= min_support]
    
    return frequent_item_sets, support

def generate_rules(frequent_item_sets, support_data, min_confidence):
    rules = {}
    
    for item_set in frequent_item_sets:
        if len(item_set) < 2:
            continue  

        for subset_len in range(1, len(item_set)):
            for subset in combinations(item_set, subset_len):
                subset = tuple(sorted(subset))  # Ensure subset is always sorted when accessed
                remaining = tuple(sorted(set(item_set) - set(subset)))

                if remaining:
                    # Calculate confidence
                    union_itemset = tuple(sorted(item_set))  # Sort item_set to ensure consistent access
                    if subset in support_data and union_itemset in support_data:
                        confidence = support_data[union_itemset] / support_data[subset]
                        
                        if confidence >= min_confidence:
                            # Store rule as (subset → remaining) with confidence
                            rules[(subset, remaining)] = confidence

    return rules

def main():
    with open(r"D:\Projects\Python\Academic\TE\DWM\EXP 5 input.csv", "r") as file:
        reader = csv.reader(file)
        Trs = [row for row in reader]
    print(Trs)

    min_support = int(input("Enter the minimum support: "))
    min_confidence = float(input("Enter the minimum confidence (0.0 - 1.0): "))

    unique_items = set(chain(*Trs))

    frequent_item_sets, support_data = apriori(Trs, unique_items, min_support)
    rules = generate_rules(frequent_item_sets, support_data, min_confidence)

    print(f"Frequent item sets: {frequent_item_sets}")
    print(f"Generated rules: {rules}")

main()
