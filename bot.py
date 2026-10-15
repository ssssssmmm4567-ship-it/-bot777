import os
import discord
from discord.ext import commands
from discord.ui import Button, View
import random

intents = discord.Intents.all()

class NovaSupremeBot(commands.Bot):
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
        print("✅ [NOVA SYSTEM] All 150+ Commands Synchronized!")

bot = NovaSupremeBot()

@bot.event
async def on_ready():
    print(f"-----------------------------------")
    print(f"🚀 Nova Bot Active: {bot.user.name}")
    print(f"👑 777 Supreme Enterprise System Ready!")
    print(f"-----------------------------------")
    await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name="over 777 Server | !help"))

# --- أزرار التفاعل للوحة التحكم (Help View) ---
class HelpView(View):
    def __init__(self, ctx):
        super().__init__(timeout=120)
        self.ctx = ctx

    @discord.ui.button(label="قسم الحماية", style=discord.ButtonStyle.danger, emoji="🛡️")
    async def mod_section(self, interaction: discord.Interaction, button: Button):
        if interaction.user != self.ctx.author:
            return await interaction.response.send_message("❌ هذه القائمة ليست لك!", ephemeral=True)
        
        embed = discord.Embed(
            title="🛡️ أوامر الحماية والسيطرة (Moderation)",
            description="إليك قائمة أوامر الحماية مرتبطة تحت بعضها:",
            color=0xffc0cb
        )
        commands_list = [
            "`!kick` — طرد العضو من السيرفر",
            "`!ban` — حظر العضو نهائياً",
            "`!unban` — فك الحظر عن العضو",
            "`!mute` — إسكات العضو مؤقتاً (Timeout)",
            "`!unmute` — فك الإسكات عن العضو",
            "`!clear` — مسح وتطهير الرسائل",
            "`!lock` — قفل الروم الحالية",
            "`!unlock` — فتح الروم الحالية",
            "`!slowmode` — ضبط السلومود للروم",
            "`!nuke` — إعادة تدوير وتطهير الروم",
            "`!hide` — إخفاء الروم عن الأعضاء",
            "`!show` — إظهار الروم للأعضاء",
            "`!warn` — إعطاء إنذار إداري للعضو",
            "`!say` — إرسال رسالة عبر البوت",
            "`!embed` — إرسال رسالة مميزة (Embed)"
        ]
        embed.add_field(name="الأوامر:", value="\n".join(commands_list), inline=False)
        await interaction.response.edit_message(embed=embed, view=self)

    @discord.ui.button(label="قسم الرولات", style=discord.ButtonStyle.primary, emoji="🎭")
    async def roles_section(self, interaction: discord.Interaction, button: Button):
        if interaction.user != self.ctx.author:
            return await interaction.response.send_message("❌ هذه القائمة ليست لك!", ephemeral=True)
        
        embed = discord.Embed(
            title="🎭 أوامر الرولات والإدارة (Roles)",
            description="إليك قائمة أوامر الرولات مرتبة تحت بعضها:",
            color=0xffc0cb
        )
        commands_list = [
            "`!roles` — عرض رولات السيرفر من الأعلى للأقل",
            "`!role` — إعطاء رتبة لعضو",
            "`!removerole` — إزالة رتبة من عضو",
            "`!check` — فحص عدد حاملي الرتبة",
            "`!allrole` — إعطاء رتبة للجميع",
            "`!r_all` — سحب رتبة من الجميع",
            "`!createrole` — إنشاء رتبة جديدة",
            "`!deleterole` — حذف رتبة من السيرفر",
            "`!rolecolor` — تغيير لون الرتبة",
            "`!rolename` — تغيير اسم الرتبة",
            "`!botroles` — عرض رولات البوت",
            "`!userroles` — عرض رولات عضو معين",
            "`!adminroles` — عرض رولات الإدارة العليا",
            "`!modroles` — عرض رولات المشرفين",
            "`!rolecount` — عدد رولات السيرفر الإجمالي"
        ]
        embed.add_field(name="الأوامر:", value="\n".join(commands_list), inline=False)
        await interaction.response.edit_message(embed=embed, view=self)

    @discord.ui.button(label="الإحصائيات", style=discord.ButtonStyle.success, emoji="📊")
    async def stats_section(self, interaction: discord.Interaction, button: Button):
        if interaction.user != self.ctx.author:
            return await interaction.response.send_message("❌ هذه القائمة ليست لك!", ephemeral=True)
        
        embed = discord.Embed(
            title="📊 أوامر الإحصائيات والأدوات (Stats)",
            description="إليك قائمة أوامر الإحصائيات مرتبة تحت بعضها:",
            color=0xffc0cb
        )
        commands_list = [
            "`!server` — عرض إحصائيات السيرفر الكاملة",
            "`!user` — عرض معلومات العضو والآيدي",
            "`!avatar` — عرض الأفاتار الشخصي",
            "`!banner` — عرض البنر الشخصي",
            "`!servericon` — عرض أيكونة السيرفر",
            "`!ping` — سرعة استجابة البوت",
            "`!uptime` — حالة تشغيل البوت",
            "`!botinfo` — معلومات البوت الشاملة",
            "`!owner` — معرفة مالك السيرفر",
            "`!boosters` — عدد داعمي السيرفر",
            "`!boostlevel` — مستوى بوستات السيرفر",
            "`!emojis` — إيموجيز السيرفر",
            "`!channels` — عدد رومات السيرفر",
            "`!bots` — عدد بوتات السيرفر",
            "`!humans` — عدد الأعضاء الحقيقيين"
        ]
        embed.add_field(name="الأوامر:", value="\n".join(commands_list), inline=False)
        await interaction.response.edit_message(embed=embed, view=self)

    @discord.ui.button(label="الترفيه", style=discord.ButtonStyle.secondary, emoji="🎮")
    async def fun_section(self, interaction: discord.Interaction, button: Button):
        if interaction.user != self.ctx.author:
            return await interaction.response.send_message("❌ هذه القائمة ليست لك!", ephemeral=True)
        
        embed = discord.Embed(
            title="🎮 أوامر الترفيه والتفاعل (Fun)",
            description="إليك قائمة أوامر الترفيه مرتبة تحت بعضها:",
            color=0xffc0cb
        )
        commands_list = [
            "`!ticket` — فتح لوحة التذاكر والدعم",
            "`!roll` — رمي النرد عشوائياً",
            "`!coin` — ملك أو كتابة",
            "`!hug` — عناق ترفيهي",
            "`!slap` — إعطاء كف ترفيهي",
            "`!kiss` — إرسال قبلة لطيفة",
            "`!rate` — تقييم أي شيء بنسبة مئوية",
            "`!ship` — نسبة التوافق العاطفي",
            "`!iq` — حساب نسبة الذكاء الوهمية",
            "`!joke` — إلقاء نكتة مضحكة",
            "`!choose` — الاختيار بين خيارات متعددة",
            "`!reverse` — عكس الحروف والكلمات",
            "`!ascii` — تحويل النص لشكل بارز",
            "`!cute` — قياس نسبة اللطافة",
            "`!handsome` — قياس نسبة الوسامة"
        ]
        embed.add_field(name="الأوامر:", value="\n".join(commands_list), inline=False)
        await interaction.response.edit_message(embed=embed, view=self)

