"""
Author: Bisnu Ray
User: https://t.me/SmartBisnuBio
Channel: https://t.me/itsSmartDev
"""

import os
import re
import asyncio
from urllib.parse import urlparse
from pyrogram import Client, filters
from aiogram import Bot, Dispatcher, types
from aiogram.types import ParseMode, InputFile
from aiogram.utils import executor

# Bot setup
BOT_TOKEN = "123456:ABCDEFGHIJLLJOdMttZ5hEZ78"   # Replace this BOT_TOKEN
bot = Bot(token=BOT_TOKEN)
dp = Dispatcher(bot)

# User Client setup
api_id = "12345678"     # Replace this api_id
api_hash = "12345678abcdefghijklm"       # Replace this api_hash
phone_number = "+123456789"       # Replace this phone_number

mail_scr_queue = asyncio.Queue()

# Admin user ID for authorization
YOUR_ADMIN_USER_ID = 1783730975     # Replace this ADMIN_USER_ID 

user_client_mail = Client("mailscr", api_id=api_id, api_hash=api_hash, phone_number=phone_number)

def filter_messages(message):
    if message is None:
        return []

    pattern = r'(\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b:\S+)'
    matches = re.findall(pattern, message)

    return matches

async def is_authorized(user_id):
    return user_id == YOUR_ADMIN_USER_ID

async def collect_channel_data(user_client_mail, channel_identifier, amount):
    messages = []

    async for message in user_client_mail.search_messages(channel_identifier):
        matches = filter_messages(message.text)
        if matches:
            messages.extend(matches)

        if len(messages) >= amount:
            break

    if not messages:
        return [], "<b>No Email and Password Combinations were found</b>"

    filtered_messages = messages[:amount]

    return filtered_messages, None

async def process_mail_scr_queue(user_client_mail, bot):
    while True:
        task = await mail_scr_queue.get()
        message, channel_identifier, amount, progress_message = task
        
        filtered_messages, error_msg = await collect_channel_data(user_client_mail, channel_identifier, amount)

        if error_msg:
            await progress_message.delete()
            await bot.send_message(message.chat.id, error_msg, parse_mode=ParseMode.HTML)
            return

        if not filtered_messages:
            await progress_message.delete()
            await bot.send_message(message.chat.id, "<b>🥲 No email and password combinations were found.</b>", parse_mode=ParseMode.HTML)
            return
        
        await progress_message.delete()

        with open(f'{channel_identifier}_combos.txt', 'w', encoding='utf-8') as file:
            for combo in filtered_messages:
                try:
                    file.write(f"{combo}\n")
                except UnicodeEncodeError:
                    continue

        with open(f'{channel_identifier}_combos.txt', 'rb') as file:
            output_message = f"""<b>Mail Scrapped Successful ✅
━━━━━━━━━━━━━━━━━━
Source: <code>{channel_identifier}</code>
Mail Amount: {len(filtered_messages)}
━━━━━━━━━━━━━━━━━━
Mail Scrapped By: <a href='https://t.me/itsSmartDev'>Smart Dev</a></b>"""
            await bot.send_document(message.chat.id, InputFile(file), caption=output_message, parse_mode=ParseMode.HTML)

        os.remove(f'{channel_identifier}_combos.txt')
        
        mail_scr_queue.task_done()

@dp.message_handler(commands=['scrmail'])
async def collect_handler(message: types.Message):
    greni = message.text.split()
    if len(greni) < 3:
        await message.reply("<b>❌ Please provide a channel with amount</b>", parse_mode=ParseMode.HTML)
        return

    channel_identifier = greni[1]
    amount = int(greni[2])

    parsed_url = urlparse(channel_identifier)
    if parsed_url.scheme and parsed_url.netloc:
        if parsed_url.path.startswith('/+'):
            try:
                chat = await user_client_mail.join_chat(channel_identifier)
                channel_identifier = chat.id
            except Exception as e:
                if "USER_ALREADY_PARTICIPANT" in str(e):
                    try:
                        chat = await user_client_mail.get_chat(channel_identifier)
                        channel_identifier = chat.id
                    except Exception as e:
                        await message.reply(f"<b>❌ Error joining this chat {channel_identifier}</b>", parse_mode=ParseMode.HTML)
                        return
                else:
                    await message.reply(f"<b>❌ Error in channel string {channel_identifier}</b>", parse_mode=ParseMode.HTML)
                    return
        else:
            channel_identifier = parsed_url.path.lstrip('/')
    else:
        channel_identifier = channel_identifier

    try:
        await user_client_mail.get_chat(channel_identifier)
    except Exception as e:
        await message.answer(f"<b>❌Please make sure the provided username is valid: {channel_identifier}</b>", parse_mode=ParseMode.HTML)
        return

    if not await is_authorized(message.from_user.id):
        if amount > 10000:
            await message.answer("<b>Request exceeds limit of 10,000</b>", parse_mode=ParseMode.HTML)
            return
        amount = min(amount, 10000)
    else:
        amount = amount

    progress_message = await message.answer("<b>Request Processing Wait....</b>", parse_mode=ParseMode.HTML)
    
    await mail_scr_queue.put((message, channel_identifier, amount, progress_message))

async def on_startup(dp):
    await user_client_mail.start()
    asyncio.create_task(process_mail_scr_queue(user_client_mail, bot))

if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True, on_startup=on_startup)
