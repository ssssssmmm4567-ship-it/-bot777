import os
import discord
from discord.ext import commands
from discord.ui import Button, View

intents = discord.Intents.all()
bot = commands.Bot(command_prefix="!", intents=intents, help_command=None)

AUTO_ROLE_NAME = None

@bot.event
async def on_ready():
    print(f"Logged in as {bot.user.name} (ID: {bot.user.id})")
    print("Bot 777 Ultra Pro Edition is Online!")
    await bot.change_presence(activity=discord.Game(name="!help | 777 Server System"))

# --- واجهة المساعدة الاحترافية الفاجرة (Pro Help View) ---
class UltraHelpView(View):
    def __init__(self):
        super().__init__(timeout=180)

    @discord.ui.button(label="AutoRole & Management", style=discord.ButtonStyle.danger, emoji="🛡️")
    async def mod_section(self, interaction: discord.Interaction, button: Button):
        embed = discord.Embed(
            title="🛡️ نظام إدارة الرتب والأوتو رول الاحترافي",
            description="قائمة الأوامر الخاصة بالحماية وإدارة الرتب داخل سيرفر 777:",
            color=0x2b2d31
        )
        embed.add_field(name="`!autorole [رول]`", value="تعيين رتبة الترحيب التلقائية للأعضاء الجدد", inline=False)
        embed.add_field(name="`!daorole`", value="إلغاء وتعطيل رتبة الأوتو رول الحالية", inline=False)
        embed.add_field(name="`!role` / `!addrole` [@عضو] [رول]", value="إضافة رتبة محددة لعضو بعينه", inline=False)
        embed.add_field(name="`!allrole` [رول]", value="إعطاء رتبة معينة لكل أعضاء السيرفر دفعة واحدة", inline=False)
        embed.add_field(name="`!r_all` [رول]", value="إزالة رتبة معينة من جميع أعضاء السيرفر", inline=False)
        embed.add_field(name="`!check` [رول]", value="إحصائية بعدد الأعضاء الذين يمتلكون الرول", inline=False)
        embed.add_field(name="`!clear [العدد]`", value="مسح رسائل الشات بسلاسة وسرعة فائقة", inline=False)
        embed.set_footer(text="777 System • Management Panel", icon_url=interaction.guild.icon.url if interaction.guild.icon else None)
        await interaction.response.edit_message(embed=embed, view=self)

    @discord.ui.button(label="Server & General", style=discord.ButtonStyle.success, emoji="📌")
    async def general_section(self, interaction: discord.Interaction, button: Button):
        embed = discord.Embed(
            title="📌 قسم الأوامر العامة ومعلومات السيرفر",
            description="استعرض معلومات الحسابات وإحصائيات السيرفر بدقة:",
            color=0x2b2d31
        )
        embed.add_field(name="`!server`", value="عرض إحصائيات السيرفر الكاملة (الأعضاء، الأونلاين، الآيدي)", inline=False)
        embed.add_field(name="`!id` [@عضو]", value="عرض بطاقة معلومات العضو والآيدي وتاريخ الانضمام", inline=False)
        embed.add_field(name="`!avatar` [@عضو]", value="عرض صورة الأفاتار الشخصية بجودة فائقة", inline=False)
        embed.add_field(name="`!banner` [@عضو]", value="عرض البنر الشخصي للحساب", inline=False)
        embed.set_footer(text="777 System • General Commands", icon_url=interaction.guild.icon.url if interaction.guild.icon else None)
        await interaction.response.edit_message(embed=embed, view=self)

    @discord.ui.button(label="Images & Filters", style=discord.ButtonStyle.secondary, emoji="🎨")
    async def image_section(self, interaction: discord.Interaction, button: Button):
        embed = discord.Embed(
            title="🎨 قسم الفلاتر وتعديل الصور",
            description="أدوات التجميل وتعديل المظهر البصري:",
            color=0x2b2d31
        )
        embed.add_field(name="`!circle` [@عضو]", value="عرض الصورة الشخصية على شكل دائرة أنيقة", inline=False)
        embed.add_field(name="`!colors`", value="استعراض علبة الألوان المتاحة في السيرفر", inline=False)
        embed.set_footer(text="777 System • Visuals & Fun", icon_url=interaction.guild.icon.url if interaction.guild.icon else None)
        await interaction.response.edit_message(embed=embed, view=self)

