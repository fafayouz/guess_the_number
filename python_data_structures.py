# Question 1: Multiply all items in a list (user can input numbers)
print("Question 1:")
try:
    sample_list = input("Enter numbers separated by space: ").split()
    numbers = [int(num) for num in sample_list]
    result = 1
    for num in numbers:
        result *= num
    print("Result =", result)
except ValueError:
    print("Invalid input! Please enter only numbers.")
print("\n" + "-"*40 + "\n")

# Question 2: Sort list of tuples by last element
print("Question 2:")
try:
    tuple_input = input("Enter tuples separated by commas (e.g., 2 5,1 2,4 4): ").split(",")
    tuple_list = [tuple(map(int, t.strip().split())) for t in tuple_input]
    sorted_list = sorted(tuple_list, key=lambda x: x[-1])
    print("Sorted list:", sorted_list)
except Exception as e:
    print("Invalid input! Please enter tuples correctly.", e)
print("\n" + "-"*40 + "\n")

# Question 3: Combine two dictionaries by adding values for common keys
print("Question 3:")
try:
    d1 = {'a': 100, 'b': 200, 'c': 300}
    d2 = {'a': 300, 'b': 200, 'd': 400}
    combined_dict = d1.copy()
    for key, value in d2.items():
        if key in combined_dict:
            combined_dict[key] += value
        else:
            combined_dict[key] = value
    print("Combined dictionary:", combined_dict)
except Exception as e:
    print("Error combining dictionaries:", e)
print("\n" + "-"*40 + "\n")

# Question 4: Generate dictionary (i, i*i) from 1 to n
print("Question 4:")
try:
    n = int(input("Enter an integer n: "))
    squared_dict = {}
    for i in range(1, n + 1):
        squared_dict[i] = i * i
    print("Dictionary:", squared_dict)
except ValueError:
    print("Invalid input! Please enter an integer.")
print("\n" + "-"*40 + "\n")

# Question 5: Sort tuple by float element
print("Question 5:")
try:
    tuple_input = input("Enter tuples with floats (e.g., item1 12.20,item2 15.10): ").split(",")
    tuple_list = [tuple(t.strip().split()) for t in tuple_input]
    sorted_tuple_list = sorted(tuple_list, key=lambda x: float(x[1]), reverse=True)
    print("Sorted tuple list:", sorted_tuple_list)
except ValueError:
    print("Invalid input! Please enter float numbers correctly.")
print("\n" + "-"*40 + "\n")

# Question 6: Create, iterate, add and remove items in a set
print("Question 6:")
try:
    my_set = {0, 1, 2, 3, 4}
    print("Original set:", my_set)

    print("Iterating over set:")
    for item in my_set:
        print(item, end=" ")
    print()

    # Add members
    my_set.add(5)
    my_set.update([6, 7])
    print("Set after adding members:", my_set)

    # Remove members safely
    my_set.remove(0)  # will throw error if 0 not present
    my_set.discard(10)  # won't throw error if 10 not present
    print("Set after removing members:", my_set)
except Exception as e:
    print("Error handling set:", e)
