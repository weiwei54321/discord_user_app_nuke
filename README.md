# discord_user_app_nuke

⚠️ **法律免責聲明**
本專案僅供 **教學、教育與研究目的** 使用。其目的在於展示 Discord 外部應用（User Apps）可能的潛在風險，幫助開發者防範類似攻擊。
- 請勿將此工具用於任何未經許可的真實伺服器。
- 使用此工具攻擊他人伺服器可能違反 Discord 的 [服務條款 (ToS)](discord.com) 並導致帳號被封鎖。
- 作者對因不當使用本工具而造成的任何損失或法律責任概不負責。

---

### 專案簡介
這是一個利用外部應用程式（User Apps）進行伺服器安全性測試及功能展示的範例。

## 授權條款 (License)
本專案採用 [MIT License](LICENSE) 授權。

---

# 開始
> 你要有一台主機 和 python環境

## 說明
> 因為有些群體會想靠這個賺錢所以我就開源 嘿嘿
> 
> 也希望你/你能在這個專案學到東西
>
> 我附上了一些些的運作原理 :>

## 所需套件

```
py-cord
```

---

### 按鈕運作
```python
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
```
解釋
> 這段程式碼當按鈕被按下時會連續發送5則訊息

---

### 指令運作及呼叫
```python
@bot.slash_command(name="send", description="發送 5 次 hi", **user_app_settings)
async def send(ctx):
    # if ctx.author.id not in AU:
        # return await ctx.respond("❌ 你不在授權名單中，無法使用此指令。", ephemeral=True)
    
    view = RV("@everyone hi")
    await ctx.respond("點擊下方按鈕打招呼", ephemeral=True, view=view)
```
解釋
> 這段程式碼會建立一個/send，使用指令會發送 點擊下方按鈕打招呼 及 一顆按鈕 按下去他就會發訊息

---
## 沒了
> 又水了一個專案 :>
>
> 記得幫我按星星
