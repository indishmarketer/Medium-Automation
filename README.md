# Medium Automation

This project automates the process of creating and publishing articles on Medium using video transcripts from YouTube.

## Features

- Automatically retrieve YouTube video links from a specified text file and download transcripts
- High-quality prompts are used to generate the content for the article.
- Uses GPT-3.5 and above models to generate headings, article body, title and tags based on video transcript 
- Generates a relevant image for the article using DALL-E
- Formats the article into HTML for publishing on Medium
- Publishes the article to your Medium account

## Usage

### Prerequisites

- Python 3.x
- API keys for the following services:
  - [OpenAI](https://openai.com/) - to access GPT-3.5 and above models
- Medium account with publishing access (Medium Integration Token)

### Configuration

- Clone the repository: `git clone https://github.com/indishmarketer/Medium-Automation.git`
- Install dependencies: `pip install -r requirements.txt` 
- Update `medium_story_creator.py`with your OpenAI API key.
- Update `medium_userid.py`with your Medium integration token
- Get your Medium User ID 
- Update `medium_publisher.py` with your Medium integration token and User ID.

### Usage

- Update `youtube_video_file.txt` with links to YouTube videos, one on each line 
- Run `python main.py`
- The program will iterate through the video links, generate articles and publish them to Medium
- Published articles will be logged in `medium_automation.log`

## Customization

- You can tweak the GPT models and sleep timer in `main.py`
- You can change the promots in `medium_prompts.py`
- Video transcription is handled by `transcripter.py`
- GPT-3 article generation happens in `medium_story_creator.py` 
- Publishing to Medium using `medium_publisher.py`

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- [OpenAI](https://openai.com/) for the GPT and DALL-E API