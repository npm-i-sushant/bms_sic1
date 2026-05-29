import input_list

def insertion_sort(elements):
    for i in range(len(elements)):
        element = elements[i]
        j = i - 1
        while j >= 0 and element < elements[j]:
            elements[j+1] = elements[j]
            j -= 1
        elements[j+1] = element
    return elements

number_of_elements = int(input("Enter the number of elements: "))
elements = input_list.input_list(number_of_elements)

print(insertion_sort(elements))