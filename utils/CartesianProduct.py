def cartesianHelper(a, b):
    result = []
    for i in range(0, len(a)):
        for j in range(0, len(b)):
            if type(a[i]) != list:
                a[i] = [a[i]]
            temp = [num for num in a[i]]
            temp.append(b[j])
            result.append(temp)
    return result


def Cartesian(arr):
    all_possible_combinations = arr[0]
    for i in range(1, len(arr)):
        all_possible_combinations = cartesianHelper(all_possible_combinations, arr[i])
    return all_possible_combinations

