# Function Caching

# Function caching is a technique used to store the results of function
# calls in memory. When the same function is called again with the same
# arguments, the previously stored result is returned instead of
# recalculating it.

# This can significantly improve performance when working with
# computationally expensive functions.

# Note:
# The cache is temporary and exists only while the program is running.
# It is not a replacement for save files or databases.

import functools

recipes = {
    
    "iron_ingot":{},
    "wood_handle":{},
    
    "iron_blade":{
        "iron_ingot": 4,
        "wood_handle":1
    },
    
    "iron_guard":{
        "iron_ingot": 2,
        "wood_handle": 1
    },
    
    "iron_longsword":{
        "iron_ingot": 2,
        "wood_handle": 2
    },
    
    "iron_dagger":{
        "iron_ingot": 3,
        "wood_handle": 1
    }
}

@functools.lru_cache(maxsize = None)
def calculate_materials(item):
    print(f"calculating materials for {item}.")
    
    if not recipes[item]:
        return {item: 1}
    
    total = {}
    
    for ingrediants, quantitiy in recipes[item].items():
        sub_materials = calculate_materials(ingrediants)
        for material, count in sub_materials.items():
            total[material] = total.get(material, 0) + count * quantitiy
            
    return total
print(calculate_materials("iron_dagger"))
print()    
print(calculate_materials("iron_dagger"))
    
