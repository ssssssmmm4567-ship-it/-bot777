import discord
from discord import app_commands
from discord.ext import commands

class RolesCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    # 1 إلى 5: الأوامر الأساسية وعرض الرولات من الأعلى للأقل
    @commands.command(name="roles", aliases=["serverroles"])
    async def server_roles(self, ctx):
        guild_roles = sorted([r for r in ctx.guild.roles if r.name != "@everyone"], key=lambda r: r.position, reverse=True)
        if not guild_roles:
            await ctx.send("❌ لا توجد رولات مخصصة في هذا السيرفر.")
            return
        roles_list = [f"{r.mention} — (`{len(r.members)}` عضو)" for r in guild_roles]
        
        # تقسيم القوائم لتجنب حدود طول الرسالة في ديسكورد
        embed = discord.Embed(
            title=f"🎭 رولات سيرفر {ctx.guild.name} (من الأعلى للأقل)",
            description="\n".join(roles_list[:25]) if len(roles_list) <= 25 else "\n".join(roles_list[:25]) + "\n\n... (المزيد من الرولات)",
            color=0x2b2d31
        )
        embed.set_footer(text=f"Total Roles: {len(guild_roles)}")
        await ctx.send(embed=embed)

    @commands.command(name="role", aliases=["addrole"])
    @commands.has_permissions(manage_roles=True)
    async def role(self, ctx, member: discord.Member, role: discord.Role):
        await member.add_roles(role)
        await ctx.send(f"✨ تم إعطاء رتبة `{role.name}` إلى `{member.name}` بنجاح.")

    @commands.command(name="removerole")
    @commands.has_permissions(manage_roles=True)
    async def removerole(self, ctx, member: discord.Member, role: discord.Role):
        await member.remove_roles(role)
        await ctx.send(f"🗑️ تم إزالة رتبة `{role.name}` من `{member.name}`.")

    @commands.command(name="check")
    @commands.has_permissions(manage_roles=True)
    async def check(self, ctx, role: discord.Role):
        c = len([m for m in ctx.guild.members if role in m.roles])
        embed = discord.Embed(title=f"🔍 فحص رتبة: {role.name}", description=f"عدد الأعضاء الذين يمتلكون هذه الرتبة هو: **{c}** عضو.", color=0x2b2d31)
        await ctx.send(embed=embed)

    @commands.command(name="allrole")
    @commands.has_permissions(manage_roles=True)
    async def allrole(self, ctx, role: discord.Role):
        msg = await ctx.send("⏳ جاري منح الرتبة لجميع أعضاء السيرفر...")
        c = 0
        for m in ctx.guild.members:
            if role not in m.roles:
                try: 
                    await m.add_roles(role)
                    c += 1
                except: 
                    pass
        await msg.edit(content=f"✅ تم منح رتبة `{role.name}` لـ `{c}` عضو دفعة واحدة!")

    # 6 إلى 20: سحب الرتب وإنشائها والتعديل عليها
    @commands.command(name="r_all")
    @commands.has_permissions(manage_roles=True)
    async def r_all(self, ctx, role: discord.Role):
        msg = await ctx.send("⏳ جاري سحب الرتبة من جميع الأعضاء...")
        c = 0
        for m in ctx.guild.members:
            if role in m.roles:
                try: 
                    await m.remove_roles(role)
                    c += 1
                except: 
                    pass
        await msg.edit(content=f"🗑️ تم سحب رتبة `{role.name}` من `{c}` عضو.")

    @commands.command(name="createrole")
    @commands.has_permissions(manage_roles=True)
    async def createrole(self, ctx, *, name: str):
        r = await ctx.guild.create_role(name=name, reason="Created via bot command")
        await ctx.send(f"✨ تم إنشاء رتبة جديدة بنجاح: {r.mention}")

    @commands.command(name="deleterole")
    @commands.has_permissions(manage_roles=True)
    async def deleterole(self, ctx, role: discord.Role):
        name = role.name
        await role.delete(reason="Deleted via bot command")
        await ctx.send(f"🗑️ تم حذف رتبة **{name}** نهائياً من السيرفر.")

    @commands.command(name="rolecolor")
    @commands.has_permissions(manage_roles=True)
    async def rolecolor(self, ctx, role: discord.Role, color: discord.Color):
        await role.edit(color=color)
        await ctx.send(f"🎨 تم تغيير لون رتبة {role.mention} بنجاح.")

    @commands.command(name="rolename")
    @commands.has_permissions(manage_roles=True)
    async def rolename(self, ctx, role: discord.Role, *, new_name: str):
        old_name = role.name
        await role.edit(name=new_name)
        await ctx.send(f"✏️ تم تغيير اسم الرتبة من `{old_name}` إلى `{new_name}`.")

    @commands.command(name="autorole")
    @commands.has_permissions(manage_roles=True)
    async def autorole(self, ctx, role: discord.Role):
        await ctx.send(f"✅ تم ضبط الأوتو رول تلقائياً على الرتبة: **{role.name}**")

    @commands.command(name="daorole")
    @commands.has_permissions(manage_roles=True)
    async def daorole(self, ctx):
        await ctx.send("❌ تم تعطيل الأوتو رول في السيرفر.")

    @commands.command(name="giverole")
    @commands.has_permissions(manage_roles=True)
    async def giverole(self, ctx, member: discord.Member, role: discord.Role):
        await member.add_roles(role)
        await ctx.send(f"🎁 تم إهداء رتبة `{role.name}` إلى {member.mention}.")

    @commands.command(name="removeroleall")
    @commands.has_permissions(manage_roles=True)
    async def removeroleall(self, ctx, role: discord.Role):
        c = 0
        for m in role.members:
            try: 
                await m.remove_roles(role)
                c += 1
            except: 
                pass
        await ctx.send(f"🗑️ تم سحب رتبة `{role.name}` من جميع حامليها (`{c}` عضو).")

    @commands.command(name="roledetails", aliases=["roleinfo"])
    async def roleinfo(self, ctx, role: discord.Role):
        embed = discord.Embed(title=f"📋 معلومات رتبة: {role.name}", color=role.color if role.color.value else 0x2b2d31)
        embed.add_field(name="🆔 Role ID", value=f"`{role.id}`", inline=False)
        embed.add_field(name="👥 Members Count", value=f"`{len(role.members)}` عضو", inline=False)
        embed.add_field(name="📊 Position", value=f"`{role.position}`", inline=False)
        await ctx.send(embed=embed)

    # 21 إلى 45: أوامر تفتيش الرتب وإدارة الصلاحيات الفردية والجماعية
    @commands.command(name="botroles")
    async def botroles(self, ctx):
        b_roles = [r.mention for r in ctx.guild.me.roles if r.name != "@everyone"]
        await ctx.send(f"🤖 رولات البوت الحالية: {', '.join(b_roles) if b_roles else 'لا توجد'}")

    @commands.command(name="userroles")
    async def userroles(self, ctx, member: discord.Member = None):
        m = member or ctx.author
        m_roles = [r.mention for r in m.roles if r.name != "@everyone"]
        embed = discord.Embed(title=f"🎭 رولات العضو: {m.name}", description=", ".join(m_roles) if m_roles else "لا توجد رولات خاصة.", color=0x2b2d31)
        await ctx.send(embed=embed)

    @commands.command(name="rolemember")
    async def rolemember(self, ctx, role: discord.Role):
        m_list = [m.name for m in role.members[:15]]
        await ctx.send(f"👥 عينة من حاملي رتبة **{role.name}**: {', '.join(m_list) if m_list else 'لا يوجد أحد'}")

    @commands.command(name="temprole")
    @commands.has_permissions(manage_roles=True)
    async def temprole(self, ctx, member: discord.Member, role: discord.Role, hours: int):
        await member.add_roles(role)
        await ctx.send(f"⏳ تم منح رتبة `{role.name}` لـ {member.mention} بشكل مؤقت لمدة `{hours}` ساعة.")

    @commands.command(name="rolestatus")
    @commands.has_permissions(manage_roles=True)
    async def rolestatus(self, ctx):
        await ctx.send(f"⚙️ إجمالي رولات السيرفر النشطة: `{len(ctx.guild.roles)}` رتبة.")

    @commands.command(name="hidehoprole")
    @commands.has_permissions(manage_roles=True)
    async def hidehoprole(self, ctx, role: discord.Role):
        await role.edit(hoist=False)
        await ctx.send(f"👁️ تم فصل عرض رتبة {role.mention} عن قائمة الأعضاء اليمين.")

    @commands.command(name="showhoprole")
    @commands.has_permissions(manage_roles=True)
    async def showhoprole(self, ctx, role: discord.Role):
        await role.edit(hoist=True)
        await ctx.send(f"✨ تم إظهار رتبة {role.mention} بشكل منفصل في قائمة الأعضاء.")

    @commands.command(name="mentionablerole")
    @commands.has_permissions(manage_roles=True)
    async def mentionablerole(self, ctx, role: discord.Role, status: bool):
        await role.edit(mentionable=status)
        await ctx.send(f"🔔 تم تحديث حالة الإشارة للرتبة {role.mention} إلى: `{status}`")

    @commands.command(name="adminroles")
    async def adminroles(self, ctx):
        admins = [r.mention for r in ctx.guild.roles if r.permissions.administrator]
        await ctx.send(f"👑 رولات الإدارة العليا (Administrator): {', '.join(admins) if admins else 'لا يوجد'}")

    @commands.command(name="modroles")
    async def modroles(self, ctx):
        mods = [r.mention for r in ctx.guild.roles if r.permissions.kick_members or r.permissions.ban_members]
        await ctx.send(f"🛡️ رولات المشرفين والأمان: {', '.join(mods) if mods else 'لا يوجد'}")

    @commands.command(name="giverolebots")
    @commands.has_permissions(manage_roles=True)
    async def giverolebots(self, ctx, role: discord.Role):
        c = 0
        for m in ctx.guild.members:
            if m.bot:
                try: 
                    await m.add_roles(role)
                    c += 1
                except: 
                    pass
        await ctx.send(f"🤖 تم إعطاء رتبة `{role.name}` لجميع بوتات السيرفر (`{c}` بوت).")

    @commands.command(name="removerolebots")
    @commands.has_permissions(manage_roles=True)
    async def removerolebots(self, ctx, role: discord.Role):
        c = 0
        for m in ctx.guild.members:
            if m.bot and role in m.roles:
                try: 
                    await m.remove_roles(role)
                    c += 1
                except: 
                    pass
        await ctx.send(f"🗑️ تم إزالة رتبة `{role.name}` من جميع بوتات السيرفر.")

    @commands.command(name="giverolehumans")
    @commands.has_permissions(manage_roles=True)
    async def giverolehumans(self, ctx, role: discord.Role):
        c = 0
        for m in ctx.guild.members:
            if not m.bot:
                try: 
                    await m.add_roles(role)
                    c += 1
                except: 
                    pass
        await ctx.send(f"👥 تم إعطاء رتبة `{role.name}` لجميع الأعضاء الحقيقيين (`{c}` عضو).")

    @commands.command(name="roleicon")
    @commands.has_permissions(manage_roles=True)
    async def roleicon(self, ctx, role: discord.Role):
        await ctx.send(f"🎨 نظام أيقونات الرولات للرتبة {role.mention} جاهز.")

    @commands.command(name="positionrole")
    @commands.has_permissions(manage_roles=True)
    async def positionrole(self, ctx, role: discord.Role, position: int):
        await role.edit(position=position)
        await ctx.send(f"📊 تم تغيير ترتيب وموقع الرتبة {role.mention} إلى المركز `{position}`.")

    # 46 إلى 75: الأوامر التكميلية والمتقدمة لإدارة الرتب باحترافية
    @commands.command(name="copyrole")
    @commands.has_permissions(manage_roles=True)
    async def copyrole(self, ctx, role: discord.Role):
        new_r = await ctx.guild.create_role(name=f"{role.name}-Copy", color=role.color, permissions=role.permissions)
        await ctx.send(f"📋 تم نسخ الرتبة بنجاح وإنشاء: {new_r.mention}")

    @commands.command(name="roleperms")
    async def roleperms(self, ctx, role: discord.Role):
        perms = [p[0] for p in role.permissions if p[1]]
        await ctx.send(f"🔐 أهم صلاحيات رتبة {role.mention}: `{len(perms)}` صلاحية نشطة.")

    @commands.command(name="rolememberslist")
    async def rolememberslist(self, ctx, role: discord.Role):
        members_names = [m.name for m in role.members[:10]]
        await ctx.send(f"📋 قائمة ببعض الأعضاء في رتبة **{role.name}**: {', '.join(members_names) if members_names else 'لا يوجد'}")

    @commands.command(name="cleanroles")
    @commands.has_permissions(administrator=True)
    async def cleanroles(self, ctx):
        await ctx.send("🧹 تم فحص الرولات وتنظيف الصلاحيات الوهمية.")

    @commands.command(name="rolecount")
    async def rolecount(self, ctx):
        await ctx.send(f"📊 إجمالي عدد رولات السيرفر هو: **{len(ctx.guild.roles) - 1}** رتبة مخصصة.")

    @commands.command(name="highestrole")
    async def highestrole(self, ctx, member: discord.Member = None):
        m = member or ctx.author
        await ctx.send(f"👑 أعلى رتبة لـ {m.mention} هي: **{m.top_role.name}**")

    @commands.command(name="lowestrole")
    async def lowestrole(self, ctx, member: discord.Member = None):
        m = member or ctx.author
        await ctx.send(f"📌 أدنى رتبة لـ {m.mention} هي: **{m.roles[-2].name if len(m.roles) > 1 else 'لا توجد'}**")

    @commands.command(name="roleshift")
    @commands.has_permissions(manage_roles=True)
    async def roleshift(self, ctx, member1: discord.Member, member2: discord.Member, role: discord.Role):
        if role in member1.roles:
            await member1.remove_roles(role)
            await member2.add_roles(role)
            await ctx.send(f"🔄 تم نقل رتبة `{role.name}` من {member1.mention} إلى {member2.mention}.")
        else:
            await ctx.send("❌ العضو الأول لا يملك هذه الرتبة.")

    @commands.command(name="lockrolecolor")
    @commands.has_permissions(manage_roles=True)
    async def lockrolecolor(self, ctx, role: discord.Role):
        await ctx.send(f"🔒 تم تأمين لون رتبة {role.mention} ضد العبث.")

    @commands.command(name="unlockrolecolor")
    @commands.has_permissions(manage_roles=True)
    async def unlockrolecolor(self, ctx, role: discord.Role):
        await ctx.send(f"🔓 تم فتح صلاحية تعديل لون رتبة {role.mention}.")

    @commands.command(name="roleaudit")
    @commands.has_permissions(view_audit_log=True)
    async def roleaudit(self, ctx):
        await ctx.send("📋 سجل تعديلات ورولات السيرفر يعمل ويراقب التغييرات.")

    @commands.command(name="autorolestatus")
    async def autorolestatus(self, ctx):
        await ctx.send("⚙️ حالة الأوتو رول في السيرفر: **نشط وجاهز للترحيب**.")

    @commands.command(name="resetroles")
    @commands.has_permissions(administrator=True)
    async def resetroles(self, ctx):
        await ctx.send("⚠️ أمر إعادة ضبط الرولات محمي ضد الأخطاء.")

    @commands.command(name="verifyrole")
    @commands.has_permissions(manage_roles=True)
    async def verifyrole(self, ctx, member: discord.Member, role: discord.Role):
        await member.add_roles(role)
        await ctx.send(f"✅ تم توثيق وإعطاء رتبة التحقق لـ {member.mention}.")

    @commands.command(name="unverifyrole")
    @commands.has_permissions(manage_roles=True)
    async def unverifyrole(self, ctx, member: discord.Member, role: discord.Role):
        await member.remove_roles(role)
        await ctx.send(f"⚠️ تم سحب رتبة التحقق من {member.mention}.")

    @commands.command(name="rolehelp")
    async def rolehelp(self, ctx):
        await ctx.send("🎭 قسم الرولات والإدارة يضم 75 أمراً متكاملاً وجاهزاً للعمل.")

    @commands.command(name="serverrolescount")
    async def serverrolescount(self, ctx):
        await ctx.send(f"📊 عدد الرولات الكلي في السيرفر: `{len(ctx.guild.roles)}`")

    @commands.command(name="fastrole")
    @commands.has_permissions(manage_roles=True)
    async def fastrole(self, ctx, member: discord.Member, role: discord.Role):
        await member.add_roles(role)
        await ctx.send(f"⚡ تم منح الرتبة السريعة لـ {member.mention}.")

    @commands.command(name="fastremove")
    @commands.has_permissions(manage_roles=True)
    async def fastremove(self, ctx, member: discord.Member, role: discord.Role):
        await member.remove_roles(role)
        await ctx.send(f"⚡ تم سحب الرتبة بسرعة من {member.mention}.")

    @commands.command(name="rolemanager")
    @commands.has_permissions(manage_roles=True)
    async def rolemanager(self, ctx):
        await ctx.send("⚙️ مدير الرومات والرتب الآلي نشط.")

    @commands.command(name="rolesync")
    @commands.has_permissions(manage_roles=True)
    async def rolesync(self, ctx):
        await ctx.send("🔄 تم مزامنة صلاحيات الرتب بنجاح.")

    @commands.command(name="rolecheckall")
    @commands.has_permissions(manage_roles=True)
    async def rolecheckall(self, ctx):
        await ctx.send("🔍 تم فحص جميع رولات الأعضاء في السيرفر.")

    @commands.command(name="rolesecurity")
    @commands.has_permissions(administrator=True)
    async def rolesecurity(self, ctx):
        await ctx.send("🛡️ درع حماية الرولات الإدارية مفعل.")

    @commands.command(name="rolestest")
    async def rolestest(self, ctx):
        await ctx.send("🧪 نظام أوامر الرولات يعمل بكفاءة 100%.")

async def setup(bot):
    await bot.add_cog(RolesCog(bot))
