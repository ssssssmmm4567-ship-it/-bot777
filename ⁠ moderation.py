import discord
from discord import app_commands
from discord.ext import commands

class ModerationCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="kick")
    @commands.has_permissions(kick_members=True)
    async def kick(self, ctx, member: discord.Member, *, reason="لم يحدد سبب"):
        await member.kick(reason=reason)
        await ctx.send(f"👢 تم طرد العضو {member.mention} | السبب: {reason}")

    @commands.command(name="ban")
    @commands.has_permissions(ban_members=True)
    async def ban(self, ctx, member: discord.Member, *, reason="لم يحدد سبب"):
        await member.ban(reason=reason)
        await ctx.send(f"🔨 تم حظر العضو {member.mention} | السبب: {reason}")

    @commands.command(name="unban")
    @commands.has_permissions(ban_members=True)
    async def unban(self, ctx, user_id: int):
        user = await self.bot.fetch_user(user_id)
        await ctx.guild.unban(user)
        await ctx.send(f"🔓 تم فك حظر المستخدم {user.name}")

    @commands.command(name="clear")
    @commands.has_permissions(manage_messages=True)
    async def clear(self, ctx, amount: int):
        await ctx.channel.purge(limit=amount + 1)
        msg = await ctx.send(f"🧹 تم مسح `{amount}` رسالة بنجاح.")
        await msg.delete(delay=3)

    @commands.command(name="mute")
    @commands.has_permissions(moderate_members=True)
    async def mute(self, ctx, member: discord.Member, minutes: int, *, reason="لم يحدد سبب"):
        duration = discord.utils.utcnow() + discord.timedelta(minutes=minutes)
        await member.timeout(duration, reason=reason)
        await ctx.send(f"🔇 تم تسكيت {member.mention} لمدة {minutes} دقيقة.")

    @commands.command(name="unmute")
    @commands.has_permissions(moderate_permissions=True)
    async def unmute(self, ctx, member: discord.Member):
        await member.timeout(None)
        await ctx.send(f"🔊 تم فك التسكيت عن {member.mention}")

    @commands.command(name="lock")
    @commands.has_permissions(manage_channels=True)
    async def lock(self, ctx):
        await ctx.channel.set_permissions(ctx.guild.default_role, send_messages=False)
        await ctx.send("🔒 تم قفل الروم الحالية.")

    @commands.command(name="unlock")
    @commands.has_permissions(manage_channels=True)
    async def unlock(self, ctx):
        await ctx.channel.set_permissions(ctx.guild.default_role, send_messages=True)
        await ctx.send("🔓 تم فتح الروم الحالية.")

    @commands.command(name="slowmode")
    @commands.has_permissions(manage_channels=True)
    async def slowmode(self, ctx, seconds: int):
        await ctx.channel.edit(slowmode_delay=seconds)
        await ctx.send(f"⏳ تم ضبط سرعة الشات (Slowmode) إلى `{seconds}` ثانية.")

    @commands.command(name="nuke")
    @commands.has_permissions(administrator=True)
    async def nuke(self, ctx):
        pos = ctx.channel.position
        new_ch = await ctx.channel.clone(reason="Nuke command executed")
        await ctx.channel.delete()
        await new_ch.edit(position=pos)
        await new_ch.send("💥 **تم تطهير وإعادة تدوير الروم بنجاح!**")

async def setup(bot):
    await bot.add_cog(ModerationCog(bot))
