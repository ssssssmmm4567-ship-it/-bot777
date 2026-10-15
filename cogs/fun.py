import random
import discord
from discord import app_commands
from discord.ext import commands
from discord.ui import Button, View

class TicketView(View):
    def __init__(self):
        super().__init__(timeout=None)

    @discord.ui.button(label="فتح تذكرة جديدة", style=discord.ButtonStyle.success, emoji="🎫", custom_id="sup_ticket_btn")
    async def open_ticket(self, interaction: discord.Interaction, button: Button):
        guild = interaction.guild
        cat = discord.utils.get(guild.categories, name="Tickets") or await guild.create_category("Tickets")
        overwrites = {
            guild.default_role: discord.PermissionOverwrite(view_channel=False),
            interaction.user: discord.PermissionOverwrite(view_channel=True, send_messages=True),
            guild.me: discord.PermissionOverwrite(view_channel=True)
        }
        ch = await guild.create_text_channel(f"ticket-{interaction.user.name}", category=cat, overwrites=overwrites)
        await ch.send(embed=discord.Embed(title="🎫 مركز الدعم الفني", description=f"مرحباً بك {interaction.user.mention}، سيتم خدمتك بواسطة الإدارة قريباً.", color=0xffc0cb))
        await interaction.response.send_message(f"✅ تم فتح تذكرتك الخاصة بنجاح: {ch.mention}", ephemeral=True)

class FunCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="ticket")
    @commands.has_permissions(administrator=True)
    async def ticket(self, ctx):
        embed = discord.Embed(
            title="🎫 لوحة الدعم الفني والتذاكر",
            description="اضغط على الزر بالأسفل لفتح تذكرة خاصة والتواصل مع الإدارة بكل إشراف واحترافية.",
            color=0xffc0cb
        )
        if ctx.guild.icon:
            embed.set_thumbnail(url=ctx.guild.icon.url)
        await ctx.send(embed=embed, view=TicketView())

    @commands.command(name="roll")
    async def roll(self, ctx):
        await ctx.send(f"🎲 النرد الحظ: **{random.randint(1, 6)}**")

    @commands.command(name="coin")
    async def coin(self, ctx):
        await ctx.send(f"🪙 نتيجة ملك أو كتابة: **{random.choice(['ملك 👑', 'كتابة 📝'])}**")

    @commands.command(name="8ball")
    async def eightball(self, ctx, *, question: str):
        answers = ["نعم بالتأكيد ✨", "ربما 🤔", "مستحيل ❌", "البصيرة تقول نعم 🤍", "إجابة غامضة جرب لاحقاً"]
        embed = discord.Embed(title=f"❓ {question}", description=f"🔮 الإجابة: **{random.choice(answers)}**", color=0xffc0cb)
        await ctx.send(embed=embed)

    @commands.command(name="colors")
    async def colors(self, ctx):
        embed = discord.Embed(title="🎨 تنسيقات وألوان السيرفر", description="🌸 وردي | 🧊 جليدي | 🤍 أبيض | 🖤 أسود دكن", color=0xffc0cb)
        await ctx.send(embed=embed)

    @commands.command(name="math")
    async def math(self, ctx, a: float, op: str, b: float):
        if op == "+": r = a + b
        elif op == "-": r = a - b
        elif op == "*": r = a * b
        elif op == "/": r = a / b if b != 0 else "خطأ (قسمة على صفر)"
        else: r = "عملية غير مسجلة"
        await ctx.send(f"🔢 نتيجة العملية الحسابية: `{r}`")

    @commands.command(name="choose")
    async def choose(self, ctx, *options):
        if options:
            await ctx.send(f"🤔 اخترت لك: **{random.choice(options)}**")
        else:
            await ctx.send("❌ يرجى كتابة الخيارات مفصولة بمسافات.")

    @commands.command(name="reverse")
    async def reverse(self, ctx, *, text: str):
        await ctx.send(text[::-1])

    @commands.command(name="ascii")
    async def ascii(self, ctx, *, text: str):
        await ctx.send(f"```text\n{text}\n```")

    @commands.command(name="hug")
    async def hug(self, ctx, member: discord.Member):
        await ctx.send(f"🫂 {ctx.author.mention} يعانق {member.mention} بحرارة ❤️")

    @commands.command(name="slap")
    async def slap(self, ctx, member: discord.Member):
        await ctx.send(f"👋 {ctx.author.mention} يعطي كفاً ترفيهياً لـ {member.mention} 😂")

    @commands.command(name="kiss")
    async def kiss(self, ctx, member: discord.Member):
        await ctx.send(f"💋 {ctx.author.mention} يرسل قبلة لطيفة إلى {member.mention} ✨")

    @commands.command(name="rate")
    async def rate(self, ctx, *, thing: str):
        await ctx.send(f"📊 تقييمي لـ **{thing}**: `{random.randint(1, 100)}%` ✨")

    @commands.command(name="ship")
    async def ship(self, ctx, member1: discord.Member, member2: discord.Member):
        await ctx.send(f"❤️ نسبة التوافق العاطفي بين {member1.mention} و {member2.mention} هي: **{random.randint(1, 100)}%** 💕")

    @commands.command(name="joke")
    async def joke(self, ctx):
        jokes = [
            "إيه أعلى درجة ذكاء؟ اسألني أنا!",
            "مرة واحد دخل صيدلية قالهم عندكم مانجو؟ قالوا لأ، قال طيب ليه لأ؟ 😂",
            "محشش سألوه شو أبطل حيوان؟ قال الفهد الاسود عشان سريع، قالوا له ليه؟ قال عشان لابس كوت رياضة!"
        ]
        await ctx.send(random.choice(jokes))

    @commands.command(name="iq")
    async def iq(self, ctx, member: discord.Member = None):
        m = member or ctx.author
        await ctx.send(f"🧠 نسبة ذكاء {m.mention} الوهمية هي: `{random.randint(60, 170)}` IQ 🚀")

    @commands.command(name="pat")
    async def pat(self, ctx, member: discord.Member):
        await ctx.send(f"✋ {ctx.author.mention} يطبطب بلطف على رأس {member.mention} 🌸")

    @commands.command(name="howgay")
    async def howgay(self, ctx, member: discord.Member = None):
        m = member or ctx.author
        await ctx.send(f"🌈 نسبة اللطافة المفرطة لـ {m.mention}: `{random.randint(1, 100)}%`")

    @commands.command(name="cute")
    async def cute(self, ctx, member: discord.Member = None):
        m = member or ctx.author
        await ctx.send(f"🌸 نسبة الكيوتد لـ {m.mention}: `{random.randint(1, 100)}%`")

    @commands.command(name="handsome")
    async def handsome(self, ctx, member: discord.Member = None):
        m = member or ctx.author
        await ctx.send(f"😎 وسامة {m.mention}: `{random.randint(50, 100)}%` ما شاء الله ✨")

    @commands.command(name="funhelp")
    async def funhelp(self, ctx):
        await ctx.send("🎮 قسم الترفيه والتذاكر يضم الألعاب وأوامر التفاعل والدعم الفني.")

    @commands.command(name="funtest")
    async def funtest(self, ctx):
        await ctx.send("🧪 نظام الترفيه والتذاكر يعمل بكفاءة تامة.")

async def setup(bot):
    await bot.add_cog(FunCog(bot))
