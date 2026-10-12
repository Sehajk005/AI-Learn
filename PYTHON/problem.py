# Powerset problem. 
# eg. [1, 2, 3] = [[], [1], [2], [3], [1, 2], [1, 3], [2, 3], [1, 2, 3]]
"""The explination of the powerset problem is that it is a set of all subsets of a given set. 
   The powerset of a set S is the set of all subsets of S, including the empty set and S itself. 
   The number of subsets of a set with n elements is 2^n, which means that the powerset of a set with n elements has 2^n elements. 
   For example, the powerset of the set {1, 2, 3} is { {}, {1}, {2}, {3}, {1, 2}, {1, 3}, {2, 3}, {1, 2, 3} }.
"""
def powerset(arr):
    if len(arr)==0:
        return [[]]
    else:
        first = arr[0]
        rest = arr[1:]
        subsets_without_first = powerset(rest)
        subsets_with_first = [[first] + subset for subset in subsets_without_first]
        return subsets_without_first + subsets_with_first

"""The explination of the powerset problem can be found in the following link: https://www.geeksforgeeks.org/power-set/"""
def powerset(arr):
    if len(arr) == 0:
        return [[]]

    smaller = powerset(arr[1:])

    result = []

    # Don't include arr[0]
    result.extend(smaller)

    # Include arr[0]
    for subset in smaller:
        result.append([arr[0]] + subset)

    return result