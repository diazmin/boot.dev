''' 
Oracle

Given a list of integers and a target sum, 
return the indices of the two numbers that add up to the target. 

Example:
nums = [2, 7, 11, 15]

target = 9

ANS: [0, 1]
'''

def finding_target_sum(nums, target):
    next_num = 0
    answer = []
    for i in range(0, len(nums)):
        #print(nums[i])
        if i != len(nums):
            next_num = i+1
        for j in nums[next_num:]:
            # print("2nd loop: ", j)
            # print("sum: ", nums[i]+j)
            if nums[i] + j == target:
                answer.append(i)
                answer.append(nums.index(j))
                return answer

print(finding_target_sum([6, 9, 8, 1], 7))