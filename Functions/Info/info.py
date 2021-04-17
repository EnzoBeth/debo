import discord
from discord.ext import commands


class info(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self._last_member = None

    # Show bot infos
    @commands.command()
    async def info(self, ctx):
        info_board = discord.Embed(
            title="Debo's Info",
            description="An 100% OpenSource Discord Bot !",
            colour=discord.Colour.purple()
        )
        info_board.set_footer(text="Debo Global Instance, Hosted in France")

        info_board.add_field(name="Commands", value="Type debo!help for commands.", inline=True)
        info_board.add_field(name="Version", value="2021.416")
        info_board.add_field(name="Developer", value="EnzoBeth#5673", inline=True)
        await ctx.send(embed=info_board)

    # Show user avatar
    @commands.command()
    async def avatar(self, ctx):
        await ctx.send(ctx.author.avatar_url)

    # Help command
    @commands.command()
    async def help(self, ctx):
        info_board = discord.Embed(
            title="Debo's Commands Help",
            colour=discord.Colour.blue()
        )
        info_board.set_footer(text="Debo Global Instance, Hosted In France")

        info_board.add_field(name="debo!avatar", value="Shows your avatar.", inline=False)
        info_board.add_field(name="debo!info", value="Info about bot.", inline=False)
        info_board.add_field(name="debo!coinflip", value="CoinFlip game.", inline=False)
        info_board.add_field(name="debo!joke", value="Makes a joke.", inline=False)
        info_board.add_field(name="debo!mirror", value="Bot mirrors your sentence.", inline=False)
        info_board.add_field(name="debo!giveaway", value='Only who has "Admin" role can use this command.',
                             inline=False)
        info_board.add_field(name="debo!brokethesentence", value='Brokes the sentence.', inline=False)
        info_board.add_field(name="debo!lenght", value='Give you info about the sentence.', inline=False)
        info_board.add_field(name="debo!minecraft", value='Shows your minecraft profile.', inline=False)
        info_board.add_field(name="debo!writinggame", value='Game for fast writing.', inline=False)
        info_board.add_field(name="debo!wiki", value='Send you the wiki link of requested thing.', inline=False)
        await ctx.send(embed=info_board)




def setup(bot):
    bot.add_cog(info(bot))
