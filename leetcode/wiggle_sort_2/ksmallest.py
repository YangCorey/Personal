import random
def kSmallest(pos, nums):
    print(pos,nums)
    pivot = random.randint(0,len(nums)-1)
    pivot_val = nums.pop(pivot)
    i,j = 0, len(nums)-1

    while i <= j:
        if nums[i] <= pivot_val:
            i += 1
        elif nums[i] > pivot_val:
            nums[i], nums[j] = nums[j], nums[i]
            j -= 1
    if i == pos:
        return pivot_val 
    elif i > pos:
        return kSmallest(pos, nums[:i])
    else:
        return kSmallest(pos-(i+1),nums[i:])

x = [1,2,2,3,3,3,3]
print(kSmallest(2,x))
