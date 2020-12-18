file = open('d5.txt')

def pass_list(file):
    result = []
    for line in file:
        result.append(line.rstrip())
    return result

passes = pass_list(file)

def highest_id(passes):
    highest = 0
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
        seat_id = row * 8 + col
        highest = max(highest, seat_id)
    
    return highest

print(highest_id(passes))