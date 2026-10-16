import discord
from discord.ext import commands

class StatsCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="server", aliases=["serverinfo"])
    async def server_info(self, ctx):
        guild = ctx.guild
        online_count = sum(1 for m in guild.members if m.status != discord.Status.offline)
        
        # حساب عمر السيرفر بالتاريخ
        created_at = guild.created_at.strftime("%Y/%m/%d")
        
        embed = discord.Embed(
            title=f"🌸 سرفر {guild.name}",
            color=0xffc0cb  # اللون الوردي الخاص بسيرفر 777
        )
        
        if guild.icon:
            embed.set_thumbnail(url=guild.icon.url)
            
        embed.add_field(name="🆔 آيدي السيرفر", value=f"`{guild.id}`", inline=False)
        
        if guild.owner:
            embed.add_field(name="👑 مالك السيرفر", value=f"{guild.owner.mention}", inline=False)
            
        embed.add_field(name="📅 تاريخ الإنشاء", value=f"`{created_at}`", inline=False)
        
        members_text = f"العدد الكلي: **{guild.member_count}** | الأونلاين: **{online_count}**"
        embed.add_field(name="👥 الأعضاء", value=members_text, inline=False)
        
        boosts = guild.premium_subscription_count
        embed.add_field(name="🚀 البوستات", value=f"`{boosts}` بوست", inline=False)
        
        text_channels = len(guild.text_channels)
        voice_channels = len(guild.voice_channels)
        categories = len(guild.categories)
        channels_summary = f"💬 كتابية: `{text_channels}` | 🔊 صوتية: `{voice_channels}` | 📁 أقسام: `{categories}`"
        embed.add_field(name="💬 الرومات", value=channels_summary, inline=False)
        
        roles_count = len(guild.roles) - 1  # خصم رتبة @everyone
        embed.add_field(name="🎭 الرولات", value=f"`{roles_count}` رتبة", inline=False)
        
        embed.set_footer(text=f"Requested by {ctx.author.name} | 777 System", icon_url=ctx.author.display_avatar.url)
        
        await ctx.send(embed=embed)

async def setup(bot):
    await bot.add_cog(StatsCog(bot))
