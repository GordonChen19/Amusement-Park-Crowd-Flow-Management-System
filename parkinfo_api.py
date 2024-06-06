import requests
from config import operating_minutes, max_fast_passes_per_slot, fast_pass_intervals

#Calling Waiting Times API from https://queue-times.com/pages/api Powered by Queue-Times.com


def get_park_data(park_id):
    """Fetch the queue times for a specific park."""
    url = f"https://queue-times.com/parks/{park_id}/queue_times.json"
    response = requests.get(url)
    queue_data = response.json()
    return queue_data

def display_queue_times(queue_data):
    """Display the queue times for the park."""
    for land in queue_data['lands']:
        print(f"Land: {land['name']}")
        for ride in land['rides']:
            status = "Open" if ride['is_open'] else "Closed"
            if status == "Open":
                wait_time = ride['wait_time']
                last_updated = ride['last_updated']
                print(f"  Ride: {ride['name']}, Status: {status}, Wait Time: {wait_time} minutes, Last Updated: {last_updated}")

def get_ride_capacity(queue_data):
    """Return a dictionary with ride capacity"""
    slots = int(operating_minutes/ fast_pass_intervals) + 1
    ride_info = {}
    for land in queue_data['lands']:
        for ride in land['rides']:
            ride_name = ride['name']
            status = "Open" if ride['is_open'] else "Closed"
            if status == "Open":
                ride_info[ride_name] = [max_fast_passes_per_slot] * (slots)
    return ride_info




queue_data = get_park_data(30)
display_queue_times(queue_data )