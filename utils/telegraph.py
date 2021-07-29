from html_telegraph_poster import TelegraphPoster


def post_to_telegraph(title, html_format_content):

    post_client = TelegraphPoster(use_api=True)
    auth_name = "@PyLyricsBot"
    bish = "https://t.me/PyLyricsBot"
    post_client.create_api_token(auth_name)
    try:
        post_page = post_client.post(
            title=title,
            author=auth_name,
            author_url=bish,
            text=html_format_content)
        return post_page["url"]
    except BaseException:
        return "t.me/PyLyricsBot"
