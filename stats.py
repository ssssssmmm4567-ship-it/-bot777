    @commands.command(name="server", aliases=["serverinfo"])
    async def server_info(self, ctx):
        guild = ctx.guild
        online_count = sum(1 for m in guild.members if m.status != discord.Status.offline)
        
        # حساب عمر السيرفر (تقريبي بالأشهر أو التاريخ)
        created_at = guild.created_at.strftime("%Y/%m/%d")
        
        embed = discord.Embed(
            description=f"● **{guild.name}**",
            color=0xffc0cb  # لون بينك فخم مطابق لهوية 777
        )
        
        if guild.icon:
            embed.set_thumbnail(url=guild.icon.url)
            
        embed.add_field(name="🆔 Server ID", value=f"`{guild.id}`", inline=False)
        
        if guild.owner:
            embed.add_field(name="👑 Owned By", value=f"{guild.owner.mention}", inline=False)
            
        embed.add_field(name="📅 Server Age", value=f"`{created_at}`", inline=False)
        embed.add_field(name="👥 Members", value=f"`{guild.member_count}`", inline=True)
        embed.add_field(name="🟢 Online", value=f"`{online_count}`", inline=True)
        embed.add_field(name="🚀 Boosts", value=f"`{guild.premium_subscription_count}`", inline=True)
        
        channels_text = f"💬 `{len(guild.text_channels)}` • 🔊 `{len(guild.voice_channels)}` • 📁 `{len(guild.categories)}`"
        embed.add_field(name="💬 Channels", value=channels_text, inline=False)
        
        roles_count = len(guild.roles) - 1
        embed.add_field(name="🎭 Roles", value=f"`{roles_count}`", inline=False)
        
        await ctx.send(embed=embed)
