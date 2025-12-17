arr1 = [1, 3, 5]
arr2 = [2, 4, 6]
def merge_sorted_arrays(arr1, arr2):
    merged = arr1 + arr2   # merge arrays
    merged.sort()          # sort the result
    return merged






def merge_sorted_arrays(arr1, arr2):
    i = j = 0
    result = []

    while i < len(arr1) and j < len(arr2):
        if arr1[i] <= arr2[j]:
            result.append(arr1[i])
            i += 1
        else:
            result.append(arr2[j])
            j += 1

    # Add remaining elements
    while i < len(arr1):
        result.append(arr1[i])
        i += 1

    while j < len(arr2):
        result.append(arr2[j])
        j += 1

    return result


arr1 = [1, 3, 5, 7]
arr2 = [2, 4, 6]

print(merge_sorted_arrays(arr1, arr2))
