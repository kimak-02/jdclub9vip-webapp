import os
from telegram import (
    Update,
    ReplyKeyboardMarkup,
    KeyboardButton,
    WebAppInfo,
    InlineKeyboardMarkup,
    InlineKeyboardButton,
)
from telegram.ext import (
    ApplicationBuilder,
    CommandHandler,
    ContextTypes,
    MessageHandler,
    filters,
)

TOKEN = "8409919660:AAEYGWhPQ03dw3VALNJwW1rbA-ep_Pxe9HU"
WEBAPP_URL = "https://jdclub9vip-webapp.vercel.app"  # mini app url

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

def img(filename: str) -> str:
    return os.path.join(BASE_DIR, "images", filename)

def main_menu_kb():
    return ReplyKeyboardMarkup(
        [
            ["📌 JDCLUB9VIP", "💡 JDCLUB9VIP Tutorial"],
            ["🔥 HOT GAME TIPS", "📞 Whatsapp Us"],
            ["👥 Join Group"],
        ],
        resize_keyboard=True
    )

def tutorial_menu_kb():
    return ReplyKeyboardMarkup(
        [
            ["💡 SMS REGISTER", "💡 AUTO DEPOSIT"],
            ["💡 INVITE DOWNLINE", "💡 CHECK DOWNLINE"],
            ["💡 FORGET PASSWORD", "💡 WITHDRAW"],
            ["⬅️ Back to Main Menu"],
        ],
        resize_keyboard=True
    )

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    caption_text = (
        "🍀 JDCLUB9VIP Elite Entertainment\n"
        "Exclusive Access. Unlimited Winning. ✔\n\n"
        "✨ SIGN UP FREE SGD29.00\n"
        "✨ DAILY LOGIN SGD99.00\n"
        "✨ WELCOME BONUS 180%\n"
        "✨ DAILY REBATE 2%\n"
        "🔥 DAILY BETTING REBATE 2% + WEEKLY REBATE 5% 🔥\n\n"
        "Customer Is Always Number One, Let Us Serve You Better 💯"
    )

    keyboard = [
        [InlineKeyboardButton("🚀 REGISTER HERE FREE SGD29.00", web_app=WebAppInfo(url=WEBAPP_URL))]
    ]

    banner_path = img("banner.jpg")
    if os.path.exists(banner_path):
        with open(banner_path, "rb") as f:
            await update.message.reply_photo(
                photo=f,
                caption=caption_text,
                reply_markup=InlineKeyboardMarkup(keyboard)
            )
    else:
        await update.message.reply_text("Tak jumpa banner: images/banner.jpg")

    await update.message.reply_text("Main Menu 👇", reply_markup=main_menu_kb())

async def text_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = (update.message.text or "").strip()
    chat_id = update.effective_chat.id

    if text == "📌 JDCLUB9VIP":
        await update.message.reply_text(
            "Open JDCLUB9VIP Mini App 👇",
            reply_markup=InlineKeyboardMarkup([
                [InlineKeyboardButton("OPEN JDCLUB9VIP (Mini App)", web_app=WebAppInfo(url=WEBAPP_URL))]
            ])
        )
        return

    if text == "💡 JDCLUB9VIP Tutorial":
        await update.message.reply_text("JDCLUB9VIP Tutorial 👇", reply_markup=tutorial_menu_kb())
        return

    if text == "🔥 HOT GAME TIPS":
        p = img("hot_game_tips.jpg")  # pastikan file ni ada
        caption = "JDCLUB9VIP Hot Game Tips Recommend Easy Get Free Spin And Jackpot🔥😍"
        if os.path.exists(p):
            with open(p, "rb") as f:
                await context.bot.send_photo(chat_id=chat_id, photo=f, caption=caption)
        else:
            await update.message.reply_text("Tak jumpa gambar: images/hot_game_tips.jpg")
        await update.message.reply_text("Main Menu 👇", reply_markup=main_menu_kb())
        return

    if text == "📞 Whatsapp Us":
        await update.message.reply_text(
            "Whatsapp Register 👇",
            reply_markup=InlineKeyboardMarkup([
                [InlineKeyboardButton("Open WhatsApp", url="https://wa.me/6588969034")]
            ])
        )
        return

    if text == "👥 Join Group":
        await update.message.reply_text(
            "Join Group 👇",
            reply_markup=InlineKeyboardMarkup([
                [InlineKeyboardButton("Join Telegram Group", url="https://t.me/JDCLUB9VIPSG")]
            ])
        )
        return

    tutorial_map = {
        "💡 SMS REGISTER": "t1_sms_register.jpg",
        "💡 AUTO DEPOSIT": "t4_auto_deposit.jpg",
        "💡 INVITE DOWNLINE": "t5_invite_downline.jpg",
        "💡 CHECK DOWNLINE": "t6_check_downline.jpg",
        "💡 FORGET PASSWORD": "t7_forget_password.jpg",
        "💡 WITHDRAW": "t8_withdraw.jpg",
    }

    if text in tutorial_map:
        p = img(tutorial_map[text])
        if os.path.exists(p):
            with open(p, "rb") as f:
                await context.bot.send_photo(chat_id=chat_id, photo=f)
        else:
            await update.message.reply_text(f"Tak jumpa gambar: images/{tutorial_map[text]}")
        await update.message.reply_text("JDCLUB9VIP Tutorial 👇", reply_markup=tutorial_menu_kb())
        return

    if text == "⬅️ Back to Main Menu":
        await update.message.reply_text("Main Menu 👇", reply_markup=main_menu_kb())
        return

    await update.message.reply_text("Type /start untuk buka menu.", reply_markup=main_menu_kb())

def main():
    app = ApplicationBuilder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, text_handler))
    print("Bot is running...")
    app.run_polling()

if __name__ == "__main__":
    main()
