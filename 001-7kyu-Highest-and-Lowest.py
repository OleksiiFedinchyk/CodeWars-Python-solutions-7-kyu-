# https://www.codewars.com/kata/554b4ac871d6813a03000035

def high_and_low(numbers):
    numbers = numbers.split(" ")
    numbers = list(map(int, numbers))
    return f"{max(numbers)} {min(numbers)}"
