# WARNING : I Don't recommend you to touch that part of the code, only edit if you know what you are doing
#           You can easily break the bot by touching an setting

import discord
from discord.ext import commands

import settings

intents = discord.Intents.default()

# Cogs list
cogs: list = ["Functions.Fun.games", "Functions.Fun.gameinfos", "Functions.Fun.otherfuncommands", "Functions.Info.info",
        "Functions.Misc.misc", "Functions.Admin.admin"]

# Load the bot prefix form settings.py
client = commands.Bot(command_prefix=settings.Prefix, help_command=None, intents=intents)

# Cogs loading part
@client.event
async def on_ready():
    print("Debo est Prêt !")
    await client.change_presence(status=discord.Status(settings.Statut), activity=discord.Game(settings.BotStatus))
    for cog in cogs:
        try:
            print(f"Changement du cog : {cog}")
            client.load_extension(cog)
            print(f"Le cog {cog} est chargé")
        except Exception as e:
            exc = "{}: {}".format(type(e).__name__, e)
            print("Impossble de charger le cog : {}\n{}".format(cog, exc))

# Run the bot with the selected token in settings.py
client.run(settings.TOKEN)
