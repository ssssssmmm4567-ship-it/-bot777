import discord
from discord.ext import commands
import datetime
import random

# ==========================================
# 1. إعداد الصلاحيات والبادئة
# ==========================================
intents = discord.Intents.default()
intents.message_content = True
intents.members = True

bot = commands.Bot(command_prefix="!", intents=intents, help_command=None)

# ==========================================
# 2. نظام الردود التلقائية (Auto-Responder)
# ==========================================
@bot.event
async def on_message(message):
    # تجاهل رسائل البوتات عشان ميعملوش تكرار
    if message.author.bot:
        return

    # تحويل النص لحروف صغيرة عشان البحث يكون سهل
    content = message.content.lower()

    # قائمة الردود التلقائية
    if "السلام عليكم" in content or "السلام عليڪم" in content:
        await message.reply("وعليكم السلام ورحمة الله وبركاته يا هلا بيك منور سيرفر 777! 🤍")
    
    elif content == "سلام":
        await message.reply("وعليكم السلام يا غالي! نورتنا ✨")

    elif "لينك" in content or "رابط" in content:
        await message.reply("🔗 ممنوع نشر الروابط هنا حفاظاً على أمان سيرفر 777! لو محتاج مساعدة كلم الإدارة.")

    elif "بوت" in content:
        await message.reply("أنا بوت سيرفر 777 الذكي، تحت أمرك في أي وقت! 🤖✨")

    elif "ازيك" in content or "عامل ايه" in content:
        await message.reply("الحمد لله تمام بشوفتك يا جميل! إزاي أقدر أساعدك في سيرفر 777 اليوم؟ 🌸")

    # ضروري جداً عشان باقي الأوامر تشتغل
    await bot.process_commands(message)

# ==========================================
# 3. أحداث التشغيل والترحيب المتقدم
# ==========================================
@bot.event
async def on_ready():
    print(f"==========================================")
    print(f"✨ تم تشغيل بوت سيرفر 777 بنجاح تام!")
    print(f"==========================================")
    activity = discord.Streaming(name="777 Community | !help", url="https://www.twitch.tv/discord")
    await bot.change_presence(status=discord.Status.online, activity=activity)

@bot.event
async def on_member_join(member):
    channel = discord.utils.get(member.guild.text_channels, name="welcome")
    if channel:
        embed = discord.Embed(
            title="🤍 أهلاً بك في عائلة 777 🤍",
            description=f"أنرت السيرفر بوجودك يا {member.mention}!
نتمنى لك أقوى أوقات ممتعة معنا ✨",
            color=0xFF69B4,
            timestamp=datetime.datetime.utcnow()
        )
        embed.set_thumbnail(url=member.display_avatar.url)
        embed.add_field(name="👥 رتبتك بيننا:", value=f"أنت العضو رقم **{member.guild.member_count}**", inline=True)
        embed.set_footer(text="777 Server Management", icon_url=member.guild.icon.url if member.guild.icon else None)
        await channel.send(embed=embed)

# ==========================================
# 4. الأزرار التفاعلية لقائمة المساعدة
# ==========================================
class HelpView(discord.ui.View):
    def __init__(self):
        super().__init__(timeout=None)

    @discord.ui.button(label="أوامر الإدارة", style=discord.ButtonStyle.danger, emoji="🛡️")
    async def mod_help(self, interaction: discord.Interaction, button: discord.ui.Button):
        embed = discord.Embed(
            title="🛡️ أوامر الإدارة والتحكم",
            description="`!clear [عدد]` - مسح الرسائل\n`!kick [@عضو]` - طرد عضو\n`!ban [@عضو]` - حظر عضو\n`!mute [@عضو]` - إسكات عضو\n`!unmute [@عضو]` - إزالة الإسكات",
            color=0xFF0000
        )
        await interaction.response.send_message(embed=embed, ephemeral=True)

    @discord.ui.button(label="الأوامر العامة", style=discord.ButtonStyle.primary, emoji="✨")
    async def general_help(self, interaction: discord.Interaction, button: discord.ui.Button):
        embed = discord.Embed(
            title="✨ الأوامر العامة والمعلومات",
            description="`!ping` - فحص سرعة البوت\n`!userinfo [@عضو]` - ملف العضو الشخصي\n`!serverinfo` - معلومات سيرفر 777\n`!avatar [@عضو]` - إظهار صورة البروفايل",
            color=0x00FF00
        )
        await interaction.response.send_message(embed=embed, ephemeral=True)

    @discord.ui.button(label="أوامر الترفيه والألعاب", style=discord.ButtonStyle.success, emoji="🎮")
    async def fun_help(self, interaction: discord.Interaction, button: discord.ui.Button):
        embed = discord.Embed(
            title="🎮 الألعاب والترفيه",
            description="`!say [نص]` - جعل البوت يردد كلامك\n`!roll` - رمي النرد (رقم عشوائي)\n`!flip` - صرة أو كتابة (Coinflip)\n`!rate [@عضو]` - نسبة الحب أو التوافق عشوائياً",
            color=0xF1C40F
        )
        await interaction.response.send_message(embed=embed, ephemeral=True)

