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
        
    return count


    # for i in range(down, n, down): 
        # pos = tree_map[i][int(i * right / down) % m]
        
    #     if pos == '#':
    #         count += 1
    #     if i >= n - down:
    #         return count   

count_11 = count_tree(tree_map, 1, 1)
count_31 = count_tree(tree_map, 3, 1)
count_51 = count_tree(tree_map, 5, 1)
count_71 = count_tree(tree_map, 7, 1)
count_12 = count_tree(tree_map, 1, 2)
product = count_11 * count_31 * count_51 * count_71 * count_12
    
# print(product)





####### DAY 4 ############

# with open("d4.txt", "a") as file4:
#   file4.write("\n")
#   file4.close()
file4 = open("d4.txt")

def batch_files(file4):
    batches = [] 
    batch = ''
    for line in file4:
        #check if line is a new line
        if line != '\n': 
            batch += ' ' + line.rstrip()
        else:
            batches.append(batch)
            batch = ''    

    return batches

batches = batch_files(file4)

def valid_info(batch):
    byr = len(batch['byr']) == 4 and int(batch['byr']) >= 1920 and int(batch['byr']) <= 2002
    iyr = len(batch['iyr']) == 4 and int(batch['iyr']) >= 2010 and int(batch['iyr']) <= 2020
    eyr = len(batch['eyr']) == 4 and int(batch['eyr']) >= 2020 and int(batch['eyr']) <= 2030

    hgt = batch['hgt'][:-2]
    if len(batch['hgt'][-2:]) == 2 and batch['hgt'][-2:] == 'cm':
        hgt = len(hgt) == 3 and int(hgt) >= 150 and int(hgt) <= 193
    else:
        hgt = len(hgt) == 2 and int(hgt) >= 59 and int(hgt) <= 76

    #hair color
    chars_nums = [chr(x) for x in range(ord('a'), ord('f') + 1)]
    chars_nums += [str(x) for x in range(10)]
    chars_nums = set(chars_nums)
    hcl = batch['hcl'][0] == '#' and len(batch['hcl'][1:]) == 6 and all(ch in chars_nums for ch in batch['hcl'][1:])

    ecl_codes = set(['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']) 
    ecl = batch['ecl'] in ecl_codes

    pid = len(batch['pid']) == 9 and int(batch['pid']) >= 1 

    return all([byr,iyr, eyr,hgt, hcl, ecl, pid])


def valid_passport(batches):
    count = 0
    for i in range(len(batches)):
        batch = batches[i]
        batch_dict = {}
        for pair in batch.split(' '):
            if pair != '':
                key, value  = pair.split(':')
                batch_dict[key] = value
        batches[i] = batch_dict
        key_set = set(['byr','iyr', 'eyr','hgt', 'hcl', 'ecl', 'pid'])
        if key_set.issubset(batches[i].keys()) and valid_info(batches[i]):
            count += 1
    return count

# print(valid_passport(batches))

