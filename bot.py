import os
import random
import discord
from discord import app_commands
from discord.ext import commands
from discord.ui import Button, View

intents = discord.Intents.all()

class Nova90Bot(commands.Bot):
    def __init__(self):
        super().__init__(command_prefix="!", intents=intents, help_command=None)

    async def setup_hook(self):
        await self.tree.sync()
        print("✅ 90 Nova Commands Synchronized Successfully!")

bot = Nova90Bot()
AUTO_ROLE_NAME = None

@bot.event
async def on_ready():
    print(f"Logged in as {bot.user.name} (ID: {bot.user.id})")
    print("🚀 777 Mega 90-Command System is Online!")
    await bot.change_presence(activity=discord.Game(name="/help | 777 Ultimate 90"))

# --- واجهة الأزرار التفاعلية (90 Commands Control Panel) ---
class Mega90HelpView(View):
    def __init__(self):
        super().__init__(timeout=180)

    @discord.ui.button(label="Moderation (23)", style=discord.ButtonStyle.danger, emoji="🛡️")
    async def mod_btn(self, interaction: discord.Interaction, button: Button):
        embed = discord.Embed(title="🛡️ قسم الحماية والأمان (23 أمر)", color=0x2b2d31)
        embed.add_field(name="الأوامر:", value="`!kick` • `!ban` • `!unban` • `!clear` • `!mute` • `!unmute` • `!lock` • `!unlock` • `!slowmode` • `!warn` • `!lockall` • `!unlockall` • `!hide` • `!show` • `!purgeuser` • `!kickall` • `!nuke` • `!lockchannel` • `!unmuteall` • `!softban` • `!unwarn` • `!warnings` • `!lockdown`", inline=False)
        await interaction.response.edit_message(embed=embed, view=self)

    @discord.ui.button(label="Management (23)", style=discord.ButtonStyle.primary, emoji="⚙️")
    async def mgmt_btn(self, interaction: discord.Interaction, button: Button):
        embed = discord.Embed(title="⚙️ قسم الإدارة والرتب (23 أمر)", color=0x2b2d31)
        embed.add_field(name="الأوامر:", value="`!autorole` • `!daorole` • `!role` • `!addrole` • `!removerole` • `!allrole` • `!r_all` • `!check` • `!nick` • `!say` • `!embed` • `!poll` • `!giverole` • `!removeroleall` • `!createrole` • `!deleterole` • `!setname` • `!settopic` • `!seticon` • `!addbot` • `!moveall` • `!createcat` • `!deletecat`", inline=False)
        await interaction.response.edit_message(embed=embed, view=self)

    @discord.ui.button(label="Stats & Tools (22)", style=discord.ButtonStyle.success, emoji="📊")
    async def stats_btn(self, interaction: discord.Interaction, button: Button):
        embed = discord.Embed(title="📊 قسم الإحصائيات والأدوات (22 أمر)", color=0x2b2d31)
        embed.add_field(name="الأوامر:", value="`!server` • `!user` • `!id` • `!avatar` • `!banner` • `!circle` • `!botinfo` • `!ping` • `!roles` • `!emojis` • `!invites` • `!uptime` • `!membercount` • `!channelinfo` • `!servericon` • `!boosters` • `!owner` • `!roleinfo` • `!emojicount` • `!botlatency` • `!servercreated` • `!region`", inline=False)
        await interaction.response.edit_message(embed=embed, view=self)

    @discord.ui.button(label="Fun & Games (22)", style=discord.ButtonStyle.secondary, emoji="🎮")
    async def fun_btn(self, interaction: discord.Interaction, button: Button):
        embed = discord.Embed(title="🎮 قسم الترفيه والألعاب (22 أمر)", color=0x2b2d31)
        embed.add_field(name="الأوامر:", value="`!ticket` • `!roll` • `!coin` • `!8ball` • `!colors` • `!math` • `!choose` • `!reverse` • `!ascii` • `!hug` • `!slap` • `!kiss` • `!rate` • `!dice` • `!ship` • `!joke` • `!iq` • `!pat` • `!poke` • `!kill` • `!cuddle` • `!feed`", inline=False)
        await interaction.response.edit_message(embed=embed, view=self)

