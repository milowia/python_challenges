def take_while(arr, pred_fun):
    res = []
    for i in arr:
        if not pred_fun(i):
            break
        res.append(i)
    return res

def is_even(num):
    return num % 2 == 0

arr = [2,100,1000,10000,5,3,4,6]
take_while(arr, is_even)