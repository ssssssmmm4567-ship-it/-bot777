import os
import discord
from discord.ext import commands
from discord.ui import Button, View

# إعداد البوت مع الأنتنتس الكاملة
intents = discord.Intents.all()
bot = commands.Bot(command_prefix="!", intents=intents, help_command=None)

# متغير لحفظ رتبة الأوتو رول داخل الذاكرة
AUTO_ROLE_NAME = None

@bot.event
async def on_ready():
    print(f"Logged in as {bot.user.name} (ID: {bot.user.id})")
    print("Bot 777 is Online in a single file and Fully Operational!")
    await bot.change_presence(activity=discord.Game(name="!help | 777 Server"))

# ----------------- قائمة المساعدة التفاعلية (Help View) -----------------
class AdvancedHelpView(View):
    def __init__(self):
        super().__init__(timeout=180)

    @discord.ui.button(label="أوامر الرتب والأوتو رول", style=discord.ButtonStyle.primary, emoji="🛡️")
    async def roles_help(self, interaction: discord.Interaction, button: Button):
        embed = discord.Embed(title="🛡️ قسم إدارة الرتب والأوتو رول المتقدم", color=0xFF69B4)
        embed.add_field(name="`!autorole [رول]`", value="تحديد رتبة تلقائية يتم إعطاؤها للأعضاء عند دخولهم السيرفر", inline=False)
        embed.add_field(name="`!daorole`", value="إلغاء وتعطيل رتبة الأوتو رول الحالية", inline=False)
        embed.add_field(name="`!role` / `!addrole` [عضو] [رول]", value="إضافة رتبة محددة لعضو معين بإشراف كامل", inline=False)
        embed.add_field(name="`!allrole` [رول]", value="إعطاء رول معين لجميع أعضاء السيرفر دفعة واحدة", inline=False)
        embed.add_field(name="`!r_all` [رول]", value="إزالة رول معين من جميع أعضاء السيرفر", inline=False)
        embed.add_field(name="`!check` [رول]", value="عرض إحصائية دقيقة لعدد الأعضاء الذين يمتلكون الرول", inline=False)
        embed.set_footer(text="سيرفر 777 | لوحة تحكم الرتب الاحترافية")
        await interaction.response.edit_message(embed=embed, view=self)

    @discord.ui.button(label="الأوامر العامة والدعوات", style=discord.ButtonStyle.success, emoji="📌")
    async def general_help(self, interaction: discord.Interaction, button: Button):
        embed = discord.Embed(title="📌 قسم الأوامر العامة والمعلومات", color=0x87CEEB)
        embed.add_field(name="`!avatar` [@عضو]", value="عرض صورة الأفاتار الخاصة بك أو بأي عضو بجودة عالية", inline=False)
        embed.add_field(name="`!banner` [@عضو]", value="عرض البنر (الغلاف) الخاص بالحساب الشخصي", inline=False)
        embed.add_field(name="`!server`", value="عرض معلومات وإحصائيات سيرفر 777 الكاملة", inline=False)
        embed.add_field(name="`!id` [@عضو]", value="عرض آيدي الحساب وتاريخ الإنشاء والانضمام للديسكورد", inline=False)
        embed.set_footer(text="سيرفر 777 | الأوامر العامة")
        await interaction.response.edit_message(embed=embed, view=self)

    @discord.ui.button(label="تعديل الصور والفلاتر", style=discord.ButtonStyle.secondary, emoji="🎨")
    async def image_help(self, interaction: discord.Interaction, button: Button):
        embed = discord.Embed(title="🎨 قسم الفلاتر، وتعديل الصور والألوان", color=0xFFB6C1)
        embed.add_field(name="`!colors`", value="فتح علبة الألوان المتاحة في السيرفر واختيار لونك", inline=False)
        embed.add_field(name="`!circle` [@عضو]", value="تعديل وعرض صورة العضو على شكل دائرة أنيقة", inline=False)
        embed.set_footer(text="سيرفر 777 | الفلاتر والترفيه")
        await interaction.response.edit_message(embed=embed, view=self)

