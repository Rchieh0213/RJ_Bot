import discord
from discord.ext import commands
import json
import random
import datetime as dt

class Commands(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def ping(self,ctx):  # 名稱為指令
        # round為四捨五入 ctx指當前頻道觸發人的各種資料
        await ctx.send(f"機器人延遲 {round(self.bot.latency*1000)}ms")

    @commands.command()
    async def tv(self,ctx):
        embed = discord.Embed(title="Code教學影片", url="https://reurl.cc/nzaord",
                            description="完整清單(點標題)", color=0xfdd408, timestamp=dt.datetime.utcnow())
        embed.add_field(
            name="看懂API", value="https://reurl.cc/V6dq65", inline=False)
        embed.add_field(name="Python + VScode 開發環境安裝",
                        value="https://reurl.cc/E79aZR", inline=False)
        embed.add_field(
            name="前置作業", value="https://reurl.cc/exNZ3Q", inline=False)
        embed.add_field(
            name="基本Bot建置", value="https://reurl.cc/KkavQq", inline=False)
        embed.add_field(name="成員 加入/離開事件訊息",
                        value="https://reurl.cc/GV3ye3", inline=False)
        embed.set_footer(text=":thinking:")
        await ctx.send(embed=embed)

    @commands.command()
    async def aa(self, ctx):
        await ctx.send(f"aaaaa")

def setup(bot):
    bot.add_cog(Commands(bot))
