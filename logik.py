import json

def sublist_in_list(sub, lis):
    return str(sub).strip('[]') in str(lis).strip('[]')

def get_comb(dice_list):
    dice_list = sorted(dice_list)
    dice_combination = []
    for combination in data['combinations']:
        if sublist_in_list(combination, dice_list):
            if len(dice_combination + combination) <= 4:
                dice_combination += combination
            else:
                dice_combination = combination
    return dice_combination

def get_comb_grade(dice_combination):
    if dice_combination:
        return data['combinations'].index(dice_combination)
    else:
        return -1

def get_comb_name(ind):
    if ind == -1: return "Нічого"
    for name, combinations_range in data['combinations_name_range'].items():
        if len(combinations_range) == 2:
            if ind in range(*combinations_range): return name
        else:
            if ind == combinations_range[0]: return name
    

with open('data.json') as f:
    data = json.load(f)