import random 
from pyrogram import filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, Message
from PURVIMUSIC.plugins.tools.pretenderdb import impo_off, impo_on, check_pretender, add_userdata, get_userdata, usr_data
from PURVIMUSIC import app

MISHI = [
"https://telegra.ph/file/f350818b3b267280ebb7b.jpg",
"https://telegra.ph/file/6f656beef0b24b1082136.jpg",
"https://telegra.ph/file/2dc5d2c417fae288275a0.jpg",
"https://telegra.ph/file/0462eacbef102ae6f0d80.jpg",
"https://telegra.ph/file/1231e8086b4bcbca8a12b.jpg",
"https://telegra.ph/file/646053f894fde8da84a87.jpg",
"https://telegra.ph/file/b11f82a48e0920f7ebcb7.jpg",
"https://telegra.ph/file/4e94c837043ea4e8b0de0.jpg",
"https://telegra.ph/file/d4b82210a6c2aa6f5c327.jpg",
"https://telegra.ph/file/29e4629051b5159a0edde.jpg",
"https://telegra.ph/file/303ea976ff9594b61c419.jpg",
"https://telegra.ph/file/29e4629051b5159a0edde.jpg",
"https://telegra.ph/file/0462eacbef102ae6f0d80.jpg",
"https://telegra.ph/file/0462eacbef102ae6f0d80.jpg",
"https://telegra.ph/file/d4b82210a6c2aa6f5c327.jpg",
"https://telegra.ph/file/d4b82210a6c2aa6f5c327.jpg",
"https://telegra.ph/file/4e94c837043ea4e8b0de0.jpg",
"https://telegra.ph/file/303ea976ff9594b61c419.jpg",
"https://telegra.ph/file/efc616221c814994eb36a.jpg",
"https://telegra.ph/file/657820a0d766b79cf71f9.jpg",
"https://telegra.ph/file/4cd6e74cb2e0ca6f721b5.jpg",
"https://telegra.ph/file/4cd6e74cb2e0ca6f721b5.jpg",
]


ROY = [
    [
        InlineKeyboardButton(
            text="ᴀᴅᴅ ᴍᴇ",
            url=f"https://t.me/NIKKU_ROBOT?startgroup=true"),
        InlineKeyboardButton(text="ᴜᴘᴅᴀᴛᴇ", url=f"https://t.me/HEROKU_CLUB")
    ],
]


@app.on_message(filters.group & ~filters.bot & ~filters.via_bot, group=69)
async def chk_usr(_, message: Message):
    if message.sender_chat or not await check_pretender(message.chat.id):
        return
    if not await usr_data(message.from_user.id):
        return await add_userdata(
            message.from_user.id,
            message.from_user.username,
            message.from_user.first_name,
            message.from_user.last_name,
        )
    usernamebefore, first_name, lastname_before = await get_userdata(message.from_user.id)
    msg = ""
    if (
        usernamebefore != message.from_user.username
        or first_name != message.from_user.first_name
        or lastname_before != message.from_user.last_name
    ):
        msg += f"""
**♥︎ ᴜsᴇʀ sʜᴏʀᴛ ɪɴғᴏʀᴍᴀᴛɪᴏɴ ♥︎**

**๏ ɴᴀᴍᴇ** ➛ {message.from_user.mention}
**๏ ᴜsᴇʀ ɪᴅ** ➛ {message.from_user.id}
"""
    if usernamebefore != message.from_user.username:
        usernamebefore = f"@{usernamebefore}" if usernamebefore else "NO USERNAME"
        usernameafter = (
            f"@{message.from_user.username}"
            if message.from_user.username
            else "NO USERNAME"
        )
        msg += """
**♥︎ ᴄʜᴀɴɢᴇᴅ ᴜsᴇʀɴᴀᴍᴇ ♥︎**

**๏ ʙᴇғᴏʀᴇ** ➛ {bef}
**๏ ᴀғᴛᴇʀ** ➛ {aft}
""".format(bef=usernamebefore, aft=usernameafter)
        await add_userdata(
            message.from_user.id,
            message.from_user.username,
            message.from_user.first_name,
            message.from_user.last_name,
        )
    if first_name != message.from_user.first_name:
        msg += """
**♥︎ ᴄʜᴀɴɢᴇs ғɪʀsᴛ ɴᴀᴍᴇ ♥︎**

**๏ ʙᴇғᴏʀᴇ** ➛ {bef}
**๏ ᴀғᴛᴇʀ** ➛ {aft}
""".format(
            bef=first_name, aft=message.from_user.first_name
        )
        await add_userdata(
            message.from_user.id,
            message.from_user.username,
            message.from_user.first_name,
            message.from_user.last_name,
        )
    if lastname_before != message.from_user.last_name:
        lastname_before = lastname_before or "NO LAST NAME"
        lastname_after = message.from_user.last_name or "NO LAST NAME"
        msg += """
**♥︎ ᴄʜᴀɴɢᴇs ʟᴀsᴛ ɴᴀᴍᴇ ♥︎**

**๏ ʙᴇғᴏʀᴇ** ➛ {bef}
**๏ ᴀғᴛᴇʀ** ➛ {aft}
""".format(
            bef=lastname_before, aft=lastname_after
        )
        await add_userdata(
            message.from_user.id,
            message.from_user.username,
            message.from_user.first_name,
            message.from_user.last_name,
        )
    if msg != "":
        await message.reply_photo(random.choice(MISHI), caption=msg, reply_markup=InlineKeyboardMarkup(ROY),)


@app.on_message(filters.group & filters.command("imposter") & ~filters.bot & ~filters.via_bot)
async def set_mataa(_, message: Message):
    if len(message.command) == 1:
        return await message.reply("**ᴅᴇᴛᴇᴄᴛ ᴘʀᴇᴛᴇɴᴅᴇʀ ᴜsᴇʀs ᴜsᴀɢᴇ : ᴘʀᴇᴛᴇɴᴅᴇʀ ᴏɴ|ᴏғғ**")
    if message.command[1] == "enable":
        cekset = await impo_on(message.chat.id)
        if cekset:
            await message.reply("**ᴘʀᴇᴛᴇɴᴅᴇʀ ᴍᴏᴅᴇ ɪs ᴀʟʀᴇᴀᴅʏ ᴇɴᴀʙʟᴇᴅ.**")
        else:
            await impo_on(message.chat.id)
            await message.reply(f"**sᴜᴄᴄᴇssғᴜʟʟʏ ᴇɴᴀʙʟᴇᴅ ᴘʀᴇᴛᴇɴᴅᴇʀ ᴍᴏᴅᴇ ғᴏʀ** {message.chat.title}")
    elif message.command[1] == "disable":
        cekset = await impo_off(message.chat.id)
        if not cekset:
            await message.reply("**ᴘʀᴇᴛᴇɴᴅᴇʀ ᴍᴏᴅᴇ ɪs ᴀʟʀᴇᴀᴅʏ ᴅɪsᴀʙʟᴇᴅ.**")
        else:
            await impo_off(message.chat.id)
            await message.reply(f"**sᴜᴄᴄᴇssғᴜʟʟʏ ᴅɪsᴀʙʟᴇᴅ ᴘʀᴇᴛᴇɴᴅᴇʀ ᴍᴏᴅᴇ ғᴏʀ** {message.chat.title}")
    else:
        await message.reply("**ᴅᴇᴛᴇᴄᴛ ᴘʀᴇᴛᴇɴᴅᴇʀ ᴜsᴇʀs ᴜsᴀɢᴇ : ᴘʀᴇᴛᴇɴᴅᴇʀ ᴏɴ|ᴏғғ**")

    
