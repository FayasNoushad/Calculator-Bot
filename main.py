import os
from dotenv import load_dotenv
from pyrogram import Client, filters
from pyrogram.types import *


load_dotenv()

Bot = Client(
    "Calculator Bot",
    bot_token=os.environ.get("BOT_TOKEN"),
    api_id=int(os.environ.get("API_ID")),
    api_hash=os.environ.get("API_HASH")
)


START_TEXT = """Hello {},
I am a simple calculator telegram bot. \
Send me /calculator for inline button keyboard or send as text. \
You can also use me in inline.

Made by @FayasNoushad"""

START_BUTTONS = InlineKeyboardMarkup(
    [
        [
            InlineKeyboardButton('⚙ Feedback ⚙', url='https://telegram.me/FayasNoushad')
        ]
    ]
)

CALCULATE_TEXT = "Made by @FayasNoushad"

CALCULATE_BUTTONS = InlineKeyboardMarkup(
    [
        [
            InlineKeyboardButton("(", callback_data="("),
            InlineKeyboardButton(")", callback_data=")"),
            InlineKeyboardButton("^", callback_data="^")
        ],
        [
            InlineKeyboardButton("%", callback_data="%"),
            InlineKeyboardButton("AC", callback_data="AC"),
            InlineKeyboardButton("DEL", callback_data="DEL"),
            InlineKeyboardButton("÷", callback_data="/")
        ],
        [
            InlineKeyboardButton("7", callback_data="7"),
            InlineKeyboardButton("8", callback_data="8"),
            InlineKeyboardButton("9", callback_data="9"),
            InlineKeyboardButton("×", callback_data="*")
        ],
        [
            InlineKeyboardButton("4", callback_data="4"),
            InlineKeyboardButton("5", callback_data="5"),
            InlineKeyboardButton("6", callback_data="6"),
            InlineKeyboardButton("-", callback_data="-")
        ],
        [
            InlineKeyboardButton("1", callback_data="1"),
            InlineKeyboardButton("2", callback_data="2"),
            InlineKeyboardButton("3", callback_data="3"),
            InlineKeyboardButton("+", callback_data="+"),
        ],
        [
            InlineKeyboardButton("00", callback_data="00"),
            InlineKeyboardButton("0", callback_data="0"),
            InlineKeyboardButton("=", callback_data="="),
            InlineKeyboardButton(".", callback_data=".")
        ]
    ]
)


@Bot.on_message(filters.command(["start"]))
async def start(_, message):
    await message.reply_text(
        text=START_TEXT.format(message.from_user.mention),
        disable_web_page_preview=True,
        reply_markup=START_BUTTONS,
        quote=True
    )


@Bot.on_message(filters.private & filters.command(["calc", "calculate", "calculator"]))
async def calculate(_, message):
    await message.reply_text(
        text=CALCULATE_TEXT,
        reply_markup=CALCULATE_BUTTONS,
        disable_web_page_preview=True,
        quote=True
    )


@Bot.on_message(filters.private & filters.text)
async def evaluate(_, message):
    try:
        data = message.text.replace("×", "*").replace("÷", "/")
        result = str(eval(data))
    except:
        return
    await message.reply_text(
        text=result,
        reply_markup=CALCULATE_BUTTONS,
        disable_web_page_preview=True,
        quote=True
    )


@Bot.on_callback_query()
async def cb_data(_, message):
        data = message.data
        try:
            message_text = message.message.text.split("\n")[0].strip().split("=")[0].strip()
            text = '' if CALCULATE_TEXT in message_text else message_text
            if data == "=":
                text = str(eval(text))
            elif data == "DEL":
                text = message_text[:-1]
            elif data == "AC":
                text = ""
            else:
                text = message_text + data
            await message.message.edit_text(
                text=f"{text}\n\n{CALCULATE_TEXT}",
                disable_web_page_preview=True,
                reply_markup=CALCULATE_BUTTONS
            )
        except Exception as error:
            print(error)


@Bot.on_inline_query()
async def inline(bot, update):
    if len(update.data) == 0:
        try:
            answers = [
                InlineQueryResultArticle(
                    title="Calculator",
                    description="New calculator",
                    input_message_content=InputTextMessageContent(
                        text=CALCULATE_TEXT,
                        disable_web_page_preview=True
                    ),
                    reply_markup=CALCULATE_BUTTONS
                )
            ]
        except Exception as error:
            print(error)
    else:
        try:
            data = update.query.replace("×", "*").replace("÷", "/")
            result = str(eval(text))
            answers = [
                InlineQueryResultArticle(
                    title="Answer",
                    description=f"Result: {result}",
                    input_message_content=InputTextMessageContent(
                        text=f"{data} = {result}",
                        disable_web_page_preview=True
                    )
                )
            ]
        except:
            pass
    await update.answer(answers)


Bot.run()
