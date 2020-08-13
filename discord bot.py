import discord
from discord.ext import commands
import json
import random
import datetime as dt
import os
import requests
with open("D:\\code\\Python\\setting.json", 'r', encoding='utf-8') as jfile:  # 載入json
    jdata = json.load(jfile)

bot = commands.Bot(command_prefix='/')  # 起手字元


@bot.event
async def on_ready():  # 機器人啟動觸發
    print(">> Bot is online <<")


@bot.command()
async def l(ctx, codes):  # 載入
    bot.load_extension(f"codes.{codes}")
    await ctx.send(f"{codes}已成功load!")


@bot.command()
async def unl(ctx, codes):  # 卸載
    bot.unload_extension(f"codes.{codes}")
    await ctx.send(f"{codes}已成功unload!")


@bot.command()
async def rel(ctx, codes):  # 重新載入
    bot.reload_extension(f"codes.{codes}")
    await ctx.send(f"{codes}已成功reload!")

# with open("github\\RJ_Bot\\DATA.json", "w", encoding="utf-8") as f:
#     json.dump(data, f)

# @bot.command()
# async def reload(ctx):  # 名稱為指令
#     # round為四捨五入 ctx指當前頻道觸發人的各種資料
#     await ctx.send(f"機器人延遲 {round(bot.latency*1000)}ms")

for filename in os.listdir('./codes'):  # 啟動機器人時 載入所有檔案
    if filename.endswith('.py'):
        bot.load_extension(f"codes.{filename[:-3]}")

if __name__ == "__main__":
    bot.run(jdata['TOKEN'])
