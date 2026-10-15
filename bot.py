import os
import discord
from discord.ext import commands

intents = discord.Intents.all()

class NovaEnterpriseBot(commands.Bot):
    def __init__(self):
        super().__init__(command_prefix="!", intents=intents, help_command=None)

    async def setup_hook(self):
        # تحميل الأقسام (Cogs) تلقائياً
        for filename in os.listdir("./cogs"):
            if filename.endswith(".py"):
                cog_name = filename[:-3]
                await self.load_extension(f"cogs.{cog_name}")
                print(f"📦 Loaded Cog: {cog_name}")
        await self.tree.sync()
        print("✅ All Cogs & Slash Commands Synchronized Successfully!")

bot = NovaEnterpriseBot()

@bot.event
async def on_ready():
    print(f"Logged in as {bot.user.name} (ID: {bot.user.id})")
    print("🚀 777 Supreme Multi-File Enterprise System is Online!")
    await bot.change_presence(activity=discord.Game(name="/help | 777 Enterprise"))

TOKEN = os.getenv("TOKEN")
bot.run(TOKEN)
