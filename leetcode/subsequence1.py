def is_subsequence(string : str, text: str) -> bool:
    pointer_string : int = 0

    if(len(string) == 0 and len(text)==0):
        return True

    if(len(string) != 0 and len(text) == 0):
        return False
    
    if(len(string) == 0 and len(text)!= 0):
        return True
    
    for char in text:
        if (char == string[pointer_string]):
            pointer_string = pointer_string + 1
        if(pointer_string >= len(string)):
            return True


    return False



tests : list[tuple[bool, str, str]] = [
    (True, "abc", "akldjhbasecferwf"),
    (True, "a", "skkkjdkjasoka"),
    (True, "cc", "bbbbbbcc"),
    (True, "aabba", "cnjshdanjnjajtirbfibera"),
    (False,"aabba", "cnjshdanjnjajtirbfiera"),
    (True, "", "aaaaa"),
    (True, "", ""),
    (False, "aaa", "")
]

for case in tests:
    # print(case[0],"- ",case[1]," - ",case[2])
    result : bool = is_subsequence(case[1], case[2])

    if(result != case[0]):
        print("failed : res ",result," != exp",case[0]," : ",case[1]," | ",case[2])
    else:
        print("pass")