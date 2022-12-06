from utils import inputfile_to_array, get_input_file

get_input_file(2)

input_list = inputfile_to_array("inputs/input_day_2.txt")

def run_round_version_1(opponent_input, your_input):
  result_map = {
    "WIN": 6,
    "DRAW": 3,
    "LOSE": 0,
  }
  opponent_shape_score  = 0
  your_shape_score = 0
  result = ''
  if opponent_input == 'A':
    opponent_shape_score = 1
    if your_input == 'X':
      your_shape_score = 1
      result = "DRAW"
    if your_input == 'Y':
      your_shape_score = 2
      result = "WIN"
    if your_input == 'Z':
      your_shape_score = 3
      result = "LOSE"
  if opponent_input == 'B':
    opponent_shape_score = 2
    if your_input == 'X':
      your_shape_score = 1
      result = "LOSE"
    if your_input == 'Y':
      your_shape_score = 2
      result = "DRAW"
    if your_input == 'Z':
      your_shape_score = 3
      result = "WIN"
  if opponent_input == 'C':
    opponent_shape_score = 3
    if your_input == 'X':
      your_shape_score = 1
      result = "WIN"
    if your_input == 'Y':
      your_shape_score = 2
      result = "LOSE"
    if your_input == 'Z':
      your_shape_score = 3
      result = "DRAW"
  result = your_shape_score + int(result_map[result])
  return result
def run_round_version_2(opponent_input, needed_result):
  result_map = {
    "X": 0,
    "Y": 3,
    "Z": 6,
  }
  your_shape_score = 0
  result = ''
  if opponent_input == 'A': # stein
    if needed_result == 'X': 
      your_shape_score = 3
    if needed_result == 'Y':
      your_shape_score = 1
    if needed_result == 'Z':
      your_shape_score = 2
  if opponent_input == 'B': # papir
    if needed_result == 'X':
      your_shape_score = 1
    if needed_result == 'Y':
      your_shape_score = 2
    if needed_result == 'Z':
      your_shape_score = 3
  if opponent_input == 'C': # saks
    if needed_result == 'X':
      your_shape_score = 2
    if needed_result == 'Y':
      your_shape_score = 3
    if needed_result == 'Z':
      your_shape_score = 1
  result = your_shape_score + int(result_map[needed_result])
  return result

def get_score_from_all_rounds_version_1(input_rounds):
  your_total_score = 0
  for i in input_rounds:
    your_round_score = run_round_version_1(i[0], i[-1])
    your_total_score = your_total_score + your_round_score
  return your_total_score

def get_score_from_all_rounds_version_2(input_rounds):
  your_total_score = 0
  for i in input_rounds:
    your_round_score = run_round_version_2(i[0], i[-1])
    your_total_score = your_total_score + your_round_score
  return your_total_score

#print(input_list)
print(get_score_from_all_rounds_version_1(input_list))
print(get_score_from_all_rounds_version_2(input_list))