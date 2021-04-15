import discord
from discord.ext import commands

import settings

intents = discord.Intents.default()

cogs: list = ["Functions.Fun.games", "Functions.Fun.gameinfos", "Functions.Fun.otherfuncommands", "Functions.Info.info",
        "Functions.Misc.misc", "Functions.NewMember.newmember", "Functions.Admin.admin"]

client = commands.Bot(command_prefix=settings.Prefix, help_command=None, intents=intents)


@client.event
async def on_ready():
    print("Debo est Prêt !")
    await client.change_presence(status=discord.Status.dnd, activity=discord.Game(settings.BotStatus))
    for cog in cogs:
        try:
            print(f"Changement du cog : {cog}")
            client.load_extension(cog)
            print(f"Le cog {cog} est chargé")
        except Exception as e:
            exc = "{}: {}".format(type(e).__name__, e)
            print("Impossble de charger le cog : {}\n{}".format(cog, exc))


client.run(settings.TOKEN)
