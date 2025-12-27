import discord
from discord.ext import commands
from discord import option

TOKEN = "TOKEN :3"
AU = [list1, list2] 

bot = commands.Bot()

class RV(discord.ui.View):
    def __init__(self, message_content: str):
        super().__init__(timeout=None)
        self.message_content = message_content

    @discord.ui.button(label="點我", style=discord.ButtonStyle.primary)
    async def button_callback(self, button, interaction):
        await interaction.response.defer()
        allowed = discord.AllowedMentions(everyone=True, users=True, roles=True)
        for _ in range(5):
            await interaction.followup.send(content=self.message_content, allowed_mentions=allowed)
            

user_app_settings = {"integration_types": {discord.IntegrationType.user_install, discord.IntegrationType.guild_install}, "contexts": {discord.InteractionContextType.guild, discord.InteractionContextType.bot_dm, discord.InteractionContextType.private_channel}}

@bot.slash_command(name="send", description="發送 5 次 hi", **user_app_settings)
async def send(ctx):
    # if ctx.author.id not in AU:
        # return await ctx.respond("❌ 你不在授權名單中，無法使用此指令。", ephemeral=True)
    
    view = RV("@everyone hi")
    await ctx.respond("點擊下方按鈕打招呼", ephemeral=True, view=view)

@bot.slash_command(name="pro_send", description="發送自定義訊息按鈕", **user_app_settings)
@option("message", description="輸入想要重複的訊息")
async def psend(ctx, message: str):
    if ctx.author.id not in AU:
        return await ctx.respond("❌ 你不在授權名單中，無法使用此指令。", ephemeral=True)
    
    view = RV(message)
    await ctx.respond(f"按鈕已發送！內容為下：\n{message}", view=view, ephemeral=True)

@bot.event
async def on_ready():
    print(f"機器人已啟動：{bot.user}")

bot.run(TOKEN)