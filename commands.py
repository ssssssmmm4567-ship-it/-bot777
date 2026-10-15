import discord
from discord.ext import commands
from discord.ui import Button, View

# قائمة المساعدة التفاعلية والأزرار
class HelpView(View):
    def __init__(self):
        super().__init__(timeout=180)

    @discord.ui.button(label="أوامر الرتب", style=discord.ButtonStyle.primary, emoji="🛡️")
    async def roles_help(self, interaction: discord.Interaction, button: Button):
        embed = discord.Embed(title="🛡️ أوامر الرتب والصلاحيات", color=0xFF69B4)
        embed.add_field(name="`!role` / `!addrole`", value="إضافة رتبة جديدة أو إعطاء رتبة لعضو", inline=False)
        embed.add_field(name="`!srole` / `!dsrole`", value="إنشاء رول خاص أو حذف رول خاص", inline=False)
        embed.add_field(name="`!autorole` / `!daorole`", value="إضافة رتبة تلقائية عند الدخول أو حذفها", inline=False)
        embed.add_field(name="`!allrole` / `!r all`", value="إعطاء رول لجميع الأعضاء أو إزالته", inline=False)
        embed.add_field(name="`!editrole` / `!nick`", value="تعديل اسم الرول أو رتبة تغيير الاسم", inline=False)
        embed.add_field(name="`!check` / `!checkvc`", value="التشييك على الأعضاء في الرول أو المتصلين بالصوت", inline=False)
        embed.set_footer(text="سيرفر 777 | قسم إدارة الرتب")
        await interaction.response.edit_message(embed=embed, view=self)

    @discord.ui.button(label="الأوامر العامة", style=discord.ButtonStyle.success, emoji="📌")
    async def general_help(self, interaction: discord.Interaction, button: Button):
        embed = discord.Embed(title="📌 الأوامر العامة ومعلومات الأعضاء", color=0x87CEEB)
        embed.add_field(name="`!avatar` / `!banner`", value="عرض صورة الشخص أو البنر الخاص به", inline=False)
        embed.add_field(name="`!user` / `!profile`", value="عرض معلومات وبروفايل العضو بالتفصيل", inline=False)
        embed.add_field(name="`!id` / `!server`", value="عرض لفل الشخص أو معلومات السيرفر", inline=False)
        embed.add_field(name="`!myinv` / `!top`", value="عرض عدد دعواتك أو توب الأعضاء بالسيرفر", inline=False)
        embed.set_footer(text="سيرفر 777 | الأوامر العامة")
        await interaction.response.edit_message(embed=embed, view=self)

    @discord.ui.button(label="تعديل الصور والألوان", style=discord.ButtonStyle.secondary, emoji="🎨")
    async def image_help(self, interaction: discord.Interaction, button: Button):
        embed = discord.Embed(title="🎨 أوامر الفلاتر، الألوان وتعديل الصور", color=0xFFB6C1)
        embed.add_field(name="`!colors` / `!color`", value="فتح علبة الألوان واختيار لون مخصص", inline=False)
        embed.add_field(name="`!circle`", value="عرض صورة العضو على شكل دائرة أنيقة", inline=False)
        embed.add_field(name="`!aremove`", value="إزالة خلفية الصور بذكاء واحترافية", inline=False)
        embed.add_field(name="`!change` / `!edit-image`", value="إضافة فلاتر وتعديل بصري على الصور", inline=False)
        embed.set_footer(text="سيرفر 777 | الفلاتر والترفيه")
        await interaction.response.edit_message(embed=embed, view=self)

# دالة لتسجيل الأوامر في البوت الرئيسي
def setup_commands(bot):
    
    @bot.command()
    async def help(ctx):
        embed = discord.Embed(
            title="🌟 قائمة مساعدة بوت سيرفر 777",
            description="أهلاً بك يا فنانة! اختر القسم المطلوب من الأزرار بالأسفل لتصفح جميع الأوامر المتاحة بكل سهولة:",
            color=0xFF69B4
        )
        embed.set_footer(text="777 Community • Powered by Railway")
        view = HelpView()
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
            await ctx.send("❌ هذا العضو ليس لديه بنر مخصص!")

    @bot.command()
    async def server(ctx):
        s = ctx.guild
        embed = discord.Embed(title=f"معلومات سيرفر {s.name}", color=0x87CEEB)
        embed.add_field(name="عدد الأعضاء", value=s.member_count, inline=True)
        embed.add_field(name="صاحب السيرفر", value=s.owner, inline=True)
        embed.add_field(name="تاريخ الإنشاء", value=s.created_at.strftime("%Y-%m-%d"), inline=True)
        if s.icon:
            embed.set_thumbnail(url=s.icon.url)
        await ctx.send(embed=embed)

    @bot.command()
    async def id(ctx, member: discord.Member = None):
        member = member or ctx.author
        embed = discord.Embed(title=f"معلومات الحساب: {member.name}", color=0xFFB6C1)
        embed.add_field(name="الآيدي (ID)", value=member.id, inline=False)
        embed.add_field(name="تاريخ الانضمام للديسكورد", value=member.created_at.strftime("%Y-%m-%d"), inline=False)
        embed.set_thumbnail(url=member.display_avatar.url)
        await ctx.send(embed=embed)

    @bot.command()
    @commands.has_permissions(manage_roles=True)
    async def role(ctx, member: discord.Member, role: discord.Role):
        await member.add_roles(role)
        await ctx.send(f"✨ تم إعطاء الرتبة `{role.name}` لـ `{member.name}` بنجاح.")

    @bot.command()
    @commands.has_permissions(manage_roles=True)
    async def addrole(ctx, member: discord.Member, role: discord.Role):
        await member.add_roles(role)
        await ctx.send(f"✅ تم إضافة الرتبة `{role.name}` للعضو `{member.name}`.")

    @bot.command()
    async def circle(ctx, member: discord.Member = None):
        member = member or ctx.author
        embed = discord.Embed(title=f"صورة دائرية لـ {member.name}", color=0xFF69B4)
        embed.set_image(url=member.display_avatar.url)
        embed.set_footer(text="تم تطبيق شكل الدائرة بنجاح")
        await ctx.send(embed=embed)

    @bot.command()
    async def colors(ctx):
        embed = discord.Embed(title="🎨 علبة الألوان المتاحة لسيرفر 777", description="اكتب `!color [اسم اللون]` لاختيار لونك المفضل!", color=0xFFB6C1)
        embed.add_field(name="الألوان البينك والآيس", value="🌸 Pink | 🧊 Ice Blue | 🤍 White | ✨ Gold", inline=False)
        await ctx.send(embed=embed)