@bot.command(name="help")
async def help_command(ctx):
    embed = discord.Embed(
        title="🌟 لوحة التحكم والتحليل المركزية - سيرفر 777",
        description="مرحباً بك في النظام الاحترافي المطور.\nاختر القسم المطلوب من الأزرار بالأسفل لتصفح الأوامر المتاحة:",
        color=0x2b2d31
    )
    if ctx.guild.icon:
        embed.set_thumbnail(url=ctx.guild.icon.url)
    embed.set_footer(text=f"Requested by {ctx.author.name}", icon_url=ctx.author.display_avatar.url)
    view = UltraHelpView()
    await ctx.send(embed=embed, view=view)

# --- أمر السيرفر الفاجر (بنفس ستايل ونظام نوفا بالضبط) ---
@bot.command()
async def server(ctx):
    s = ctx.guild
    online_count = sum(1 for m in s.members if m.status != discord.Status.offline)
    
    embed = discord.Embed(title=s.name, color=0x2b2d31)
    if s.icon:
        embed.set_thumbnail(url=s.icon.url)
        
    embed.add_field(name="🆔 Server ID", value=f"`{s.id}`", inline=False)
    embed.add_field(name="👑 Owned By", value=f"{s.owner.mention if s.owner else 'Unknown'}", inline=False)
    embed.add_field(name="📅 Server Age", value=f"{discord.utils.format_dt(s.created_at, 'R')}", inline=False)
    embed.add_field(name="👥 Members", value=f"**Total:** {s.member_count} | **Online:** {online_count}", inline=False)
    embed.add_field(name="💬 Channels", value=f"Text: {len(s.text_channels)} | Voice: {len(s.voice_channels)}", inline=False)
    embed.add_field(name="🎭 Roles", value=f"{len(s.roles)}", inline=False)
    
    embed.set_footer(text="777 System • Server Statistics")
    await ctx.send(embed=embed)

# --- أمر الآيدي الاحترافي الفخم ---
@bot.command(name="id", aliases=["profile", "user"])
async def user_id(ctx, member: discord.Member = None):
    member = member or ctx.author
    embed = discord.Embed(title=f"User Profile: {member.name}", color=0x2b2d31)
    embed.set_thumbnail(url=member.display_avatar.url)
    embed.add_field(name="🆔 User ID", value=f"`{member.id}`", inline=False)
    embed.add_field(name="📅 Discord Join Date", value=f"{discord.utils.format_dt(member.created_at, 'R')}", inline=False)
    embed.add_field(name="📥 Server Join Date", value=f"{discord.utils.format_dt(member.joined_at, 'R') if member.joined_at else 'Unknown'}", inline=False)
    embed.set_footer(text="777 System • User Card")
    await ctx.send(embed=embed)

# --- أوامر الإدارة والرتب الفاجرة ---
@bot.command()
@commands.has_permissions(manage_roles=True)
async def role(ctx, member: discord.Member, role: discord.Role):
    await member.add_roles(role)
    embed = discord.Embed(title="✨ Role Updated", description=f"تم إعطاء الرتبة `{role.name}` بنجاح إلى العضو `{member.name}`.", color=0x00FF00)
    await ctx.send(embed=embed)

@bot.command()
@commands.has_permissions(manage_roles=True)
async def addrole(ctx, member: discord.Member, role: discord.Role):
    await member.add_roles(role)
    embed = discord.Embed(title="✨ Role Added", description=f"تم إضافة الرتبة `{role.name}` لـ `{member.name}`.", color=0x00FF00)
    await ctx.send(embed=embed)

@bot.command()
@commands.has_permissions(manage_roles=True)
async def allrole(ctx, role: discord.Role):
    msg = await ctx.send("⏳ جاري منح الرتبة لجميع الأعضاء، يرجى الانتظار...")
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
    msg = await ctx.send("⏳ جاري إزالة الرتبة من جميع الأعضاء...")
    count = 0
    for member in ctx.guild.members:
        if role in member.roles:
            try:
                await member.remove_roles(role)
                count += 1
            except:
                pass
    await msg.edit(content=f"🗑️ تم إزالة الرتبة `{role.name}` من `{count}` عضواً.")

