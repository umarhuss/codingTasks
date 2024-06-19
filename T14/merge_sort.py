def merge_sort(list_of_strings):
    if len(list_of_strings)<=1:
        return list_of_strings
    
    midpoint = len(list_of_strings) //2
    left_side = list_of_strings[:midpoint]
    right_side = list_of_strings[midpoint:]
    
    left_side_sorted = merge_sort(left_side)
    right_side_sorted = merge_sort(right_side)

    return merged(left_side_sorted,right_side_sorted)

def merged(left, right):
    i,j = 0,0
    merged = []

    while i < len(left) and j < len(right):
        if len(left[i]) >= len(right[j]):
            merged.append(left[i])
            i += 1
        else:
            merged.append(right[j])
            j += 1

    while i < len(left):
        merged.append(left[i])
        i += 1

    while j < len(right):
        merged.append(right[j])
        j += 1

    return merged


list_1 = [
    "persistence",
    "resilience",
    "optimism",
    "innovation",
    "perseverance",
    "determination",
    "creativity",
    "empowerment",
    "collaboration",
    "synergy",
    "ambition",
    "transformation",
    "inspiration"
]

list_2 = [
    "compassion",
    "gratitude",
    "harmony",
    "enthusiasm",
    "generosity",
    "integrity",
    "loyalty",
    "dedication",
    "consistency",
    "authenticity",
    "reliability",
    "responsibility",
    "fairness"
]

list_3 = [
    "exploration",
    "imagination",
    "curiosity",
    "adventure",
    "wonder",
    "discovery",
    "vision",
    "innovation",
    "originality",
    "invention",
    "creativity",
    "pioneering",
    "aspiration"
]

print(merge_sort(list_1))

