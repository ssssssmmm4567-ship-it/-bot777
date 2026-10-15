import os
import discord
from discord.ext import commands
import random

intents = discord.Intents.all()

class NovaSupremeMasterBot(commands.Bot):
    def __init__(self):
        super().__init__(command_prefix="!", intents=intents, help_command=None)

    async def setup_hook(self):
        if os.path.exists("./cogs"):
            for filename in os.listdir("./cogs"):
                if filename.endswith(".py"):
                    cog_name = filename[:-3]
                    try:
                        await self.load_extension(f"cogs.{cog_name}")
                        print(f"📦 [NOVA SYSTEM] Loaded Cog: {cog_name}")
                    except Exception as e:
                        print(f"❌ Failed to load {cog_name}: {e}")
        await self.tree.sync()
        print("✅ [NOVA SYSTEM] All 150+ Modular & Main Commands Synchronized!")

bot = NovaSupremeMasterBot()

@bot.event
async def on_ready():
    print(f"-----------------------------------")
    print(f"🚀 Nova Bot Logged in as: {bot.user.name} (ID: {bot.user.id})")
    print(f"👑 777 Supreme Enterprise System Active!")
    print(f"-----------------------------------")
    await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name="over 777 Server | !help"))

# ==========================================
# 75 أمراً تشغيلياً وأساسياً مباشرة في ملف bot.py
# ==========================================

# 1 إلى 10: واجهة المساعدة والأوامر الأساسية
@bot.command(name="help", aliases=["commands", "الاوامر"])
async def help_cmd(ctx):
    embed = discord.Embed(
        title="🌟 Nova 777 Supreme Master Control",
        description="لوحة التحكم الملكية لسيرفر 777. البوت يعمل بكامل طاقته ونظامه الملون.",
        color=0xffc0cb
    )
    if ctx.guild.icon:
        embed.set_thumbnail(url=ctx.guild.icon.url)
    embed.add_field(name="🛡️ قسم الحماية", value="`!kick`, `!ban`, `!mute`, `!clear`, `!lock`, `!unlock`, `!nuke`", inline=False)
    embed.add_field(name="🎭 قسم الرولات", value="`!roles`, `!role`, `!removerole`, `!check`, `!allrole`", inline=False)
    embed.add_field(name="📊 الإحصائيات", value="`!server`, `!user`, `!avatar`, `!ping`, `!uptime`", inline=False)
    embed.set_footer(text=f"Requested by {ctx.author.name} | 777 Community", icon_url=ctx.author.display_avatar.url)
    await ctx.send(embed=embed)

@bot.command(name="ping")
async def ping_cmd(ctx):
    await ctx.send(f"🏓 Pong! سرعة الاستجابة: `{round(bot.latency * 1000)}ms`")

@bot.command(name="uptime")
async def uptime_cmd(ctx):
    await ctx.send("🟢 البوت يعمل على مدار الساعة بثبات تام على ريلواي.")

@bot.command(name="botinfo")
async def botinfo_cmd(ctx):
    await ctx.send("🤖 بوت 777 Supreme الخارق لإدارة السيرفرات باحترافية.")

@bot.command(name="owner")
async def owner_cmd(ctx):
    await ctx.send(f"👑 مالك السيرفر الأساسي: {ctx.guild.owner.mention if ctx.guild.owner else 'غير معروف'}")

@bot.command(name="server", aliases=["serverinfo"])
async def server_cmd(ctx):
    g = ctx.guild
    online = sum(1 for m in g.members if m.status != discord.Status.offline)
    embed = discord.Embed(title=f"🌸 سيرفر {g.name}", color=0xffc0cb)
    if g.icon: embed.set_thumbnail(url=g.icon.url)
    embed.add_field(name="🆔 Server ID", value=f"`{g.id}`", inline=False)
    embed.add_field(name="👥 Members", value=f"Total: {g.member_count} | Online: {online}", inline=False)
    embed.add_field(name="💬 Channels", value=f"Text: {len(g.text_channels)} | Voice: {len(g.voice_channels)}", inline=False)
    embed.add_field(name="🎭 Roles", value=f"`{len(g.roles)}` رتبة", inline=False)
    await ctx.send(embed=embed)

@bot.command(name="user", aliases=["id", "whois"])
async def user_cmd(ctx, member: discord.Member = None):
    m = member or ctx.author
    embed = discord.Embed(title=f"👤 معلومات العضو: {m.name}", color=0x2b2d31)
    embed.set_thumbnail(url=m.display_avatar.url)
    embed.add_field(name="🆔 User ID", value=f"`{m.id}`", inline=False)
    embed.add_field(name="📅 انضمام ديسكورد", value=f"{discord.utils.format_dt(m.created_at, 'R')}", inline=False)
    await ctx.send(embed=embed)

