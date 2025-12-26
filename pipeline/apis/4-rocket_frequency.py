#!/usr/bin/env python3
"""
Script that displays the number of launches per rocket
"""
import requests


if __name__ == '__main__':
    # Get all launches
    launches_url = "https://api.spacexdata.com/v4/launches"
    response = requests.get(launches_url)

    if response.status_code != 200:
        exit(1)

    launches = response.json()

    # Count launches per rocket ID
    rocket_counts = {}
    for launch in launches:
        rocket_id = launch.get('rocket')
        if rocket_id:
            rocket_counts[rocket_id] = rocket_counts.get(rocket_id, 0) + 1

    # Get rocket names
    rockets_url = "https://api.spacexdata.com/v4/rockets"
    rockets_response = requests.get(rockets_url)

    rocket_names = {}
    if rockets_response.status_code == 200:
        rockets = rockets_response.json()
        for rocket in rockets:
            rocket_names[rocket.get('id')] = rocket.get('name')

    # Build list with rocket names and counts
    results = []
    for rocket_id, count in rocket_counts.items():
        name = rocket_names.get(rocket_id, "Unknown")
        results.append((name, count))

    # Sort by count descending, then by name ascending
    results_sorted = sorted(results, key=lambda x: (-x[1], x[0]))

    # Print results
    for name, count in results_sorted:
        print("{}: {}".format(name, count))
