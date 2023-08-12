#!/usr/bin/python3
"""
get dashboard id from data dog
"""
import requests
import os

# Set your Datadog API and APP keys using environment variables
DD_SITE = "datadoghq.com"
DD_API_KEY = os.environ.get("DD_API_KEY")
DD_APP_KEY = os.environ.get("DD_APP_KEY")

# Make the API request to retrieve the list of dashboards
url = f"https://api.{DD_SITE}/api/v1/dashboard"
headers = {
    "Content-Type": "application/json",
    "DD-API-KEY": DD_API_KEY,
    "DD-APPLICATION-KEY": DD_APP_KEY,
}

response = requests.get(url, headers=headers)

# Check if the request was successful
if response.status_code == 200:
    dashboards = response.json().get("dashboards", [])
    for dashboard in dashboards:
        dashboard_id = dashboard.get("id")
        dashboard_name = dashboard.get("title")
        print(f"Dashboard Name: {dashboard_name}, ID: {dashboard_id}")
else:
    print(f"Error: {response.status_code} - {response.text}")
