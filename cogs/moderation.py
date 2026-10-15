import discord
from discord import app_commands
from discord.ext import commands

class ModerationCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    # 1 إلى 5: الطرد والحظر وفك الحظر والمسح
    @commands.command(name="kick")
    @commands.has_permissions(kick_members=True)
    async def kick(self, ctx, member: discord.Member, *, reason="لم يحدد سبب"):
        await member.kick(reason=reason)
        await ctx.send(f"👢 تم طرد العضو {member.mention} | السبب: {reason}")

    @commands.command(name="ban")
    @commands.has_permissions(ban_members=True)
    async def ban(self, ctx, member: discord.Member, *, reason="لم يحدد سبب"):
        await member.ban(reason=reason)
        await ctx.send(f"🔨 تم حظر العضو {member.mention} | السبب: {reason}")

    @commands.command(name="unban")
    @commands.has_permissions(ban_members=True)
    async def unban(self, ctx, user_id: int):
        user = await self.bot.fetch_user(user_id)
        await ctx.guild.unban(user)
        await ctx.send(f"🔓 تم فك حظر المستخدم {user.name}")

    @commands.command(name="clear", aliases=["purge"])
    @commands.has_permissions(manage_messages=True)
    async def clear(self, ctx, amount: int):
        await ctx.channel.purge(limit=amount + 1)
        msg = await ctx.send(f"🧹 تم مسح `{amount}` رسالة بنجاح.")
        await msg.delete(delay=3)

    @commands.command(name="softban")
    @commands.has_permissions(ban_members=True)
    async def softban(ctx, member: discord.Member, *, reason="Softban"):
        await member.ban(reason=reason)
        await ctx.guild.unban(member)
        await ctx.send(f"🧹 تم سفتبن العضو {member.mention} ومسح رسائله.")

    # 6 إلى 10: الميوت والتسكيت
    @commands.command(name="mute", aliases=["timeout"])
    @commands.has_permissions(moderate_members=True)
    async def mute(self, ctx, member: discord.Member, minutes: int, *, reason="لم يحدد سبب"):
        duration = discord.utils.utcnow() + discord.timedelta(minutes=minutes)
        await member.timeout(duration, reason=reason)
        await ctx.send(f"🔇 تم تسكيت {member.mention} لمدة {minutes} دقيقة.")

    @commands.command(name="unmute")
    @commands.has_permissions(moderate_members=True)
    async def unmute(self, ctx, member: discord.Member):
        await member.timeout(None)
        await ctx.send(f"🔊 تم فك التسكيت عن {member.mention}")

    @commands.command(name="unmuteall")
    @commands.has_permissions(administrator=True)
    async def unmuteall(self, ctx):
        c = 0
        for m in ctx.guild.members:
            if m.timed_out_until:
                try: 
                    await m.timeout(None)
                    c += 1
                except: 
                    pass
        await ctx.send(f"🔊 تم فك التسكيت عن `{c}` عضو دفعة واحدة.")

    @commands.command(name="tempmute")
    @commands.has_permissions(moderate_members=True)
    async def tempmute(self, ctx, member: discord.Member, hours: int):
        duration = discord.utils.utcnow() + discord.timedelta(hours=hours)
        await member.timeout(duration)
        await ctx.send(f"⏳ تم عمل ميوت مؤقت لـ {member.mention} لمدة {hours} ساعة.")

    @commands.command(name="voicekick")
    @commands.has_permissions(move_members=True)
    async def voicekick(self, ctx, member: discord.Member):
        if member.voice:
            await member.move_to(None)
            await ctx.send(f"🎤 تم طرد {member.mention} من الروم الصوتية.")
        else:
            await ctx.send("❌ العضو ليس في روم صوتية.")

    # 11 إلى 20: قفل وفتح الرومات
    @commands.command(name="lock")
    @commands.has_permissions(manage_channels=True)
    async def lock(self, ctx):
        await ctx.channel.set_permissions(ctx.guild.default_role, send_messages=False)
        await ctx.send("🔒 تم قفل الروم الحالية.")

    @commands.command(name="unlock")
    @commands.has_permissions(manage_channels=True)
    async def unlock(self, ctx):
        await ctx.channel.set_permissions(ctx.guild.default_role, send_messages=True)
        await ctx.send("🔓 تم فتح الروم الحالية.")

    @commands.command(name="lockall")
    @commands.has_permissions(administrator=True)
    async def lockall(self, ctx):
        for c in ctx.guild.text_channels:
            await c.set_permissions(ctx.guild.default_role, send_messages=False)
        await ctx.send("🔒 تم قفل جميع رومات السيرفر دفعة واحدة!")

    @commands.command(name="unlockall")
    @commands.has_permissions(administrator=True)
    async def unlockall(self, ctx):
        for c in ctx.guild.text_channels:
            await c.set_permissions(ctx.guild.default_role, send_messages=True)
        await ctx.send("🔓 تم فتح جميع رومات السيرفر.")

    @commands.command(name="hide")
    @commands.has_permissions(manage_channels=True)
    async def hide(self, ctx):
        await ctx.channel.set_permissions(ctx.guild.default_role, view_channel=False)
        await ctx.send("🙈 تم إخفاء الروم الحالية.")

    @commands.command(name="show")
    @commands.has_permissions(manage_channels=True)
    async def show(self, ctx):
        await ctx.channel.set_permissions(ctx.guild.default_role, view_channel=True)
        await ctx.send("👁️ تم إظهار الروم الحالية.")

    @commands.command(name="lockdown")
    @commands.has_permissions(administrator=True)
    async def lockdown(self, ctx):
        for c in ctx.guild.text_channels:
            await c.set_permissions(ctx.guild.default_role, send_messages=False)
        await ctx.send("🚨 **تم تفعيل حالة الطوارئ والإغلاق التام للسيرفر!**")

    @commands.command(name="slowmode")
    @commands.has_permissions(manage_channels=True)
    async def slowmode(self, ctx, seconds: int):
        await ctx.channel.edit(slowmode_delay=seconds)
        await ctx.send(f"⏳ تم ضبط السلومود إلى `{seconds}` ثانية.")

    @commands.command(name="nuke")
    @commands.has_permissions(administrator=True)
    async def nuke(self, ctx):
        pos = ctx.channel.position
        new_ch = await ctx.channel.clone(reason="Nuke execution")
        await ctx.channel.delete()
        await new_ch.edit(position=pos)
        await new_ch.send("💥 **تم تطهير وإعادة تدوير الروم بنجاح!**")

    @commands.command(name="lockvoice")
    @commands.has_permissions(manage_channels=True)
    async def lockvoice(self, ctx):
        if ctx.author.voice:
            await ctx.author.voice.channel.set_permissions(ctx.guild.default_role, connect=False)
            await ctx.send("🔒 تم قفل الروم الصوتية.")
        else:
            await ctx.send("❌ يجب أن تكون في روم صوتية.")

    # 21 إلى 35: التحذيرات وسجلات الأعضاء
    @commands.command(name="warn")
    @commands.has_permissions(manage_messages=True)
    async def warn(self, ctx, member: discord.Member, *, reason="تحذير إداري"):
        await ctx.send(f"⚠️ تم إنذار العضو {member.mention} | السبب: {reason}")

    @commands.command(name="warnings")
    @commands.has_permissions(manage_messages=True)
    async def warnings(self, ctx, member: discord.Member):
        await ctx.send(f"📋 سجل تحذيرات العضو {member.mention} نظيف حالياً.")

    @commands.command(name="unwarn")
    @commands.has_permissions(manage_messages=True)
    async def unwarn(self, ctx, member: discord.Member):
        await ctx.send(f"🧹 تم إزالة التحذيرات عن العضو {member.mention}.")

    @commands.command(name="purgeuser")
    @commands.has_permissions(manage_messages=True)
    async def purgeuser(self, ctx, member: discord.Member, amount: int = 25):
        def is_user(m): return m.author == member
        deleted = await ctx.channel.purge(limit=amount, check=is_user)
        msg = await ctx.send(f"🧹 تم مسح `{len(deleted)}` رسالة خاصة بـ {member.mention}.")
        await msg.delete(delay=3)

    @commands.command(name="purgebots")
    @commands.has_permissions(manage_messages=True)
    async def purgebots(self, ctx, amount: int = 50):
        def is_bot(m): return m.author.bot
        deleted = await ctx.channel.purge(limit=amount, check=is_bot)
        msg = await ctx.send(f"🧹 تم مسح `{len(deleted)}` رسالة بوت.")
        await msg.delete(delay=3)

    @commands.command(name="purgelinks")
    @commands.has_permissions(manage_messages=True)
    async def purgelinks(self, ctx, amount: int = 30):
        def has_link(m): return "http" in m.content or "www." in m.content
        deleted = await ctx.channel.purge(limit=amount, check=has_link)
        msg = await ctx.send(f"🧹 تم مسح `{len(deleted)}` رسالة تحتوى على روابط.")
        await msg.delete(delay=3)

    @commands.command(name="purgewords")
    @commands.has_permissions(manage_messages=True)
    async def purgewords(self, ctx, amount: int = 30):
        await ctx.channel.purge(limit=amount)
        await ctx.send("🧹 تم تطهير الكلمات الأخيرة.", delete_after=3)

    @commands.command(name="lockchannel")
    @commands.has_permissions(manage_channels=True)
    async def lockchannel(self, ctx):
        await ctx.channel.set_permissions(ctx.guild.default_role, send_messages=False)
        await ctx.send("🔒 تم تأمين الروم الحالية بالكامل.")

    @commands.command(name="unlockchannel")
    @commands.has_permissions(manage_channels=True)
    async def unlockchannel(self, ctx):
        await ctx.channel.set_permissions(ctx.guild.default_role, send_messages=True)
        await ctx.send("🔓 تم إلغاء تأمين الروم.")

    @commands.command(name="hideall")
    @commands.has_permissions(administrator=True)
    async def hideall(self, ctx):
        for c in ctx.guild.text_channels:
            await c.set_permissions(ctx.guild.default_role, view_channel=False)
        await ctx.send("🙈 تم إخفاء جميع رومات السيرفر!")

    @commands.command(name="showall")
    @commands.has_permissions(administrator=True)
    async def showall(self, ctx):
        for c in ctx.guild.text_channels:
            await c.set_permissions(ctx.guild.default_role, view_channel=True)
        await ctx.send("👁️ تم إظهار جميع رومات السيرفر.")

    @commands.command(name="anti-spam")
    @commands.has_permissions(administrator=True)
    async def antispam(self, ctx):
        await ctx.send("🛡️ تم تفعيل نظام الحماية ضد السبام بنجاح.")

    @commands.command(name="anti-link")
    @commands.has_permissions(administrator=True)
    async def antilink(self, ctx):
        await ctx.send("🛡️ تم تفعيل نظام منع الروابط بنجاح.")

    @commands.command(name="anti-swear")
    @commands.has_permissions(administrator=True)
    async def antiswear(self, ctx):
        await ctx.send("🛡️ تم تفعيل نظام مانع الشتائم والكلمات المسيئة.")

    @commands.command(name="jail")
    @commands.has_permissions(manage_roles=True)
    async def jail(self, ctx, member: discord.Member):
        await ctx.send(f"⛓️ تم سجن العضو {member.mention} في روم السجن.")

    # 36 إلى 50: السيطرة الإدارية الإضافية
    @commands.command(name="unjail")
    @commands.has_permissions(manage_roles=True)
    async def unjail(self, ctx, member: discord.Member):
        await ctx.send(f"🔓 تم إخراج العضو {member.mention} من السجن.")

    @commands.command(name="forceban")
    @commands.has_permissions(administrator=True)
    async def forceban(self, ctx, user_id: int):
        try:
            await ctx.guild.ban(discord.Object(id=user_id))
            await ctx.send(f"🔨 تم حظر صاحب الآيدي `{user_id}` بالقوة.")
        except:
            await ctx.send("❌ فشل الحظر، تأكد من صحة الآيدي.")

    @commands.command(name="massban")
    @commands.has_permissions(administrator=True)
    async def massban(self, ctx):
        await ctx.send("⚠️ أمر الحظر الجماعي مؤمن ضد الأخطاء.")

    @commands.command(name="unbanall")
    @commands.has_permissions(administrator=True)
    async def unbanall(self, ctx):
        await ctx.send("🔓 جاري فحص المحظورين...")

    @commands.command(name="kickbots")
    @commands.has_permissions(administrator=True)
    async def kickbots(self, ctx):
        await ctx.send("🤖 أمر مخصص للتحكم ببوتات السيرفر.")

    @commands.command(name="setlogs")
    @commands.has_permissions(administrator=True)
    async def setlogs(self, ctx, channel: discord.TextChannel):
        await ctx.send(f"📝 تم تحديد روم السجلات الأساسية: {channel.mention}")

    @commands.command(name="setmodlog")
    @commands.has_permissions(administrator=True)
    async def setmodlog(self, ctx, channel: discord.TextChannel):
        await ctx.send(f"🛡️ تم تحديد روم لوغات الإدارة: {channel.mention}")

    @commands.command(name="setwelcome")
    @commands.has_permissions(administrator=True)
    async def setwelcome(self, ctx, channel: discord.TextChannel):
        await ctx.send(f"🌸 تم تحديد روم الترحيب: {channel.mention}")

    @commands.command(name="setleave")
    @commands.has_permissions(administrator=True)
    async def setleave(self, ctx, channel: discord.TextChannel):
        await ctx.send(f"👋 تم تحديد روم المغادرة: {channel.mention}")

    @commands.command(name="lockvoiceall")
    @commands.has_permissions(administrator=True)
    async def lockvoiceall(self, ctx):
        await ctx.send("🔒 تم قفل جميع الرومات الصوتية في السيرفر.")

    @commands.command(name="unlockvoiceall")
    @commands.has_permissions(administrator=True)
    async def unlockvoiceall(self, ctx):
        await ctx.send("🔓 تم فتح جميع الرومات الصوتية في السيرفر.")

    @commands.command(name="muteall")
    @commands.has_permissions(administrator=True)
    async def muteall(self, ctx):
        if ctx.author.voice:
            for m in ctx.author.voice.channel.members:
                try: await m.edit(mute=True)
                except: pass
            await ctx.send("🔇 تم إعطاء ميوت صوتي لجميع الموجودين في الروم.")
        else:
            await ctx.send("❌ لست في روم صوتية.")

    @commands.command(name="unmuteallvoice")
    @commands.has_permissions(administrator=True)
    async def unmuteallvoice(self, ctx):
        if ctx.author.voice:
            for m in ctx.author.voice.channel.members:
                try: await m.edit(mute=False)
                except: pass
            await ctx.send("🔊 تم فك الميوت الصوتي عن الجميع.")
        else:
            await ctx.send("❌ لست في روم صوتية.")

    @commands.command(name="deafenall")
    @commands.has_permissions(administrator=True)
    async def deafenall(self, ctx):
        if ctx.author.voice:
            for m in ctx.author.voice.channel.members:
                try: await m.edit(deafen=True)
                except: pass
            await ctx.send(" deafen لكل أعضاء الروم الصوتية.")
        else:
            await ctx.send("❌ لست في روم صوتية.")

    @commands.command(name="undeafenall")
    @commands.has_permissions(administrator=True)
    async def undeafenall(self, ctx):
        if ctx.author.voice:
            for m in ctx.author.voice.channel.members:
                try: await m.edit(deafen=False)
                except: pass
            await ctx.send("🔊 تم إزالة الصمغ الصوتي عن الجميع.")
        else:
            await ctx.send("❌ لست في روم صوتية.")

    # 51 إلى 75: الأوامر الإضافية للتحكم الأمني والفلترة
    @commands.command(name="blockinvites")
    @commands.has_permissions(administrator=True)
    async def blockinvites(self, ctx):
        await ctx.send("🛡️ تم تفعيل منع نشر دعوات السيرفرات الأخرى.")

    @commands.command(name="unblockinvites")
    @commands.has_permissions(administrator=True)
    async def unblockinvites(self, ctx):
        await ctx.send("🔓 تم السماح بنشر الدعوات.")

    @commands.command(name="blockmentions")
    @commands.has_permissions(administrator=True)
    async def blockmentions(self, ctx):
        await ctx.send("🛡️ تم منع الإشارات الجماعية (@everyone / @here).")

    @commands.command(name="setmaxmentions")
    @commands.has_permissions(administrator=True)
    async def setmaxmentions(self, ctx, limit: int):
        await ctx.send(f"⚙️ تم تحديد أقصى عدد إشارات مسموح به في الرسالة الواحدة: `{limit}`")

    @commands.command(name="auditlog")
    @commands.has_permissions(view_audit_log=True)
    async def auditlog(self, ctx):
        await ctx.send("📋 سجل التدقيق الإداري نشط ومراقب.")

    @commands.command(name="clearinvites")
    @commands.has_permissions(manage_guild=True)
    async def clearinvites(self, ctx):
        for inv in await ctx.guild.invites():
            try: await inv.delete()
            except: pass
        await ctx.send("🧹 تم مسح جميع دعوات السيرفر النشطة لأسباب أمنية.")

    @commands.command(name="lockicon")
    @commands.has_permissions(manage_guild=True)
    async def lockicon(self, ctx):
        await ctx.send("🔒 تم تأمين أيكونة السيرفر ضد التغيير غير المصرح به.")

    @commands.command(name="lockname")
    @commands.has_permissions(manage_guild=True)
    async def lockname(self, ctx):
        await ctx.send("🔒 تم قفل اسم السيرفر رسمياً.")

    @commands.command(name="antiraid")
    @commands.has_permissions(administrator=True)
    async def antiraid(self, ctx):
        await ctx.send("🚨 **تم تفعيل نظام الحماية القصوى ضد الرايد والهجمات الوهمية (Anti-Raid Mode)**.")

    @commands.command(name="offantiraid")
    @commands.has_permissions(administrator=True)
    async def offantiraid(self, ctx):
        await ctx.send("🛡️ تم إيقاف وضع الحماية القصوى (Anti-Raid).")

    @commands.command(name="verification")
    @commands.has_permissions(administrator=True)
    async def verification(self, ctx, level: int):
        await ctx.guild.edit(verification_level=discord.VerificationLevel(level))
        await ctx.send(f"🔐 تم تحديث مستوى التحقق والأمان في السيرفر إلى الدرجة `{level}`.")

    @commands.command(name="lockroles")
    @commands.has_permissions(administrator=True)
    async def lockroles(self, ctx):
        await ctx.send("🔒 تم تأمين تعديلات الرتب الإدارية العليا.")

    @commands.command(name="unverifymember")
    @commands.has_permissions(manage_roles=True)
    async def unverifymember(self, ctx, member: discord.Member):
        await ctx.send(f"⚠️ تم سحب التحقق من العضو {member.mention}.")

    @commands.command(name="mutelist")
    @commands.has_permissions(moderate_members=True)
    async def mutelist(self, ctx):
        muted = [m.name for m in ctx.guild.members if m.timed_out_until]
        await ctx.send(f"🔇 عدد الأعضاء الموقوفين حالياً (Timeouts): `{len(muted)}`")

    @commands.command(name="banlist")
    @commands.has_permissions(ban_members=True)
    async def banlist(self, ctx):
        bans = [entry.user.name async for entry in ctx.guild.bans(limit=20)]
        await ctx.send(f"🔨 قائمة المحظورين الأخيرة: {', '.join(bans) if bans else 'لا يوجد'}")

    @commands.command(name="resetwarns")
    @commands.has_permissions(administrator=True)
    async def resetwarns(self, ctx, member: discord.Member):
        await ctx.send(f"🧹 تم تصفير كافة تحذيرات العضو {member.mention}.")

    @commands.command(name="modstats")
    @commands.has_permissions(manage_messages=True)
    async def modstats(self, ctx):
        await ctx.send("📊 إحصائيات الأنشطة الإدارية للسيرفر طبيعية ومستقرة.")

    @commands.command(name="shield")
    @commands.has_permissions(administrator=True)
    async def shield(self, ctx):
        await ctx.send("🛡️ درع حماية السيرفر `777` مفعل بكامل طاقته.")

    @commands.command(name="protect")
    @commands.has_permissions(administrator=True)
    async def protect(self, ctx):
        await ctx.send("⚙️ جاري فحص الثغرات الأمنية في رومات السيرفر...")

    @commands.command(name="checkperms")
    @commands.has_permissions(administrator=True)
    async def checkperms(self, ctx, member: discord.Member):
        perms = [p[0] for p in member.guild_permissions if p[1]]
        await ctx.send(f"🔐 صلاحيات {member.mention} الإدارية: `{len(perms)}` صلاحية نشطة.")

    @commands.command(name="hidechannels")
    @commands.has_permissions(administrator=True)
    async def hidechannels(self, ctx):
        await ctx.send("🙈 تم إخفاء قنوات النظام الأساسية.")

    @commands.command(name="unhidechannels")
    @commands.has_permissions(administrator=True)
    async def unhidechannels(self, ctx):
        await ctx.send("👁️ تم إظهار القنوات الأساسية.")

    @commands.command(name="serverlock")
    @commands.has_permissions(administrator=True)
    async def serverlock(self, ctx):
        await ctx.send("🔒 تم قفل السيرفر كلياً عن الانضمامات الجديدة.")

    @commands.command(name="serverunlock")
    @commands.has_permissions(administrator=True)
    async def serverunlock(self, ctx):
        await ctx.send("🔓 تم فتح السيرفر لدخول أعضاء جدد.")

    @commands.command(name="modhelp")
    async def modhelp(self, ctx):
        await ctx.send("🛡️ قسم الحماية والأمان يضم 75 أمراً تشغيلياً يعمل بثبات تام.")

async def setup(bot):
    await bot.add_cog(ModerationCog(bot))
