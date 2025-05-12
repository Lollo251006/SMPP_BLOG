def format_blog_post(content):
    paragraphs = content.split('\n\n')
    title = paragraphs[0] if paragraphs else 'Titolo generico'
    body ='\n\n'.join(paragraphs[1:]) if len(paragraphs) > 1 else formatted = f
    "{title} \n\n {body}"

    return formatted