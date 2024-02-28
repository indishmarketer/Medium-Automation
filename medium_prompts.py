prompt_for_headings = """Generate all the chapters or subheadings for this [CONTENT]. Ensure that no part of the CONTENT is overlooked and format the Chapters as concise subheadings.
CONTENT = {content}"""

prompt_for_article = """Write an engaging blog post by formatting the provided [content] with the specified [headings], ensuring the original sentences remain unchanged.

**Guidelines:**

1. Incorporate all provided headings into the post.
2. Maintain the original sentence structure without alteration.
3. Utilize simple English vocabulary consistent with the provided content's style.
4. Do not introduce new information beyond the provided content.

**Content:**
{transcription}

**Headings:**
{subheadings}

**Important Notes:** 
- Create a substantial post; do not shorten it.
- Adhere to all guidelines strictly.

**Requirements:**
1. Use an H1 tag for the title.
2. Utilize H2 tags for section headings.
3. Employ P tags for paragraphs.
4. Exclude full HTML, head, or body tags.

**Output:**
Provide the formatted blog content using H1, H2, and P tags correctly.

**Output Format:**
HTML format
"""

image_prompt = """A stock footage style image visually representing the concept and ideas expressed in a blog post titled '{blog_post_title}'"""

tags_prompt = """Medium article title: "{title}"
Generate 5 Medium article tags that are relevant to the title above, in this exact format: ["tag1", "tag2", "tag3", "tag4", "tag5"]. Warning: Do not include any additional texts in the output other than this ["tag1", "tag2", "tag3", "tag4", "tag5"]."""