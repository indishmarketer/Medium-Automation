from youtube_transcript_api import YouTubeTranscriptApi

def get_caption_text(video_link):
    try:
        # Extract the video ID from the YouTube video link
        video_id = video_link.split("?v=")[1]

        # Get the transcript for the video
        transcript = YouTubeTranscriptApi.get_transcript(video_id)

        # Combine the transcript into a single text
        transcript_text = ' '.join([entry['text'] for entry in transcript])

        return transcript_text
    except Exception as e:
        print(f"Failed to retrieve transcript: {str(e)}")
        return None