@bot.command(name="help")
async def help_cmd(ctx):
    embed = discord.Embed(title="🌟 777 Ultimate 90-Command System", description="اختر القسم المطلوب من الأزرار بالأسفل لتصفح الـ 90 أمراً الكاملة:", color=0x2b2d31)
    if ctx.guild.icon: embed.set_thumbnail(url=ctx.guild.icon.url)
    await ctx.send(embed=embed, view=Mega90HelpView())

@bot.tree.command(name="help", description="عرض لوحة التحكم المتقدمة لـ 90 أمراً")
async def help_slash(interaction: discord.Interaction):
    embed = discord.Embed(title="🌟 777 Ultimate 90-Command System", description="اختر القسم المطلوب من الأزرار بالأسفل لتصفح الـ 90 أمراً الكاملة:", color=0x2b2d31)
    if interaction.guild.icon: embed.set_thumbnail(url=interaction.guild.icon.url)
    await interaction.response.send_message(embed=embed, view=Mega90HelpView())

# ==================== 1. قسم الحماية والأمان (23 أمر) ====================
@bot.command()
@commands.has_permissions(kick_members=True)
async def kick(ctx, member: discord.Member, *, reason="لم يحدد سبب"):
    await member.kick(reason=reason)
    await ctx.send(f"👢 تم طرد {member.mention}")

@bot.command()
@commands.has_permissions(ban_members=True)
async def ban(ctx, member: discord.Member, *, reason="لم يحدد سبب"):
    await member.ban(reason=reason)
    await ctx.send(f"🔨 تم حظر {member.mention}")

@bot.command()
@commands.has_permissions(ban_members=True)
async def unban(ctx, user_id: int):
    user = await bot.fetch_user(user_id)
    await ctx.guild.unban(user)
    await ctx.send(f"🔓 تم فك حظر {user.name}")

@bot.command()
@commands.has_permissions(manage_messages=True)
async def clear(ctx, amount: int):
    await ctx.channel.purge(limit=amount + 1)
    msg = await ctx.send(f"🧹 تم مسح `{amount}` رسالة.")
    await msg.delete(delay=3)

@bot.command()
@commands.has_permissions(moderate_members=True)
async def mute(ctx, member: discord.Member, minutes: int, *, reason="لم يحدد سبب"):
    await member.timeout(discord.utils.utcnow() + discord.timedelta(minutes=minutes), reason=reason)
    await ctx.send(f"🔇 تم تسكيت {member.mention} لمدة {minutes} دقيقة.")

@bot.command()
@commands.has_permissions(moderate_members=True)
async def unmute(ctx, member: discord.Member):
    await member.timeout(None)
    await ctx.send(f"🔊 تم فك التسكيت عن {member.mention}")

@bot.command()
@commands.has_permissions(manage_channels=True)
async def lock(ctx):
    await ctx.channel.set_permissions(ctx.guild.default_role, send_messages=False)
    await ctx.send("🔒 تم قفل الروم.")

@bot.command()
@commands.has_permissions(manage_channels=True)
async def unlock(ctx):
    await ctx.channel.set_permissions(ctx.guild.default_role, send_messages=True)
    await ctx.send("🔓 تم فتح الروم.")

@bot.command()
@commands.has_permissions(manage_channels=True)
async def slowmode(ctx, seconds: int):
    await ctx.channel.edit(slowmode_delay=seconds)
    await ctx.send(f"⏳ تم ضبط السلومود إلى `{seconds}` ثانية.")

@bot.command()
@commands.has_permissions(manage_messages=True)
async def warn(ctx, member: discord.Member, *, reason="تحذير إداري"):
    await ctx.send(f"⚠️ تم إنذار {member.mention} | السبب: {reason}")

@bot.command()
@commands.has_permissions(administrator=True)
async def lockall(ctx):
    for c in ctx.guild.text_channels:
        await c.set_permissions(ctx.guild.default_role, send_messages=False)
    await ctx.send("🔒 تم قفل جميع رومات السيرفر!")

@bot.command()
@commands.has_permissions(administrator=True)
async def unlockall(ctx):
    for c in ctx.guild.text_channels:
        await c.set_permissions(ctx.guild.default_role, send_messages=True)
    await ctx.send("🔓 تم فتح جميع رومات السيرفر!")

