#!/usr/bin/env python3
"""
Script that prints the location of a specific GitHub user
"""
import requests
import sys
import time


if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("Usage: ./2-user_location.py <github_api_url>")
        sys.exit(1)

    url = sys.argv[1]
    response = requests.get(url)

    if response.status_code == 404:
        print("Not found")
    elif response.status_code == 403:
        # Rate limit exceeded
        reset_time = int(response.headers.get('X-Ratelimit-Reset', 0))
        current_time = int(time.time())
        minutes_until_reset = (reset_time - current_time) // 60
        print("Reset in {} min".format(minutes_until_reset))
    elif response.status_code == 200:
        data = response.json()
        location = data.get('location')
        print(location)
