#!/usr/bin/env python3
"""
Module that retrieves starships from SWAPI based on passenger capacity
"""
import requests


def availableShips(passengerCount):
    """
    Returns the list of ships that can hold a given number of passengers.

    Args:
        passengerCount: minimum number of passengers the ship must hold

    Returns:
        List of ship names that can hold at least passengerCount passengers.
        Returns an empty list if no ships are available.
    """
    ships = []
    url = "https://swapi-api.hbtn.io/api/starships/"

    while url:
        response = requests.get(url)
        if response.status_code != 200:
            return []

        data = response.json()

        for ship in data.get('results', []):
            passengers = ship.get('passengers', '0')
            # Remove commas from numbers (e.g., "1,000" -> "1000")
            passengers = passengers.replace(',', '')

            # Skip if passengers is not a valid number (e.g., "n/a", "unknown")
            if not passengers.isdigit():
                continue

            if int(passengers) >= passengerCount:
                ships.append(ship['name'])

        # Get next page URL for pagination
        url = data.get('next')

    return ships
