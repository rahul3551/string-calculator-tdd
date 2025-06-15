def add(numbers):
    if numbers == "":
        return 0  
    if numbers.startswith("//"):
        delimiter = numbers[2]
        numbers = numbers[3:]
        numbers = numbers.replace(delimiter, ',')
       
    numbers = numbers.replace("\n", ",")
    return sum([int(i) for i in numbers.split(',') if i])