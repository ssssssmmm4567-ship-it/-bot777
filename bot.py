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
    print("Bot 777 is Online and Ready!")
    await bot.change_presence(activity=discord.Game(name="!help | 777 Server"))

class AdvancedHelpView(View):
    def __init__(self):
        super().__init__(timeout=180)

    @discord.ui.button(label="أوامر الرتب والأوتو رول", style=discord.ButtonStyle.primary, emoji="🛡️")
    async def roles_help(self, interaction: discord.Interaction, button: Button):
        embed = discord.Embed(title="🛡️ قسم إدارة الرتب والأوتو رول المتقدم", color=0xFF69B4)
        embed.add_field(name="`!autorole [رول]`", value="تحديد رتبة تلقائية للأعضاء الجدد", inline=False)
        embed.add_field(name="`!daorole`", value="إلغاء رتبة الأوتو رول", inline=False)
        embed.add_field(name="`!role` / `!addrole` [عضو] [رول]", value="إضافة رتبة لعضو", inline=False)
        embed.add_field(name="`!allrole` [رول]", value="إعطاء رول لجميع الأعضاء دفعة واحدة", inline=False)
        embed.add_field(name="`!r_all` [رول]", value="إزالة رول من جميع الأعضاء", inline=False)
        embed.add_field(name="`!check` [رول]", value="عرض عدد الأعضاء الذين يمتلكون الرول", inline=False)
        embed.set_footer(text="سيرفر 777")
        await interaction.response.edit_message(embed=embed, view=self)

    @discord.ui.button(label="الأوامر العامة", style=discord.ButtonStyle.success, emoji="📌")
    async def general_help(self, interaction: discord.Interaction, button: Button):
        embed = discord.Embed(title="📌 الأوامر العامة ومعلومات السيرفر", color=0x87CEEB)
        embed.add_field(name="`!avatar` [@عضو]", value="عرض الأفاتار", inline=False)
        embed.add_field(name="`!banner` [@عضو]", value="عرض البنر", inline=False)
        embed.add_field(name="`!server`", value="معلومات السيرفر", inline=False)
        embed.add_field(name="`!id` [@عضو]", value="معلومات الحساب والآيدي", inline=False)
        embed.set_footer(text="سيرفر 777")
        await interaction.response.edit_message(embed=embed, view=self)

    @discord.ui.button(label="تعديل الصور", style=discord.ButtonStyle.secondary, emoji="🎨")
    async def image_help(self, interaction: discord.Interaction, button: Button):
        embed = discord.Embed(title="🎨 الفلاتر وتعديل الصور", color=0xFFB6C1)
        embed.add_field(name="`!colors`", value="عرض علبة الألوان", inline=False)
        embed.add_field(name="`!circle` [@عضو]", value="صورة دائرية", inline=False)
        embed.set_footer(text="سيرفر 777")
        await interaction.response.edit_message(embed=embed, view=self)

@bot.command(name="help")
async def help_command(ctx):
    embed = discord.Embed(
        title="🌟 لوحة المساعدة - بوت سيرفر 777",
        description="اختر القسم المطلوب من الأزرار بالأسفل:",
        color=0xFF69B4
    )
    view = AdvancedHelpView()
    await ctx.send(embed=embed, view=view)

@bot.command()
async def avatar(ctx, member: discord.Member = None):
    member = member or ctx.author
    embed = discord.Embed(title=f"أفاتار {member.name}", color=0xFF69B4)
    embed.set_image(url=member.display_avatar.url)
    await ctx.send(embed=embed)

@bot.command()
async def banner(ctx, member: discord.Member = None):
    member = member or ctx.author
    user_obj = await bot.fetch_user(member.id)
    if user_obj.banner:
        embed = discord.Embed(title=f"بنر {member.name}", color=0xFF69B4)
        embed.set_image(url=user_obj.banner.url)
        await ctx.send(embed=embed)
    else:
        await ctx.send("❌ هذا العضو ليس لديه بنر!")

@bot.command()
async def server(ctx):
    s = ctx.guild
    embed = discord.Embed(title=f"سيرفر {s.name}", color=0x87CEEB)
    embed.add_field(name="الأعضاء", value=s.member_count)
    embed.add_field(name="المالك", value=s.owner)
    await ctx.send(embed=embed)

@bot.command()
async def id(ctx, member: discord.Member = None):
    member = member or ctx.author
    embed = discord.Embed(title=f"معلومات {member.name}", color=0xFFB6C1)
    embed.add_field(name="ID", value=member.id)
    await ctx.send(embed=embed)

@bot.command()
@commands.has_permissions(manage_roles=True)
async def role(ctx, member: discord.Member, role: discord.Role):
    await member.add_roles(role)
    await ctx.send(f"✨ تم إعطاء الرتبة `{role.name}` لـ `{member.name}`.")

@bot.command()
@commands.has_permissions(manage_roles=True)
async def addrole(ctx, member: discord.Member, role: discord.Role):
    await member.add_roles(role)
    await ctx.send(f"✅ تم إضافة `{role.name}` لـ `{member.name}`.")

@bot.command()
@commands.has_permissions(manage_roles=True)
async def allrole(ctx, role: discord.Role):
    count = 0
    for member in ctx.guild.members:
        if role not in member.roles:
            try:
                await member.add_roles(role)
                count += 1
            except:
                pass
    await ctx.send(f"✅ تم إعطاء الرتبة لـ `{count}` عضواً!")

@bot.command(name="r_all")
@commands.has_permissions(manage_roles=True)
async def r_all(ctx, role: discord.Role):
    count = 0
    for member in ctx.guild.members:
        if role in member.roles:
            try:
                await member.remove_roles(role)
                count += 1
            except:
                pass
    await ctx.send(f"🗑️ تم إزالة الرتبة من `{count}` عضواً.")

@bot.command()
@commands.has_permissions(manage_roles=True)
async def check(ctx, role: discord.Role):
    c = len([m for m in ctx.guild.members if role in m.roles])
    await ctx.send(f"🔍 عدد الأعضاء برتبة `{role.name}` هو: **{c}**")

@bot.command()
@commands.has_permissions(manage_roles=True)
async def autorole(ctx, role: discord.Role):
    global AUTO_ROLE_NAME
    AUTO_ROLE_NAME = role.name
    await ctx.send(f"✅ تم ضبط الأوتو رول على: `{role.name}`")

@bot.command()
@commands.has_permissions(manage_roles=True)
async def daorole(ctx):
    global AUTO_ROLE_NAME
    AUTO_ROLE_NAME = None
    await ctx.send("❌ تم إلغاء الأوتو رول.")

@bot.command()
async def circle(ctx, member: discord.Member = None):
    member = member or ctx.author
    embed = discord.Embed(title=f"صورة دائرية لـ {member.name}", color=0xFF69B4)
    embed.set_image(url=member.display_avatar.url)
    await ctx.send(embed=embed)

@bot.command()
async def colors(ctx):
    await ctx.send("🎨 الألوان المتاحة: Pink | Ice Blue | White | Gold")

@bot.event
async def on_member_join(member):
    ch = discord.utils.get(member.guild.text_channels, name="welcome") or member.guild.system_channel
    if ch:
        embed = discord.Embed(title="🌸 نورت السيرفر!", description=f"أهلاً بك يا {member.mention}", color=0xFF69B4)
        embed.set_thumbnail(url=member.display_avatar.url)
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
