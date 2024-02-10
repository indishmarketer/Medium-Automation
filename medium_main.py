import medium_prompts
import medium_publisher
import medium_story_creator
import transcripter
import get_next_video
import time
import logging

# Configure logging
logging.basicConfig(filename='medium_automation.log', level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def main():
    # Configurable parameters
    file_path = "youtube_video_file.txt"  # Replace with the actual file path
    selected_model = "gpt-3.5-turbo-16k"
    sleep_duration = 24 * 60 * 60  # Sleep for 24 hours

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
                    logging.warning("Transcript not available for video link: {}. Skipping.".format(video_link))
                    continue

                logging.info("--- Step 1: Generating Headings ---")
                headings = medium_story_creator.generate_headings(prompt_1, selected_model)
                logging.info("Headings: {}".format(headings))

                prompt_2 = medium_prompts.prompt_for_article.format(transcription=transcript, subheadings=headings)
                medium_article = medium_story_creator.generate_medium_article(prompt_2, selected_model)

                logging.info("--- Step 2: Generating Medium Article ---")
                logging.info("Medium Article: {}".format(medium_article))

                story_title_original = medium_story_creator.generate_title(medium_article)
                story_title = story_title_original.replace('"', '')

                logging.info("--- Step 3: Generating Title ---")
                logging.info("Title with quotations: {}".format(story_title_original))
                logging.info("Title without quotations: {}".format(story_title))

                prompt_3 = medium_prompts.image_prompt.format(blog_post_title=story_title)
                image_url = medium_story_creator.generate_image(prompt_3)

                logging.info("--- Step 4: Generating Image ---")
                logging.info("Image URL: {}".format(image_url))

                prompt_4 = medium_prompts.prompt_for_html_formatting.format(blog_post=medium_article, image=image_url)
                html_formatted_article = medium_story_creator.html_formatting(prompt_4, selected_model)

                logging.info("--- Step 5: HTML Formatting ---")
                logging.info("HTML Formatted Article: {}".format(html_formatted_article))

                prompt_5 = medium_prompts.tags_prompt.format(title=story_title)
                tags_for_story = medium_story_creator.medium_story_tags_create(prompt_5)

                logging.info("--- Step 6: Generating Tags ---")
                logging.info("Tags for Story: {}".format(tags_for_story))

                success = medium_publisher.publish_medium_story(story_title, html_formatted_article, tags_for_story)

                if success:
                    logging.info("Post published successfully!")
                else:
                    logging.error("Failed to publish post.")
            except Exception as e:
                logging.error(f"An error occurred while processing video link: {next_link}. Error: {e}")

            # Introduce a sleep timer
            logging.info("--- Waiting for {} hours ---".format(sleep_duration // 3600))
            time.sleep(sleep_duration)
        else:
            logging.info("No more video links. Exiting the program.")
            break  # Exit the loop if there are no more video links

if __name__ == "__main__":
    main()
