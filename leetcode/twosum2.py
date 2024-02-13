def two_sum(numbers : list[int], target: int)->list[int]:
    left_idx    : int = 0
    right_idx   : int = len(numbers)-1

    while(numbers[left_idx] + numbers[right_idx] != target):
        if(numbers[left_idx] + numbers[right_idx] > target):
            right_idx = right_idx - 1
        else:
            left_idx = left_idx + 1
    
    return([left_idx+1, right_idx+1])



tests : list[tuple[int, list[int], list[int]]] = [
    (0, [1,2], [0,0,3,4]),
    (9, [1,2], [2,7,11,15]),
    (6, [1,3], [2,3,4]),
    (-1,[1,2], [-1,0]),
    (77, [9,14], [1,3,4,6,7,8,9,12,34,55,89,90,56,43])
]


for test in tests:
    res : list[int] = two_sum(test[2], test[0])

    if(test[1]!=res):
        print("fail : expected",test[1]," recieved",res," : ",test[2])
    else:
        print("pass")