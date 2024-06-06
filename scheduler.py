from datetime import datetime
from parkinfo_api import get_park_data, get_ride_capacity
from config import opening_time, fast_pass_intervals, get_minute_difference


#Shanghai Disneyland id is 30
queue_data = get_park_data(park_id=30)
ride_capacity = get_ride_capacity(queue_data)


#Look for the nearest slot to user's preferred slot without being too close to user's occupied slots

def nearest_vacant_slot(available_slots, preferred_slot, slots_occupied_by_group, group_size, min_index):
    best_slot = None
    def occupy_slots(slot):
        nonlocal best_slot
        global ride_capacity
        slots_occupied_by_group.add(slot)
        slots_occupied_by_group.add(slot - 1)
        slots_occupied_by_group.add(slot + 1)
        available_slots[slot] -= group_size
        best_slot = slot
    i = preferred_slot
    j = preferred_slot
    # Search for nearest open slot in both directions
    while i >= min_index or j < len(available_slots):
        if i >= min_index and i not in slots_occupied_by_group and available_slots[i] >= group_size:
            occupy_slots(i)
            break
        elif j < len(available_slots) and j not in slots_occupied_by_group and available_slots[j] >= group_size:
            occupy_slots(j)
            break
        i -= 1
        j += 1
    
    return slots_occupied_by_group, best_slot


def scheduler(groupSize, ridePreference, timePreference): 
    global ride_capacity
    group_schedule = {}
    slots_occupied_by_group = set()

    current_time = datetime.now()
    current_time_string = current_time.strftime("%H:%M")
    min_index = max(get_minute_difference(opening_time, current_time_string)/fast_pass_intervals,0)
    print(min_index)

    for ride in ridePreference:
        available_slots = ride_capacity[ride]
        slots_occupied_by_group, best_slot = nearest_vacant_slot(available_slots, timePreference[ride], slots_occupied_by_group, groupSize, min_index)
        if best_slot is not None:
            group_schedule[ride] = best_slot
    
    return group_schedule
