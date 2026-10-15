import discord
from discord import app_commands
from discord.ext import commands

class StatsCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="server")
    async def server(self, ctx):
        g = ctx.guild
        online = sum(1 for m in g.members if m.status != discord.Status.offline)
        embed = discord.Embed(title=g.name, color=0x2b2d31)
        if g.icon: embed.set_thumbnail(url=g.icon.url)
        embed.add_field(name="🆔 ID", value=f"`{g.id}`", inline=False)
        embed.add_field(name="👥 Members", value=f"Total: {g.member_count} | Online: {online}", inline=False)
        await ctx.send(embed=embed)

    @commands.command(name="user", aliases=["id"])
    async def user_info(self, ctx, member: discord.Member = None):
        m = member or ctx.author
        embed = discord.Embed(title=f"User: {m.name}", color=0x2b2d31)
        embed.set_thumbnail(url=m.display_avatar.url)
        embed.add_field(name="🆔 ID", value=f"`{m.id}`", inline=False)
        await ctx.send(embed=embed)

    @commands.command(name="avatar")
    async def avatar(self, ctx, member: discord.Member = None):
        m = member or ctx.author
        await ctx.send(embed=discord.Embed(title=f"Avatar: {m.name}", color=0x2b2d31).set_image(url=m.display_avatar.url))

    @commands.command(name="ping")
    async def ping(self, ctx):
        await ctx.send(f"🏓 Pong! `{round(self.bot.latency * 1000)}ms`")

async def setup(bot):
    await bot.add_cog(StatsCog(bot))
