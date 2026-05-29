
def sum_of_digits(n):
    sum = 0
    for i in str(n):
        sum += int(i)
    return sum

input_number = int(input("Enter the input_number: "))

while True:
    if sum_of_digits(input_number) < 10:
        lucky_digit = sum_of_digits(input_number)
        break
    else:
        input_number = sum_of_digits(input_number)

print(f"The lucky digit is {lucky_digit}")
