import os
import discord
from discord import app_commands
from discord.ext import commands
from discord.ui import Button, View

intents = discord.Intents.all()

class NovaProBot(commands.Bot):
    def __init__(self):
        super().__init__(command_prefix="!", intents=intents, help_command=None)

    async def setup_hook(self):
        await self.tree.sync()
        print("✅ Slash commands successfully synced with Discord!")

bot = NovaProBot()
AUTO_ROLE_NAME = None

@bot.event
async def on_ready():
    print(f"Logged in as {bot.user.name} (ID: {bot.user.id})")
    print("🚀 777 Ultimate Nova-Style System is Online!")
    await bot.change_presence(activity=discord.Game(name="/help | 777 Ultimate System"))

class UltraHelpView(View):
    def __init__(self):
        super().__init__(timeout=180)

    @discord.ui.button(label="Moderation & Security", style=discord.ButtonStyle.danger, emoji="🔨")
    async def mod_sec(self, interaction: discord.Interaction, button: Button):
        embed = discord.Embed(
            title="🔨 Moderation & Security Panel",
            description="Control and protection commands for 777 server:",
            color=0x2b2d31
        )
        embed.add_field(name="`!kick` / `/kick`", value="Kick a member from the server", inline=False)
        embed.add_field(name="`!ban` / `/ban`", value="Ban a member permanently", inline=False)
        embed.add_field(name="`!clear` / `/clear`", value="Purge chat messages smoothly", inline=False)
        embed.add_field(name="`!autorole [role]`", value="Set automatic role for newcomers", inline=False)
        embed.add_field(name="`!daorole`", value="Disable auto-role system", inline=False)
        embed.add_field(name="`!role` / `!addrole` [@user] [role]", value="Add a specific role to a user", inline=False)
        embed.add_field(name="`!allrole [role]`", value="Give a role to all members at once", inline=False)
        embed.add_field(name="`!r_all [role]`", value="Remove a role from all members", inline=False)
        embed.set_footer(text="777 System • Security Engine")
        await interaction.response.edit_message(embed=embed, view=self)

    @discord.ui.button(label="Server & User Stats", style=discord.ButtonStyle.success, emoji="📊")
    async def general_sec(self, interaction: discord.Interaction, button: Button):
        embed = discord.Embed(
            title="📊 Statistics & User Info Panel",
            description="Explore precise server statistics and user cards:",
            color=0x2b2d31
        )
        embed.add_field(name="`!server` / `/server`", value="Show advanced server statistics (Nova Style)", inline=False)
        embed.add_field(name="`!id` / `/user`", value="Show user profile card, ID, and join dates", inline=False)
        embed.add_field(name="`!avatar` [@user]", value="View user avatar in high quality", inline=False)
        embed.add_field(name="`!banner` [@user]", value="View user custom banner", inline=False)
        embed.set_footer(text="777 System • Information Engine")
        await interaction.response.edit_message(embed=embed, view=self)

    @discord.ui.button(label="Visuals & Images", style=discord.ButtonStyle.secondary, emoji="🎨")
    async def image_sec(self, interaction: discord.Interaction, button: Button):
        embed = discord.Embed(
            title="🎨 Visuals & Filters Panel",
            description="Aesthetic and styling tools:",
            color=0x2b2d31
        )
        embed.add_field(name="`!circle` [@user]", value="Show user avatar inside a circular frame", inline=False)
        embed.add_field(name="`!colors`", value="View server color palette options", inline=False)
        embed.set_footer(text="777 System • Visual Engine")
        await interaction.response.edit_message(embed=embed, view=self)

@bot.command(name="help")
async def help_cmd(ctx):
    embed = discord.Embed(
        title="🌟 777 Control Panel • Central System",
        description="Welcome to the advanced system.\nPlease select a section using the buttons below:",
        color=0x2b2d31
    )
    if ctx.guild.icon:
        embed.set_thumbnail(url=ctx.guild.icon.url)
    embed.set_footer(text=f"Requested by {ctx.author.name}", icon_url=ctx.author.display_avatar.url)
    view = UltraHelpView()
    await ctx.send(embed=embed, view=view)

@bot.tree.command(name="help", description="Show bot control panel and command list")
async def help_slash(interaction: discord.Interaction):
    embed = discord.Embed(
        title="🌟 777 Control Panel • Central System",
        description="Welcome to the advanced system.\nPlease select a section using the buttons below:",
        color=0x2b2d31
    )
    if interaction.guild.icon:
        embed.set_thumbnail(url=interaction.guild.icon.url)
    view = UltraHelpView()
    await interaction.response.send_message(embed=embed, view=view)

def build_server_embed(guild):
    online_count = sum(1 for m in guild.members if m.status != discord.Status.offline)
    embed = discord.Embed(title=guild.name, color=0x2b2d31)
    if guild.icon:
        embed.set_thumbnail(url=guild.icon.url)
        
    embed.add_field(name="🆔 Server ID", value=f"`{guild.id}`", inline=False)
    embed.add_field(name="👑 Owned By", value=f"{guild.owner.mention if guild.owner else 'Unknown'}", inline=False)
    embed.add_field(name="📅 Server Age", value=f"{discord.utils.format_dt(guild.created_at, 'R')}", inline=False)
    embed.add_field(name="👥 Members", value=f"**Total:** {guild.member_count} | **Online:** {online_count}", inline=False)
    embed.add_field(name="💬 Channels", value=f"Text: {len(guild.text_channels)} | Voice: {len(guild.voice_channels)}", inline=False)
    embed.add_field(name="🎭 Roles", value=f"{len(guild.roles)}", inline=False)
    embed.set_footer(text="777 System • Server Statistics")
    return embed