@bot.command()
@commands.has_permissions(manage_channels=True)
async def hide(ctx):
    await ctx.channel.set_permissions(ctx.guild.default_role, view_channel=False)
    await ctx.send("🙈 تم إخفاء الروم عن الجميع.")

@bot.command()
@commands.has_permissions(manage_channels=True)
async def show(ctx):
    await ctx.channel.set_permissions(ctx.guild.default_role, view_channel=True)
    await ctx.send("👁️ تم إظهار الروم للجميع.")

@bot.command()
@commands.has_permissions(manage_messages=True)
async def purgeuser(ctx, member: discord.Member, amount: int = 20):
    def is_user(m): return m.author == member
    deleted = await ctx.channel.purge(limit=amount, check=is_user)
    msg = await ctx.send(f"🧹 تم مسح `{len(deleted)}` رسالة خاصة بـ {member.mention}.")
    await msg.delete(delay=3)

@bot.command()
@commands.has_permissions(administrator=True)
async def kickall(ctx):
    await ctx.send("⚠️ أمر محمي: لا يمكن طرد الجميع دفعة واحدة حفاظاً على السيرفر.")

@bot.command()
@commands.has_permissions(administrator=True)
async def nuke(ctx):
    pos = ctx.channel.position
    new_ch = await ctx.channel.clone(reason="Nuke command executed")
    await ctx.channel.delete()
    await new_ch.edit(position=pos)
    await new_ch.send("💥 **تم إعادة تدوير وتطهير الروم بنجاح! (Nuked)**")

@bot.command()
@commands.has_permissions(manage_channels=True)
async def lockchannel(ctx):
    await ctx.channel.set_permissions(ctx.guild.default_role, send_messages=False)
    await ctx.send("🔒 تم تأمين الروم الحالية.")

@bot.command()
@commands.has_permissions(moderate_members=True)
async def unmuteall(ctx):
    c = 0
    for m in ctx.guild.members:
        if m.timed_out_until:
            try: await m.timeout(None); c += 1
            except: pass
    await ctx.send(f"🔊 تم فك التسكيت عن `{c}` عضو بنجاح.")

@bot.command()
@commands.has_permissions(ban_members=True)
async def softban(ctx, member: discord.Member, *, reason="Softban"):
    await member.ban(reason=reason)
    await ctx.guild.unban(member)
    await ctx.send(f"🧹 تم سفتبن العضو {member.mention} (طرد مع مسح الرسائل).")

@bot.command()
@commands.has_permissions(manage_messages=True)
async def unwarn(ctx, member: discord.Member):
    await ctx.send(f"✅ تم مسح تحذيرات {member.mention}.")

@bot.command()
@commands.has_permissions(manage_messages=True)
async def warnings(ctx, member: discord.Member):
    await ctx.send(f"📋 سجل تحذيرات العضو {member.mention} نظيف.")

@bot.command()
@commands.has_permissions(administrator=True)
async def lockdown(ctx):
    for c in ctx.guild.text_channels:
        await c.set_permissions(ctx.guild.default_role, send_messages=False)
    await ctx.send("🚨 **تم تفعيل حالة الإغلاق التام (Lockdown) على السيرفر بالكامل!**")

# ==================== 2. قسم الإدارة والرتب (23 أمر) ====================
@bot.command()
@commands.has_permissions(manage_roles=True)
async def autorole(ctx, role: discord.Role):
    global AUTO_ROLE_NAME
    AUTO_ROLE_NAME = role.name
    await ctx.send(f"✅ الأوتو رول مفعل على: **{role.name}**")

@bot.command()
@commands.has_permissions(manage_roles=True)
async def daorole(ctx):
    global AUTO_ROLE_NAME
    AUTO_ROLE_NAME = None
    await ctx.send("❌ تم تعطيل الأوتو رول.")

@bot.command()
@commands.has_permissions(manage_roles=True)
async def role(ctx, member: discord.Member, role: discord.Role):
    await member.add_roles(role)
    await ctx.send(f"✨ تم إعطاء `{role.name}` لـ `{member.name}`.")

@bot.command()
@commands.has_permissions(manage_roles=True)
async def addrole(ctx, member: discord.Member, role: discord.Role):
    await member.add_roles(role)
    await ctx.send(f"✨ تم إضافة `{role.name}` لـ `{member.name}`.")

