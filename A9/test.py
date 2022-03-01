
# Python 3 implementation of the approach
 
# Recursive function that returns true if
# the array can be divided into two sub-arrays
# satisfying the given condition
def split53(nums):
    return split53Helper(0, nums, 0, 0)

# similar to the groupSum family.
# for each element, decide if it's in one collection or another(based on constraints),
# and give the rest to recursive calls to itself. 
def split53Helper(start, nums, c1, c2):
    # base case: nums elements run out, and the two collections have same sum
    if start == len(nums): 
        return c1 == c2
    # check if is divisible by 5 or 3 and decide where should it go
    if nums[start] % 5 == 0:
        split53Helper(start + 1, nums, c1 + nums[start], c2)
    elif nums[start] % 3 == 0 and not nums[start] % 5 == 0: 
        # implicitly checked if is divisible by 5
        split53Helper(start + 1, nums, c1, c2 + nums[start])
    # the rest may go either way
    # if split53Helper(start + 1, nums, c1 + nums[start], c2): 
    #     # put nums[start] to c1
    #     # print(c1)
    #     # print(c2)
    else:
        return split53Helper(start + 1, nums, c1 + nums[start], c2) or split53Helper(start + 1, nums, c1, c2 + nums[start])
# Driver code
if __name__ == "__main__":
     
    nums = [ 3,5,8 ]
    if split53(nums):
        print("Yes")
    else:
        print("No")
print(nums) 