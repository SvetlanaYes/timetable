from utils.TimeOperations import sub_times

def get_break_durations(possible_combination):
    durations = []
    for i in range(len(possible_combination) - 1):
        tmp = sub_times(possible_combination[i + 1].start, possible_combination[i].end)
        if not tmp:
            return []
        time_to_minute = tmp.minute + 60*tmp.hour
        durations.append(time_to_minute)
    return durations


def analyzer(all_possible_combinations):
    consecutive_breaks = []
    min_duration_of_break_combination = []
    sample = {}
    count = 0
    for el in all_possible_combinations:
        durations = get_break_durations(el)
        if durations:
            sample[count] = el
            count += 1
            consecutive_breaks.append(durations)
    if not consecutive_breaks:
        return []
    for el in consecutive_breaks:
        min_duration_of_break_combination.append(min(el))
    max_ = max(min_duration_of_break_combination)
    if max_ < 120:
        indexes = [i for i, x in enumerate(min_duration_of_break_combination) if x == max_]
    else:
        indexes = [i for i, x in enumerate(min_duration_of_break_combination) if x >= 120]
    result = [list(sample[x]) for x in sample.keys() if x in indexes]

    return result
