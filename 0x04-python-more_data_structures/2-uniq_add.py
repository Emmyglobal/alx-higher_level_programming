#!/user/bin/python3
def uniq_add(my_list=[]):
    mat = set(my_list)
    sum = 0
    
    for i in mat:
        sum += i
    return sum
