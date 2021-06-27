# © @Aditya1190 [ Telegram ]

from WebStreamer.bot import StreamBot
from WebStreamer.vars import Var
from WebStreamer.utils.human_readable import humanbytes
from WebStreamer.utils.database import Database
from pyrogram import filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from pyrogram.errors import UserNotParticipant
db = Database(Var.DATABASE_URL, Var.SESSION_NAME)


@StreamBot.on_message(filters.command('start') & filters.private & ~filters.edited)
async def start(b, m):
    if not await db.is_user_exist(m.from_user.id):
        await db.add_user(m.from_user.id)
        await b.send_message(
            Var.BIN_CHANNEL,
            f"**NEW USER JOINED:** \n\n__MY NEW FRIEND__ [{m.from_user.first_name}](tg://user?id={m.from_user.id}) __STARTED YOUR BOT !!__"
        )
    usr_cmd = m.text.split("_")[-1]
    if usr_cmd == "/start":
        if Var.UPDATES_CHANNEL != "None":
            try:
                user = await b.get_chat_member(Var.UPDATES_CHANNEL, m.chat.id)
                if user.status == "kicked":
                    await b.send_message(
                        chat_id=m.chat.id,
                        text="__SORRY SIR, You Are Banned To Use Me. Contact The Developer__\n\n @Aditya1190 **They Will Help You**",
                        parse_mode="markdown",
                        disable_web_page_preview=True
                    )
                    return
            except UserNotParticipant:
                await b.send_message(
                    chat_id=m.chat.id,
                    text="<i>Jᴏɪɴ ᴍʏ ᴄʜᴀɴɴᴇʟ ᴛᴏ ᴜsᴇ ᴍᴇ 🔐</i>",
                    reply_markup=InlineKeyboardMarkup(
                        [
                            [
                                InlineKeyboardButton("Jᴏɪɴ ɴᴏᴡ 🔓", url=f"https://t.me/{Var.UPDATES_CHANNEL}")
                            ]
                        ]
                    ),
                    parse_mode="HTML"
                )
                return
            except Exception:
                await b.send_message(
                    chat_id=m.chat.id,
                    text="<i>Something Wrong Contact My Developer</i> <b><a href='http://t.me/Aditya1190'>[ CLICK HERE ]</a></b>",
                    parse_mode="HTML",
                    disable_web_page_preview=True)
                return
        await m.reply_text(
            text="""
<i>👋 ʜᴇʏ, ᴛʜɪs ɪs ғɪʟᴇ ᴛᴏ ʟɪɴᴋ ɢᴇɴ ʙᴏᴛ</i>\n
<i>ᴄʟɪᴄᴋ ᴏɴ /help ᴛᴏ ɢᴇᴛ ᴍᴏʀᴇ ɪɴғᴏʀᴍᴀᴛɪᴏɴ</i>\n
<i><b>🍃 ʙᴏᴛ ᴍᴀɪɴᴛᴀɪɴᴇᴅ ʙʏ :</b>@Aditya1190</i>\n\n
<i><u>𝗪𝗔𝗥𝗡𝗜𝗡𝗚 🚸</u></i>\n
<b>🔞 ᴘᴏʀɴ ᴄᴏɴᴛᴇɴᴛꜱ ʟᴇᴀᴅꜱ ᴛᴏ ᴘᴇʀᴍᴀɴᴇɴᴛ ʙᴀɴ ʏᴏᴜ.</b>""",
            parse_mode="HTML",
            disable_web_page_preview=True,
            reply_markup=InlineKeyboardMarkup( [ [InlineKeyboardButton('My Father 🍂', url='https://t.me/Aditya1190'), 
                                                                                       InlineKeyboardButton('Join', url='https://t.me/Netflix_Latest_Movies') ] ]  ) )
                                                                                       
                                                                                       
                                                                            
    else:
        if Var.UPDATES_CHANNEL != "None":
            try:
                user = await b.get_chat_member(Var.UPDATES_CHANNEL, m.chat.id)
                if user.status == "kicked":
                    await b.send_message(
                        chat_id=m.chat.id,
                        text="**sᴏʀʀʏ sɪʀ, ʏᴏᴜ ᴀʀᴇ ʙᴀɴɴᴇᴅ ᴛᴏ ᴜsᴇ ᴍᴇ. ǫᴜɪᴄᴋʟʏ ᴄᴏɴᴛᴀᴄᴛ** @Aditya1190",
                        parse_mode="markdown",
                        disable_web_page_preview=True
                    )
                    return
            except UserNotParticipant:
                await b.send_message(
                    chat_id=m.chat.id,
                    text="**ᴘʟᴇᴀsᴇ ᴊᴏɪɴ ᴍʏ ᴄʜᴀɴɴᴇʟ ᴛᴏ ᴜsᴇ ᴛʜɪs ʙᴏᴛ**!\n\n**ᴅᴜᴇ ᴛᴏ ᴏᴠᴇʀʟᴏᴀᴅ, ᴏɴʟʏ ᴄʜᴀɴɴᴇʟ sᴜʙsᴄʀɪʙᴇʀs ᴄᴀɴ ᴜsᴇ ᴛʜᴇ ʙᴏᴛ**!",
                    reply_markup=InlineKeyboardMarkup(
                        [
                            [
                                InlineKeyboardButton("🤖 Join Channel", url=f"https://t.me/{Var.UPDATES_CHANNEL}")
                            ],
                            [
                                InlineKeyboardButton("🔄 Refresh / Try Again",
                                                     url=f"https://t.me/AdityaInstantFileToLinkBot.herokuapp.com/{usr_cmd}") # Chnage ur app name
                            ]
                        ]
                    ),
                    parse_mode="markdown"
                )
                return
            except Exception:
                await b.send_message(
                    chat_id=m.chat.id,
                    text="**sᴏᴍᴇᴛʜɪɴɢ ᴡᴇɴᴛ ᴡʀᴏɴɢ. ᴄᴏɴᴛᴀᴄᴛ ᴍᴇ** [ᴀᴅɪᴛʏᴀ](https://t.me/Aditya1190).",
                    parse_mode="markdown",
                    disable_web_page_preview=True)
                return

        get_msg = await b.get_messages(chat_id=Var.BIN_CHANNEL, message_ids=int(usr_cmd))

        file_size = None
        if get_msg.video:
            file_size = f"{humanbytes(get_msg.video.file_size)}"
        elif get_msg.document:
            file_size = f"{humanbytes(get_msg.document.file_size)}"
        elif get_msg.audio:
            file_size = f"{humanbytes(get_msg.audio.file_size)}"

        file_name = None
        if get_msg.video:
            file_name = f"{get_msg.video.file_name}"
        elif get_msg.document:
            file_name = f"{get_msg.document.file_name}"
        elif get_msg.audio:
            file_name = f"{get_msg.audio.file_name}"

        stream_link = "https://{}/{}".format(Var.FQDN, get_msg.message_id) if Var.ON_HEROKU or Var.NO_PORT else \
            "http://{}:{}/{}".format(Var.FQDN,
                                     Var.PORT,
                                     get_msg.message_id)

        msg_text ="""
<i><u>𝐘𝐨𝐮𝐫 𝐏𝐞𝐫𝐦𝐚𝐧𝐞𝐧𝐭 𝐋𝐢𝐧𝐤 𝐆𝐞𝐧𝐞𝐫𝐚𝐭𝐞𝐝 !</u></i>

<b>📂 Fɪʟᴇ ɴᴀᴍᴇ :</b> <i>{}</i>

<b>📦 Fɪʟᴇ ꜱɪᴢᴇ :</b> <i>{}</i>

<b>📥 Dᴏᴡɴʟᴏᴀᴅ :</b> <i>{}</i>

<i>🍃 Bᴏᴛ Mᴀɪɴᴛᴀɪɴᴇᴅ Bʏ :</i> <b>@Aditya1190</b>

"""

        await m.reply_text(
            text=msg_text.format(file_name, file_size, stream_link),
            parse_mode="HTML",
            reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("Dᴏᴡɴʟᴏᴀᴅ ɴᴏᴡ 📥", url=stream_link)]])
        )


