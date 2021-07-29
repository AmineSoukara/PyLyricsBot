import random
import time

from lyricsgenius import Genius
from pyrogram import Client, filters
from pyromod.helpers import ikb

from utils.configs import Tr, Var
from utils.telegraph import post_to_telegraph

Ly = Client(
    "Lyrics Lite Bot",
    bot_token=Var.BOT_TOKEN,
    api_id=Var.API_ID,
    api_hash=Var.API_HASH,
)

genius = Genius(Var.API)

STARTPIC = "https://i.imgur.com/gv2SzKr.jpg"

START_BTN = ikb(
    [
        [
            ("💬 Updates Channel", "t.me/damiensoukara", "url"),
            ("🗣 Support Group", "t.me/damienhelp", "url"),
        ],
        [
            ("👾 About", "about"),
            ("📚 Help", "help"),
            ("❌", "close"),
        ],
        [
            (
                "🔗 Source Code",
                "https://github.com/AmineSoukara/PyLyricsBot/fork",
                "url",
            ),
            ("👨‍💻 Developer", "https://bio.link/aminesoukara", "url"),
        ],
    ]
)


HOMEBTN = ikb([[("🏠", "home"), ("❌", "close")]])
CLOSEBTN = [("❌", "close")]


@Ly.on_callback_query()
async def cdata(c, q):

    data = q.data
    # userid = q.from_user.id
    pwait = Tr.WAIT
    if data == "home":
        await q.answer(pwait)
        await q.message.edit_text(
            text=Tr.START_TEXT.format(q.from_user.mention),
            reply_markup=START_BTN,
            disable_web_page_preview=True,
        )
    elif data == "help":
        await q.answer(pwait)
        await q.message.edit_text(
            text=Tr.HELP_TEXT, reply_markup=HOMEBTN, disable_web_page_preview=True
        )
    elif data == "about":
        await q.answer(pwait)
        await q.message.edit_text(
            text=Tr.ABOUT_TEXT,
            reply_markup=HOMEBTN,
            disable_web_page_preview=True,
        )
    elif data == "close":
        await q.message.delete(True)
        try:
            await q.message.reply_to_message.delete(True)
        except BaseException:
            pass
    elif data.startswith("lytr_"):
        id = data.split("_", 1)[1]
        # lyrics = genius.lyrics(int(id)).replace("URLCopyEmbedCopy", "").replace("EmbedShare", "")
        r = genius.search_song(song_id=int(id))
        await q.answer(
            f"{Tr.SEARCHING}\n\n{Tr.SONG} {r.title}\n{Tr.ARTIST} {r.artist}",
            show_alert=True,
        )
        lyrics = r.lyrics.replace("URLCopyEmbedCopy", "").replace("EmbedShare", "")

        test = f"""<p align="center"><a href="#"><img src="{r.song_art_image_url}" width="250"></a></p>"""

        final = test + f"{lyrics}\n-\n📜 From : @PyLyricsBot"
        song_title = r.title
        song_artist = r.artist.replace("&", "ft")
        name = f"{song_title} {song_artist}"
        # name = f"{r.full_title}"
        done = final.replace("\n", "<br/>")
        link = post_to_telegraph(name, done)
        time.sleep(random.randint(1, 6))
        cap = f"{Tr.SONG} {r.title}\n{Tr.ARTIST} {r.artist}\n"

        LyBTN = ikb(
            [
                [
                    ("🔗 Genius", r.url, "url"),
                    ("🔗 Telegraph", link, "url"),
                ],
                [
                    ("❌", "close"),
                ],
            ]
        )

        await q.message.reply_photo(
            r.song_art_image_url, caption=cap, reply_markup=LyBTN
        )
    else:
        await q.message.delete()


@Ly.on_message(filters.private & filters.command(["start"]))
async def start(c, m):
    await m.reply_photo(
        photo=STARTPIC,
        caption=Tr.START_TEXT.format(m.from_user.mention),
        reply_markup=START_BTN,
    )


@Ly.on_message(filters.private & filters.text)
async def lytxt(c, m):
    if not Var.API:
        return await m.reply_text(
            Tr.ERR_TEXT,
            quote=True,
            # reply_markup=ikb(CLOSEBTN),
        )

    await m.reply_chat_action("typing")

    title = m.text

    try:
        request = genius.search_songs(title, Var.PAGENUM)
    except BaseException:
        return await m.reply(
            Tr.ERRTOKEN_TEXT,
            quote=True,
        )

    x = [
        (f"• {hits['result']['full_title']}", f"lytr_{hits['result']['id']}")
        for hits in request["hits"]
    ]
    buttons = list(zip(x[::2], x[1::2]))
    if len(x) % 2 == 1:
        buttons.append((x[-1],))
    if len(x) == 0:
        return await m.reply(Tr.NORES)

    buttons.append(CLOSEBTN)
    await m.reply_text(
        text=f"{Tr.SEARCHING} {title}",
        quote=True,
        reply_markup=ikb(buttons),
    )


Ly.run()
