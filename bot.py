from telegram import Update, KeyboardButton, ReplyKeyboardMarkup
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes
from config import TOKEN


# Admin chat ID (replace with actual chat ID of the admin)
ADMIN_CHAT_ID = 123456789

# Boshlanish xabari
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    welcome_text = (
        "Assalomu alaykum  👉IT WORLD👈  o'quv markazining rasmiy botiga xush kelibsiz🖐🖐🖐"
    )
    # Asosiy menyu tugmachalari
    keyboard = [
        [KeyboardButton("🌐Ishtimoiy sahifalar"), KeyboardButton("💳To'lov qilish")],
        [KeyboardButton("🔖Kurslar🔖"), KeyboardButton("📍Manzil📍")],
        [KeyboardButton("💻Bizning xizmatlar"), KeyboardButton("📞Bog'lanish")],
        [KeyboardButton("📝Taklif va Mulohazalar uchun")],
    ]
    reply_markup = ReplyKeyboardMarkup(keyboard, resize_keyboard=True)
    await update.message.reply_text(welcome_text, reply_markup=reply_markup)

# Feedback from users
async def shikoyatlar(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text("""Taklif yoki mulohazalaringizni kiriting: \n
    📞 Murojat uchun: 
    Namanga shaxar: (+998)-99-936-22-11
    Chortoq tuman: (+998)-90-796-22-11\n
    Fikringizni bildirish uchun:
    @taklif_mulohaza
    """)
    return 1

async def receive_feedback(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    feedback = update.message.text
    await update.message.reply_text("Fikringiz uchun rahmat!")
    await context.bot.send_message(chat_id=ADMIN_CHAT_ID, text=f"Foydalanuvchi fikri:\n{feedback}")

# Tarmog'lar
async def tarmoglar(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    tarmog = """
Instagram: @it_world_markaz\n
Telegram: @IT_World_Centre
    """
    await update.message.reply_text(tarmog)

# To'lov qilish
async def tolov_qilish(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    tolov_text = """
    Hurmatli FOYDALANUVCHI to'lovni oyning 10-sanasigacha qilsangiz 5 % chegirma bilan to'lashingiz mumkin bo'ladi. To'lov qilgandan so'ng chekini @IT_World_Centre ga yuborishni unutmang.

💳 To'lov qilish uchun karta raqami:
    - 9860040114263664
    - Karimbekov Yusufbek
    """
    await update.message.reply_text(tolov_text)

# Kurslar bo'limi
async def kurslar(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    keyboard = [
        [KeyboardButton("IT"), KeyboardButton("DTM")],
        [KeyboardButton("Til kurslari"), KeyboardButton("Kids")],
        [KeyboardButton("♻️Ortga qaytish")],
    ]
    reply_markup = ReplyKeyboardMarkup(keyboard, resize_keyboard=True)
    await update.message.reply_text("📌 Kurslar bo'limini tanlang:", reply_markup=reply_markup)

# Kurs kategoriyalari
async def it_courses(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    keyboard = [
        [KeyboardButton("Full Stack"), KeyboardButton("Python")],
        [KeyboardButton("3Ds Max"), KeyboardButton("Web dasturlash")],
        [KeyboardButton("IT Kids (2-6-sinflar Robototexnika)"), KeyboardButton("♻️Ortga qaytish")],
    ]
    reply_markup = ReplyKeyboardMarkup(keyboard, resize_keyboard=True)
    await update.message.reply_text("📌 IT kurslari:", reply_markup=reply_markup)

async def dtm_courses(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    keyboard = [
        [KeyboardButton("Matematika"), KeyboardButton("Fizika")],
        [KeyboardButton("Kimyo"), KeyboardButton("Biologiya")],
        [KeyboardButton("Ona tili"), KeyboardButton("Adabiyot")],
        [KeyboardButton("Tarix"), KeyboardButton("♻️Ortga qaytish")],
    ]
    reply_markup = ReplyKeyboardMarkup(keyboard, resize_keyboard=True)
    await update.message.reply_text("📌 DTM kurslari:", reply_markup=reply_markup)

async def foreign_courses(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    keyboard = [
        [KeyboardButton("Ingliz tili"), KeyboardButton("Rus tili")],
        [KeyboardButton("Nemis tili"), KeyboardButton("Turk tili")],
        [KeyboardButton("Kores tili"), KeyboardButton("♻️Ortga qaytish")],
    ]
    reply_markup = ReplyKeyboardMarkup(keyboard, resize_keyboard=True)
    await update.message.reply_text("📌 Til kurslari:", reply_markup=reply_markup)

async def kids_courses(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    keyboard = [
        [KeyboardButton("Matematika"), KeyboardButton("Kimyo")],
        [KeyboardButton("♻️Ortga qaytish")],
    ]
    reply_markup = ReplyKeyboardMarkup(keyboard, resize_keyboard=True)
    await update.message.reply_text("📌 Kids kurslari:", reply_markup=reply_markup)

# Kurs haqida ma'lumot
async def kurs_malumoti(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    kurslar_info = {
        "Full Stack": """Full Stack dasturlash kursimiz 12 oyga moljallangan bolib bumda siz 6 oy dasturlashning Front-end qismini mukammal organib, kigingi 6 oyda esa Python dasturini organaib Full Stack dasturchi bolib chiqasz""",
        "Python": """Python, Django kursimiz 8 oyga moljallangan bolib 7 oy nazariy bilimlar beriladi va 8-oyda amaliy ishlar qilinadi.""",
        "3Ds Max": "3Ds Max kursi haqida ma'lumot.",
        "Web dasturlash": """Web dasturlash kursimiz 10 oyga moljallangan bolib 6 oy siz Front-end yonalishini mukammal organasiz va 4 oy Back-end "Node.js" yonalishini organasz.""",
        "IT Kids (2-6-sinflar robototexnika)": "IT Kids kursi haqida ma'lumot.",
        "Matematika": "Matematika kursi haqida ma'lumot.",
        "Fizika": "Fizika kursi haqida ma'lumot.",
        "Kimyo": "Kimyo kursi haqida ma'lumot.",
        "Biologiya": "Biologiya kursi haqida ma'lumot.",
        "Ona tili": "Ona tili kursi haqida ma'lumot.",
        "Adabiyot": "Adabiyot kursi haqida ma'lumot.",
        "Tarix": "Tarix kursi haqida ma'lumot.",
        "Ingliz tili": "Ingliz tili kursi haqida ma'lumot.",
        "Rus tili": "Rus tili kursi haqida ma'lumot.",
        "Nemis tili": "Nemis tili kursi haqida ma'lumot.",
        "Turk tili": "Turk tili kursi haqida ma'lumot.",
        "Kores tili": "Kores tili kursi haqida ma'lumot.",
    }

    course_name = update.message.text
    if course_name in kurslar_info:
        await update.message.reply_text(kurslar_info[course_name])
    elif course_name == "♻️Ortga qaytish":
        await kurslar(update, context)


# Manzil
async def manzil(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    location_text = (
        """📍 Manzil: [Namangan shaxar Zera buloq ko'chasi: 
Mo'njal: Chorsu Mehmonxona ro'parasi: IT World o'quv markazi]\n
(https://maps.google.com/maps?q=41.004969,71.679603&ll=41.004969,71.679603&z=16)\n
📍 Manzil: [Chortoq tumani Namangan MFY Namangan ko'chasi: 
Mo'njal: Sobiq Oxunbabayev Kinoteatr ro'parasi: IT World o'quv markazi]\n
(https://maps.google.com/maps?q=41.078162,71.810112&ll=41.078162,71.810112&z=16)"""
    )
    await update.message.reply_text(location_text, parse_mode="Markdown", reply_markup=ReplyKeyboardMarkup([
        [KeyboardButton("🌐Ishtimoiy sahifalar"), KeyboardButton("💳To'lov qilish")],
        [KeyboardButton("🔖Kurslar🔖"), KeyboardButton("📍Manzil📍")],
        [KeyboardButton("💻Bizning xizmatlar"), KeyboardButton("📞Bog'lanish")],
        [KeyboardButton("📝Taklif va Mulohazalar uchun")],
    ], resize_keyboard=True))


#Bizning xizmatlar
async def xizmatkorsatish(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    xizmatlar = """Biznesingizni biz bilan tizimlashtiring;
    💻Bizning xizmatlar: 
Web site 
Telegram bot 
📞Ma'lumot uchun:
    (+998)-90-757-71-16
    (+998)-97-776-60-05
    (+998)-93-214-70-48
"""
    keyboard = [
        [KeyboardButton("🌐Ishtimoiy sahifalar"), KeyboardButton("💳To'lov qilish")],
        [KeyboardButton("🔖Kurslar🔖"), KeyboardButton("📍Manzil📍")],
        [KeyboardButton("💻Bizning xizmatlar"), KeyboardButton("📞Bog'lanish")], 
        [KeyboardButton("📝Taklif va Mulohazalar uchun")],
    ]
    reply_markup = ReplyKeyboardMarkup(keyboard, resize_keyboard=True)
    await update.message.reply_text(xizmatlar, reply_markup=reply_markup)



# Bog'lanish
async def boglanish(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    contact_text = """📞 TELFON RAQAM: 
    Namanga shaxar: (+998)-99-936-22-11
    Chortoq tuman: (+998)-90-796-22-11"""
    keyboard = [
        [KeyboardButton("🌐Ishtimoiy sahifalar"), KeyboardButton("💳To'lov qilish")],
        [KeyboardButton("🔖Kurslar🔖"), KeyboardButton("📍Manzil📍")],
        [KeyboardButton("💻Bizning xizmatlar"), KeyboardButton("📞Bog'lanish")], 
        [KeyboardButton("📝Taklif va Mulohazalar uchun")],
    ]
    reply_markup = ReplyKeyboardMarkup(keyboard, resize_keyboard=True)
    await update.message.reply_text(contact_text, reply_markup=reply_markup)



# Boshqarish
def main() -> None:
    application = Application.builder().token(TOKEN).build()

    # Boshlanish
    application.add_handler(CommandHandler("start", start))

    # Asosiy menyu
    application.add_handler(MessageHandler(filters.TEXT & filters.Regex("🌐Ishtimoiy sahifalar"), tarmoglar))
    application.add_handler(MessageHandler(filters.TEXT & filters.Regex("💳To'lov qilish"), tolov_qilish))
    application.add_handler(MessageHandler(filters.TEXT & filters.Regex("🔖Kurslar🔖"), kurslar))
    application.add_handler(MessageHandler(filters.TEXT & filters.Regex("📍Manzil📍"), manzil))
    application.add_handler(MessageHandler(filters.TEXT & filters.Regex("💻Bizning xizmatlar"), xizmatkorsatish))
    application.add_handler(MessageHandler(filters.TEXT & filters.Regex("📞Bog'lanish"), boglanish))
    application.add_handler(MessageHandler(filters.TEXT & filters.Regex("📝Taklif va Mulohazalar uchun"), shikoyatlar))
    application.add_handler(MessageHandler(filters.TEXT & filters.Regex("♻️Ortga qaytish"), start))

    # Kurs kategoriyalari
    application.add_handler(MessageHandler(filters.TEXT & filters.Regex("IT"), it_courses))
    application.add_handler(MessageHandler(filters.TEXT & filters.Regex("DTM"), dtm_courses))
    application.add_handler(MessageHandler(filters.TEXT & filters.Regex("Til kurslari"), foreign_courses))
    application.add_handler(MessageHandler(filters.TEXT & filters.Regex("Kids"), kids_courses))

    # Kurslar haqida ma'lumot
    kurs_nomi_filter = filters.TEXT & (
        filters.Regex("Full Stack") | filters.Regex("Python") |
        filters.Regex("3Ds Max") | filters.Regex("Web dasturlash") |
        filters.Regex("IT Kids \\(2-6-sinflar\\)") |filters.Regex("Matematika") | 
        filters.Regex("Fizika") | filters.Regex("Kimyo") |
        filters.Regex("Biologiya") | filters.Regex("Ona tili") | 
        filters.Regex("Adabiyot") | filters.Regex("Tarix") | 
        filters.Regex("Ingliz tili") | filters.Regex("Rus tili") | 
        filters.Regex("Nemis tili") | filters.Regex("Turk tili") | 
        filters.Regex("Kores tili") 
    )
    application.add_handler(MessageHandler(kurs_nomi_filter, kurs_malumoti))

    # Mulohaza qabul qilish
    application.add_handler(MessageHandler(filters.TEXT & filters.Regex("Taklif va Mulohazalar uchun"), shikoyatlar))
    application.add_handler(MessageHandler(filters.TEXT, receive_feedback))

    application.run_polling()

if __name__ == "__main__":
    main()