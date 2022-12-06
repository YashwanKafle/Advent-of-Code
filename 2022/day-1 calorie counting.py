with open("day1.in") as file:
    data = [ i for i in file.read().strip().split("\n")]

max_calorie = 0
max_calorie2 = 0
max_calorie3 = 0

check_sum = 0

for calorie in data:

    if calorie == '':
        if check_sum > max_calorie:
            max_calorie3 = max_calorie2
            max_calorie2 = max_calorie
            max_calorie = check_sum
        elif check_sum > max_calorie2:
            max_calorie3 = max_calorie2
            max_calorie2 = check_sum
        elif check_sum > max_calorie3:
            max_calorie3 = check_sum
        
        check_sum = 0

    else :
        check_sum +=int(calorie)

print(f"Part 1 ans : {max_calorie}")
print(f"Part 2 ans : {max_calorie+max_calorie2+max_calorie3}")