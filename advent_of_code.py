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

######## Day 2 #############

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


########## DAY 3 ##############

file3 = open("aoc_d3.txt")

def map(file3):
    full_map = []
    for line in file3:
        full_map.append(list(line.rstrip()))
    return full_map

tree_map = map(file3)



def count_tree(tree_map, right, down):
    count = 0

    n = len(tree_map)
    m = len(tree_map[0])

    i = down
    j = right
    while i <= n - down:
        pos = tree_map[i][j % m]
        if pos == '#':
            count += 1
        i += down
        j += right
        if i >= n - down:
            return count


    # for i in range(down, n, down): 
    #     pos = tree_map[i][int(i * right / down) % m]
        
    #     if pos == '#':
    #         count += 1
    #     if i >= n - down:
    #         return count   

count_11 = count_tree(tree_map, 1, 1)
count_31 = count_tree(tree_map, 3, 1)
count_51 = count_tree(tree_map, 5, 1)
count_71 = count_tree(tree_map, 7, 1)
count_12 = count_tree(tree_map, 1, 2)
print(count_11, count_31, count_51,count_71, count_12)

product = count_11 * count_31 * count_51 * count_71 * count_12
    
print(product)

