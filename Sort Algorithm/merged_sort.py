def merged_sort(numbers, low, high):
    if len(numbers) <= 1:
        return numbers
    if low < high:
        mid = (low + high) // 2
        left = merged_sort(numbers, low, mid)
        right = merged_sort(numbers, mid + 1, high)
    return merge(left, right)

def merge(left, right):
    result = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result.extend(left[i:])
    result.extend(right[j:])
    return result

nums = [38, 27, 43, 3, 9, 82, 10]
sorted_nums = merged_sort(nums, 0, len(nums) - 1)
print("Sorted array:", sorted_nums)