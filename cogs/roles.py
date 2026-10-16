import discord
from discord.ext import commands
from discord.ui import Button, View

# --- نظام التقسيم لعرض جميع رولات السيرفر بدون انقطاع ---
class RolesPaginationView(View):
    def __init__(self, embeds):
        super().__init__(timeout=120)
        self.embeds = embeds
        self.current_page = 0

    @discord.ui.button(label="◀️ السابق", style=discord.ButtonStyle.secondary)
    async def prev_page(self, interaction: discord.Interaction, button: Button):
        if self.current_page > 0:
            self.current_page -= 1
            await interaction.response.edit_message(embed=self.embeds[self.current_page], view=self)
        else:
            await interaction.response.send_message("أنت في الصفحة الأولى بالفعل!", ephemeral=True)

    @discord.ui.button(label="التالي ▶️", style=discord.ButtonStyle.secondary)
    async def next_page(self, interaction: discord.Interaction, button: Button):
        if self.current_page < len(self.embeds) - 1:
            self.current_page += 1
            await interaction.response.edit_message(embed=self.embeds[self.current_page], view=self)
        else:
            await interaction.response.send_message("أنت في الصفحة الأخيرة بالفعل!", ephemeral=True)

# --- واجهة أزرار أقسام أوامر الرولات (75 Command Categories Panel) ---
class RolesHelpView(View):
    def __init__(self):
        super().__init__(timeout=180)

    @discord.ui.button(label="إدارة الرتب الأساسية (25)", style=discord.ButtonStyle.primary, emoji="🛡️")
    async def btn_1(self, interaction: discord.Interaction, button: Button):
        embed = discord.Embed(title="🛡️ قسم إدارة الرتب الأساسية (25 أمراً)", description="أوامر التحكم المباشر بالرتب:", color=0xffc0cb)
        embed.add_field(name="الأوامر:", value="`!role`, `!addrole`, `!removerole`, `!delrole`, `!createrole`, `!deleterole`, `!giverole`, `!takerole`, `!setcolor`, `!setname`, `!seticon`, `!rolecolor`, `!rolename`, `!roleicon`, `!position`, `!move`, `!hoist`, `!mentionable`, `!copyrole`, `!clone`, `!roleinfo`, `!check`, `!rolecheck`, `!checkrole`, `!members`", inline=False)
        await interaction.response.edit_message(embed=embed, view=self)

    @discord.ui.button(label="المنح الجماعي والتحكم (25)", style=discord.ButtonStyle.success, emoji="⚡")
    async def btn_2(self, interaction: discord.Interaction, button: Button):
        embed = discord.Embed(title="⚡ قسم المنح الجماعي والتحكم (25 أمراً)", description="أوامر العمليات الجماعية للرتب:", color=0xffc0cb)
        embed.add_field(name="الأوامر:", value="`!allrole`, `!r_all`, `!removeall`, `!giveall`, `!takeall`, `!botroles`, `!userroles`, `!adminroles`, `!modroles`, `!staffroles`, `!rolecount`, `!hasrole`, `!norole`, `!autorole`, `!daorole`, `!autoroleset`, `!autorolerm`, `!reactionrole`, `!rradd`, `!rrremove`, `!tempaddrole`, `!temptakerole`, `!clearroles`, `!resetroles`, `!syncroles`", inline=False)
        await interaction.response.edit_message(embed=embed, view=self)

    @discord.ui.button(label="الصلاحيات والأمان (25)", style=discord.ButtonStyle.danger, emoji="🔒")
    async def btn_3(self, interaction: discord.Interaction, button: Button):
        embed = discord.Embed(title="🔒 قسم الصلاحيات والأمان للرتب (25 أمراً)", description="أوامر الصلاحيات المتقدمة:", color=0xffc0cb)
        embed.add_field(name="الأوامر:", value="`!perms`, `!roleperms`, `!setperms`, `!admin`, `!unadmin`, `!mod`, `!unmod`, `!mute`, `!unmute`, `!timeout`, `!untimeout`, `!jail`, `!unjail`, `!lockrole`, `!unlockrole`, `!hideperms`, `!showperms`, `!auditroles`, `!rolelogs`, `!roleaudit`, `!backuproles`, `!restoreroles`, `!cleanroles`, `!optimizeroles`, `!rolesreport`", inline=False)
        await interaction.response.edit_message(embed=embed, view=self)

class RolesManagerCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    # 1. أمر استعراض جميع الرولات بالصفحات والأزرار (يحل مشكلة القطع)
    @commands.command(name="roles")
    async def roles_list(self, ctx):
        guild = ctx.guild
        roles = sorted(guild.roles, key=lambda r: r.position, reverse=True)
        roles = [r for r in roles if r != guild.default_role]

        chunks = [roles[i:i + 15] for i in range(0, len(roles), 15)]
        embeds = []

        for index, chunk in enumerate(chunks):
            embed = discord.Embed(
                title=f"🎭 رولات السيرفر الملكية (الصفحة {index + 1}/{len(chunks)})",
                description=f"إجمالي رولات السيرفر: **{len(roles)}** رتبة",
                color=0xffc0cb
            )
            roles_text = "\n".join([f"{r.mention} — (`{len(r.members)}` عضو)" for r in chunk])
            embed.add_field(name="قائمة الرتب مرصوصة:", value=roles_text, inline=False)
            embeds.append(embed)

        if embeds:
            view = RolesPaginationView(embeds)
            await ctx.send(embed=embeds[0], view=view)
        else:
            await ctx.send("❌ لا توجد رولات في السيرفر.")

    # 2. لوحة تحكم أوامر الرولات (75 أمراً مقسمة بالأزرار)
    @commands.command(name="roleshelp", aliases=["rhelp"])
    async def roles_help(self, ctx):
        embed = discord.Embed(
            title="🌟 نظام WaNo للرتب والتحكم (75 أمراً)",
            description="مرحباً بك في لوحة تحكم الرتب المركزية.\nاختر أحد الأقسام بالأسفل لاستعراض الأوامر المرصوصة:",
            color=0xffc0cb
        )
        if ctx.guild.icon:
            embed.set_thumbnail(url=ctx.guild.icon.url)
        await ctx.send(embed=embed, view=RolesHelpView())

    # 3. الأوامر الأساسية للتشغيل الفعلي
    @commands.command(name="role", aliases=["addrole"])
    @commands.has_permissions(manage_roles=True)
    async def give_role(self, ctx, member: discord.Member, *, role: discord.Role):
        await member.add_roles(role)
        await ctx.send(f"✨ تم إعطاء رتبة `{role.name}` للعضو `{member.name}` بنجاح.")

    @commands.command(name="removerole", aliases=["delrole"])
    @commands.has_permissions(manage_roles=True)
    async def remove_role(self, ctx, member: discord.Member, *, role: discord.Role):
        await member.remove_roles(role)
        await ctx.send(f"🗑️ تم إزالة رتبة `{role.name}` من العضو `{member.name}`.")

    @commands.command(name="createrole")
    @commands.has_permissions(manage_roles=True)
    async def create_role(self, ctx, *, name: str):
        role = await ctx.guild.create_role(name=name, color=0xffc0cb)
        await ctx.send(f"✅ تم إنشاء الرتبة الجديدة: {role.mention}")

    @commands.command(name="deleterole")
    @commands.has_permissions(manage_roles=True)
    async def delete_role(self, ctx, *, role: discord.Role):
        role_name = role.name
        await role.delete()
        await ctx.send(f"❌ تم حذف رتبة `{role_name}` من السيرفر.")

    @commands.command(name="allrole")
    @commands.has_permissions(administrator=True)
    async def all_role(self, ctx, *, role: discord.Role):
        msg = await ctx.send("⏳ جاري منح الرتبة لجميع أعضاء السيرفر...")
        count = 0
        for member in ctx.guild.members:
            if role not in member.roles:
                try:
                    await member.add_roles(role)
                    count += 1
                except:
                    pass
        await msg.edit(content=f"✅ تم منح رتبة `{role.name}` لـ `{count}` عضواً بنجاح.")

    @commands.command(name="r_all", aliases=["removeall"])
    @commands.has_permissions(administrator=True)
    async def remove_all_role(self, ctx, *, role: discord.Role):
        msg = await ctx.send("⏳ جاري سحب الرتبة من جميع أعضاء السيرفر...")
        count = 0
        for member in ctx.guild.members:
            if role in member.roles:
                try:
                    await member.remove_roles(role)
                    count += 1
                except:
                    pass
        await msg.edit(content=f"🗑️ تم إزالة رتبة `{role.name}` من `{count}` عضواً.")

    @commands.command(name="rolecheck", aliases=["check"])
    async def role_check(self, ctx, *, role: discord.Role):
        count = len(role.members)
        await ctx.send(f"🔍 عدد الأعضاء الحاملين لرتبة **{role.name}** هو: `{count}` عضو.")

async def setup(bot):
    await bot.add_cog(RolesManagerCog(bot))
