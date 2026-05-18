# Read input from stdin
# Example: n = int(input())
# Example: arr = list(map(int, input().split()))

testcases = int(input())

for _ in range(testcases):
    length1 = int(input())
    arr1 = input().split()

    if length1 == 1:
        newarr = arr1
        strtoprint = ""
        for char in newarr:
            strtoprint += char + " "
        print(strtoprint)
        continue
    
    newarr = []

    first = 0
    last = length1 - 1

    middle = length1 // 2

    while len(arr1) > 0:
        newarr.append(arr1[0])
        arr1 = arr1[1:]
        if len(arr1) > 0:
            newarr.append(arr1[len(arr1)-1])
            arr1 = arr1[:-1]


    # while (first < middle and first < length1) or (last > middle and last >= 0):
    #     newarr.append(arr1[first])
    #     newarr.append(arr1[last])
    #     first += 1
    #     last -= 1
    
    strtoprint = ""
    for char in newarr:
        strtoprint += char + " "
    print(strtoprint)