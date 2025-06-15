def add(numbers):
    if numbers == "":
        return 0  
    if numbers.startswith("//"):
        delimiter = numbers[2]
        numbers = numbers[3:]
        numbers = numbers.replace(delimiter, ',')
       
    numbers = numbers.replace("\n", ",")

    num_list = [int(i) for i in numbers.split(',') if i]

    negatives = [n for n in num_list if n<0]
    if negatives:
        raise ValueError(f"negative numbers not allowed: {','.join(map(str, negatives))}")
    return sum(num_list)

# print(add('-2,-3'))