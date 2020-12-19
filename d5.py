file = open('d5.txt')

def pass_list(file):
    result = []
    for line in file:
        result.append(line.rstrip())
    return result

passes = pass_list(file)

def ids(passes):
    id_list = []
    for boarding_pass in passes:
        start = 0
        end = 127
        for letter in boarding_pass[:7]: #FBFBBFFRLR
            if letter == 'F':
                end = start + int((end - start )/2)
            else:
                start = start + int((end - start )/2) + 1
        row = start
        

        start_col = 0
        end_col = 7        
        for letter in boarding_pass[7:]:
            if letter == 'L':
                end_col = start_col + int((end_col - start_col)/2)
            else:
                start_col = start_col + int((end_col - start_col)/2) + 1
        col = start_col
        
        id_list.append(row * 8 + col)
    
    return id_list

id_list = ids(passes)

# print(max(id_list))


def pass_id(id_list):
    id_list.sort()
    full_list = [x for x in range(id_list[0], id_list[-1]+1)]
    id_list = set(id_list)
    
    for id_num in full_list:
        if id_num not in id_list:
            return id_num

print(pass_id(id_list))