@bot.command()
async def server(ctx):
    await ctx.send(embed=build_server_embed(ctx.guild))

@bot.tree.command(name="server", description="Show advanced server statistics")
async def server_slash(interaction: discord.Interaction):
    await interaction.response.send_message(embed=build_server_embed(interaction.guild))

@bot.command()
@commands.has_permissions(kick_members=True)
async def kick(ctx, member: discord.Member, *, reason="No reason provided"):
    await member.kick(reason=reason)
    embed = discord.Embed(title="👢 Kick Action Executed", description=f"**Target:** {member.mention}\n**By:** {ctx.author.mention}\n**Reason:** {reason}", color=0xFF0000)
    await ctx.send(embed=embed)

@bot.tree.command(name="kick", description="Kick a disruptive member")
@app_commands.checks.has_permissions(kick_members=True)
async def kick_slash(interaction: discord.Interaction, member: discord.Member, reason: str = "No reason provided"):
    await member.kick(reason=reason)
    embed = discord.Embed(title="👢 Kick Action Executed", description=f"**Target:** {member.mention}\n**By:** {interaction.user.mention}\n**Reason:** {reason}", color=0xFF0000)
    await interaction.response.send_message(embed=embed)

@bot.command()
@commands.has_permissions(ban_members=True)
async def ban(ctx, member: discord.Member, *, reason="No reason provided"):
    await member.ban(reason=reason)
    embed = discord.Embed(title="🔨 Ban Action Executed", description=f"**Target:** {member.mention}\n**By:** {ctx.author.mention}\n**Reason:** {reason}", color=0xFF0000)
    await ctx.send(embed=embed)

@bot.tree.command(name="ban", description="Ban a member permanently")
@app_commands.checks.has_permissions(ban_members=True)
async def ban_slash(interaction: discord.Interaction, member: discord.Member, reason: str = "No reason provided"):
    await member.ban(reason=reason)
    embed = discord.Embed(title="🔨 Ban Action Executed", description=f"**Target:** {member.mention}\n**By:** {interaction.user.mention}\n**Reason:** {reason}", color=0xFF0000)
    await interaction.response.send_message(embed=embed)

@bot.command()
@commands.has_permissions(manage_messages=True)
async def clear(ctx, amount: int):
    await ctx.channel.purge(limit=amount + 1)
    msg = await ctx.send(f"🧹 Successfully purged `{amount}` messages.")
    await msg.delete(delay=3)

@bot.tree.command(name="clear", description="Purge a specific amount of messages")
@app_commands.checks.has_permissions(manage_messages=True)
async def clear_slash(interaction: discord.Interaction, amount: int):
    await interaction.channel.purge(limit=amount)
    await interaction.response.send_message(f"🧹 Successfully purged `{amount}` messages.", ephemeral=True)

@bot.command(name="id", aliases=["user", "profile"])
async def user_id(ctx, member: discord.Member = None):
    m = member or ctx.author
    embed = discord.Embed(title=f"User Profile • {m.name}", color=0x2b2d31)
    embed.set_thumbnail(url=m.display_avatar.url)
    embed.add_field(name="🆔 User ID", value=f"`{m.id}`", inline=False)
    embed.add_field(name="📅 Account Created", value=f"{discord.utils.format_dt(m.created_at, 'R')}", inline=False)
    embed.add_field(name="📥 Server Joined", value=f"{discord.utils.format_dt(m.joined_at, 'R') if m.joined_at else 'N/A'}", inline=False)
    embed.set_footer(text="777 System • User Intelligence")
    await ctx.send(embed=embed)

@bot.command()
@commands.has_permissions(manage_roles=True)
async def role(ctx, member: discord.Member, role: discord.Role):
    await member.add_roles(role)
    embed = discord.Embed(title="✨ Role Granted", description=f"Successfully granted `{role.name}` to `{member.name}`.", color=0x00FF00)
    await ctx.send(embed=embed)

@bot.command()
@commands.has_permissions(manage_roles=True)
async def autorole(ctx, role: discord.Role):
    global AUTO_ROLE_NAME
    AUTO_ROLE_NAME = role.name
    embed = discord.Embed(title="🛡️ AutoRole Active", description=f"✅ AutoRole successfully set to: **{role.name}**", color=0x00FF00)
    await ctx.send(embed=embed)

@bot.command()
@commands.has_permissions(manage_roles=True)
async def daorole(ctx):
    global AUTO_ROLE_NAME
    AUTO_ROLE_NAME = None
    embed = discord.Embed(title="🛡️ AutoRole Disabled", description="❌ AutoRole system has been disabled.", color=0xFF0000)
    await ctx.send(embed=embed)

@bot.event
async def on_member_join(member):
    ch = discord.utils.get(member.guild.text_channels, name="welcome") or member.guild.system_channel
    if ch:
        embed = discord.Embed(
            title="🌸 New Member Arrived",
            description=f"Welcome {member.mention} to 777 Server! We are glad to have you here.",
            color=0x2b2d31
        )
        embed.set_thumbnail(url=member.display_avatar.url)
        embed.set_footer(text=f"Total Members: {member.guild.member_count}")
        await ch.send(embed=embed)
        
    global AUTO_ROLE_NAME
    if AUTO_ROLE_NAME:
        r = discord.utils.get(member.guild.roles, name=AUTO_ROLE_NAME)
        if r:
            try:
                await member.add_roles(r)
            except Exception as e:
                print(f"AutoRole assignment error: {e}")

TOKEN = os.getenv("TOKEN")
bot.run(TOKEN)
