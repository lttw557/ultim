import random
import string
import asyncio
from telegram import Update
from telegram.ext import Application, MessageHandler, filters, ContextTypes

# ===== НАСТРОЙКИ =====
TOKEN = "8906474519:AAGLdemExK3LMp6wPNPFHRM9blSTBFjlVxU"                 # токен от @BotFather
MY_USER_ID = 8585176339              # ваш ID (число)
# =====================

# Жуткие символы
SYMBOLS = ["𐕣", "⸸", "𖤐"]

# Фраза, которую будет повторять (можете заменить на свою, но я не рекомендую "kill myself")
PHRASE = "i want to end it all"

# Генератор случайного набора букв/цифр
def gibberish(length):
    return ''.join(random.choices(string.ascii_letters + string.digits, k=length))

# Асинхронная функция, отправляющая серию сообщений
async def send_series(update: Update):
    # Количество сообщений в серии (от 3 до 6)
    count = random.randint(3, 6)
    for _ in range(count):
        # Случайно выбираем, что отправить
        choice = random.choice(["gibberish", "phrase", "symbols", "mixed"])
        if choice == "gibberish":
            text = gibberish(random.randint(8, 15))
            # добавляем пару символов
            for _ in range(random.randint(1, 3)):
                text += random.choice(SYMBOLS)
        elif choice == "phrase":
            repeat = random.randint(3, 10)
            text = (PHRASE + " ") * repeat
            text = text.strip()
            # иногда добавляем символы между словами
            if random.random() > 0.5:
                words = text.split()
                for i in range(1, len(words), 2):
                    words[i] = words[i] + random.choice(SYMBOLS)
                text = ' '.join(words)
        elif choice == "symbols":
            text = ''.join(random.choices(SYMBOLS, k=random.randint(5, 15)))
        else:  # mixed
            parts = []
            for _ in range(random.randint(2, 5)):
                if random.random() > 0.5:
                    parts.append(gibberish(random.randint(3, 6)))
                else:
                    parts.append(random.choice(SYMBOLS))
            text = ' '.join(parts)
        # Отправляем сообщение
        await update.message.reply_text(text)
        # Пауза от 0,5 до 1,5 секунды
        await asyncio.sleep(random.uniform(0.5, 1.5))

# Обработчик входящих сообщений
async def handle(update: Update, context: ContextTypes.DEFAULT_TYPE):
    # Запускаем серию (игнорируем context, он не нужен)
    await send_series(update)

# Главная функция
def main():
    app = Application.builder().token(TOKEN).build()
    # Фильтр: только текстовые сообщения (не команды) и только от вашего ID
    app.add_handler(MessageHandler(
        filters.TEXT & ~filters.COMMAND & filters.User(user_id=MY_USER_ID),
        handle
    ))
    print("Бот запущен и будет отвечать только вам (по ID).")
    app.run_polling()

if __name__ == "__main__":
    main()
