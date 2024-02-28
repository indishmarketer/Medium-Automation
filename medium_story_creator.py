import openai
import requests
from bs4 import BeautifulSoup

key = "YOUR_OPENAI_API_KEY"
openai.api_key = key
selected_model = "gpt-3.5-turbo-16k"

def generate_headings(prompt, selected_model):
    try:
        response = openai.ChatCompletion.create(  # Use ChatCompletion for chat models
            model=selected_model,  # Adjust the model name as needed
            messages=[{"role": "system", "content": "You write subheadings for blog posts."},
                      {"role": "user", "content": prompt}]
        )
        return response.choices[0].message["content"].strip()
    except Exception as e:
        print(f"Error in generate_headings: {e}")
        return None

# Generate blog post
def generate_medium_article(prompt, selected_model):
    try:
        response = openai.ChatCompletion.create(  # Use ChatCompletion for chat models
            model=selected_model,  # Adjust the model name as needed
            messages=[{"role": "system", "content": "You write best blog post from video script."},
                      {"role": "user", "content": prompt}]
        )
        return response.choices[0].message["content"].strip()
    except Exception as e:
        print(f"Error in generate_medium_article: {e}")
        return None

def generate_title(html_content):
    # Parse the HTML content
    soup = BeautifulSoup(html_content, 'html.parser')

    # Find the first h1 tag
    title_tag = soup.find('h1')

    if title_tag:
        # Get the text inside the h1 tag
        title = title_tag.text.strip()
        return title
    else:
        print("No title (h1 tag) found in the HTML content.")
        return None

def generate_image(prompt):
    try:
        url = "https://api.openai.com/v1/images/generations"
        headers = {
            "Content-Type": "application/json",
            "Authorization": f"Bearer {key}"  # Use the actual API key here
        }

        data = {
            "model": "dall-e-3",
            "prompt": prompt,
            "n": 1,
            "size": "1792x1024",
            "style": "natural"
        }

        response = requests.post(url, headers=headers, json=data)

        # Check if the request was successful
        if response.status_code == 200:
            result = response.json()
            # Retrieve the image URL from the correct path
            image_url = result['data'][0]['url']
            return image_url
        else:
            print(f"Error in generate_image: {response.status_code}")
            return None
    except Exception as e:
        print(f"Error in generate_image: {e}")
        return None

from bs4 import BeautifulSoup

def html_formatting(article_html, image_link):
    # Parse the HTML content
    soup = BeautifulSoup(article_html, 'html.parser')

    # Find the first paragraph tag
    first_paragraph = soup.find('p')

    if first_paragraph:
        # Create a new image tag
        new_img_tag = soup.new_tag('img', src=image_link)

        # Insert the image tag after the first paragraph tag
        first_paragraph.insert_after(new_img_tag)
    else:
        print("No paragraph tag found in the HTML content.")

    # Return the modified HTML content
    return str(soup)


def medium_story_tags_create(prompt):
    try:
        response = openai.ChatCompletion.create( 
            model="gpt-3.5-turbo",
            messages=[{"role": "system", "content": prompt}],
        )
        return response.choices[0].message["content"].strip()
    except Exception as e:
        print(f"Error in medium_story_tags_create: {e}")
        return None