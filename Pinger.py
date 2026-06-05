Enterimport asyncio
from aiogram import Bot

# ========== توکن ربات نگهبان ==========
PINGER_TOKEN = "8653351122:AAFsbxjt3PKYc8DczZyaNwg1PzUAZFyp8gk"
# ====================================

MAIN_BOT_USERNAME = "@OrgKonohaBot"

bot = Bot(token=PINGER_TOKEN)

async def send_ping():
    while True:
        await asyncio.sleep(300)
        try:
            await bot.send_message(chat_id=MAIN_BOT_USERNAME, text="⏱️ Ping")
            print("✅ Ping sent")
        except Exception as e:
            print(f"❌ Error: {e}")

async def main():
    print("🚀 Pinger started...")
    await send_ping()

if __name__ == "__main__":
    asyncio.run(main())
