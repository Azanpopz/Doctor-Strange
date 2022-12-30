import os
from pyrogram import Client, filters, enums
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, Message, User, ChatJoinRequest
from myscript import script
from info import PICS
import os
import logging
import random
import asyncio

from pyrogram import Client, filters, enums
from pyrogram.errors import ChatAdminRequired, FloodWait
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from database.ia_filterdb import Media, get_file_details, unpack_new_file_id
from database.users_chats_db import db
from info import CHANNELS, ADMINS, AUTH_CHANNEL, LOG_CHANNEL, PICS, BATCH_FILE_CAPTION, CUSTOM_FILE_CAPTION, PROTECT_CONTENT, MSG_ALRT, MAIN_CHANNEL
from utils import get_settings, get_size, is_subscribed, save_group_settings, temp
from database.connections_mdb import active_connection
import re
import json
import base64
logger = logging.getLogger(__name__)


pr0fess0r_99=Client(
    "Auto Approved Bot",
    bot_token = os.environ["BOT_TOKEN"],
    api_id = int(os.environ["API_ID"]),
    api_hash = os.environ["API_HASH"]
)

FILE_CHANNEL=int(os.environ.get("FILE_CHANNEL", None))
TEXT=os.environ.get("APPROVED_WELCOME_TEXT", "ʜᴇʟʟᴏ {mention}\nᴡᴇʟᴄᴏᴍᴇ ᴛᴏ ᴍʏ ᴄʜᴀɴɴᴇʟ.{title}\n\nᴏɴʟʏ ɴᴇᴡ ᴀɴᴅ ʟᴏᴡ ꜱɪᴢᴇ ᴍᴏᴠɪᴇ ᴀᴠᴀɪʟᴀʙʟᴇ. ᴇɴᴊᴏʏɪɴɢ🔥🔥")
APPROVED = os.environ.get("APPROVED_WELCOME", "on").lower()

@Client.on_chat_join_request(filters.chat(FILE_CHANNEL))
async def autoapprove(client: pr0fess0r_99, message: ChatJoinRequest):
    chat=message.chat # Chat
    user=message.from_user # User
    print(f"{user.first_name} Joined 🤝") # Logs
    await client.approve_chat_join_request(chat_id=chat.id, user_id=user.id)
    if APPROVED == "on":
        buttons = [[
            InlineKeyboardButton('⚚ ᴀᴅᴅ ᴍᴇ ᴛᴏ ʏᴏᴜʀ ɢʀᴏᴜᴘ ⚚', url=f'http://t.me/{temp.U_NAME}?startgroup=true')
            ],[
            InlineKeyboardButton('ᴍᴏᴠɪᴇ ɢʀᴏᴜᴘ', url='https://t.me/at3movies'),
            InlineKeyboardButton('♚ ᴏᴡɴᴇʀ ♚', url='https://t.me/aboutexinos')
            ],[      
            InlineKeyboardButton('〄 ʜᴇʟᴘ 〄', callback_data='help'),
            InlineKeyboardButton('⍟ ᴀʙᴏᴜᴛ ⍟', callback_data='about')
            ],[
            InlineKeyboardButton('⌬ sᴜᴘᴘᴏʀᴛ ⌬', url='https://t.me/czdbotz_support')
        ]]         
        reply_markup = InlineKeyboardMarkup(buttons)
        await client.send_message(chat_id=chat.id, text=Hello {message.from_user.mention} welcome to {message.chat.title} group),
            reply_markup=reply_markup,
            parse_mode=enums.ParseMode.HTML
        )
        print("Welcome....")

print("Auto Approved Bot")

