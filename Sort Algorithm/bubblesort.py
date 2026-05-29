import Sort_Algorithm.bubble_sort_func as bubble_sort_func
import input_list

number_of_elements = int(input("Enter the number of elements: "))
elements = input_list.input_list(number_of_elements)

print(bubble_sort_func.bubble_sort(elements))