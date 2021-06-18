import os
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton

FayasNoushad = Client(
    "Calculator Bot",
    bot_token = os.environ["BOT_TOKEN"],
    api_id = int(os.environ["API_ID"]),
    api_hash = os.environ["API_HASH"]
)

buttons = InlineKeyboardMarkup(
        [[
        InlineKeyboardButton("DEL", callback_data="DEL"),
        InlineKeyboardButton("AC", callback_data="AC"),
        ],[
        InlineKeyboardButton("(", callback_data="("),
        InlineKeyboardButton(")", callback_data=")"),
        ],[
        InlineKeyboardButton("7", callback_data="7"),
        InlineKeyboardButton("8", callback_data="8"),
        InlineKeyboardButton("9", callback_data="9"),
        InlineKeyboardButton("/", callback_data="/"),
        ],[
        InlineKeyboardButton("4", callback_data="4"),
        InlineKeyboardButton("5", callback_data="5"),
        InlineKeyboardButton("6", callback_data="6"),
        InlineKeyboardButton("*", callback_data="*"),
        ],[
        InlineKeyboardButton("1", callback_data="1"),
        InlineKeyboardButton("2", callback_data="2"),
        InlineKeyboardButton("3", callback_data="3"),
        InlineKeyboardButton("-", callback_data="-"),
        ],[
        InlineKeyboardButton(".", callback_data="."),
        InlineKeyboardButton("0", callback_data="0"),
        InlineKeyboardButton("=", callback_data="="),
        InlineKeyboardButton("+", callback_data="+"),
        ]]
    )

@FayasNoushad.on_callback_query()
async def cb_data(bot, update):
    key = update.data
    await update.message.edit(
        text=f"{update.text} {key}",
        disable_web_page_preview=True,
        reply_markup=buttons
    )

FayasNoushad.run()
