time_list = ["02:05","23:59","01:00"]

def remove_semicolon(el):
    seperated_time = el.split(":")
    time_in_min = (int(seperated_time[0]) * 60) + int(seperated_time[1])
    return time_in_min

def find_min_minutes_def(times):
    if len(times) < 2:
        raise ValueError("List should have atleast 2 items")
    
    updated_list = list(map(remove_semicolon, times))
    
    updated_list.sort()
    updated_list.append(updated_list[0]+1440)

    minimum_minutes_def = updated_list[1] - updated_list[0]

    for index in range(len(updated_list) - 1):
        if updated_list[index + 1] - updated_list[index] < minimum_minutes_def:
            minimum_minutes_def = updated_list[index + 1] - updated_list[index]
            
    return minimum_minutes_def


print(find_min_minutes_def(time_list))
# find_min_minutes_def(time_list)
