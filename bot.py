import os
import discord
from discord.ext import commands
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('MTU2Mzg5NzQ5NzgwODY2NjcwNg.G-8ZRC.VYKpEaxk_vYc4_YC9-tBp3Wu27hTUrGf6h5l5Y')

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print(f'Bot online como {bot.user}!')

@bot.command(name='oi')
async def ola(ctx):
    await ctx.send(f'Olá {ctx.author.name}!')

bot.run(TOKEN)