# ----------------- أمر المساعدة الرئيسي (Help) -----------------
@bot.command(name="help")
async def help_command(ctx):
    embed = discord.Embed(
        title="🌟 لوحة المساعدة الرسمية - بوت سيرفر 777",
        description="أهلاً بك يا فنانة في لوحة التحكم المركزية! استخدم الأزرار بالأسفل للتنقل بين الأقسام بكل سهولة واحترافية:",
        color=0xFF69B4
    )
    if ctx.guild.icon:
        embed.set_thumbnail(url=ctx.guild.icon.url)
    embed.set_footer(text="777 Bot • Powered by Railway & GitHub")
    view = AdvancedHelpView()
    await ctx.send(embed=embed, view=view)

# ----------------- الأوامر العامة -----------------
@bot.command()
async def avatar(ctx, member: discord.Member = None):
    member = member or ctx.author
    embed = discord.Embed(title=f"✨ أفاتار العضو: {member.name}", color=0xFF69B4)
    embed.set_image(url=member.display_avatar.url)
    embed.set_footer(text=f"طلب بواسطة {ctx.author.name}")
    await ctx.send(embed=embed)

@bot.command()
async def banner(ctx, member: discord.Member = None):
    member = member or ctx.author
    user_obj = await bot.fetch_user(member.id)
    if user_obj.banner:
        embed = discord.Embed(title=f"🎨 بنر العضو: {member.name}", color=0xFF69B4)
        embed.set_image(url=user_obj.banner.url)
        await ctx.send(embed=embed)
    else:
        await ctx.send("❌ عذراً، هذا العضو ليس لديه بنر مخصص لحسابه!")

@bot.command()
async def server(ctx):
    s = ctx.guild
    embed = discord.Embed(title=f"📊 إحصائيات سيرفر {s.name}", color=0x87CEEB)
    embed.add_field(name="👑 صاحب السيرفر", value=s.owner, inline=True)
    embed.add_field(name="👥 عدد الأعضاء", value=s.member_count, inline=True)
    embed.add_field(name="📅 تاريخ الإنشاء", value=s.created_at.strftime("%Y-%m-%d"), inline=True)
    if s.icon:
        embed.set_thumbnail(url=s.icon.url)
    await ctx.send(embed=embed)

@bot.command()
async def id(ctx, member: discord.Member = None):
    member = member or ctx.author
    embed = discord.Embed(title=f"🆔 معلومات حساب: {member.name}", color=0xFFB6C1)
    embed.add_field(name="الآيدي (ID)", value=member.id, inline=False)
    embed.add_field(name="تاريخ الانضمام للديسكورد", value=member.created_at.strftime("%Y-%m-%d"), inline=False)
    embed.set_thumbnail(url=member.display_avatar.url)
    await ctx.send(embed=embed)

# ----------------- أوامر الرتب والإدارة -----------------
@bot.command()
@commands.has_permissions(manage_roles=True)
async def role(ctx, member: discord.Member, role: discord.Role):
    await member.add_roles(role)
    await ctx.send(f"✨ تم بنجاح إعطاء الرتبة `{role.name}` للعضو `{member.name}`.")

@bot.command()
@commands.has_permissions(manage_roles=True)
async def addrole(ctx, member: discord.Member, role: discord.Role):
    await member.add_roles(role)
    await ctx.send(f"✅ تم إضافة الرتبة `{role.name}` إلى `{member.name}`.")

@bot.command()
@commands.has_permissions(manage_roles=True)
async def allrole(ctx, role: discord.Role):
    msg = await ctx.send(f"⏳ جاري إعطاء الرتبة `{role.name}` لجميع الأعضاء... أرجو الانتظار.")
    count = 0
    for member in ctx.guild.members:
        if role not in member.roles:
            try:
                await member.add_roles(role)
                count += 1
            except:
                pass
    await msg.edit(content=f"✅ تم بنجاح إعطاء الرتبة `{role.name}` لـ `{count}` عضواً!")

