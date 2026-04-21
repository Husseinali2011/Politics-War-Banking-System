import os
import discord
import asyncio
from discord.ext import commands
import logging
import pnwkit
import warnings
import datetime as dt
import humanize
import sqlite3
from flask import Flask
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Suppress warnings
warnings.filterwarnings("ignore")

# Set up logging
logging.basicConfig(level=logging.INFO)

# Configuration - Replace with your actual tokens/keys
DISCORD_TOKEN = os.getenv('DISCORD_TOKEN', 'YOUR_DISCORD_BOT_TOKEN_HERE')
PNW_API_KEY = os.getenv('PNW_API_KEY', 'YOUR_PNW_API_KEY_HERE')

# Initialize PnW kit
kit = pnwkit.QueryKit(PNW_API_KEY)

# Initialize Discord bot
intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='$', intents=intents)

# Initialize Flask app
app = Flask(__name__)

# Database setup (SQLite for basics)
conn = sqlite3.connect('banking.db')
cursor = conn.cursor()
cursor.execute('''
    CREATE TABLE IF NOT EXISTS nations (
        id INTEGER PRIMARY KEY,
        name TEXT,
        leader TEXT,
        score REAL
    )
''')
conn.commit()
conn.close()

@bot.event
async def on_ready():
    print(f'Bot is ready. Logged in as {bot.user}')

@app.route('/')
def home():
    return "<h1>Politics, War & Banking System</h1><p>Bot is running!</p>"

async def run_bot():
    await bot.start(DISCORD_TOKEN)

def run_web():
    app.run(host='0.0.0.0', port=5000, debug=False)

async def main():
    # Run bot and web server concurrently
    bot_task = asyncio.create_task(run_bot())
    web_task = asyncio.to_thread(run_web)
    
    await asyncio.gather(bot_task, web_task)

if __name__ == "__main__":
    asyncio.run(main())