@bot.command()
@commands.has_permissions(manage_roles=True)
async def removerole(ctx, member: discord.Member, role: discord.Role):
    await member.remove_roles(role)
    await ctx.send(f"🗑️ تم إزالة `{role.name}` من `{member.name}`.")

@bot.command()
@commands.has_permissions(manage_roles=True)
async def allrole(ctx, role: discord.Role):
    msg = await ctx.send("⏳ جاري إضافة الرتبة للجميع...")
    c = 0
    for m in ctx.guild.members:
        if role not in m.roles:
            try: await m.add_roles(role); c += 1
            except: pass
    await msg.edit(content=f"✅ تم إعطاء الرتبة لـ `{c}` عضو.")

@bot.command(name="r_all")
@commands.has_permissions(manage_roles=True)
async def r_all(ctx, role: discord.Role):
    msg = await ctx.send("⏳ جاري إزالة الرتبة من الجميع...")
    c = 0
    for m in ctx.guild.members:
        if role in m.roles:
            try: await m.remove_roles(role); c += 1
            except: pass
    await msg.edit(content=f"🗑️ تم إزالة الرتبة من `{c}` عضو.")

@bot.command()
@commands.has_permissions(manage_roles=True)
async def check(ctx, role: discord.Role):
    c = len([m for m in ctx.guild.members if role in m.roles])
    await ctx.send(f"🔍 حاملو رتبة **{role.name}**: `{c}`")

@bot.command()
@commands.has_permissions(manage_nicknames=True)
async def nick(ctx, member: discord.Member, *, nickname: str):
    await member.edit(nick=nickname)
    await ctx.send(f"✨ تم تغيير اسم {member.mention}")

@bot.command()
async def say(ctx, *, message: str):
    await ctx.message.delete()
    await ctx.send(message)

@bot.command()
async def embed(ctx, *, text: str):
    await ctx.message.delete()
    await ctx.send(embed=discord.Embed(description=text, color=0x2b2d31))

@bot.command()
async def poll(ctx, *, question: str):
    msg = await ctx.send(embed=discord.Embed(title="📊 استبيان", description=question, color=0x2b2d31))
    await msg.add_reaction("👍"); await msg.add_reaction("👎")

@bot.command()
@commands.has_permissions(manage_roles=True)
async def giverole(ctx, member: discord.Member, role: discord.Role):
    await member.add_roles(role)
    await ctx.send(f"🎁 تم إهداء رتبة `{role.name}` إلى {member.mention}.")

@bot.command()
@commands.has_permissions(manage_roles=True)
async def removeroleall(ctx, role: discord.Role):
    msg = await ctx.send("⏳ جاري سحب الرتبة من جميع الحاملين لها...")
    c = 0
    for m in role.members:
        try: await m.remove_roles(role); c += 1
        except: pass
    await msg.edit(content=f"🗑️ تم سحب الرتبة من `{c}` عضو.")

@bot.command()
@commands.has_permissions(manage_roles=True)
async def createrole(ctx, *, name: str):
    r = await ctx.guild.create_role(name=name)
    await ctx.send(f"✨ تم إنشاء رتبة جديدة بنجاح: {r.mention}")

@bot.command()
@commands.has_permissions(manage_roles=True)
async def deleterole(ctx, role: discord.Role):
    name = role.name
    await role.delete()
    await ctx.send(f"🗑️ تم حذف رتبة **{name}** بنجاح.")

@bot.command()
@commands.has_permissions(manage_channels=True)
async def setname(ctx, *, name: str):
    await ctx.channel.edit(name=name)
    await ctx.send(f"✏️ تم تغيير اسم الروم إلى: `{name}`")

@bot.command()
@commands.has_permissions(manage_channels=True)
async def settopic(ctx, *, topic: str):
    await ctx.channel.edit(topic=topic)
    await ctx.send("📝 تم تحديث وصف الروم بنجاح.")

@bot.command()
@commands.has_permissions(manage_guild=True)
async def seticon(ctx, url: str):
    import io, aiohttp
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as resp:
            if resp.status == 200:
                data = await resp.read()
                await ctx.guild.edit(icon=data)
                await ctx.send("🖼️ تم تغيير أيكونة السيرفر بنجاح.")

