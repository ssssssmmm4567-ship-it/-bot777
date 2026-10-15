import discord
from discord import app_commands
from discord.ext import commands

class RolesCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="roles", aliases=["serverroles"])
    async def server_roles(self, ctx):
        guild_roles = sorted([r for r in ctx.guild.roles if r.name != "@everyone"], key=lambda r: r.position, reverse=True)
        if not guild_roles:
            await ctx.send("❌ لا توجد رولات مخصصة.")
            return
        roles_list = [f"{r.mention} — (`{len(r.members)}` عضو)" for r in guild_roles]
        embed = discord.Embed(title=f"🎭 رولات سيرفر {ctx.guild.name} (من الأعلى للأقل)", description="\n".join(roles_list[:25]), color=0x2b2d31)
        await ctx.send(embed=embed)

    @commands.command(name="role", aliases=["addrole"])
    @commands.has_permissions(manage_roles=True)
    async def role(self, ctx, member: discord.Member, role: discord.Role):
        await member.add_roles(role)
        await ctx.send(f"✨ تم إعطاء رتبة `{role.name}` لـ `{member.name}`.")

    @commands.command(name="removerole")
    @commands.has_permissions(manage_roles=True)
    async def removerole(self, ctx, member: discord.Member, role: discord.Role):
        await member.remove_roles(role)
        await ctx.send(f"🗑️ تم إزالة رتبة `{role.name}` من `{member.name}`.")

    @commands.command(name="allrole")
    @commands.has_permissions(manage_roles=True)
    async def allrole(self, ctx, role: discord.Role):
        msg = await ctx.send("⏳ جاري منح الرتبة للجميع...")
        c = 0
        for m in ctx.guild.members:
            if role not in m.roles:
                try: await m.add_roles(role); c += 1
                except: pass
        await msg.edit(content=f"✅ تم إعطاء الرتبة لـ `{c}` عضو.")

    @commands.command(name="check")
    @commands.has_permissions(manage_roles=True)
    async def check(self, ctx, role: discord.Role):
        c = len([m for m in ctx.guild.members if role in m.roles])
        await ctx.send(f"🔍 حاملو رتبة **{role.name}**: `{c}` عضو.")

async def setup(bot):
    await bot.add_cog(RolesCog(bot))
