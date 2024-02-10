import openai
import requests

key = "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"
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

# Generate the title using OpenAI API
def generate_title(blog_post):
    try:
        prompt = "Generate a suitable, consise, attention-grabbing short title for the given Medium Story. Avoid using quotation marks or symbols in the title:\n" + blog_post
        response = openai.ChatCompletion.create(  # Use ChatCompletion for chat models
            model="gpt-3.5-turbo-16k",  # Adjust the model name as needed
            messages=[{"role": "system", "content": "You are a blog post title writer."},
                      {"role": "user", "content": prompt}]
        )
        return response.choices[0].message["content"].strip()
    except Exception as e:
        print(f"Error in generate_title: {e}")
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

def html_formatting(prompt, selected_model):
    try:
        response = openai.ChatCompletion.create(  # Use ChatCompletion for chat models
            model=selected_model,  # Adjust the model name as needed
            messages=[{"role": "system", "content": "You are a html formatter."},
                      {"role": "user", "content": prompt}]
        )
        return response.choices[0].message["content"].strip() 
    except Exception as e:
        print(f"Error in html_formatting: {e}")
        return None

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