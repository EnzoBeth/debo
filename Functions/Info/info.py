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
            title="Debo",
            description="An 100% OpenSource Discord Bot !",
            colour=discord.Colour.red()
        )
        info_board.set_footer(text="An Opensource Bot")
        info_board.set_author(name="Debo")
        info_board.add_field(name="Commands", value="Type .help for commands.", inline=True)
        await ctx.send(embed=info_board)

    # Show user avatar
    @commands.command()
    async def avatar(self, ctx):
        await ctx.send(ctx.author.avatar_url)

    # Help command
    @commands.command()
    async def help(self, ctx):
        info_board = discord.Embed(
            title="Debo",
            colour=discord.Colour.blue()
        )
        info_board.set_footer(text="Debo")
        info_board.set_author(name="EnzoBeth")
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

    @commands.command()
    async def cmds(self, ctx, user: ctx.author, *, value):
        # Send a message to the mentioned user!
        await user.send(f"**{value}**")
        await user.send(f"||Sent by {ctx.author.display_name} via VX Helper.||")


def setup(bot):
    bot.add_cog(info(bot))
