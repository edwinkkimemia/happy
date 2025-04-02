# Step 1: Create an empty list called my_list
my_list = []
print("Initial list:", my_list)

# Step 2: Append the elements 10, 20, 30, 40 to my_list
my_list.append(10)
my_list.append(20)
my_list.append(30)
my_list.append(40)
print("After appending 10, 20, 30, 40:", my_list)

# Step 3: Insert the value 15 at the second position (index 1)
my_list.insert(1, 15)
print("After inserting 15 at second position:", my_list)

# Step 4: Extend my_list with another list [50, 60, 70]
my_list.extend([50, 60, 70])
print("After extending with [50, 60, 70]:", my_list)

# Step 5: Remove the last element from my_list
my_list.pop()
print("After removing the last element:", my_list)

# Step 6: Sort my_list in ascending order
my_list.sort()
print("After sorting in ascending order:", my_list)

# Step 7: Find and print the index of the value 30
index_of_30 = my_list.index(30)
print("Index of 30:", index_of_30)