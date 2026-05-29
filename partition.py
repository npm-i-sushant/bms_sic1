def partition_array(numbers):
    pivot = numbers[-1]
    i = 0
    j = 0
    for i in range(len(numbers) - 1):
        if numbers[i] < pivot:
            numbers[i], numbers[j] = numbers[j], numbers[i]
            j += 1
    numbers[-1], numbers[j] = numbers[j], numbers[-1]
    return numbers
l = [12, 33, 21, 1, 3, 4, 5, 44, 15]
print(partition_array(l))