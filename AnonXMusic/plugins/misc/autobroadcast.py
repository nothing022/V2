import asyncio
import datetime
from AnonXMusic import app
from pyrogram import Client
from config import START_IMG_URL
from AnonXMusic.utils.database import get_served_chats
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton


MESSAGE = f"""‣  тнιѕ ιѕ  [Nᴏᴛʜɪɴɢ Rᴏʙᴏᴛ](https://t.me/{app.username}})"""🫧­­­­­­­­­­­­­  
                                                                                                                                                      ➜ A ᴛᴇʟᴇɢʀᴀᴍ ʙᴏᴛ ᴡɪᴛʜ sᴏᴍᴇ ᴀᴅᴠᴀɴᴄᴇᴅ ғᴇᴀᴛᴜʀᴇs.

🔐ᴜꜱᴇ » [/start](https://t.me/{app.username}?start=help) ᴛᴏ ᴄʜᴇᴄᴋ ʙᴏᴛ

BUTTON = InlineKeyboardMarkup(
    [
        [
            InlineKeyboardButton("Add me", url=f"https://t.me/{app.username}?startgroup=s&admin=delete_messages+manage_video_chats+pin_messages+invite_users")
        ]
    ]
)

async def send_message_to_chats():
    try:
        chats = await get_served_chats()

        for chat_info in chats:
            chat_id = chat_info.get('chat_id')
            if isinstance(chat_id, int):  # Check if chat_id is an integer
                try:
                    await app.send_photo(chat_id, photo=START_IMG_URL, caption=MESSAGE, reply_markup=BUTTON)
                    await asyncio.sleep(3)  # Sleep for 1 second between sending messages
                except Exception as e:
                    pass  # Do nothing if an error occurs while sending message
    except Exception as e:
        pass  # Do nothing if an error occurs while fetching served chats
async def continuous_broadcast():
    while True:
        await send_message_to_chats()
        await asyncio.sleep(50000)  # Sleep (30000 seconds) between next broadcast

# Start the continuous broadcast loop
asyncio.create_task(continuous_broadcast())
