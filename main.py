import os
import sys
import discord
from discord.ext import commands
from discord import app_commands
from sources.strinova_steam_rss import *
from functions.config import *

# Please, edit if necessary
cfgFile = "config.json"

if os.path.exists(cfgFile):
    config = readConfig(cfgFile)
else:
    createConfig(cfgFile)
    sys.exit(f"Please edit {cfgFile}")

intents = discord.Intents.all()
bot = commands.Bot(command_prefix = config['prefix'], intents = intents)

class MyClient(discord.Client):
    def __init__(self):
        super().__init__(intents=intents)
        self.tree = app_commands.CommandTree(self)

    async def setup_hook(self):
        await self.tree.sync()

client = MyClient()

@client.tree.command(name="latestpost", description="Get the latest post from Strinova RSS newsfeed in Steam")
async def getbadge(interaction: discord.Interaction):
    post = LatestSteamPost()
    embedMsg = discord.Embed(title = post['title'], description = post['description'], color = 0x00ff00)
    await interaction.response.send_message(ephemeral = True, embed = embedMsg)

client.run(config['token'])
