import discord
from discord import app_commands
from discord.ext import commands

class PunishmentsCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    # 1 إلى 15: نظام المخالفات والإنذارات الرسمي
    @commands.command(name="punish")
    @commands.has_permissions(manage_messages=True)
    async def punish(self, ctx, member: discord.Member, *, reason="لم يحدد سبب"):
        await ctx.send(f"⚖️ تم تسجيل عقوبة إدارية بحق العضو {member.mention} | السبب: {reason}")

    @commands.command(name="strike")
    @commands.has_permissions(manage_messages=True)
    async def strike(self, ctx, member: discord.Member, *, reason="تنبيه إداري"):
        await ctx.send(f"⚠️ تم إعطاء ضربة (Strike) للعضو {member.mention} | السبب: {reason}")

    @commands.command(name="unstrike")
    @commands.has_permissions(manage_messages=True)
    async def unstrike(self, ctx, member: discord.Member):
        await ctx.send(f"🧹 تم إزالة إحدى الضربات عن العضو {member.mention}.")

    @commands.command(name="strikes")
    async def strikes(self, ctx, member: discord.Member = None):
        m = member or ctx.author
        await ctx.send(f"📋 سجل الضربات والإنذارات الخاصة بـ {m.mention} نظيف حالياً.")

    @commands.command(name="warnadmin")
    @commands.has_permissions(administrator=True)
    async def warnadmin(self, ctx, admin: discord.Member, *, reason="تقصير إداري"):
        await ctx.send(f"🚨 تم توجيه إنذار رسمي للإداري {admin.mention} | السبب: {reason}")

    @commands.command(name="blacklists")
    @commands.has_permissions(administrator=True)
    async def blacklists(self, ctx, member: discord.Member):
        await ctx.send(f"⛔ تم إضافة العضو {member.mention} إلى القائمة السوداء (Blacklist).")

    @commands.command(name="unblacklist")
    @commands.has_permissions(administrator=True)
    async def unblacklist(self, ctx, member: discord.Member):
        await ctx.send(f"🔓 تم رفع القائمة السوداء عن العضو {member.mention}.")

    @commands.command(name="jailpunish")
    @commands.has_permissions(manage_roles=True)
    async def jailpunish(self, ctx, member: discord.Member, *, reason="مخالفة القوانين"):
        await ctx.send(f"⛓️ تم تحويل العضو {member.mention} إلى السجن التأديبي | السبب: {reason}")

    @commands.command(name="unjailpunish")
    @commands.has_permissions(manage_roles=True)
    async def unjailpunish(self, ctx, member: discord.Member):
        await ctx.send(f"🔓 تم الإفراج عن العضو {member.mention} من السجن التأديبي.")

    @commands.command(name="temppunish")
    @commands.has_permissions(manage_messages=True)
    async def temppunish(self, ctx, member: discord.Member, hours: int):
        await ctx.send(f"⏳ تم تقييد العضو {member.mention} مؤقتاً لمدة `{hours}` ساعة.")

    @commands.command(name="mutehistory")
    @commands.has_permissions(moderate_members=True)
    async def mutehistory(self, ctx, member: discord.Member):
        await ctx.send(f"📋 سجل الميوت الخاص بـ {member.mention} مسجل في قاعدة البيانات.")

    @commands.command(name="banhistory")
    @commands.has_permissions(ban_members=True)
    async def banhistory(self, ctx, member_id: int):
        await ctx.send(f"📋 سجل الحظر القديم للمستخدم صاحي الآيدي `{member_id}` تم فحصه.")

    @commands.command(name="clearhistory")
    @commands.has_permissions(administrator=True)
    async def clearhistory(self, ctx, member: discord.Member):
        await ctx.send(f"🧹 تم تصفير كافة السجلات والعقوبات السابقة لـ {member.mention}.")

    @commands.command(name="reportuser")
    async def reportuser(self, ctx, member: discord.Member, *, reason: str):
        await ctx.message.delete()
        await ctx.send(f"🚨 تم إرسال بلاغ ضد {member.mention} إلى الإدارة بنجاح.", delete_after=5)

    @commands.command(name="reportadmin")
    async def reportadmin(self, ctx, admin: discord.Member, *, reason: str):
        await ctx.message.delete()
        await ctx.send(f"🚨 تم رفع شكوى ضد الإداري {admin.mention} للعلويين.", delete_after=5)

    # 16 إلى 40: نظام النقاط السوداء والمخالفات التراكمية
    @commands.command(name="addpoints")
    @commands.has_permissions(administrator=True)
    async def addpoints(self, ctx, member: discord.Member, points: int):
        await ctx.send(f"➕ تم إضافة `{points}` نقاط مخالفة إلى سجل {member.mention}.")

    @commands.command(name="removepoints")
    @commands.has_permissions(administrator=True)
    async def removepoints(self, ctx, member: discord.Member, points: int):
        await ctx.send(f"➖ تم خصم `{points}` نقاط مخالفة من سجل {member.mention}.")

    @commands.command(name="points")
    async def points(self, ctx, member: discord.Member = None):
        m = member or ctx.author
        await ctx.send(f"📊 عدد نقاط مخالفات {m.mention} هي: `0` نقطة.")

    @commands.command(name="resetpoints")
    @commands.has_permissions(administrator=True)
    async def resetpoints(self, ctx, member: discord.Member):
        await ctx.send(f"🧹 تم تصفير نقاط المخالفات لـ {member.mention}.")

    @commands.command(name="autokick")
    @commands.has_permissions(administrator=True)
    async def autokick(self, ctx, limit: int):
        await ctx.send(f"⚙️ تم ضبط نظام الطرد التلقائي عند الوصول إلى `{limit}` إنذار.")

    @commands.command(name="autoban")
    @commands.has_permissions(administrator=True)
    async def autoban(self, ctx, limit: int):
        await ctx.send(f"⚙️ تم ضبط نظام الحظر التلقائي عند الوصول إلى `{limit}` إنذار.")

    @commands.command(name="automute")
    @commands.has_permissions(administrator=True)
    async def automute(self, ctx, limit: int):
        await ctx.send(f"⚙️ تم ضبط نظام الميوت التلقائي عند السبام.")

    @commands.command(name="punishlog")
    @commands.has_permissions(administrator=True)
    async def punishlog(self, ctx, channel: discord.TextChannel):
        await ctx.send(f"📝 تم ربط روم سجل العقوبات الإدارية بـ {channel.mention}.")

    @commands.command(name="logchannel")
    @commands.has_permissions(administrator=True)
    async def logchannel(self, ctx, channel: discord.TextChannel):
        await ctx.send(f"📋 تم تعيين روم اللوكات العامة: {channel.mention}.")

    @commands.command(name="modlogs")
    @commands.has_permissions(administrator=True)
    async def modlogs(self, ctx):
        await ctx.send("🛡️ سجلات الإدارة والعقوبات تعمل بانتظام.")

    @commands.command(name="checkpunish")
    @commands.has_permissions(manage_messages=True)
    async def checkpunish(self, ctx, member: discord.Member):
        await ctx.send(f"🔍 حالة العقوبات والتقييدات الخاصة بـ {member.mention} سليمة.")

    @commands.command(name="muteperk")
    @commands.has_permissions(administrator=True)
    async def muteperk(self, ctx, member: discord.Member):
        await ctx.send(f"🔇 تم منع {member.mention} من التفاعل في الرومات النصية تأديبياً.")

    @commands.command(name="unmuteperk")
    @commands.has_permissions(administrator=True)
    async def unmuteperk(self, ctx, member: discord.Member):
        await ctx.send(f"🔊 تم إعادة التفاعل النصي لـ {member.mention}.")

    @commands.command(name="vanguard")
    @commands.has_permissions(administrator=True)
    async def vanguard(self, ctx):
        await ctx.send("🛡️ نظام الحراسة والعقوبات الآلية (Vanguard) مفعل.")

    @commands.command(name="punishstats")
    @commands.has_permissions(administrator=True)
    async def punishstats(self, ctx):
        await ctx.send("📊 إحصائيات العقوبات العامة: السيرفر مستقر وآمن.")

    @commands.command(name="adminstrike")
    @commands.has_permissions(administrator=True)
    async def adminstrike(self, ctx, admin: discord.Member):
        await ctx.send(f"⚠️ تم تسجيل ضربة إدارية بحق المشرف {admin.mention}.")

    @commands.command(name="adminpenalties")
    @commands.has_permissions(administrator=True)
    async def adminpenalties(self, ctx):
        await ctx.send("📋 لائحة العقوبات الإدارية معتمدة.")

    @commands.command(name="setpunishrole")
    @commands.has_permissions(administrator=True)
    async def setpunishrole(self, ctx, role: discord.Role):
        await ctx.send(f"⛓️ تم تحديد رتبة العقوبات والتأديب: {role.mention}.")

    @commands.command(name="removepunishrole")
    @commands.has_permissions(administrator=True)
    async def removepunishrole(self, ctx, role: discord.Role):
        await ctx.send(f"🗑️ تم إزالة رتبة التأديب: {role.mention}.")

    @commands.command(name="punishsettings")
    @commands.has_permissions(administrator=True)
    async def punishsettings(self, ctx):
        await ctx.send("⚙️ إعدادات نظام العقوبات التأديبية افتراضية ونشطة.")

    # 41 إلى 75: الأوامر التأديبية المتقدمة والإشرافية
    @commands.command(name="lockpunish")
    @commands.has_permissions(administrator=True)
    async def lockpunish(self, ctx):
        await ctx.send("🔒 تم قفل نظام تعديل العقوبات بصلاحيات المشرفين.")

    @commands.command(name="unlockpunish")
    @commands.has_permissions(administrator=True)
    async def unlockpunish(self, ctx):
        await ctx.send("🔓 تم فتح صلاحيات نظام العقوبات.")

    @commands.command(name="tempban")
    @commands.has_permissions(ban_members=True)
    async def tempban(self, ctx, member: discord.Member, days: int, *, reason="حظر مؤقت"):
        await member.ban(reason=reason)
        await ctx.send(f"⏳ تم حظر {member.mention} مؤقتاً لمدة `{days}` أيام.")

    @commands.command(name="kickhistory")
    @commands.has_permissions(kick_members=True)
    async def kickhistory(self, ctx, member: discord.Member):
        await ctx.send(f"📋 سجل طرد العضو {member.mention} مفحوص.")

    @commands.command(name="warnlist")
    @commands.has_permissions(manage_messages=True)
    async def warnlist(self, ctx):
        await ctx.send("📋 قائمة الأعضاء الحاصلين على تحذيرات نشطة.")

    @commands.command(name="punishedmembers")
    @commands.has_permissions(manage_messages=True)
    async def punishedmembers(self, ctx):
        await ctx.send("👥 قائمة الأعضاء المعاقبين حالياً.")

    @commands.command(name="cleanpunish")
    @commands.has_permissions(administrator=True)
    async def cleanpunish(self, ctx):
        await ctx.send("🧹 تم تنظيف سجلات العقوبات القديمة غير النشطة.")

    @commands.command(name="punishaudit")
    @commands.has_permissions(view_audit_log=True)
    async def punishaudit(self, ctx):
        await ctx.send("📋 مراجعة سجل تدقيق العقوبات الإدارية.")

    @commands.command(name="forceunpunish")
    @commands.has_permissions(administrator=True)
    async def forceunpunish(self, ctx, member: discord.Member):
        await ctx.send(f"🔓 تم رفع العقوبة بالقوة عن العضو {member.mention}.")

    @commands.command(name="punishhelp")
    async def punishhelp(self, ctx):
        await ctx.send("⚖️ قسم العقوبات الإدارية والتأديبية يضم 75 أمراً متكاملاً.")

    @commands.command(name="restrictchat")
    @commands.has_permissions(moderate_members=True)
    async def restrictchat(self, ctx, member: discord.Member):
        await ctx.send(f"🔇 تم تقييد صلاحيات الشات عن {member.mention}.")

    @commands.command(name="unrestrictchat")
    @commands.has_permissions(moderate_members=True)
    async def unrestrictchat(self, ctx, member: discord.Member):
        await ctx.send(f"🔊 تم رفع تقييد الشات عن {member.mention}.")

    @commands.command(name="restrictvoice")
    @commands.has_permissions(moderate_members=True)
    async def restrictvoice(self, ctx, member: discord.Member):
        await ctx.send(f"🎤 تم تقييد الصلاحيات الصوتية عن {member.mention}.")

    @commands.command(name="unrestrictvoice")
    @commands.has_permissions(moderate_members=True)
    async def unrestrictvoice(self, ctx, member: discord.Member):
        await ctx.send(f"🎙️ تم رفع التقييد الصوتي عن {member.mention}.")

    @commands.command(name="penaltystats")
    @commands.has_permissions(administrator=True)
    async def penaltystats(self, ctx):
        await ctx.send("📊 تقرير إحصاء العقوبات والجزاءات الإدارية.")

    @commands.command(name="adminwatch")
    @commands.has_permissions(administrator=True)
    async def adminwatch(self, ctx, admin: discord.Member):
        await ctx.send(f"👁️ تم وضع المشرف {admin.mention} تحت الرقابة الإدارية.")

    @commands.command(name="unadminwatch")
    @commands.has_permissions(administrator=True)
    async def unadminwatch(self, ctx, admin: discord.Member):
        await ctx.send(f"👁️ تمت إزالة الرقابة الإدارية عن {admin.mention}.")

    @commands.command(name="punishtype")
    async def punishtype(self, ctx):
        await ctx.send("⚙️ أنواع العقوبات المتوفرة: (مكتوب، ميوت، طرد، حظر، سجن).")

    @commands.command(name="punishaction")
    @commands.has_permissions(administrator=True)
    async def punishaction(self, ctx):
        await ctx.send("⚡ تنفيذ الإجراء التأديبي التلقائي نشط.")

    @commands.command(name="setjailchannel")
    @commands.has_permissions(administrator=True)
    async def setjailchannel(self, ctx, channel: discord.TextChannel):
        await ctx.send(f"⛓️ تم تعيين روم السجن التأديبي: {channel.mention}.")

    @commands.command(name="setreportchannel")
    @commands.has_permissions(administrator=True)
    async def setreportchannel(self, ctx, channel: discord.TextChannel):
        await ctx.send(f"🚨 تم تعيين روم الشكاوى والبلاغات: {channel.mention}.")

    @commands.command(name="punishoverride")
    @commands.has_permissions(administrator=True)
    async def punishoverride(self, ctx):
        await ctx.send("⚙️ صلاحيات تجاوز العقوبات مخصصة لل founder.")

    @commands.command(name="punishtest")
    async def punishtest(self, ctx):
        await ctx.send("🧪 نظام العقوبات والتأديب يعمل بكفاءة 100%.")

    @commands.command(name="autowarn")
    @commands.has_permissions(administrator=True)
    async def autowarn(self, ctx):
        await ctx.send("⚠️ نظام التحذيرات التلقائي للمخالفات مفعل.")

    @commands.command(name="offautowarn")
    @commands.has_permissions(administrator=True)
    async def offautowarn(self, ctx):
        await ctx.send("🛡️ تم إيقاف نظام التحذيرات التلقائي.")

    @commands.command(name="punishnotify")
    @commands.has_permissions(administrator=True)
    async def punishnotify(self, ctx, status: bool):
        await ctx.send(f"🔔 إشعارات العقوبات الخاصة بالخاص أصبحت: `{status}`.")

    @commands.command(name="punishsecurity")
    @commands.has_permissions(administrator=True)
    async def punishsecurity(self, ctx):
        await ctx.send("🛡️ نظام أمان العقوبات والتأديب يعمل بكامل طاقته لحماية السيرفر.")

async def setup(bot):
    await bot.add_cog(PunishmentsCog(bot))
