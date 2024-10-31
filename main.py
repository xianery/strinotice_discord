import os
import sys
import discord
from discord.ext import commands
from discord import app_commands
from functions.strinova_steam_rss import *
from functions.config import *

# Please, edit if necessary
cfgFile = "config.json"

if os.path.exists(cfgFile):
    config = readConfig(cfgFile)
else:
    createConfig(cfgFile)
    sys.exit(f"Please edit {cfgFile}")

class CoreSetup(commands.Bot):
    def __init__(self):
        super().__init__(command_prefix = config['prefix'], intents = discord.Intents.all())

    async def setup_hook(self):
        # Registering commands
        self.tree.add_command(latestpost)
        await self.tree.sync() 

core = CoreSetup()

@app_commands.command(name = "latestpost", description = "Get the latest post from Strinova RSS newsfeed in Steam")
async def latestpost(interaction: discord.Interaction):
    post = LatestSteamPost()
    embedMsg = discord.Embed(title = post['title'], description = post['description'], color = 0x00ff00)
    await interaction.response.send_message(ephemeral = True, embed = embedMsg)

# @app_commands.command(name = "feedchannel", description = "")
# async def selectFeedChannel():
#     pass

core.run(config['token'])
