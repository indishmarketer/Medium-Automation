import medium_prompts
import medium_publisher
import medium_story_creator
import transcripter
import get_next_video

def main():
    # Configurable parameters
    file_path = "youtube_video_file.txt"  # Replace with the actual file path
    selected_model = "gpt-3.5-turbo-16k"

    current_link = 0
    while True:
        next_link, current_link = get_next_video.get_next_video_link(file_path, current_link)

        if next_link is not None:
            try:
                # Input YouTube video link from the user
                video_link = next_link
                transcript = transcripter.get_caption_text(video_link)

                if transcript is not None:
                    prompt_1 = medium_prompts.prompt_for_headings.format(content=transcript)
                else:
                    print("Warning: Transcript not available for video link: {}. Skipping.".format(video_link))
                    continue

                print("--- Step 1: Generating Headings ---")
                headings = medium_story_creator.generate_headings(prompt_1, selected_model)
                print("Headings: {}".format(headings))

                print("--- Step 2: Generating Medium Article ---")
                prompt_2 = medium_prompts.prompt_for_article.format(transcription=transcript, subheadings=headings)
                medium_article = medium_story_creator.generate_medium_article(prompt_2, selected_model)
                print("Medium Article: {}".format(medium_article))

                print("--- Step 3: Generating Title ---")
                story_title = medium_story_creator.generate_title(medium_article)
                print("Story Title: {}".format(story_title))

                print("--- Step 4: Generating Image ---")
                prompt_3 = medium_prompts.image_prompt.format(blog_post_title=story_title)
                image_url = medium_story_creator.generate_image(prompt_3)
                print("Image URL: {}".format(image_url))

                print("--- Step 5: HTML Formatting ---")
                html_formatted_article = medium_story_creator.html_formatting(medium_article, image_url)
                print("HTML Formatted Article: {}".format(html_formatted_article))

                print("--- Step 6: Generating Tags ---")
                prompt_5 = medium_prompts.tags_prompt.format(title=story_title)
                tags_for_story = medium_story_creator.medium_story_tags_create(prompt_5)
                print("Tags for Story: {}".format(tags_for_story))

                success = medium_publisher.publish_medium_story(story_title, html_formatted_article, tags_for_story)

                if success:
                    print("Post published successfully!")
                else:
                    print("Error: Failed to publish post.")
            except Exception as e:
                print(f"Error: An error occurred while processing video link: {next_link}. Error: {e}")

        else:
            print("No more video links. Exiting the program.")
            break  # Exit the loop if there are no more video links

if __name__ == "__main__":
    main()