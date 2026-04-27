'''
🔹 Beginner Level
- Get the first 3 elements.
- Get the last 3 elements.
- Get every other element.
- Reverse the list using slicing.
- Get elements from index 2 to index 5 (inclusive of index 2, exclusive of index 5).
- Get every 2nd element from index 1 to index 6.

🔹 Intermediate Level
- Get every third element starting from index 1.
- Get all elements except the first two.
- Get all elements except the last three.
- Get elements from index 2 to 8, but skip every 2 elements.

🔹 Challenge Level
- Get the last 5 elements in reverse order.
- Get every second element, but going backwards (i.e., reversed and skipping one each time).
- Get the middle 4 elements (don’t hardcode indices—make it work even if the list gets longer).
- Write a slice that returns only [10, 20, 30] using slicing without counting from the front (use negative indexing).
- Create a slice that removes the first and last items from the list.

'''

def slicing_practice_beginner(nums):
    print(f"first three elements: {nums[:3]}")
    print(f"last three elements: {nums[-3:]}")
    print(f"every other element: {nums[::2]}")
    print(f"elements form index 2 to index 5:: {nums[2:5]}")
    print(f"first three elements {nums[0:3]}")
    print(f"every 2nd element from index 1 to index 6: {nums[1:7:2]}")


def slicing_practice_intermediate(nums):
    print(f"every third element starting from index 1: {nums[1::3]}")
    print(f"all elements except the first two: {nums[2:]}")
    print(f"all elements except the last three: {nums[:-3]}")
    print(f"elements from index 2 to 8, but skip every 2 elements: {nums[2:9:2]}")

def slicing_practice_challenge(nums):
    print(f"last 5 elements in reverse order: {nums[:-5:-1]}")
    print(f"every second element backwards: {nums[::-2]}")

    # the middle 4 elements
    mid = len(nums) // 2
    start = mid - 2
    end = mid + 2
    print(f"the middle 4 elements: {nums[start:end]}") 

    # 10-20-30 backwards
    selected_nums = nums[-5::-2]
    print(f"10-20-30 backwards: {selected_nums[::-1]}") 

    # removes the first and last items from the list
    end = len(nums) - 1
    print(f"removes the first and last items from the list: {nums[1:end]}") 


#slicing_practice_beginner(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
#slicing_practice_intermediate(nums = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50])
slicing_practice_challenge(nums = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50])