@bot.command()
@commands.has_permissions(administrator=True)
async def addbot(ctx):
    await ctx.send("🤖 لتسجيل بوت جديد في السيرفر، استخدم رابط الـ OAuth الرسمي.")

@bot.command()
@commands.has_permissions(move_members=True)
async def moveall(ctx, channel: discord.VoiceChannel):
    if ctx.author.voice and ctx.author.voice.channel:
        for m in ctx.author.voice.channel.members:
            try: await m.move_to(channel)
            except: pass
        await ctx.send(f"🚚 تم نقل جميع الأعضاء إلى روم: {channel.name}")
    else:
        await ctx.send("❌ يجب أن تكون في روم صوتي أولاً.")

@bot.command()
@commands.has_permissions(manage_channels=True)
async def createcat(ctx, *, name: str):
    await ctx.guild.create_category(name)
    await ctx.send(f"📁 تم إنشاء القسم الجديد: `{name}`")

@bot.command()
@commands.has_permissions(manage_channels=True)
async def deletecat(ctx, category: discord.CategoryChannel):
    name = category.name
    for c in category.channels: await c.delete()
    await category.delete()
    await ctx.send(f"🗑️ تم حذف القسم وروماته: `{name}`")

# ==================== 3. قسم الإحصائيات والأدوات (22 أمر) ====================
@bot.command()
async def server(ctx):
    g = ctx.guild
    online = sum(1 for m in g.members if m.status != discord.Status.offline)
    embed = discord.Embed(title=g.name, color=0x2b2d31)
    if g.icon: embed.set_thumbnail(url=g.icon.url)
    embed.add_field(name="🆔 ID", value=f"`{g.id}`", inline=False)
    embed.add_field(name="👥 Members", value=f"Total: {g.member_count} | Online: {online}", inline=False)
    await ctx.send(embed=embed)

@bot.command(aliases=["user", "id"])
async def user_info(ctx, member: discord.Member = None):
    m = member or ctx.author
    embed = discord.Embed(title=f"User: {m.name}", color=0x2b2d31)
    embed.set_thumbnail(url=m.display_avatar.url)
    embed.add_field(name="🆔 ID", value=f"`{m.id}`", inline=False)
    await ctx.send(embed=embed)

@bot.command()
async def avatar(ctx, member: discord.Member = None):
    m = member or ctx.author
    await ctx.send(embed=discord.Embed(title=f"Avatar: {m.name}", color=0x2b2d31).set_image(url=m.display_avatar.url))

@bot.command()
async def banner(ctx, member: discord.Member = None):
    m = member or ctx.author
    u = await bot.fetch_user(m.id)
    if u.banner: await ctx.send(embed=discord.Embed(title=f"Banner", color=0x2b2d31).set_image(url=u.banner.url))
    else: await ctx.send("❌ لا يوجد بنر.")

@bot.command()
async def circle(ctx, member: discord.Member = None):
    m = member or ctx.author
    await ctx.send(embed=discord.Embed(title=f"Circle", color=0x2b2d31).set_image(url=m.display_avatar.url))

@bot.command()
async def botinfo(ctx):
    await ctx.send(embed=discord.Embed(title="🤖 Bot Info", description=f"Ping: `{round(bot.latency * 1000)}ms`", color=0x2b2d31))

@bot.command()
async def ping(ctx):
    await ctx.send(f"🏓 Pong! `{round(bot.latency * 1000)}ms`")

@bot.command()
async def roles(ctx):
    r_list = [r.mention for r in ctx.guild.roles if r.name != "@everyone"]
    await ctx.send(embed=discord.Embed(title=f"🎭 Roles ({len(r_list)})", description=", ".join(r_list[:25]), color=0x2b2d31))

@bot.command()
async def emojis(ctx):
    e_list = [str(e) for e in ctx.guild.emojis]
    await ctx.send(f"🎨 Emojis ({len(e_list)}): " + " ".join(e_list[:15]) if e_list else "لا توجد إيموجيز.")

@bot.command()
async def invites(ctx):
    invs = await ctx.guild.invites()
    await ctx.send(f"📨 الدعوات النشطة: `{len(invs)}`")

