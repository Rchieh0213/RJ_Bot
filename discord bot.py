import discord
from discord.ext import commands

bot = commands.Bot(command_prefix='!')


@bot.event
async def on_ready():  # 機器人啟動觸發
    print(">> Bot is online <<")


@bot.event
async def on_member_join(member):  # 成員加入觸發
    print(f"{member} join!")
    channel = bot.get_channel(742460237830946849)  # 設定機器人 文字頻道
    await channel.send(f"{member} join!")  # 輸出文字


@bot.event
async def on_member_remove(member):  # 成員離開觸發
    print(f"{member} leave!")
    channel = bot.get_channel(742460237830946849)  # 設定機器人 文字頻道
    await channel.send(f"{member} leave!")  # 輸出文字


@bot.command()
async def ping(ctx):#名稱為指令
    await ctx.send(f"機器人延遲 {round(bot.latency*1000)}ms")  # round為四捨五入 ctx指當前頻道觸發人的各種資料
bot.run("NzQyNDUwNDM3MDg0NDEzOTky.XzGS2g.PQblE8LHEmdDqfISSwOOFmcHHI8")