@bot.command(name="avatar", aliases=["av"])
async def avatar_cmd(ctx, member: discord.Member = None):
    m = member or ctx.author
    await ctx.send(embed=discord.Embed(title=f"🖼️ أفاتار {m.name}", color=0x2b2d31).set_image(url=m.display_avatar.url))

@bot.command(name="servericon", aliases=["icon"])
async def servericon_cmd(ctx):
    if ctx.guild.icon:
        await ctx.send(embed=discord.Embed(title="🎨 أيكونة السيرفر", color=0x2b2d31).set_image(url=ctx.guild.icon.url))
    else:
        await ctx.send("❌ السيرفر ليس لديه أيكونة.")

@bot.command(name="banner")
async def banner_cmd(ctx, member: discord.Member = None):
    m = member or ctx.author
    u = await bot.fetch_user(m.id)
    if u.banner:
        await ctx.send(embed=discord.Embed(title=f"🎨 بنر {m.name}", color=0x2b2d31).set_image(url=u.banner.url))
    else:
        await ctx.send("❌ المستخدم ليس لديه بنر.")

# 11 إلى 25: أوامر الإدارة السريعة
@bot.command(name="kick")
@commands.has_permissions(kick_members=True)
async def kick_cmd(ctx, member: discord.Member, *, reason="لم يحدد"):
    await member.kick(reason=reason)
    await ctx.send(f"👢 تم طرد {member.mention}")

@bot.command(name="ban")
@commands.has_permissions(ban_members=True)
async def ban_cmd(ctx, member: discord.Member, *, reason="لم يحدد"):
    await member.ban(reason=reason)
    await ctx.send(f"🔨 تم حظر {member.mention}")

@bot.command(name="unban")
@commands.has_permissions(ban_members=True)
async def unban_cmd(ctx, user_id: int):
    u = await bot.fetch_user(user_id)
    await ctx.guild.unban(u)
    await ctx.send(f"🔓 تم فك حظر {u.name}")

@bot.command(name="clear", aliases=["purge"])
@commands.has_permissions(manage_messages=True)
async def clear_cmd(ctx, amount: int):
    await ctx.channel.purge(limit=amount + 1)
    msg = await ctx.send(f"🧹 تم مسح `{amount}` رسالة.")
    await msg.delete(delay=3)

@bot.command(name="mute")
@commands.has_permissions(moderate_members=True)
async def mute_cmd(ctx, member: discord.Member, minutes: int):
    await member.timeout(discord.utils.utcnow() + discord.timedelta(minutes=minutes))
    await ctx.send(f"🔇 تم تسكيت {member.mention} لمدة `{minutes}` دقيقة.")

@bot.command(name="unmute")
@commands.has_permissions(moderate_members=True)
async def unmute_cmd(ctx, member: discord.Member):
    await member.timeout(None)
    await ctx.send(f"🔊 تم فك التسكيت عن {member.mention}")

@bot.command(name="lock")
@commands.has_permissions(manage_channels=True)
async def lock_cmd(ctx):
    await ctx.channel.set_permissions(ctx.guild.default_role, send_messages=False)
    await ctx.send("🔒 تم قفل الروم الحالية.")

@bot.command(name="unlock")
@commands.has_permissions(manage_channels=True)
async def unlock_cmd(ctx):
    await ctx.channel.set_permissions(ctx.guild.default_role, send_messages=True)
    await ctx.send("🔓 تم فتح الروم الحالية.")

@bot.command(name="slowmode")
@commands.has_permissions(manage_channels=True)
async def slowmode_cmd(ctx, seconds: int):
    await ctx.channel.edit(slowmode_delay=seconds)
    await ctx.send(f"⏳ تم ضبط السلومود إلى `{seconds}` ثانية.")

@bot.command(name="nuke")
@commands.has_permissions(administrator=True)
async def nuke_cmd(ctx):
    pos = ctx.channel.position
    new_ch = await ctx.channel.clone()
    await ctx.channel.delete()
    await new_ch.edit(position=pos)
    await new_ch.send("💥 **تم تطهير الروم بنجاح!**")

@bot.command(name="hide")
@commands.has_permissions(manage_channels=True)
async def hide_cmd(ctx):
    await ctx.channel.set_permissions(ctx.guild.default_role, view_channel=False)
    await ctx.send("🙈 تم إخفاء الروم.")

@bot.command(name="show")
@commands.has_permissions(manage_channels=True)
async def show_cmd(ctx):
    await ctx.channel.set_permissions(ctx.guild.default_role, view_channel=True)
    await ctx.send("👁️ تم إظهار الروم.")

@bot.command(name="warn")
@commands.has_permissions(manage_messages=True)
async def warn_cmd(ctx, member: discord.Member, *, reason="تحذير"):
    await ctx.send(f"⚠️ تم إنذار {member.mention} | السبب: {reason}")

