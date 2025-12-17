from telegram import InlineKeyboardButton
from telegram.utils.helpers import escape_markdown as es


def welcome_msg():
    welcome_msg = '''<b>Welcome to the Bot</b>
<i>Send any Instagram username or profile URL to fetch the profile picture.</i>

Example:
<b>virat.kohli</b>
<b>thenameisyash</b>'''

    return welcome_msg


def acc_type(val):
    if val:
        return "Private Account"
    else:
        return "Public Account"


def create_caption(user):
    caption_msg = f'''📌 *Name*: {es(user.full_name, version=2)}
👥 *Followers*: {es(str(user.followers), version=2)}
👤 *Following*: {es(str(user.followees), version=2)}
🔐 *Account Type*: {acc_type(user.is_private)}

Thank you for using the bot.'''

    return caption_msg


def get_username(url):
    try:
        data = url.split("/")[3]
        if "?" in data:
            data = data.split("?")
            return data[0]
        return data
    except Exception:
        return "incorrect format"