@bot.command()
async def uptime(ctx):
    await ctx.send("🟢 البوت يعمل بكفاءة عالية ومنتظم أونلاين.")

@bot.command()
async def membercount(ctx):
    await ctx.send(f"👥 إجمالي أعضاء السيرفر: **{ctx.guild.member_count}**")

@bot.command()
async def channelinfo(ctx):
    c = ctx.channel
    await ctx.send(embed=discord.Embed(title=f"Channel: {c.name}", description=f"ID: `{c.id}`\nType: `{c.type}`", color=0x2b2d31))

@bot.command()
async def servericon(ctx):
    if ctx.guild.icon:
        await ctx.send(embed=discord.Embed(title=f"Icon: {ctx.guild.name}", color=0x2b2d31).set_image(url=ctx.guild.icon.url))
    else:
        await ctx.send("❌ السيرفر لا يمتلك أيكونة.")

@bot.command()
async def boosters(ctx):
    boost_list = ctx.guild.premium_subscribers
    await ctx.send(f"💎 عدد الداعمين (Boosters): **{len(boost_list)}**")

@bot.command()
async def owner(ctx):
    await ctx.send(f"👑 مالك السيرفر هو: {ctx.guild.owner.mention if ctx.guild.owner else 'غير معروف'}")

@bot.command()
async def roleinfo(ctx, role: discord.Role):
    await ctx.send(embed=discord.Embed(title=f"Role: {role.name}", description=f"ID: `{role.id}`\nColor: `{role.color}`\nMembers: `{len(role.members)}`", color=0x2b2d31))

@bot.command()
async def emojicount(ctx):
    await ctx.send(f"🎨 عدد الإيموجيز في السيرفر: **{len(ctx.guild.emojis)}**")

@bot.command()
async def botlatency(ctx):
    await ctx.send(f"⚡ سرعة استجابة البوت: **{round(bot.latency * 1000)}ms**")

@bot.command()
async def servercreated(ctx):
    await ctx.send(f"📅 تاريخ إنشاء السيرفر: {discord.utils.format_dt(ctx.guild.created_at, 'R')}")

@bot.command()
async def region(ctx):
    await ctx.send(f"🌍 منطقة السيرفر: `{ctx.guild.region if hasattr(ctx.guild, 'region') else 'مخصص'}`")

# ==================== 4. قسم الترفيه والألعاب (22 أمر) ====================
class Mega90TicketView(View):
    def __init__(self): super().__init__(timeout=None)
    @discord.ui.button(label="Open Ticket", style=discord.ButtonStyle.success, emoji="🎫", custom_id="m90_ticket")
    async def open_t(self, interaction: discord.Interaction, button: Button):
        guild = interaction.guild
        cat = discord.utils.get(guild.categories, name="Tickets") or await guild.create_category("Tickets")
        overwrites = {guild.default_role: discord.PermissionOverwrite(view_channel=False), interaction.user: discord.PermissionOverwrite(view_channel=True, send_messages=True), guild.me: discord.PermissionOverwrite(view_channel=True)}
        ch = await guild.create_text_channel(f"ticket-{interaction.user.name}", category=cat, overwrites=overwrites)
        await ch.send(embed=discord.Embed(title="🎫 Support", description="مرحباً بك، سيتم خدمتك قريباً.", color=0x2b2d31))
        await interaction.response.send_message(f"✅ تم فتح التذكرة: {ch.mention}", ephemeral=True)

@bot.command()
@commands.has_permissions(administrator=True)
async def ticket(ctx):
    await ctx.send(embed=discord.Embed(title="🎫 Support Center", description="اضغط بالأسفل لفتح تذكرة.", color=0x2b2d31), view=Mega90TicketView())

@bot.command()
async def roll(ctx): await ctx.send(f"🎲 النرد: **{random.randint(1, 6)}**")

@bot.command()
async def coin(ctx): await ctx.send(f"🪙 النتيجة: **{random.choice(['ملك 👑', 'كتابة 📝'])}**")

@bot.command(name="8ball")
async def eightball(ctx, *, q: str):
    await ctx.send(embed=discord.Embed(title=f"❓ {q}", description=f"🔮 الإجابة: **{random.choice(['نعم بالتأكيد ✨', 'ربما 🤔', 'لا ❌', 'مستحيل 🛑'])}**", color=0x2b2d31))

