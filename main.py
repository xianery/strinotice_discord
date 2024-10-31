import os
import sys
import discord
from discord.ext import commands
from discord import app_commands
from functions.strinova_steam_rss import *
from functions.config import *
from functions.server_info import *

# Please, edit if necessary
cfgFile = "config.json"
serversFile = "servers.json"

if os.path.exists(cfgFile):
        config = readConfig(cfgFile)
else:
        createConfig(cfgFile)
        sys.exit(f"Please edit {cfgFile}")

if not(os.path.exists(serversFile)):
        createServerFile(serversFile)

class CoreSetup(commands.Bot):
        def __init__(self):
                super().__init__(command_prefix = config['prefix'], intents = discord.Intents.all())

        async def setup_hook(self):
                # Registering commands
                self.tree.add_command(sendLatestPost)
                self.tree.add_command(selectFeedChannel)
                await self.tree.sync() 

core = CoreSetup()

@app_commands.command(name = "latestpost", description = "Get the latest post from Strinova RSS newsfeed in Steam")
async def sendLatestPost(interaction: discord.Interaction):
        post = LatestSteamPost()
        embedMsg = discord.Embed(title = post['title'], description = post['description'], color = 0x00ff00)
        await interaction.response.send_message(ephemeral = True, embed = embedMsg)

@app_commands.command(name = "feedchannel", description = "Select channel where will sends news")
async def selectFeedChannel(interaction: discord.Integration, channel: discord.TextChannel):
        embedMsg = discord.Embed(title = f"Done!", description = f"<#{channel.id}> selected as newsfeed channel for bot", color = 0x00ff00)

        serversData = loadServersInfo(serversFile)

        if interaction.guild.id in serversData:
                changeChannel(serversFile, interaction.guild.id, channel.id)
        else:
                addServer(serversFile, interaction.guild.id, channel.id)

        await interaction.response.send_message(ephemeral = True, embed = embedMsg)

core.run(config['token'])
