def bubble_sort(elements):
    for i in range(len(elements)-2):
        sorted = True
        for j in range(len(elements)-2-i):
            if elements[j] > elements[j+1]:
                elements[j], elements[j+1] = elements[j+1], elements[j]
                sorted = False
        if sorted:
            break

    return elements