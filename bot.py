import os
import random
import webbrowser

from discord.ext import commands
from dotenv import load_dotenv

load_dotenv()
token = os.getenv('DISCORD_TOKEN')

bot = commands.Bot(command_prefix='!')

@bot.event
async def on_ready():
    print(f'{bot.user.name} has connect to discord')

@bot.command(name="99")
async def nine_nine(ctx):
    await ctx.send("Hello bot")

@bot.command(name="play")
async def play_browser(ctx, arg):
    webbrowser.open(arg)

@bot.command(name="join")
async def join(ctx):
    print(f'{ctx.author.voice}')
    await bot.join_voice_chanel()

bot.run(token)
