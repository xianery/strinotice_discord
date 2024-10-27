import os
import sys
import discord
from discord.ext import commands
from sources.strinova_steam_rss import *
from functions.config import *

# Please, edit if necessary
cfgFile = "config.json"

if os.path.exists(cfgFile):
    config = readConfig(cfgFile)
else:
    createConfig(cfgFile)
    sys.exit(f"Please edit {cfgFile}")

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix=config['prefix'], intents=intents)

@bot.command(name="latest")
async def latest(ctx):
        post = LatestSteamPost()
        await ctx.send("# " + post['title'] + "\n" + post['description'])

bot.run(config['token'])