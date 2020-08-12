import discord
from discord.ext import commands
import json
import random
import datetime as dt
import os
import requests
with open("setting.json", 'r', encoding='utf-8') as jfile:  # 載入json
    jdata = json.load(jfile)

bot = commands.Bot(command_prefix='/')#起手字元

@bot.event
async def on_ready():  # 機器人啟動觸發
    print(">> Bot is online <<")

@bot.command()
async def load(ctx, codes):  # 載入
    bot.load_extension(f"codes.{codes}")
    await ctx.send(f"{codes}已成功load!")
@bot.command()
async def unload(ctx, codes):  # 卸載
    bot.unload_extension(f"codes.{codes}")
    await ctx.send(f"{codes}已成功unload!")
@bot.command()
async def reload(ctx, codes):  # 重新載入
    bot.reload_extension(f"codes.{codes}")
    await ctx.send(f"{codes}已成功reload!")

@bot.command()
async def tv(ctx):
    imag1 = "https: // imgur.com / StZHCvA.png"
    imag2 =
    imag3 =
    if data["earthquakeInfo"]["magnitude"]["magnitudeValue"]<4
    embed = discord.Embed(title=data["reportType"], url="https://reurl.cc/nzaord",description="完整清單(點標題)", color=0xfdd408, timestamp=dt.datetime.utcnow())
    embed.add_field(name="規模:", value="芮氏"+str(data["earthquakeInfo"]["magnitude"]["magnitudeValue"]), inline=False)
    embed.set_author(name=data["reportType"])
    embed.set_image(url=data["reportImageURI"])
    embed.set_footer(text="臺灣交通部中央氣象局提供",
                     icon_url="https://imgur.com/NKP107p.png")
    await ctx.send(embed=embed)

url = "https://opendata.cwb.gov.tw/api/v1/rest/datastore/E-A0016-001?Authorization=rdec-key-123-45678-011121314"
res = requests.get(url).text
data = json.loads(res)["records"]["earthquake"][0]

# with open("github\\RJ_Bot\\DATA.json", "w", encoding="utf-8") as f:
#     json.dump(data, f)

# @bot.command()
# async def reload(ctx):  # 名稱為指令
#     # round為四捨五入 ctx指當前頻道觸發人的各種資料
#     await ctx.send(f"機器人延遲 {round(bot.latency*1000)}ms")

for filename in os.listdir('./codes'):#啟動機器人時 載入所有檔案
    if filename.endswith('.py'):
        bot.load_extension(f"codes.{filename[:-3]}")

if __name__ == "__main__":
    bot.run(jdata['TOKEN'])

