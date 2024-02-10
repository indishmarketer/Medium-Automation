import requests
import json

def publish_medium_story(title, content, tags):
    # Set your access token and user ID
    access_token = "27ed4ff6393804935c67d60f45a58e832eb59043197fb0c86a5b942271f011134"
    user_id = "1a3d38180fec82a2df6bcca394d9c05447cd3badade77a7f4dc24a72cfcb784a1"

    # Convert the string representation to an actual list
    tags_list = json.loads(tags)

    # Set the API endpoint for creating a post
    api_url = f"https://api.medium.com/v1/users/{user_id}/posts"

    # Set headers for the request
    headers = {
        "Authorization": f"Bearer {access_token}",
        "Content-Type": "application/json",
        "Accept": "application/json",
        "Accept-Charset": "utf-8"
    }

    # Set the content of your post
    post_content = {
        "title": title,
        "contentFormat": "html",  # or "markdown"
        "content": content,
        "tags": tags_list,  # Optional: Add your tags
        "publishStatus": "public",  # or "draft" for a draft post
        "notifyFollowers": True  # Set to True to notify followers
    }

    # Print the payload before making the POST request
    print("\nAPI Request Payload:")
    print(post_content)

    # Make the POST request
    response = requests.post(api_url, headers=headers, json=post_content)

    # Check if the request was successful (status code 201)
    if response.status_code == 201:
        return True
    else:
        # Print the error message if the request was not successful
        print(f"Error {response.status_code}: {response.text}")
        return False