def even_squares(nums):
    result = []
    for num in nums:
        if num %2 == 0:
            result.append(num ** 2)
    return result

def merge_unique_sorted(list1, list2):
    merged = list1 + list2 
    unique = set(merged)
    result = sorted(unique)
    return result

def common_elements(list1, list2):
    result = []
    for item in list1:
        if item in list2:
            if item not in result:
                result.append(item)
    return result

def split_positive(nums):
    positive = []
    non_positive = []
    for num in nums:
        if num > 0:
            positive.append(num)
        else:
            non_positive.append(num)
    return positive, non_positive

def capitalize_all(strings):
    result = []
    for s in strings:
        result.append(s.capitalize())
    return result

def invert_dict(d):
    result ={}
    for key in d:
        value = d[key]
        result[value] =key
    return result
    
def merge_dicts(dict1, dict2):
    result ={}

    for key in dict1:
        result[key] = dict1[key]

    for key in dict2:
        if key in result:
            result[key] = result[key] + dict2[key]
        else:
            result[key] = dict2[key]
    return result

def char_count(s):
    result = {}
    for char in s:
        if char in result:
            result[char] = result[char] + 1
        else:
            result[char] = 1
    return result

def find_key_by_value(d, value):
    for key in d:
        if d[key] == value:
            return key

def diff_set(a, b):
    return a - b

def has_intersection(a, b):
    common = a & b
    if len(common) > 0:
        return True
    else:
        return False

def unique_elements(list):
    result = []
    for item in list:
        if item not in result:
            result.append(item)
    return result

if __name__ =="__main__":
    print(even_square([1,2,3,4,5]))