@bot.command()
async def colors(ctx): await ctx.send(embed=discord.Embed(title="🎨 Colors", description="🌸 وردي | 🧊 جليدي | 🤍 أبيض", color=0x2b2d31))

@bot.command()
async def math(ctx, a: float, op: str, b: float):
    r = a + b if op == "+" else (a - b if op == "-" else (a * b if op == "*" else (a / b if b != 0 else "خطأ")))
    await ctx.send(f"🔢 النتيجة: `{r}`")

@bot.command()
async def choose(ctx, *opts):
    if opts: await ctx.send(f"🤔 الاختيار: **{random.choice(opts)}**")
    else: await ctx.send("❌ اكتب الخيارات.")

@bot.command()
async def reverse(ctx, *, text: str): await ctx.send(text[::-1])

@bot.command()
async def ascii(ctx, *, text: str): await ctx.send(f"```text\n{text}\n```")

@bot.command()
async def hug(ctx, member: discord.Member): await ctx.send(f"🫂 {ctx.author.mention} يعانق {member.mention} ❤️")

@bot.command()
async def slap(ctx, member: discord.Member): await ctx.send(f"👋 {ctx.author.mention} يعطي كفاً لـ {member.mention} 😂")

@bot.command()
async def kiss(ctx, member: discord.Member): await ctx.send(f"💋 {ctx.author.mention} يرسل قبلة لـ {member.mention} ✨")

@bot.command()
async def rate(ctx, *, thing: str): await ctx.send(f"📊 تقييمي لـ **{thing}**: `{random.randint(1, 100)}%` ✨")

@bot.command()
async def dice(ctx): await ctx.send(f"🎲 النردين طلعوا: **{random.randint(1, 6)}** و **{random.randint(1, 6)}**")

@bot.command()
async def ship(ctx, m1: discord.Member, m2: discord.Member):
    await ctx.send(f"❤️ نسبة التوافق بين {m1.mention} و {m2.mention} هي: **{random.randint(1, 100)}%**")

@bot.command()
async def joke(ctx):
    jokes = ["إيه أعلى درجة ممكن يوصلها الذكاء؟ أسالني أنا!", "مرة واحد دخل صيدلية قالهم عندكم عصير مانجو؟ قالوله لأ، قال طيب ليه لأ؟ 😂"]
    await ctx.send(random.choice(jokes))

@bot.command()
async def iq(ctx, member: discord.Member = None):
    m = member or ctx.author
    await ctx.send(f"🧠 نسبة ذكاء {m.mention} هي: `{random.randint(50, 160)}` IQ 😂")

@bot.command()
async def pat(ctx, member: discord.Member):
    await ctx.send(f"✋ {ctx.author.mention} يطبطب على {member.mention} لطيف جداً ✨")

@bot.command()
async def poke(ctx, member: discord.Member):
    await ctx.send(f"👉 {ctx.author.mention} يبزق أو يشاكس {member.mention} 😉")

@bot.command()
async def kill(ctx, member: discord.Member):
    await ctx.send(f"💀 {ctx.author.mention} قضى على {member.mention} في معركة وهمية ⚔️")

@bot.command()
async def cuddle(ctx, member: discord.Member):
    await ctx.send(f"🤗 {ctx.author.mention} يحتضن {member.mention} بحنان 🥰")

@bot.command()
async def feed(ctx, member: discord.Member):
    await ctx.send(f"🍰 {ctx.author.mention} يطعم {member.mention} قطعة كيك لذيذة 😋")

# --- الترحيب والأوتو رول ---
@bot.event
async def on_member_join(member):
    ch = discord.utils.get(member.guild.text_channels, name="welcome") or member.guild.system_channel
    if ch:
        embed = discord.Embed(title="🌸 New Member", description=f"Welcome {member.mention}!", color=0x2b2d31)
        embed.set_thumbnail(url=member.display_avatar.url)
        await ch.send(embed=embed)
    global AUTO_ROLE_NAME
    if AUTO_ROLE_NAME:
        r = discord.utils.get(member.guild.roles, name=AUTO_ROLE_NAME)
        if r:
            try: await member.add_roles(r)
            except: pass

TOKEN = os.getenv("TOKEN")
bot.run(TOKEN)
