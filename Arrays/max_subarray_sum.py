a_list = [-2,1,-3,4,-1,2,1,-5,4]
a_list.sort(reverse=True)

max_sum_array = []

def find_max_sum_array():
    for i in range(0,len(a_list)):
        if(i==0):
            max_sum_array.append(a_list[i])
        elif(a_list[i]+sum(max_sum_array) >= sum(max_sum_array)):
            max_sum_array.append(a_list[i])
    print(max_sum_array)

find_max_sum_array()