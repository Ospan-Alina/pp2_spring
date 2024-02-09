
def has33(nums):
    for i in range(len(nums) - 1):
        if nums[i] == 3 and  nums[i + 1] == 3:
            return True
    return False
            
nums = [int(x) for x in input().split()]
has33(nums)

if has33(nums) == False:
    print('False')
else:
    print('True')
        

