'''
Implemented by Svetlana Yesayan and Inesa Aficaryan.
Description:
    The program get all possible breaks for given start time, end time and span_id from json file
Libraries:
    time, sys, json
Usage: python3 program.py
'''
try:
    import os
    import sys
    import json
    from datetime import time
except ImportError as exception:
    print("%s - Please install the necessary libraries." % exception)
    sys.exit(1)

import utils.CartesianProduct as cartesian
from src.class_.Break import Break
from utils.Analyzer import analyzer
from utils.TimeOperations import sub_times, add_times

data = 'utils/data.json'


def get_break_information(span_id):
    with open(data, 'r') as f:
        break_info = json.load(f)
    return break_info[str(span_id)]


def get_real_times(shift, class_start, class_end, start_type, break_duration):
    if start_type == 'RELATIVE_TO_CLASS_START':
        real_start = add_times(class_start, shift)
    else:
        real_start = sub_times(class_end, shift)
    if not real_start or real_start > class_end or real_start < class_start:
        return False, False
    if break_duration == 60:
        real_end = add_times(real_start, time(hour=1))
    else:
        real_end = add_times(real_start, time(minute=break_duration))
    if not real_end or real_end > class_end:
        return False, False
    return real_start, real_end


def program(class_start_time, class_end_time, span_id):
    if int(span_id) > 20:
        raise KeyError("Span_id should be <= 20")
    break_info = get_break_information(span_id)
    break_times = []
    if class_end_time < class_start_time:
        raise ValueError("Start time should be < than End time")
    for el in break_info:
        start_time = el["start_times"]
        start_type = el["start_time_type"]
        break_duration = el["break_duration"]
        break_times_element = []
        for opt in start_time:
            opt_ = time.fromisoformat(opt)
            real_start, real_end = get_real_times(opt_, class_start_time, class_end_time, start_type, break_duration)
            if not real_start:
                continue
            break_times_element.append(Break(real_start, real_end, break_duration))
        if not break_times_element:
            # You need to place as much as possible. I mean there might be a following case you have 4 templates 
            # and there is a template from which break can not be place that does not mean that you should not place breakes at all.
            # For example we use the same span for monday and wednesday:
            # On Monday you have 7hours of classes and hence you will have 3 breaks place but let's say on wednesday you have 3 hours of classes.
            # would it be right to not place breakes because of that? :)
            return []
        break_times.append(break_times_element)
    if len(break_times) == 1:
        filtered_combinations = []
        for el in break_times:
            filtered_combinations.append(el)
            return filtered_combinations
    all_possible_combinations = cartesian.Cartesian(break_times)
    filtered_combinations = analyzer(all_possible_combinations)
    return filtered_combinations


def main():
    if len(sys.argv) != 4:
        print("Specify correct arguments!")
        return
    try:
        class_start_time = time.fromisoformat(sys.argv[1])
        class_end_time = time.fromisoformat(sys.argv[2])
    except ValueError:
        print("Start and End time should be in 'hour:minute:00' format")
        return
    span_id = sys.argv[3]
    result = program(class_start_time, class_end_time, span_id)

    if result:
        for i in result:
            for j in i:
                print(j.start, j.end, j.duration)



if __name__ == "__main__":
    main()
