import discord
from discord.ext import commands

# Replace with your bot token
TOKEN = "YOUR_BOT_TOKEN"

# Set command prefix
intents = discord.Intents.default()
intents.messages = True
bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user}')

@bot.command()
async def hello(ctx):
    await ctx.send("Hello! I'm a bot.")

@bot.command()
async def ping(ctx):
    await ctx.send(f'Pong! {round(bot.latency * 1000)}ms')

bot.run(TOKEN)
