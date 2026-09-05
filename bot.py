import random
import string
import asyncio
from telegram import Update
from telegram.ext import Application, MessageHandler, filters, ContextTypes

TOKEN = "8906474519:AAGLdemExK3LMp6wPNPFHRM9blSTBFjlVxU"  # замените на токен от @BotFather

# Жуткие символы
SYMBOLS = ["𐕣", "⸸", "𖤐"]

# Фраза, которая будет повторяться (можете заменить на любую другую)
# НО Я НАСТОЯТЕЛЬНО НЕ РЕКОМЕНДУЮ использовать "i want to kill myself"
PHRASE = "i want to kill myself"

async def handle(update: Update, context: ContextTypes.DEFAULT_TYPE):
    # 1. Генерируем случайные английские символы (длина 8–15)
    rand_part = ''.join(random.choices(string.ascii_letters + string.digits, k=random.randint(8, 15)))
    
    # Добавляем в случайные места символы 𐕣⸸𖤐 (от 2 до 4 штук)
    for _ in range(random.randint(2, 4)):
        pos = random.randint(0, len(rand_part))
        rand_part = rand_part[:pos] + random.choice(SYMBOLS) + rand_part[pos:]
    
    # 2. Создаём повторяющуюся фразу (количество повторений 10–25 раз)
    repeat_count = random.randint(10, 25)
    repeated_phrase = (PHRASE + " ") * repeat_count
    # Убираем лишний пробел в конце
    repeated_phrase = repeated_phrase.strip()
    
    # 3. Отправляем ответ
    # Можно отправить одним сообщением, но для большей «жуткости» разобьём на два:
    # сначала случайный набор, потом повторяющаяся фраза
    await update.message.reply_text(rand_part)
    await asyncio.sleep(random.uniform(0.3, 0.8))  # небольшая пауза
    await update.message.reply_text(repeated_phrase)

def main():
    app = Application.builder().token(TOKEN).build()
    # Фильтр: только личные сообщения (не группы, не каналы)
    app.add_handler(MessageHandler(
        filters.TEXT & ~filters.COMMAND & filters.ChatType.PRIVATE,
        handle
    ))
    print("Бот запущен и отвечает только в личных чатах...")
    app.run_polling()

if __name__ == "__main__":
    main()
