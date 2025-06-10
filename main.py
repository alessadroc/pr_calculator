import os
from dotenv import load_dotenv
from pr_calculation_model import calculate_pr
from graph import Graph
import discord
from discord.ext import commands
from discord import app_commands

load_dotenv('.env')
Token = os.getenv("DISCORD_TOKEN")

class Client(commands.Bot):
    async def on_ready(self):
        print(f"Logged on as {self.user} successfully.")
        
        try:
            guild = discord.Object(id = 1371811106590425140)
            synced = await self.tree.sync(guild=guild)
            print(f"Synced {len(synced)} commands to {guild.id}")

        except Exception as e:
            print(f"Error syncing the commands: {e}")
        

    async def on_message(self, message):
        if message.author == self.user:
            return
        
        if message.content.startswith("hello"):
            await message.channel.send(f"Hi there {message.author}!")

    async def on_reaction_add(self, reaction, user):
        await reaction.message.channel.send(f"Hi {user}, you reacted using {reaction}!")

intents = discord.Intents.default()
intents.message_content = True
client = Client(command_prefix = "/", intents=intents) # command prefix is outdated, note this for changing later on

GUILD_ID = discord.Object(id = 1371811106590425140)

# main calculation command
@client.tree.command(name="calculatepr", description="Predicts PR gain by event name and placement", guild=GUILD_ID)
async def calculatepr(interaction: discord.Interaction, event: str, placement: int):
    
    await interaction.response.send_message(f"Calculating PR for event {event} and placement {placement}")

    print(f"Calculating PR for event {event}, and placement {placement} by requests of {interaction.user}")
    
    event = str(event)
    placement = int(placement)
    
    result = calculate_pr(event, placement)

    print(f"sending {result} to the server")

    msg = await interaction.original_response()
    await msg.edit(content=f"**{str(result)}** PR for placing #{placement} in {event}")

# list command
@client.tree.command(name="events", description="Lists all supported tournaments", guild=GUILD_ID)
async def events(interaction: discord.Interaction):
    tournaments = ["Solo Cash Cup Opens", 
                   "Solo Cash Cup Finals", 
                   "FNCS Division 1", 
                   "FNCS Division 2", 
                   "FNCS Division 3", 
                   "Performance Evaluation Opens", 
                   "Performance Evaluation Opens",
                   "FNCS Showdown"
                   ]
    
    await interaction.response.send_message(f"Supported Tournaments: {tournaments}")

client.run(token=Token)

# Server ID for dev server; 1380426485554216982