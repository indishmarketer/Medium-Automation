import requests

# Set your access token
access_token = "MEDIUM_INTEGRATION_TOKEN"

# Set the API endpoint
api_url = "https://api.medium.com/v1/me"

# Set headers for the request
headers = {
    "Authorization": f"Bearer {access_token}",
    "Content-Type": "application/json",
    "Accept": "application/json",
    "Accept-Charset": "utf-8"
}

# Make the GET request
response = requests.get(api_url, headers=headers)

# Check if the request was successful (status code 200)
if response.status_code == 200:
    # Parse the JSON response
    user_data = response.json()["data"]

    # Extract user details
    user_id = user_data["id"]
    username = user_data["username"]
    name = user_data["name"]
    url = user_data["url"]
    imageUrl = user_data["imageUrl"]

    # Print or use the user details as needed
    print(f"User ID: {user_id}")
    print(f"Username: {username}")
    print(f"Name: {name}")
    print(f"URL: {url}")
    print(f"Image URL: {imageUrl}")
else:
    # Print the error message if the request was not successful
    print(f"Error {response.status_code}: {response.text}")
