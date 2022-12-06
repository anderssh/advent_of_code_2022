from utils import inputfile_to_array, get_input_file

get_input_file(1)

input_list = inputfile_to_array("inputs/input_day_1.txt")

def make_calorie_list(input_list):
    calorie_list = []
    single_ration = []
    for element in input_list:
        if element == "":
            calorie_list.append(single_ration)
            single_ration = []
        else:
            single_ration.append(int(element))
    return calorie_list

def get_biggest_ration(calorie_list):
    biggest_ration = 0
    for index, calories_ration in enumerate(calorie_list):
        ration_sum = sum(calories_ration)
        if ration_sum > biggest_ration:
            biggest_ration = ration_sum
            biggest_ration_index = index
    return biggest_ration, biggest_ration_index

def get_top_n_rations(calorie_list, number_of_rations_to_sum = 3):
    biggest_ration_list=[]
    for i in range(number_of_rations_to_sum):
        biggest_ration,biggest_ration_index =  get_biggest_ration(calorie_list)
        biggest_ration_list.append(biggest_ration)
        calorie_list.pop(biggest_ration_index)
    return sum(biggest_ration_list)

calorie_list = make_calorie_list(input_list)
biggest_ration,_ = get_biggest_ration(calorie_list)
top_3_rations = get_top_n_rations(calorie_list)
print(biggest_ration)
print(top_3_rations)