@bot.command()
@commands.has_permissions(manage_roles=True)
async def check(ctx, role: discord.Role):
    c = len([m for m in ctx.guild.members if role in m.roles])
    embed = discord.Embed(title=f"🔍 Role Check: {role.name}", description=f"عدد الأعضاء الذين يمتلكون هذه الرتبة حالياً: **{c}** عضو.", color=0x2b2d31)
    await ctx.send(embed=embed)

@bot.command()
@commands.has_permissions(manage_messages=True)
async def clear(ctx, amount: int):
    await ctx.channel.purge(limit=amount + 1)
    msg = await ctx.send(f"🧹 تم بنجاح مسح `{amount}` رسالة.")
    await msg.delete(delay=3)

# --- إدارة الأوتو رول ---
@bot.command()
@commands.has_permissions(manage_roles=True)
async def autorole(ctx, role: discord.Role):
    global AUTO_ROLE_NAME
    AUTO_ROLE_NAME = role.name
    embed = discord.Embed(title="🛡️ AutoRole System", description=f"✅ تم تفعيل الأوتو رول بنجاح! الرتبة التلقائية للأعضاء الجدد: **{role.name}**", color=0x00FF00)
    await ctx.send(embed=embed)

@bot.command()
@commands.has_permissions(manage_roles=True)
async def daorole(ctx):
    global AUTO_ROLE_NAME
    AUTO_ROLE_NAME = None
    embed = discord.Embed(title="🛡️ AutoRole System", description="❌ تم إلغاء وتعطيل الأوتو رول التلقائي.", color=0xFF0000)
    await ctx.send(embed=embed)

# --- الأوامر العامة والصور ---
@bot.command()
async def avatar(ctx, member: discord.Member = None):
    member = member or ctx.author
    embed = discord.Embed(title=f"Avatar: {member.name}", color=0x2b2d31)
    embed.set_image(url=member.display_avatar.url)
    await ctx.send(embed=embed)

@bot.command()
async def banner(ctx, member: discord.Member = None):
    member = member or ctx.author
    user_obj = await bot.fetch_user(member.id)
    if user_obj.banner:
        embed = discord.Embed(title=f"Banner: {member.name}", color=0x2b2d31)
        embed.set_image(url=user_obj.banner.url)
        await ctx.send(embed=embed)
    else:
        await ctx.send("❌ هذا العضو ليس لديه بنر مخصص!")

@bot.command()
async def circle(ctx, member: discord.Member = None):
    member = member or ctx.author
    embed = discord.Embed(title=f"Circle Avatar: {member.name}", color=0x2b2d31)
    embed.set_image(url=member.display_avatar.url)
    await ctx.send(embed=embed)

@bot.command()
async def colors(ctx):
    embed = discord.Embed(title="🎨 Color Palette • 777", description="🌸 Pink | 🧊 Ice Blue | 🤍 White | ✨ Gold", color=0x2b2d31)
    await ctx.send(embed=embed)

# --- ترحيب وأوتو رول تلقائي ---
@bot.event
async def on_member_join(member):
    ch = discord.utils.get(member.guild.text_channels, name="welcome") or member.guild.system_channel
    if ch:
        embed = discord.Embed(
            title="🌸 New Member Arrived!",
            description=f"أهلاً بك يا {member.mention} في عائلتنا بـ سيرفر 777، نتمنى لك أوقاتاً ممتعة معنا!",
            color=0x2b2d31
        )
        embed.set_thumbnail(url=member.display_avatar.url)
        embed.set_footer(text=f"Member Count: {member.guild.member_count}")
        await ch.send(embed=embed)
        
    global AUTO_ROLE_NAME
    if AUTO_ROLE_NAME:
        r = discord.utils.get(member.guild.roles, name=AUTO_ROLE_NAME)
        if r:
            try:
                await member.add_roles(r)
            except:
                pass

TOKEN = os.getenv("TOKEN")
bot.run(TOKEN)
