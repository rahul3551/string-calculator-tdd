def add(numbers):
    if numbers == "":
        return 0  
    if "," in numbers:
        return sum(map(int, numbers.split(",")))
    return int(numbers)
