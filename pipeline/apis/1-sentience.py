#!/usr/bin/env python3
"""
Module that retrieves home planets of sentient species from SWAPI
"""
import requests


def sentientPlanets():
    """
    Returns the list of names of the home planets of all sentient species.

    Returns:
        List of planet names where sentient species originate from.
    """
    planets = []
    url = "https://swapi-api.hbtn.io/api/species/"

    while url:
        response = requests.get(url)
        if response.status_code != 200:
            return []

        data = response.json()

        for species in data.get('results', []):
            classification = species.get('classification', '').lower()
            designation = species.get('designation', '').lower()

            # Check if species is sentient
            if 'sentient' in classification or 'sentient' in designation:
                homeworld = species.get('homeworld')
                if homeworld:
                    # Fetch homeworld details to get the planet name
                    planet_response = requests.get(homeworld)
                    if planet_response.status_code == 200:
                        planet_data = planet_response.json()
                        planet_name = planet_data.get('name')
                        if planet_name and planet_name not in planets:
                            planets.append(planet_name)
                else:
                    # If homeworld is null, add "unknown"
                    if "unknown" not in planets:
                        planets.append("unknown")

        # Get next page URL for pagination
        url = data.get('next')

    return planets
