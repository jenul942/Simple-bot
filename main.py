import os
import telebot
import time
import asyncio

Jrbot = Client(
   "Simple Bot",
   api_id=Config.APP_ID,
   api_hash=Config.API_HASH,
   bot_token=Config.TG_BOT_TOKEN,
)

@Jrbot.on_message(filters.command("start"))
async def start(client, message):
   if message.chat.type == 'private':
       await Jebot.send_message(
               chat_id=message.chat.id,
               text="""<b>Hey There, I'm Simple Bot""",


print(
    """
Bot Started!
Join @HelpSinhalen
"""
)

Jrbot.run()