# ==========================================
# 5. أوامر البوت الكاملة
# ==========================================

@bot.command(name="help")
async def help_command(ctx):
    embed = discord.Embed(
        title="✨ مركز أوامر سيرفر 777 الشامل ✨",
        description="اضغط على الأزرار في الأسفل لتصفح جميع الأوامر المتاحة بكل اقسامها:",
        color=0x7289DA
    )
    embed.set_thumbnail(url=bot.user.display_avatar.url)
    await ctx.send(embed=embed, view=HelpView())

@bot.command(name="ping")
async def ping(ctx):
    latency = round(bot.latency * 1000)
    embed = discord.Embed(title="🏓 Pong!", description=f"سرعة استجابة سيرفر البوت: **{latency}ms**", color=0x57F287)
    await ctx.send(embed=embed)

@bot.command(name="clear")
@commands.has_permissions(manage_messages=True)
async def clear(ctx, amount: int = 5):
    await ctx.channel.purge(limit=amount + 1)
    msg = await ctx.send(f"🧹 تم بنجاح مسح **{amount}** رسالة!")
    await discord.utils.sleep_until(datetime.datetime.utcnow() + datetime.timedelta(seconds=3))
    await msg.delete()

@bot.command(name="kick")
@commands.has_permissions(kick_members=True)
async def kick(ctx, member: discord.Member, *, reason="بدون سبب"):
    await member.kick(reason=reason)
    await ctx.send(f"🚪 تم طرد العضو **{member.display_name}** بنجاح. السبب: {reason}")

@bot.command(name="ban")
@commands.has_permissions(ban_members=True)
async def ban(ctx, member: discord.Member, *, reason="بدون سبب"):
    await member.ban(reason=reason)
    await ctx.send(f"⛔ تم حظر العضو **{member.display_name}** نهائياً. السبب: {reason}")

@bot.command(name="userinfo")
async def userinfo(ctx, member: discord.Member = None):
    member = member or ctx.author
    roles = [role.mention for role in member.roles[1:]] or ["لا توجد رتب"]
    embed = discord.Embed(title=f"معلومات المستخدم: {member.display_name}", color=member.color)
    embed.set_thumbnail(url=member.display_avatar.url)
    embed.add_field(name="الاسم الحقيقي:", value=member.name, inline=True)
    embed.add_field(name="الآيدي:", value=member.id, inline=True)
    embed.add_field(name="تاريخ الانضمام للسيرفر:", value=member.joined_at.strftime("%Y-%m-%d"), inline=False)
    embed.add_field(name="الرتب:", value=", ".join(roles), inline=False)
    await ctx.send(embed=embed)

@bot.command(name="serverinfo")
async def serverinfo(ctx):
    guild = ctx.guild
    embed = discord.Embed(title=f"📊 إحصائيات سيرفر 777", color=0x9B59B6)
    if guild.icon:
        embed.set_thumbnail(url=guild.icon.url)
    embed.add_field(name="اسم السيرفر:", value=guild.name, inline=True)
    embed.add_field(name="صاحب السيرفر:", value=guild.owner.mention, inline=True)
    embed.add_field(name="عدد الأعضاء الكلي:", value=f"**{guild.member_count}** عضو", inline=True)
    embed.add_field(name="عدد الرومات:", value=len(guild.channels), inline=True)
    await ctx.send(embed=embed)

@bot.command(name="avatar")
async def avatar(ctx, member: discord.Member = None):
    member = member or ctx.author
    embed = discord.Embed(title=f"🖼️ صورة بروفايل: {member.name}", color=0x3498DB)
    embed.set_image(url=member.display_avatar.url)
    await ctx.send(embed=embed)

@bot.command(name="say")
async def say(ctx, *, text: str):
    await ctx.message.delete()
    await ctx.send(text)

@bot.command(name="flip")
async def flip(ctx):
    result = random.choice(["🪙 صرة (Heads)", "🪙 كتابة (Tails)"])
    await ctx.send(f"النتيجة طلعت: **{result}**")

@bot.command(name="rate")
async def rate(ctx, member: discord.Member):
    percentage = random.randint(0, 100)
    await ctx.send(f"💖 نسبة التوافق بين {ctx.author.mention} و {member.mention} هي: **{percentage}%**")

# ==========================================
# 6. معالجة الأخطاء
# ==========================================
@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.MissingPermissions):
        await ctx.send("❌ عذراً، لا تمتلك الصلاحيات الكافية لاستخدام هذا الأمر!")
    elif isinstance(error, commands.MissingRequiredArgument):
        await ctx.send("⚠️ يرجى كتابة كافة تفاصيل الأمر بشكل صحيح.")

# ==========================================
# 7. تشغيل البوت عبر متغير البيئة (Railway)
# ==========================================
import os
TOKEN = os.getenv("TOKEN")
bot.run(TOKEN)