# --- أمر المساعدة الرئيسي مع الأزرار ---
@bot.command(name="help", aliases=["اوامر", "الاوامر"])
async def help_command(ctx):
    embed = discord.Embed(
        title="🌟 لوحة التحكم الملكية لسيرفر 777",
        description="أهلاً بك يا جودي في لوحة تحكم بوت **Nova 777 Supreme**.\nاختر القسم المناسب من الأزرار بالأسفل لعرض الأوامر مرتبة تحت بعضها بكامل تفاصيلها:",
        color=0xffc0cb
    )
    if ctx.guild.icon:
        embed.set_thumbnail(url=ctx.guild.icon.url)
    embed.set_footer(text=f"طلب بواسطة {ctx.author.name} | 777 Enterprise", icon_url=ctx.author.display_avatar.url)
    
    view = HelpView(ctx)
    await ctx.send(embed=embed, view=view)

# --- تضمين بعض الأوامر السريعة للتأكد من عمل البوت بالكامل ---
@bot.command(name="ping")
async def ping_cmd(ctx):
    await ctx.send(f"🏓 سرعة استجابة البوت: `{round(bot.latency * 1000)}ms`")

@bot.command(name="server", aliases=["serverinfo"])
async def server_cmd(ctx):
    g = ctx.guild
    online = sum(1 for m in g.members if m.status != discord.Status.offline)
    embed = discord.Embed(title=f"🌸 سيرفر {g.name}", color=0xffc0cb)
    if g.icon: embed.set_thumbnail(url=g.icon.url)
    embed.add_field(name="🆔 آيدي السيرفر", value=f"`{g.id}`", inline=False)
    embed.add_field(name="👥 الأعضاء", value=f"العدد الكلي: `{g.member_count}` | الأونلاين: `{online}`", inline=False)
    embed.add_field(name="🎭 الرولات", value=f"`{len(g.roles)}` رتبة", inline=False)
    await ctx.send(embed=embed)

TOKEN = os.getenv("TOKEN")
if TOKEN:
    bot.run(TOKEN)
else:
    print("❌ Error: TOKEN environment variable not found!")
