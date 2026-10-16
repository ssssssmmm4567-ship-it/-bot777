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

@bot.command(name="roles")
async def roles_list(ctx):
    guild = ctx.guild
    # ترتيب الرولات من الأعلى للأقل
    roles = sorted(guild.roles, key=lambda r: r.position, reverse=True)
    # استثناء رتبة @everyone
    roles = [r for r in roles if r != guild.default_role]

    chunks = [roles[i:i + 15] for i in range(0, len(roles), 15)]
    embeds = []

    for index, chunk in enumerate(chunks):
        embed = discord.Embed(
            title=f"🎭 رولات السيرفر (الصفحة {index + 1}/{len(chunks)})",
            description=f"إجمالي رولات السيرفر: **{len(roles)}** رتبة",
            color=0x2b2d31
        )
        roles_text = "\n".join([f"{r.mention} — (`{len(r.members)}` عضو)" for r in chunk])
        embed.add_field(name="القائمة:", value=roles_text, inline=False)
        embeds.append(embed)

    if embeds:
        view = RolesPaginationView(embeds)
        await ctx.send(embed=embeds[0], view=view)
    else:
        await ctx.send("❌ لا توجد رولات في السيرفر.")
