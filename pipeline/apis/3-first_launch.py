#!/usr/bin/env python3
"""
Script that displays the first SpaceX launch
"""
import requests


if __name__ == '__main__':
    # Get the latest launch
    launch_url = "https://api.spacexdata.com/v5/launches/latest"
    response = requests.get(launch_url)

    if response.status_code != 200:
        exit(1)

    launch = response.json()

    # Get launch details
    launch_name = launch.get('name')
    launch_date = launch.get('date_local')
    rocket_id = launch.get('rocket')
    launchpad_id = launch.get('launchpad')

    # Fetch rocket name
    rocket_url = "https://api.spacexdata.com/v4/rockets/{}".format(rocket_id)
    rocket_response = requests.get(rocket_url)
    rocket_name = "Unknown"
    if rocket_response.status_code == 200:
        rocket_data = rocket_response.json()
        rocket_name = rocket_data.get('name')

    # Fetch launchpad details
    launchpad_url = "https://api.spacexdata.com/v4/launchpads/{}".format(
        launchpad_id)
    launchpad_response = requests.get(launchpad_url)
    launchpad_name = "Unknown"
    launchpad_locality = "Unknown"
    if launchpad_response.status_code == 200:
        launchpad_data = launchpad_response.json()
        launchpad_name = launchpad_data.get('name')
        launchpad_locality = launchpad_data.get('locality')

    # Format and print the output
    print("{} ({}) {} - {} ({})".format(
        launch_name, launch_date, rocket_name,
        launchpad_name, launchpad_locality))
