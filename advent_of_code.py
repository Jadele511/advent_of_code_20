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


def valid_password(file2):

    valid_pw_count = 0

    for line in file2:
        least_to_most, letter, pw = line.split(' ')

        least = int(least_to_most.split('-')[0])
        most = int(least_to_most.split('-')[1])
        letter = letter[0]

        letter_count = pw.count(letter)
        if letter_count >= least and letter_count <= most:
            valid_pw_count += 1
    return valid_pw_count




def valid_password_2(file2):

    valid_pw_count = 0

    for line in file2:
        indexes, letter, pw = line.split(' ')

        first_idx = int(indexes.split('-')[0])
        second_idx = int(indexes.split('-')[1])
        letter = letter[0]

        if (pw[first_idx-1] == letter and pw[second_idx-1] != letter) or (pw[first_idx-1] != letter and pw[second_idx-1] == letter):
            valid_pw_count += 1 

    return valid_pw_count

