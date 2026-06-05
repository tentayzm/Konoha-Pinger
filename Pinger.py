import asyncio
import os
from aiogram import Bot

PINGER_TOKEN = os.getenv("PINGER_TOKEN")
AI_BOT = "@OrgKonohaBot"

bot = Bot(token=PINGER_TOKEN)

async def send_ping():
    while True:
        await asyncio.sleep(300)
        try:
            await bot.send_message(chat_id=AI_BOT, text="⏱️")
            print("✅ Ping sent")
        except Exception as e:
            print(f"❌ Error: {e}")

async def main():
    print("🚀 Pinger started...")
    await send_ping()

if __name__ == "__main__":
    asyncio.run(main())
