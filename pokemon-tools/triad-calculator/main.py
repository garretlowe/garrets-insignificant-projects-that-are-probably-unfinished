import json

TYPES = dict()
with open('../types.json') as file: TYPES = json.load(file)
TYPE_NAMES = list(TYPES.keys())

def find_third_type(triads: list, perfect_triads: list, type1: str, type2: str, index: int = 0) -> None:
    if index >= len(TYPES[type2]['super_effective']): return
    type3 = TYPES[type2]['super_effective'][index]
    if type1 in TYPES[type3]['super_effective']:
        final_types = [type1, type2, type3]
        final_types.sort()
        if final_types not in triads: triads.append(final_types)
        types_are_perfect_triad = (type3 in TYPES[type1]['not_very_effective'] and 
                                   type1 in TYPES[type2]['not_very_effective'] and 
                                   type2 in TYPES[type3]['not_very_effective'])
        if final_types not in perfect_triads and types_are_perfect_triad: perfect_triads.append(final_types)
    find_third_type(triads, perfect_triads, type1, type2, index + 1)


def find_second_type(triads: list, perfect_triads: list, type1: str, index: int = 0) -> None:
    if index >= len(TYPES[type1]['super_effective']): return
    type2 = TYPES[type1]['super_effective'][index]
    find_third_type(triads, perfect_triads, type1, type2)
    find_second_type(triads, perfect_triads, type1, index + 1)


def find_triads(triads: list, perfect_triads: list, index: int = 0) -> None:
    if index >= len(TYPE_NAMES): return
    type1 = TYPE_NAMES[index]
    find_second_type(triads, perfect_triads, type1)
    find_triads(triads, perfect_triads, index + 1)


def print_lists_in_list(arr: list, index: int = 0) -> None:
    if index >= len(arr): return
    print(*arr[index])
    print_lists_in_list(arr, index + 1)

triads = []
perfect_triads = []
find_triads(triads, perfect_triads)

print('Triads:')
triads.sort()
print_lists_in_list(triads)
        
print('\nPerfect Triads:')
perfect_triads.sort()
print_lists_in_list(perfect_triads)