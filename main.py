import settings
import discord
import re
from activate_server import activate_server

TOKEN = settings.TOKEN

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)


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

    await user_message.reply(bot_message)


activate_server()
client.run(TOKEN)
