import discord
from discord.ext import commands
import random
import time

class StatsCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.start_time = time.time()

    # --- مجموعة 1 إلى 25: إحصائيات السيرفر ومعلوماته الأساسية (بالشكل الفخم المطلوب) ---
    @commands.command(name="server", aliases=["serverinfo"])
    async def server_info(self, ctx):
        guild = ctx.guild
        online_count = sum(1 for m in guild.members if m.status != discord.Status.offline)
        
        embed = discord.Embed(
            title=f"🌸 سيرفر {guild.name}",
            color=0xffc0cb  # اللون الوردي الخاص بسيرفر 777
        )
        
        if guild.icon: 
            embed.set_thumbnail(url=guild.icon.url)
            
        embed.add_field(name="🆔 آيدي السيرفر", value=f"`{guild.id}`", inline=False)
        
        if guild.owner: 
            embed.add_field(name="👑 مالك السيرفر", value=f"{guild.owner.mention}", inline=False)
            
        members_text = f"العدد الكلي: **{guild.member_count}** | الأونلاين: **{online_count}**"
        embed.add_field(name="👥 الأعضاء", value=members_text, inline=False)
        
        roles_count = len(guild.roles) - 1  # خصم رتبة @everyone لتظهر بدقة
        embed.add_field(name="🎭 الرولات", value=f"`{roles_count}` رتبة", inline=False)
        
        embed.set_footer(text=f"Requested by {ctx.author.name} | 777 System", icon_url=ctx.author.display_avatar.url)
        await ctx.send(embed=embed)

    @commands.command(name="stats")
    async def stats_cmd(self, ctx): await ctx.invoke(self.bot.get_command('server'))
    
    @commands.command(name="serverstats")
    async def server_stats_cmd(self, ctx): await ctx.invoke(self.bot.get_command('server'))

    @commands.command(name="servericon")
    async def server_icon(self, ctx):
        if ctx.guild.icon: await ctx.send(embed=discord.Embed(title=f"Icon: {ctx.guild.name}", color=0xffc0cb).set_image(url=ctx.guild.icon.url))
        else: await ctx.send("❌ السيرفر لا يملك أيكونة.")

    @commands.command(name="serverbanner")
    async def server_banner(self, ctx):
        if ctx.guild.banner: await ctx.send(embed=discord.Embed(title=f"Banner: {ctx.guild.name}", color=0xffc0cb).set_image(url=ctx.guild.banner.url))
        else: await ctx.send("❌ السيرفر لا يملك بنر.")

    @commands.command(name="servercreated")
    async def server_created(self, ctx): await ctx.send(f"📅 تم إنشاء سيرفر **{ctx.guild.name}** في تاريخ: `{ctx.guild.created_at.strftime('%Y/%m/%d - %H:%M')}`")

    @commands.command(name="owner", aliases=["serverowner"])
    async def owner_cmd(self, ctx): await ctx.send(f"👑 مالك السيرفر هو: {ctx.guild.owner.mention} (`{ctx.guild.owner.id}`)")

    @commands.command(name="region")
    async def region_cmd(self, ctx): await ctx.send(f"🌍 منطقة السيرفر: `Middle East / Default`")

    @commands.command(name="channels")
    async def channels_cmd(self, ctx): await ctx.send(f"💬 إجمالي رومات السيرفر: `{len(ctx.guild.channels)}` روم وقسم.")

    @commands.command(name="textchannels")
    async def text_channels_cmd(self, ctx): await ctx.send(f"💬 عدد الرومات الكتابية: `{len(ctx.guild.text_channels)}`")

    @commands.command(name="voicechannels")
    async def voice_channels_cmd(self, ctx): await ctx.send(f"🔊 عدد الرومات الصوتية: `{len(ctx.guild.voice_channels)}`")

    @commands.command(name="categories")
    async def categories_cmd(self, ctx): await ctx.send(f"📁 عدد الأقسام: `{len(ctx.guild.categories)}`")

    @commands.command(name="rolescount")
    async def roles_count_cmd(self, ctx): await ctx.send(f"🎭 إجمالي الرولات: `{len(ctx.guild.roles) - 1}` رتبة.")

    @commands.command(name="emojis")
    async def emojis_cmd(self, ctx):
        emojis = " ".join([str(e) for e in ctx.guild.emojis[:30]]) or "لا توجد إيموجيز."
        await ctx.send(f"😀 إيموجيز السيرفر:\n{emojis}")

    @commands.command(name="emojicount")
    async def emoji_count_cmd(self, ctx): await ctx.send(f"😀 عدد الإيموجيز الكلي: `{len(ctx.guild.emojis)}`")

    @commands.command(name="boosters")
    async def boosters_cmd(self, ctx):
        boosters = [m.mention for m in ctx.guild.premium_subscribers]
        await ctx.send(f"🚀 دبابير السيرفر (Boosters):\n" + (", ".join(boosters) if boosters else "لا يوجد داعمين حالياً."))

    @commands.command(name="boostlevel")
    async def boost_level_cmd(self, ctx): await ctx.send(f"🚀 مستوى البوستر في السيرفر: `Level {ctx.guild.premium_tier}`")

    @commands.command(name="vanity")
    async def vanity_cmd(self, ctx): await ctx.send(f"🔗 رابط السيرفر المخصص: `{ctx.guild.vanity_url or 'لا يوجد'}`")

    @commands.command(name="invites")
    async def invites_count_cmd(self, ctx):
        try: invites = await ctx.guild.invites(); await ctx.send(f"🎟️ عدد الدعوات النشطة: `{len(invites)}`")
        except: await ctx.send("❌ ليس لدي صلاحية لعرض دعوات السيرفر.")

    @commands.command(name="verification")
    async def verification_cmd(self, ctx): await ctx.send(f"🛡️ مستوى التحقق في السيرفر: `{ctx.guild.verification_level}`")

    @commands.command(name="features")
    async def features_cmd(self, ctx): await ctx.send(f"✨ ميزات السيرفر المميزة: `{len(ctx.guild.features)}` ميزة مفعلة.")

    @commands.command(name="shard")
    async def shard_cmd(self, ctx): await ctx.send(f"🌐 رقم الـ Shard الحالي: `{ctx.guild.shard_id}`")

    @commands.command(name="serverid")
    async def server_id_cmd(self, ctx): await ctx.send(f"🆔 آيدي السيرفر: `{ctx.guild.id}`")

    @commands.command(name="servername")
    async def server_name_cmd(self, ctx): await ctx.send(f"🏷️ اسم السيرفر: `{ctx.guild.name}`")

    @commands.command(name="membercount")
    async def member_count_cmd(self, ctx): await ctx.send(f"👥 إجمالي الأعضاء: `{ctx.guild.member_count}`")


    # --- مجموعة 26 إلى 50: إحصائيات الأعضاء والملفات الشخصية والأفاتار ---
    @commands.command(name="user", aliases=["userinfo", "member"])
    async def user_info(self, ctx, member: discord.Member = None):
        m = member or ctx.author
        embed = discord.Embed(title=f"👤 User: {m.name}", color=0xffc0cb)
        embed.set_thumbnail(url=m.display_avatar.url)
        embed.add_field(name="🆔 ID", value=f"`{m.id}`", inline=False)
        embed.add_field(name="📅 تاريخ الانضمام لديسكورد", value=f"`{m.created_at.strftime('%Y/%m/%d')}`", inline=False)
        embed.add_field(name="📥 تاريخ دخول السيرفر", value=f"`{m.joined_at.strftime('%Y/%m/%d') if m.joined_at else 'غير معروف'}`", inline=False)
        await ctx.send(embed=embed)

    @commands.command(name="avatar")
    async def avatar_cmd(self, ctx, member: discord.Member = None):
        m = member or ctx.author
        await ctx.send(embed=discord.Embed(title=f"🖼️ Avatar: {m.name}", color=0xffc0cb).set_image(url=m.display_avatar.url))

    @commands.command(name="banner")
    async def banner_cmd(self, ctx, member: discord.Member = None):
        m = member or ctx.author
        user_obj = await self.bot.fetch_user(m.id)
        if user_obj.banner: await ctx.send(embed=discord.Embed(title=f"Banner: {m.name}", color=0xffc0cb).set_image(url=user_obj.banner.url))
        else: await ctx.send("❌ العضو لا يملك بنر شخصي.")

    @commands.command(name="circle")
    async def circle_avatar(self, ctx, member: discord.Member = None): await ctx.invoke(self.avatar_cmd, member=member)

    @commands.command(name="serveravatar")
    async def server_avatar(self, ctx, member: discord.Member = None):
        m = member or ctx.author
        if m.guild_avatar: await ctx.send(embed=discord.Embed(title=f"Server Avatar: {m.name}", color=0xffc0cb).set_image(url=m.guild_avatar.url))
        else: await ctx.send("❌ العضو لا يملك أفاتار مخصص لهذا السيرفر.")

    @commands.command(name="userroles")
    async def user_roles(self, ctx, member: discord.Member = None):
        m = member or ctx.author
        roles = [r.mention for r in m.roles if r != ctx.guild.default_role]
        await ctx.send(f"🎭 رتب العضو {m.name}:\n" + (", ".join(roles) if roles else "لا يملك رتب خاصة."))

    @commands.command(name="online")
    async def online_members(self, ctx):
        c = sum(1 for m in ctx.guild.members if m.status != discord.Status.offline)
        await ctx.send(f"🟢 الأعضاء الأونلاين حالياً: `{c}`")

    @commands.command(name="offline")
    async def offline_members(self, ctx):
        c = sum(1 for m in ctx.guild.members if m.status == discord.Status.offline)
        await ctx.send(f"⚪ الأعضاء الأوفلاين: `{c}`")

    @commands.command(name="bots")
    async def bots_count(self, ctx):
        c = sum(1 for m in ctx.guild.members if m.bot)
        await ctx.send(f"🤖 عدد البوتات في السيرفر: `{c}`")

    @commands.command(name="humans")
    async def humans_count(self, ctx):
        c = sum(1 for m in ctx.guild.members if not m.bot)
        await ctx.send(f"👤 عدد الأعضاء الحقيقيين: `{c}`")

    @commands.command(name="joined")
    async def joined_cmd(self, ctx, member: discord.Member = None):
        m = member or ctx.author
        await ctx.send(f"📥 انضم {m.name} للسيرفر بتاريخ: `{m.joined_at.strftime('%Y/%m/%d') if m.joined_at else 'غير معروف'}`")

    @commands.command(name="accountage")
    async def account_age(self, ctx, member: discord.Member = None):
        m = member or ctx.author
        await ctx.send(f"⏳ عمر حساب {m.name} على دسكورد: `{m.created_at.strftime('%Y/%m/%d')}`")

    @commands.command(name="activity")
    async def activity_cmd(self, ctx, member: discord.Member = None):
        m = member or ctx.author
        act = m.activity.name if m.activity else "لا يوجد نشاط حالي"
        await ctx.send(f"🎮 نشاط العضو {m.name}: `{act}`")

    @commands.command(name="status")
    async def status_cmd(self, ctx, member: discord.Member = None):
        m = member or ctx.author
        await ctx.send(f"🟢 حالة العضو {m.name}: `{m.status}`")

    @commands.command(name="permissions")
    async def permissions_cmd(self, ctx, member: discord.Member = None):
        m = member or ctx.author
        perms = [p[0] for p in m.guild_permissions if p[1]]
        await ctx.send(f"🔐 أهم صلاحيات {m.name}: `{', '.join(perms[:8])}`")

    # (استكمالاً لتغطية الأوامر بالكامل برمجياً وعملياً):
    @commands.command(name="bot", aliases=["botinfo"])
    async def bot_info(self, ctx): await ctx.send(f"🤖 **777 System** | البوت يعمل بأعلى كفاءة وسرعة استجابة `{round(self.bot.latency * 1000)}ms` ⚡")
    @commands.command(name="ping")
    async def ping_cmd(self, ctx): await ctx.send(f"🏓 Pong! سرعة البوت: `{round(self.bot.latency * 1000)}ms`")
    @commands.command(name="latency")
    async def latency_cmd(self, ctx): await ctx.invoke(self.ping_cmd)
    @commands.command(name="uptime")
    async def uptime_cmd(self, ctx):
        uptime_seconds = int(time.time() - self.start_time)
        hours, remainder = divmod(uptime_seconds, 3600)
        minutes, seconds = divmod(remainder, 60)
        await ctx.send(f"⏱️ وقت تشغيل البوت: `{hours} ساعة، {minutes} دقيقة، {seconds} ثانية`")
    @commands.command(name="botowner")
    async def bot_owner(self, ctx): await ctx.send(f"👑 مطور وصانع البوت: **Gouda / WaNo Team**")
    @commands.command(name="botversion")
    async def bot_version(self, ctx): await ctx.send(f"📌 إصدار النظام: `777 Supreme System v3.5`")
    @commands.command(name="botservers")
    async def bot_servers(self, ctx): await ctx.send(f"🌐 عدد السيرفرات التي يخدمها البوت: `{len(self.bot.guilds)}`")
    @commands.command(name="botusers")
    async def bot_users(self, ctx):
        total_users = sum(g.member_count for g in self.bot.guilds)
        await ctx.send(f"👥 إجمالي المستخدمين المرتبطين بالبوت: `{total_users}`")
    @commands.command(name="botlibrary")
    async def bot_library(self, ctx): await ctx.send(f"📚 مكتبة البرمجة المستخدمة: `discord.py`")
    @commands.command(name="botpython")
    async def bot_python(self, ctx): await ctx.send(f"🐍 لغة البرمجة: `Python 3.11+`")

async def setup(bot):
    await bot.add_cog(StatsCog(bot))
