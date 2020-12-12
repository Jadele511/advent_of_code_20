file1 = open("aoc_d1.txt")

def sum_2020(file1):
    nums = []
    for line in file1:
        nums.append(int(line.rstrip()))

    nums_set = set(nums)
    for num in nums:
        other_num = 2020 - num
        if other_num in nums_set:
            return num * other_num       




def sum_three_2020(file1):
    nums = []
    for line in file1:
        nums.append(int(line.rstrip()))

    n = len(nums)
    for i in range(n-2):
        nums_set = set(nums[i+2:])
        for j in range(i+1, n-1):
            other_num = 2020 - nums[i] - nums[j]
            if other_num in nums_set:
                return nums[i] * nums[j] * other_num    



file2 = open("aoc_d2.txt")


