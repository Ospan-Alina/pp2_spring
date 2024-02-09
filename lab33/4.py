def checkPrm(n):
    if n <= 0:
        return "NOt defined"
    elif n == 1:
        return "Not prime number"
    else:
        for i in range(2, n):
            cnt = 0
            if n % i == 0:
                return "Not prime number"
        return "Prime"
            


def filter_prime(lst):
    prm_list = [ ]
    for i in lst:
        str = checkPrm(i)
        if str == "Prime":
            prm_list.append(i)
    return prm_list
        
        

lst = [20, 10, 4, 5] #20 10 4 5

print(filter_prime(lst))

        