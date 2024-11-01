import os
import sys
import discord
import asyncio
from discord.ext import tasks, commands
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

@core.event
async def on_ready():
        publishNewsPost.start()

@tasks.loop(seconds = 10)
async def publishNewsPost():
        serversData = loadServersInfo(serversFile)
        post = latestSteamPost()
        embedMsg = discord.Embed(title = post['title'], description = post['description'], color = 0x00ff00)
        print(readConfig(cfgFile)["latest_post_date"] + " | " + post["date"])
        
        if readConfig(cfgFile)["latest_post_date"] != post["date"]:
                updatePostDate(cfgFile, post["date"])

                for server in serversData:
                        guild = core.get_guild(int(server))

                        if guild:
                                channel = guild.get_channel(serversData[server]["selected_channel"])

                                if channel:
                                        await channel.send(embed = embedMsg)

@app_commands.command(name = "latestpost", description = "Get the latest post from Strinova RSS newsfeed in Steam")
async def sendLatestPost(interaction: discord.Interaction):
        post = latestSteamPost()
        embedMsg = discord.Embed(title = post['title'], description = post['description'], color = 0x00ff00)

        updatePostDate(cfgFile, post["date"])

        await interaction.response.send_message(ephemeral = True, embed = embedMsg)

@app_commands.command(name = "feedchannel", description = "Select channel where will sends news")
async def selectFeedChannel(interaction: discord.Integration, channel: discord.TextChannel):
        embedMsg = discord.Embed(title = f"Done!", description = f"<#{channel.id}> selected as newsfeed channel for bot", color = 0x00ff00)

        serversData = loadServersInfo(serversFile)

        if interaction.guild_id  in serversData:
                changeChannel(serversFile, interaction.guild_id, int(channel.id))
        else:
                addServer(serversFile, interaction.guild_id, int(channel.id))

        await interaction.response.send_message(ephemeral = True, embed = embedMsg)

core.run(config['token'])
