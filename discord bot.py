import discord
from discord.ext import commands
import json
import random
import datetime as dt
import os

with open("setting.json",'r',encoding='utf-8') as jfile:
    jdata = json.load(jfile)

bot = commands.Bot(command_prefix='/')#起手字元

@bot.event
async def on_ready():  # 機器人啟動觸發
    print(">> Bot is online <<")

@bot.command()
async def load(ctx,codes):
    bot.load_extension(f"codes.{codes}")
    await ctx.send(f"{codes}已成功load!")
@bot.command()
async def unload(ctx, codes):  # 名稱為指令
    bot.unload_extension(f"codes.{codes}")
    await ctx.send(f"{codes}已成功unload!")
@bot.command()
async def reload(ctx, codes):  # 名稱為指令
    bot.reload_extension(f"codes.{codes}")
    await ctx.send(f"{codes}已成功reload!")


# @bot.command()
# async def reload(ctx):  # 名稱為指令
#     # round為四捨五入 ctx指當前頻道觸發人的各種資料
#     await ctx.send(f"機器人延遲 {round(bot.latency*1000)}ms")

# @bot.command()
# async def tv(ctx):
#         embed = discord.Embed(title="Code教學影片", url="https://reurl.cc/nzaord", description="完整清單(點標題)", color=0xfdd408, timestamp=dt.datetime.utcnow())
#         embed.add_field(name="看懂API", value="https://reurl.cc/V6dq65", inline=False)
#         embed.add_field(name="Python + VScode 開發環境安裝",value="https://reurl.cc/E79aZR", inline=False)
#         embed.add_field(name="前置作業", value="https://reurl.cc/exNZ3Q", inline=False)
#         embed.add_field(name="基本Bot建置", value="https://reurl.cc/KkavQq", inline=False)
#         embed.add_field(name="成員 加入/離開事件訊息",value="https://reurl.cc/GV3ye3", inline=False)
#         embed.set_footer(text=":thinking:")
#         await ctx.send(embed=embed)

for filename in os.listdir('./codes'):
    if filename.endswith('.py'):
        bot.load_extension(f"codes.{filename[:-3]}")

if __name__ == "__main__":
    bot.run(jdata['TOKEN'])

