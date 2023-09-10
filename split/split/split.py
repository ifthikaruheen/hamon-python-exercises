import math
import random

def split(items, ratios):
    items_length = len(items)
    main_list = []
    for ratio in ratios:
        sublist_length = math.ceil(items_length * ratio)
        sublist_length = min(sublist_length, len(items))
        sub_list = random.sample(items, sublist_length)
        items = [item for item in items if item not in sub_list]
        main_list.append(sub_list)

    return main_list


