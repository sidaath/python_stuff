def h_index(citations : list) -> int:
    books_count : int = len(citations)
    offset      : int = books_count

    citation_counts : list = [0 for i in citations]
    citation_counts.append(0)

    for item in citations:
        if(item > books_count):
            citation_counts[offset] = citation_counts[offset] + 1
        else:
            citation_counts[item] = citation_counts[item] + 1
    
    sum : int = 0

    for i in range(offset, 0, -1):
        sum = sum + citation_counts[i]
        if(sum >= i):
            return i

    return 0



tests : dict[int, list] = {    
    1 : [1],
    0 : [0,0,0,],
    2 : [2,2,2,2,2,2],
    3 : [3,2,2,3,3],
    3 : [2,5,3,5,4],
    2 : [4,0,0,4],
    4 : [2,7,7,7,4],
    2 : [1,7,9,2],
    3 : [3,0,6,1,5,90]
}

for expected_val, array in tests.items():
    result : int = h_index(array)
    if(expected_val != h_index(array)):
        print("fail : ",array)
        print("exp : ",expected_val," returned ",result)
    else:
        print("pass")


