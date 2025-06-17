import os
from dotenv import load_dotenv
from pr_calculation_model import calculate_pr
from graph import Graph
import discord
from discord.ext import commands
from discord import app_commands
from io import BytesIO

load_dotenv('.env')
Token = os.getenv("DISCORD_TOKEN")

class Client(commands.Bot):
    async def on_ready(self):
        print(f"Logged on as {self.user} successfully.")
        
        try:
            guild = discord.Object(id=1371811106590425140)
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

class View(discord.ui.View):
    def __init__(self, event: str, placement: int):
        super().__init__()
        self.event = event
        self.placement = placement

    @discord.ui.button(label="Show Graph", style=discord.ButtonStyle.blurple, emoji="📈")
    async def button_callback(self, interaction: discord.Interaction, button: discord.ui.Button):
        print(f"Generating graph by request of {interaction.user}")

        # graph calling and sending to message
        graph = Graph(event=self.event, placement=self.placement, user=interaction.user)
        fig = graph.plot_graph()
        buf = BytesIO()
        fig.savefig(buf, format='png', dpi=300, bbox_inches='tight')
        buf.seek(0)
        file = discord.File(fp=buf, filename="graph.png")

        print(f"Sending Graph to Server by request of {interaction.user}")

        await interaction.response.send_message(file=file)

intents = discord.Intents.default()
intents.message_content = True
client = Client(command_prefix="/", intents=intents)
GUILD_ID = discord.Object(id=1371811106590425140)

# Available tournaments
tournaments = [
        "Solo Cash Cup Opens", 
        "Solo Cash Cup Finals", 
        "FNCS Division 1",
        "FNCS Division 2", 
        "FNCS Division 3", 
        "Performance Evaluation Opens",
        "Performance Evaluation Finals", 
        "FNCS Showdown"
    ]

async def event_autocomplete(interaction: discord.Interaction, current: str):
    return [
        app_commands.Choice(name=event, value=event)
        for event in tournaments if current.lower() in event.lower()
    ][:25] 

# Main Calculation command and also the autocomplete options
@client.tree.command(name="calculatepr", description="Predicts PR gain by event name and placement", guild=GUILD_ID)
@app_commands.describe(event="Select the event", placement="Your placement")
@app_commands.autocomplete(event=event_autocomplete)
async def calculatepr(interaction: discord.Interaction, event: str, placement: int):
    await interaction.response.send_message(f"Calculating PR for event {event} and placement {placement}")
    print(f"Calculating PR for event {event}, and placement {placement} by request of {interaction.user}")

    event = event.lower()

    result = calculate_pr(event, placement)

    print(f"Sending {result} to the server")
    msg = await interaction.original_response()

    view = View(event=event, placement=placement)
    await msg.edit(content=f"**{result}** PR for placing #{placement} in {event}", view=view)


@client.tree.command(name="events", description="Lists all supported tournaments", guild=GUILD_ID)
async def events(interaction: discord.Interaction):
    tournaments = [
        "Solo Cash Cup Opens", "Solo Cash Cup Finals", "FNCS Division 1",
        "FNCS Division 2", "FNCS Division 3", "Performance Evaluation Opens",
        "Performance Evaluation Opens", "FNCS Showdown"
    ]
    await interaction.response.send_message(f"Supported Tournaments: {tournaments}")

client.run(token=Token)