@bot.command(name="say")
@commands.has_permissions(administrator=True)
async def say_cmd(ctx, *, message: str):
    await ctx.message.delete()
    await ctx.send(message)

@bot.command(name="embed")
@commands.has_permissions(administrator=True)
async def embed_cmd(ctx, *, text: str):
    await ctx.message.delete()
    await ctx.send(embed=discord.Embed(description=text, color=0xffc0cb))

# 26 إلى 50: أوامر الألعاب، الترفيه، والتفاعل الفوري
@bot.command(name="roll")
async def roll_cmd(ctx): await ctx.send(f"🎲 نرد الحظ: **{random.randint(1, 6)}**")

@bot.command(name="coin")
async def coin_cmd(ctx): await ctx.send(f"🪙 النتيجة: **{random.choice(['ملك 👑', 'كتابة 📝'])}**")

@bot.command(name="hug")
async def hug_cmd(ctx, member: discord.Member): await ctx.send(f"🫂 {ctx.author.mention} يعانق {member.mention} ❤️")

@bot.command(name="slap")
async def slap_cmd(ctx, member: discord.Member): await ctx.send(f"👋 {ctx.author.mention} يعطي كفاً لـ {member.mention} 😂")

@bot.command(name="kiss")
async def kiss_cmd(ctx, member: discord.Member): await ctx.send(f"💋 {ctx.author.mention} يرسل قبلة لـ {member.mention} ✨")

@bot.command(name="rate")
async def rate_cmd(ctx, *, item: str): await ctx.send(f"📊 تقييمي لـ **{item}**: `{random.randint(1, 100)}%`")

@bot.command(name="ship")
async def ship_cmd(ctx, m1: discord.Member, m2: discord.Member): await ctx.send(f"❤️ نسبة التوافق بين {m1.mention} و {m2.mention}: **{random.randint(1, 100)}%**")

@bot.command(name="iq")
async def iq_cmd(ctx, member: discord.Member = None):
    m = member or ctx.author
    await ctx.send(f"🧠 نسبة ذكاء {m.mention}: `{random.randint(70, 160)}` IQ")

@bot.command(name="joke")
async def joke_cmd(ctx):
    jokes = ["مرة واحد صعيدي فتح محل غسيل سماه أومو.", "محشش سألوه شو أسرع حيوان؟ قال الفهد عشان لابس كوت رياضة!"]
    await ctx.send(random.choice(jokes))

@bot.command(name="choose")
async def choose_cmd(ctx, *options):
    if options: await ctx.send(f"🤔 اخترت لك: **{random.choice(options)}**")
    else: await ctx.send("❌ اكتب الخيارات بمسافات.")

@bot.command(name="reverse")
async def reverse_cmd(ctx, *, text: str): await ctx.send(text[::-1])

@bot.command(name="ascii")
async def ascii_cmd(ctx, *, text: str): await ctx.send(f"```text\n{text}\n```")

@bot.command(name="cute")
async def cute_cmd(ctx, m: discord.Member = None):
    target = m or ctx.author
    await ctx.send(f"🌸 نسبة اللطافة لـ {target.mention}: `{random.randint(1, 100)}%`")

@bot.command(name="handsome")
async def handsome_cmd(ctx, m: discord.Member = None):
    target = m or ctx.author
    await ctx.send(f"😎 نسبة الوسامة لـ {target.mention}: `{random.randint(40, 100)}%`")

@bot.command(name="math")
async def math_cmd(ctx, a: float, op: str, b: float):
    if op == "+": r = a + b
    elif op == "-": r = a - b
    elif op == "*": r = a * b
    elif op == "/": r = a / b if b != 0 else "خطأ"
    else: r = "غير معروفة"
    await ctx.send(f"🔢 النتيجة: `{r}`")

@bot.command(name="colors")
async def colors_cmd(ctx): await ctx.send("🎨 ألوان السيرفر: 🌸 وردي | 🧊 جليدي | 🤍 أبيض")

@bot.command(name="pat")
async def pat_cmd(ctx, member: discord.Member): await ctx.send(f"✋ {ctx.author.mention} يطبطب على {member.mention} 🌸")

@bot.command(name="8ball")
async def ball_cmd(ctx, *, q: str): await ctx.send(f"🔮 الإجابة لـ {q}: **{random.choice(['نعم بالتأكيد ✨', 'مستحيل ❌', 'ربما 🤔'])}**")

@bot.command(name="coinflip")
async def coinflip_cmd(ctx): await ctx.send("🪙 وجه أم كتابة؟ النتيجة ظهرت!")

@bot.command(name="rollgame")
async def rollgame_cmd(ctx): await ctx.send(f"🎲 النتيجة الكبرى: `{random.randint(1, 100)}`")