@StreamBot.on_message(filters.command('help') & filters.private & ~filters.edited)
async def help_handler(bot, message):
    if not await db.is_user_exist(message.from_user.id):
        await db.add_user(message.from_user.id)
        await bot.send_message(
            Var.BIN_CHANNEL,
            f"**NEW USER JOINED**\n\n__MY NEW FRINED__ [{message.from_user.first_name}](tg://user?id={message.from_user.id}) __STARTED YOUR BOT !!__"
        )
    if Var.UPDATES_CHANNEL is not None:
        try:
            user = await bot.get_chat_member(Var.UPDATES_CHANNEL, message.chat.id)
            if user.status == "kicked":
                await bot.send_message(
                    chat_id=message.chat.id,
                    text="<i>sᴏʀʀʏ sɪʀ, ʏᴏᴜ ᴀʀᴇ ʙᴀɴɴᴇᴅ ᴛᴏ ᴜsᴇ ᴍᴇ. ᴄᴏɴᴛᴀᴄᴛ ᴛʜᴇ ᴅᴇᴠᴇʟᴏᴘᴇʀ</i>",
                    parse_mode="HTML",
                    disable_web_page_preview=True
                )
                return
        except UserNotParticipant:
            await bot.send_message(
                chat_id=message.chat.id,
                text="**ᴘʟᴇᴀsᴇ ᴊᴏɪɴ ᴍʏ ᴜᴘᴅᴀᴛᴇs ᴄʜᴀɴɴᴇʟ ᴛᴏ ᴜsᴇ ᴛʜɪs ʙᴏᴛ!**\n\n__ᴅᴜᴇ ᴛᴏ ᴏᴠᴇʀʟᴏᴀᴅ, ᴏɴʟʏ ᴄʜᴀɴɴᴇʟ sᴜʙsᴄʀɪʙᴇʀs ᴄᴀɴ ᴜsᴇ ᴛʜᴇ ʙᴏᴛ!__",
                reply_markup=InlineKeyboardMarkup(
                    [
                        [
                            InlineKeyboardButton("🤖 Jᴏɪɴ Cʜᴀɴɴᴇʟ", url=f"https://t.me/{Var.UPDATES_CHANNEL}")
                        ]
                    ]
                ),
                parse_mode="markdown"
            )
            return
        except Exception:
            await bot.send_message(
                chat_id=message.chat.id,
                text="__Sᴏᴍᴇᴛʜɪɴɢ ᴡᴇɴᴛ Wʀᴏɴɢ. Cᴏɴᴛᴀᴄᴛ ᴍᴇ__ [Aᴠɪsʜᴋᴀʀ Pᴀᴛɪʟ](https://t.me/Aditya1190).",
                parse_mode="markdown",
                disable_web_page_preview=True)
            return
    await message.reply_text(
        text="""
<i>Sᴇɴᴅ ᴍᴇ ᴀɴʏ ꜰɪʟᴇ (ᴏʀ) ᴍᴇᴅɪᴀ ꜰʀᴏᴍ ᴛᴇʟᴇɢʀᴀᴍ.</i>\n
<i>I ᴡɪʟʟ ᴘʀᴏᴠɪᴅᴇ ᴇxᴛᴇʀɴᴀʟ ᴅɪʀᴇᴄᴛ ᴅᴏᴡɴʟᴏᴀᴅ ʟɪɴᴋ !.</i>\n
<u>𝗪𝗔𝗥𝗡𝗜𝗡𝗚 🚸</u>\n
<b>ᴘᴏʀɴ ᴄᴏɴᴛᴇɴᴛꜱ ʟᴇᴀᴅꜱ ᴛᴏ ᴘᴇʀᴍᴀɴᴇɴᴛ ʙᴀɴ ʏᴏᴜ.</b>\n
<i>Cᴏɴᴛᴀᴄᴛ ᴅᴇᴠᴇʟᴏᴘᴇʀ (ᴏʀ) ʀᴇᴘᴏʀᴛ ʙᴜɢꜱ</i> <b>: <a href='https://t.me/Aditya1190'>[ ᴄʟɪᴄᴋ ʜᴇʀᴇ ]</a></b>""",
        parse_mode="HTML",
        disable_web_page_preview=True,
        reply_markup=InlineKeyboardMarkup(
            [
                [InlineKeyboardButton("🏵 DEV", url="https://t.me/Aditya1190")],
                [InlineKeyboardButton("Join", url="https://t.me/Netflix_Latest_Movies")]
            ]
        )
    )
