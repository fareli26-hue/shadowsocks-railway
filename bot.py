from pyrogram import Client, filters
import yt_dlp
import os

BOT_TOKEN = os.getenv("BOT_TOKEN")

app = Client(
    "ytbot",
    bot_token=BOT_TOKEN
)

@app.on_message(filters.command("start"))
def start(client, message):
    message.reply_text("✅ لینک یوتیوب را بفرست تا برایت دانلود کنم")

@app.on_message(filters.text & ~filters.command("start"))
def download(client, message):
    url = message.text
    msg = message.reply("در حال دانلود... ⏳")

    ydl_opts = {
        "outtmpl": "video.mp4",
        "format": "best"
    }

    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])

        msg.edit("✅ دانلود تمام شد!")
        message.reply_video("video.mp4")
        os.remove("video.mp4")
    except Exception as e:
        msg.edit(f"❌ خطا:\n{e}")

app.run()
