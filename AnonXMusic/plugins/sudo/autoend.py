from pyrogram import filters
from pyrogram.types import Message

from AnonXMusic import app
from AnonXMusic.misc import SUDOERS
from AnonXMusic.utils.database import autoend_off, autoend_on


@app.on_message(filters.command(["/autoend","autoend","المغادره","مغادره"], "") & SUDOERS)
async def auto_end_stream(_, message: Message):
    usage = " <b>المغادره التلقائيه :</b>\n\n❃ تفعيل المغادره \n⚡️ عند التفعيل سيغادر المساعد المحادثه الصوتيه عندما لا يوجد احد سواه\n\n❃ تعطيل المغادره\n⚡️ سيبقى المساعد في المحادثه الصوتيه ولا يغادرها"
    if len(message.command) != 2:
        return await message.reply_text(usage)
    state = message.text.split(None, 1)[1].strip().lower()
    if state == "تفعيل":
        await autoend_on()
        await message.reply_text(
            "❃ تم تفعيل المغادره التلقائيه.\n\n سيغادر المساعد تلقائيا عند نزول الكل من المحادثه الصوتيه ."
        )
    elif state == "تعطيل":
        await autoend_off()
        await message.reply_text("❃ تم تعطيل المغادره التلقائيه.")
    else:
        await message.reply_text(usage)
