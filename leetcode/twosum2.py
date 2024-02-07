def two_sum(numbers : list[int], target: int)->list[int]:
    req_num : int = 0
    idx_two : int = 0

    for index, number in enumerate(numbers):
        req_num = target - number
        try:
            idx_two = numbers.index(req_num)
            if(idx_two == index):
                try:
                    idx_two = numbers.index(req_num, index+1)
                    return([index+1, idx_two+1])
                except:
                    continue
            else:
                return([index+1, idx_two+1])
        except:
            continue
    return[0,0]



tests : list[tuple[int, list[int], list[int]]] = [
    (0, [1,2], [0,0,3,4]),
    (9, [1,2], [2,7,11,15]),
    (6, [1,3], [2,3,4]),
    (-1,[1,2], [-1,0])
]


for test in tests:
    res : list[int] = two_sum(test[2], test[0])

    if(test[1]!=res):
        print("fail : expected",test[1]," recieved",res," : ",test[2])
    else:
        print("pass")