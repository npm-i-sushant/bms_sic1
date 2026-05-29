import input_list

def selection_sort(elements):
    for i in range(len(elements)):
        replacing_index = i
        for j in range(i+1, len(elements)):
            if elements[replacing_index] > elements[j]:
                replacing_index = j
        elements[i], elements[replacing_index] = elements[replacing_index], elements[i]
    return elements


number_of_elements = int(input("Enter the number of elements: "))
elements = input_list.input_list(number_of_elements)

print(selection_sort(elements))