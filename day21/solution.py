import copy

def day21():
    food_strings = [line.rstrip() for line in open('input.txt')]
    allergens_map = {}
    food_list = []
    for line in food_strings:
        contains_split = line.replace(")", "").split("(contains ")
        food = set(contains_split[0].rstrip().split(" "))
        food_list.append(food)
        allergens = set(a.strip() for a in contains_split[1].split(","))
        for allergen in allergens:
            if allergen not in allergens_map:
                allergens_map[allergen] = copy.deepcopy(food)
            else:
                allergens_map[allergen] &= food
         
    

    allergen_count = 0
    while allergen_count != len(allergens_map):        
        for allergen_name, ingredients in allergens_map.items():
            allergen_count += len(ingredients)
            if len(ingredients) == 1:                
                for other_allergen_name in allergens_map.keys():
                    if allergen_name == other_allergen_name:
                        continue
                    allergens_map[other_allergen_name] -= ingredients

        allergen_count = 0
        for allergen_name, ingredients in allergens_map.items():
            allergen_count += len(ingredients)

    all_allergens = set()
    for allergen_name, ingredients in allergens_map.items():
        all_allergens.update(ingredients)

    allergen_free_count = 0
    for food in food_list:
        allergen_free_count += len(food - all_allergens)

    strings = []
    for allergen_name in sorted(allergens_map.keys()):
        strings.append(list(allergens_map[allergen_name])[0])

    print("\n****************************************************")
    print("\nDay 21: Part 1")
    print("Answer: {}".format(allergen_free_count))

    print("\nDay 21: Part 2")
    print("Answer: {}".format(",".join(strings)))
    print("\n****************************************************")


if __name__ == '__main__':
    day21()