import random

import discord
from discord import member
from discord.ext import commands


class admin(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    # pick an random user to giveaway
    @commands.command()
    @commands.has_permissions(administrator=True)
    @commands.guild_only()
    async def giveaway(self, ctx):
        await ctx.send(f"Winner: {random.choice(ctx.guild.members).mention}")

    # ban mentioned user
    @commands.command()
    @commands.has_permissions(administrator=True)
    async def ban(self, ctx, user: discord.User = None, reason=None):
        if user is None or user == self.message.author:
            await self.channel.send("You cannot ban yourself")
            return
        if reason is None:
            reason = "For being a jerk!"
        message = f"You have been banned from {self.guild.name} for {reason}"
        await member.send(message)
        await ctx.guild.ban(user)
        await self.channel.send(f"{user} is banned!")

    # Kick mentioned user
    @commands.command()
    @commands.has_permissions(administrator=True)
    async def kick(self, ctx, user: discord.user = None, reason=None):
        if user == None or user == self.message.author:
            await ctx.send("You cannot kick yourself")
            return
        messagekick = f"You have been kicked form {self.guild.name}"
        await member.send(messagekick)
        await ctx.guild.kick(user)
        await ctx.send(f"{user} have been kicked !")

    # User Admin perm check command
    @commands.command()
    @commands.has_permissions(administrator=True)
    async def root(self, ctx):
        await ctx.send("You are administrator")

    # DM The mentioned used
    @commands.command()
    async def dm(self, ctx, user: discord.User, *, value):
        await user.send(f"**{value}**")


def setup(bot):
    bot.add_cog(admin(bot))
