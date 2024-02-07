def twoSum(numbers : list[int], target: int)->list[int]:
    for index, number in enumerate(numbers):
        for x in range(0, len(numbers)):
            if (x == index):
                continue
            else:
                if(numbers[index] + numbers[x] == target):
                    return [index, x]
    return[0,0]
