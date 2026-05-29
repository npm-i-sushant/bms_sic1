def input_list(number_of_elements):
    elements = []
    print(f"Enter {number_of_elements} elements: ")
    for i in range(number_of_elements):
        elements.append(input(f"Enter element {i+1}: "))
    return elements