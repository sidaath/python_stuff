#container with most water

def max_area(heights : list[int], debug:bool = False) -> int:
    max_len : int = len(heights)
    max_area: int = 0 
    area    : int = 0
    c_height: int = 0
    c_len   : int = 0

    for index, height in enumerate(heights):
        # print("index = ",index," | height = ",height)
        for i in range(index+1, max_len):
            # print(" id2=",i," h2=",heights[i])
            c_height    = min(height, heights[i])
            c_len       = i - index
            area        = c_height * c_len
            if(area > max_area):
                # if(debug):
                #     print("   new area = ",area)
                max_area = area

    return max_area



tests : dict[int, list[int]] = {
    49 : [1,8,6,2,5,4,8,3,7],
    1  : [1,1]
}

for expected, heights in tests.items():
    res : int = max_area(heights)

    if(expected == res):
        print("pass")
    else:
        max_area(heights, debug=True)
        print("fail : expected ",expected," recieved ",res," : ",heights)