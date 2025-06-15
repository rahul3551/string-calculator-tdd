def add(numbers):
    if numbers == "":
        return 0  
    if "," in numbers or "\n" in numbers:
        numbers = numbers.replace("\n", ",")
        return sum(map(int, numbers.split(",")))
    return int(numbers)
