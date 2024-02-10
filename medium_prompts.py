prompt_for_headings = """Generate all the chapters or subheadings for this [CONTENT]. Ensure that no part of the CONTENT is overlooked and format the Chapters as concise subheadings.
CONTENT = {content}"""

prompt_for_article = """"Convert the provided [content] into an engaging blog post by formatting it with the specified [headings].

Guidelines:

1. Ensure all provided headings are utilized in the post.
2. Aim to create a lengthy, comprehensive post.
3. Use simple English words and match the writing style of the content.
4. Do not add additional information beyond what is provided in the content.

content: {transcription}

headings: {subheadings}

Important notes: Please create a lengthy post, do not shorten. Also ensure all guidelines are followed."""

prompt_for_html_formatting = """Format the following blog post text using:

1. An H1 tag for the title
2. H2 tags for section headings
3. P tags for paragraphs
4. An IMG tag after the first paragraph to include the image provided
5. No need for full HTML, head or body tags.

Blog Post = {blog_post}

Image = {image}

Output just the formatted blog content using the H1, H2, P, and IMG tags properly

Caution: Avoid placing the IMG tag at the end of the post. Insert the IMG tag only after the first <p> tag."""

image_prompt = """A stock footage style image visually representing the concept and ideas expressed in a blog post titled '{blog_post_title}'"""

tags_prompt = """Medium article title: "{title}"
Generate 5 Medium article tags that are relevant to the title above, in this exact format: ["tag1", "tag2", "tag3", "tag4", "tag5"]. Warning: Do not include any additional texts in the output other than this ["tag1", "tag2", "tag3", "tag4", "tag5"]."""