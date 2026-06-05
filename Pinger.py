import asyncio
from aiogram import Bot

PINGER_TOKEN = "8653351122:AAFsbxjt3PKYc8DczZyaNwg1PzUAZFyp8gk"
AI_BOT = "@OrgKonohaBot"

bot = Bot(token=PINGER_TOKEN)

async def send_ping():
    while True:
        await asyncio.sleep(300)  # 5 دقیقه
        try:
            await bot.send_message(chat_id=AI_BOT, text="⏱️")
            print("✅ Ping sent to AI bot")
        except Exception as e:
            print(f"❌ Error: {e}")

async def main():
    print("🚀 Pinger started. Keeping AI bot awake.")
    await send_ping()

if __name__ == "__main__":
    asyncio.run(main())
