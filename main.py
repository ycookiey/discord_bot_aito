import os
import discord
import re
from activate_server import activate_server
import google.generativeai as genai
import textwrap
from IPython.display import Markdown

TOKEN = os.getenv("TOKEN")
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
BOT_ID = os.getenv("BOT_ID")

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)

genai.configure(api_key=GEMINI_API_KEY)
model = genai.GenerativeModel("gemini-pro")


def to_markdown(text):
    text = text.replace("•", "  *")
    return Markdown(textwrap.indent(text, "> ", predicate=lambda _: True))


@client.event
async def on_ready():
    print(f"We have logged in as {client.user}")


@client.event
async def on_message(user_message):
    if user_message.author == client.user:
        return

    user_text: str = user_message.content
    if user_text.startswith("/"):
        bot_message = "https://www.google.com/search?q=" + "+".join(
            re.split("[ 　]+", user_text.strip())
        )
    elif user_text.endswith("とは？") or user_text.endswith("とは?"):
        bot_message = "https://www.google.com/search?q=" + "+".join(
            re.split("[ 　]+", user_text[:-3].strip())
        )
    elif client.user.mentioned_in(user_message):
        bot_message = model.generate_content(user_text.replace(f"<@{BOT_ID}>", "")).text
    await user_message.reply(bot_message)


activate_server()
client.run(TOKEN)
