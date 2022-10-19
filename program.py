#python3.7 >
import sys
import json
from datetime import datetime, time, date
import utils.CartesianProduct as cartesian
from src.class_.Break import Break
from src.class_.Duration import Duration

data = 'utils/data.json'


def get_break_information(span_id):
    with open(data, 'r') as f:
        break_info = json.load(f)
    return break_info[span_id]


def break_analyzer(possible_combination):
    for i in range(len(possible_combination)):
        if possible_combination[i].start.hour > possible_combination[i + 1].start.hour:
            return False
        elif possible_combination[i].start.hour == possible_combination[i + 1].start.hour and possible_combination[i].start.minute > possible_combination[i + 1].start.minute:
            return False
        if i == len(possible_combination) - 2:
            break
    return True


def analyzer(all_possible_combinations):
    filtered_break_comb = []
    for el in all_possible_combinations:
        if break_analyzer(el):
            filtered_break_comb.append(el)
    return filtered_break_comb



def main():
    if len(sys.argv) != 4:
        print("Specify correct arguments!")
        return
    class_start_time = time.fromisoformat(sys.argv[1])
    class_end_time = time.fromisoformat(sys.argv[2])
    span_id = sys.argv[3]
    break_info = get_break_information(span_id)
    print(break_info)
    break_times = []
    for el in break_info:
        start_time = el["start_times"]
        start_type = el["start_time_type"]
        break_duration = el["break_duration"]
        if break_duration == 60:
            break_duration = 0
        break_times_element = []
        if start_type == 'RELATIVE_TO_CLASS_START':
            for opt in start_time:
                opt_ = time.fromisoformat(opt)
                hour = class_start_time.hour + opt_.hour
                minute = opt_.minute + class_start_time.minute
                if hour > 23 or hour > class_end_time.hour:
                    continue
                if minute > 59:
                    hour += 1
                    minute = minute - 60
                real_time_duration = Duration(time(hour, minute), break_duration)
                break_times_element.append(real_time_duration)
        if start_type == 'RELATIVE_TO_SHIFT_END':
            for opt in start_time:
                opt_ = time.fromisoformat(opt)
                minute = class_end_time.minute - opt_.minute
                hour = class_start_time.hour - opt_.hour
                if minute < 0:
                    hour = class_end_time.hour - 1
                    minute = minute * (-1)
                if hour < 1 or hour < class_start_time.hour:
                    continue
                real_time_duration = Duration(time(hour,minute), break_duration)
                break_times_element.append(real_time_duration)
        if not break_times_element:
            print("false")
            return
        break_times.append(break_times_element)
    all_possible_combinations = cartesian.Cartesian(break_times)
    print(analyzer(all_possible_combinations))


if __name__ == "__main__":
    main()