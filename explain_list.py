# Creating a set
my_set = {10, 20, 30, 40, 20}

print("Original Set:", my_set)   # {40, 10, 20, 30} (no duplicates)

# Adding & removing
my_set.add(50)
my_set.remove(20)

print("Modified Set:", my_set)   # {40, 10, 50, 30}

# Set operations
set_a = {1, 2, 3, 4}
set_b = {3, 4, 5, 6}

print("Union:", set_a | set_b)        # {1, 2, 3, 4, 5, 6}
print("Intersection:", set_a & set_b) # {3, 4}
print("Difference:", set_a - set_b)   # {1, 2}