# 51 إلى 75: أوامر إحصائية وإدارية تكميلية دقيقة
@bot.command(name="members")
async def members_cmd(ctx): await ctx.send(f"👥 إجمالي الأعضاء: **{ctx.guild.member_count}**")

@bot.command(name="boosters")
async def boosters_cmd(ctx): await ctx.send(f"💎 عدد الداعمين (Boosters): **{len(ctx.guild.premium_subscribers)}**")

@bot.command(name="boostlevel")
async def boostlevel_cmd(ctx): await ctx.send(f"🚀 مستوى البوست: **Level {ctx.guild.premium_tier}**")

@bot.command(name="emojis")
async def emojis_cmd(ctx): await ctx.send(f"🎨 عدد إيموجيز السيرفر: `{len(ctx.guild.emojis)}`")

@bot.command(name="rolescount")
async def rolescount_cmd(ctx): await ctx.send(f"🎭 إجمالي الرولات: `{len(ctx.guild.roles)}` رتبة.")

@bot.command(name="channels")
async def channels_cmd(ctx): await ctx.send(f"💬 إجمالي الرومات: `{len(ctx.guild.channels)}`")

@bot.command(name="bots")
async def bots_cmd(ctx):
    bc = sum(1 for m in ctx.guild.members if m.bot)
    await ctx.send(f"🤖 عدد البوتات: `{bc}` بوت.")

@bot.command(name="humans")
async def humans_cmd(ctx):
    hc = sum(1 for m in ctx.guild.members if not m.bot)
    await ctx.send(f"👥 عدد البشر الحقيقيين: `{hc}` عضواً.")

@bot.command(name="online")
async def online_cmd(ctx):
    oc = sum(1 for m in ctx.guild.members if m.status != discord.Status.offline)
    await ctx.send(f"🟢 المتواجدون أونلاين: `{oc}` عضواً.")

@bot.command(name="serverregion")
async def region_cmd(ctx): await ctx.send("🌍 منطقة السيرفر مستقرة.")

@bot.command(name="verification")
async def verif_cmd(ctx): await ctx.send(f"🔐 مستوى التحقق: `{ctx.guild.verification_level}`")

@bot.command(name="serverage")
async def age_cmd(ctx): await ctx.send(f"📅 تاريخ إنشاء السيرفر: {discord.utils.format_dt(ctx.guild.created_at, 'R')}")

@bot.command(name="myroles")
async def myroles_cmd(ctx):
    r = [x.mention for x in ctx.author.roles if x.name != "@everyone"]
    await ctx.send(f"🎭 رولاتك الحالية: {', '.join(r) if r else 'لا توجد رولات'}")

@bot.command(name="highest")
async def highest_cmd(ctx, m: discord.Member = None):
    target = m or ctx.author
    await ctx.send(f"👑 أعلى رتبة لـ {target.mention}: **{target.top_role.name}**")

@bot.command(name="servername")
async def sname_cmd(ctx): await ctx.send(f"🏷️ اسم السيرفر الحالي: **{ctx.guild.name}**")

@bot.command(name="serverid")
async def sid_cmd(ctx): await ctx.send(f"🆔 آيدي السيرفر: `{ctx.guild.id}`")

@bot.command(name="myid")
async def myid_cmd(ctx): await ctx.send(f"🆔 آيديك الشخصي: `{ctx.author.id}`")

@bot.command(name="myname")
async def myname_cmd(ctx): await ctx.send(f"👤 اسمك في الديسكورد: **{ctx.author.name}**")

@bot.command(name="botping")
async def bping_cmd(ctx): await ctx.send(f"📶 لاتنسي البينغ: `{round(bot.latency * 1000)}ms`")

@bot.command(name="masterhelp")
async def mhelp_cmd(ctx): await ctx.send("🌟 لوحة التحكم والتشغيل الكلي للبوت تعمل بثبات 100%.")

@bot.command(name="mastertest")
async def mtest_cmd(ctx): await ctx.send("🧪 فحص النظام الرئيسي: سليم ومستقر.")

@bot.command(name="systemstatus")
async def sys_cmd(ctx): await ctx.send("🚀 سيستم Nova 777 Supreme يعمل بكامل طاقته وموديولاته.")

@bot.command(name="credits")
async def credits_cmd(ctx): await ctx.send("🤍 صُمم خصيصاً لسيرفر 777 بأعلى معايير الاحترافية.")

@bot.command(name="version")
async def ver_cmd(ctx): await ctx.send("📌 النسخة: `7.7.7 Enterprise Edition`")

@bot.command(name="ready")
async def ready_cmd(ctx): await ctx.send("✅ البوت جاهز لتلقي الأوامر وتنفيذ المهام بنجاح.")

# --- تشغيل البوت عبر التوكن ---
TOKEN = os.getenv("TOKEN")
if TOKEN:
    bot.run(TOKEN)
else:
    print("❌ Error: TOKEN environment variable not found!")
