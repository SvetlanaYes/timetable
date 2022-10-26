from timetable.src.class_.Break import Break
import datetime
from timetable.program import program


def isEqual(list1, list2):
    for element1, element2 in zip(list1, list2):
        for el1, el2 in zip(element1, element2):
            if el1 != el2:
                return False
    return True


def test1():
    start_class_time = datetime.time(9, 0, 0)
    end_class_time = datetime.time(17, 0, 0)
    span_id = 1
    result = program(start_class_time, end_class_time, span_id)
    correct_result = [[Break(datetime.time(10, 30, 0), datetime.time(10, 45, 0), 15), Break(datetime.time(11, 0, 0), datetime.time(11, 15, 0), 15), Break(datetime.time(11, 30, 0), datetime.time(11, 45, 0), 15), Break(datetime.time(12, 0, 0), datetime.time(12, 15, 0), 15), Break(datetime.time(12, 30, 0), datetime.time(13, 30, 0), 60)]]

    print(isEqual(result, correct_result))

def test2():
    start_class_time = datetime.time(9, 0, 0)
    end_class_time = datetime.time(10, 0, 0)
    span_id = 1
    result = program(start_class_time, end_class_time, span_id)
    correct_result = []

    print(isEqual(result, correct_result))

def test3():
    start_class_time = datetime.time(10, 0, 6)
    end_class_time = datetime.time(19, 0, 0)
    span_id = 6
    result = program(start_class_time, end_class_time, span_id)
    correct_result = [[Break(datetime.time(11, 30, 0), datetime.time(11, 45, 0), 15), Break(datetime.time(13, 0, 0), datetime.time(13, 30, 0), 30)]]

    print(isEqual(result, correct_result))

def test4():
    start_class_time = datetime.time(10, 0, 6)
    end_class_time = datetime.time(19, 0, 0)
    span_id = 11
    result = program(start_class_time, end_class_time, span_id)
    correct_result = []

    print(isEqual(result, correct_result))