@bot.command(name="r_all")
@commands.has_permissions(manage_roles=True)
async def r_all(ctx, role: discord.Role):
    msg = await ctx.send(f"⏳ جاري إزالة الرتبة `{role.name}` من جميع الأعضاء...")
    count = 0
    for member in ctx.guild.members:
        if role in member.roles:
            try:
                await member.remove_roles(role)
                count += 1
            except:
                pass
    await msg.edit(content=f"🗑️ تم بنجاح إزالة الرتبة `{role.name}` من `{count}` عضواً.")

@bot.command()
@commands.has_permissions(manage_roles=True)
async def check(ctx, role: discord.Role):
    members_count = len([m for m in ctx.guild.members if role in m.roles])
    embed = discord.Embed(title=f"🔍 إحصائية رتبة: {role.name}", description=f"عدد الأعضاء الذين يمتلكون هذه الرتبة حالياً هو: **{members_count}** عضو.", color=0xFF69B4)
    await ctx.send(embed=embed)

# ----------------- أوامر إدارة الأوتو رول -----------------
@bot.command()
@commands.has_permissions(manage_roles=True)
async def autorole(ctx, role: discord.Role):
    global AUTO_ROLE_NAME
    AUTO_ROLE_NAME = role.name
    embed = discord.Embed(title="🛡️ نظام الأوتو رول", description=f"✅ تم تفعيل الأوتو رول بنجاح! الرتبة التلقائية الجديدة للأعضاء الجدد هي: **{role.name}**", color=0x00FF00)
    await ctx.send(embed=embed)

@bot.command()
@commands.has_permissions(manage_roles=True)
async def daorole(ctx):
    global AUTO_ROLE_NAME
    AUTO_ROLE_NAME = None
    embed = discord.Embed(title="🛡️ نظام الأوتو رول", description="❌ تم إلغاء وتعطيل رتبة الأوتو رول التلقائية بنجاح.", color=0xFF0000)
    await ctx.send(embed=embed)

# ----------------- أوامر تعديل الصور -----------------
@bot.command()
async def circle(ctx, member: discord.Member = None):
    member = member or ctx.author
    embed = discord.Embed(title=f"⚪ الصورة الدائرية لـ {member.name}", color=0xFF69B4)
    embed.set_image(url=member.display_avatar.url)
    await ctx.send(embed=embed)

@bot.command()
async def colors(ctx):
    embed = discord.Embed(title="🎨 علبة الألوان لسيرفر 777", description="اختر لونك المفضل للتنسيق!", color=0xFFB6C1)
    embed.add_field(name="الألوان المتاحة", value="🌸 Pink | 🧊 Ice Blue | 🤍 White | ✨ Gold", inline=False)
    await ctx.send(embed=embed)

# ----------------- الحدث التلقائي: دخول عضو جديد -----------------
@bot.event
async def on_member_join(member):
    # 1. إرسال ترحيب
    welcome_channel = discord.utils.get(member.guild.text_channels, name="welcome") or member.guild.system_channel
    if welcome_channel:
        embed = discord.Embed(
            title="🌸 عضو جديد أنار سيرفر 777!",
            description=f"أهلاً بك يا {member.mention} في عائلتنا، نتمنى لك قضاء أوقات ممتعة معنا!",
            color=0xFF69B4
        )
        embed.set_thumbnail(url=member.display_avatar.url)
        embed.set_footer(text=f"رقم العضو: {member.guild.member_count}")
        await welcome_channel.send(embed=embed)
    
    # 2. إعطاء الأوتو رول لو متفعلة
    global AUTO_ROLE_NAME
    if AUTO_ROLE_NAME:
        role_obj = discord.utils.get(member.guild.roles, name=AUTO_ROLE_NAME)
        if role_obj:
            try:
                await member.add_roles(role_obj)
            except Exception as e:
                print(f"Failed to assign auto role: {e}")

# تشغيل البوت بأمان
TOKEN = os.getenv("TOKEN")
bot.run(TOKEN)
