# Reverse an list from start to end

a = [1,2,3,4,5,6,7]

def reverse(arr, start, end):
    while(start<end):
        arr[start], arr[end] = arr[end], arr[start]
        start +=1
        end -=1
    print(arr)

reverse(a,3,6)