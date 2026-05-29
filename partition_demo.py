import partition as pt
numbers = input("Enter the numbers for partition: ").split()
# import sys
# numbers = [int(value) for value in sys.argv[1:]]

for i in range(len(numbers)):
    numbers[i] = int(numbers[i])

print(pt.partition_array(numbers))

# for i in range(len(numbers)):
#     if numbers[i] > last_index:
#         j += 1
#     elif numbers[i] < last_index and j > 0:
#         for k in range(j):
#             numbers[i], numbers[i-k-1] = numbers[i-k-1], numbers[i]
# numbers[-1], numbers[-j-1] = numbers[-j-1], numbers[-1]
# print(numbers)