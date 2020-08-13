import discord
from discord.ext import commands
import json
import random
import datetime as dt
import requests
import time
class Commands(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def ping(self,ctx):  # 名稱為指令
        # round為四捨五入 ctx指當前頻道觸發人的各種資料
        await ctx.send(f"機器人延遲 {round(self.bot.latency*1000)}ms")


    # @commands.command()
    # async def tv(self,ctx):
    #     embed = discord.Embed(title="Code教學影片", url="https://reurl.cc/nzaord",
    #                         description="完整清單(點標題)", color=0xfdd408, timestamp=dt.datetime.utcnow())
    #     embed.add_field(
    #         name="看懂API", value="https://reurl.cc/V6dq65", inline=False)
    #     embed.add_field(name="Python + VScode 開發環境安裝",
    #                     value="https://reurl.cc/E79aZR", inline=False)
    #     embed.add_field(
    #         name="前置作業", value="https://reurl.cc/exNZ3Q", inline=False)
    #     embed.add_field(
    #         name="基本Bot建置", value="https://reurl.cc/KkavQq", inline=False)
    #     embed.add_field(name="成員 加入/離開事件訊息",
    #                     value="https://reurl.cc/GV3ye3", inline=False)
    #     embed.set_footer(text=":thinking:")
    #     await ctx.send(embed=embed)
    @commands.command()
    async def tv(self, ctx):
        url = "https://opendata.cwb.gov.tw/api/v1/rest/datastore/E-A0016-001?Authorization=rdec-key-123-45678-011121314"  # 爬蟲 爬地震API
        res = requests.get(url).text
        data = json.loads(res)["records"]["earthquake"][0]
        MLdata = data["earthquakeInfo"]["magnitude"]["magnitudeValue"]
        if MLdata < 5.0:
            ptcolor = "https://imgur.com/VlNYrho.png"
            color_ = 0x16C60C
            color_icon = "🟢"
            ML = "小型地震"
        if 5.0 <= MLdata < 7.0:
            ptcolor = "https://imgur.com/qAuvrKf.png"
            color_ = 0xFFF100
            color_icon = "🟡"
            ML = "中型地震"
        if 7.0 <= MLdata:
            ptcolor = "https://imgur.com/qAuvrKf.png"
            color_ = 0xE81224
            color_icon = "🔴"
            ML = "大型地震"
        if data["earthquakeNo"] % 100 == 0:
            earthquakeNo = "沒有編號 `(小區域有感地震)`"
        else:
            earthquakeNo = str(data["earthquakeNo"] % 100)
        ttme=dt.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        embed = discord.Embed(color=color_,)  # timestamp=
        embed.add_field(name="編號:", value=earthquakeNo, inline=True)
        embed.add_field(name="規模:", value=f"{color_icon }" + u'\uFE0E' + f" 芮氏 **{MLdata}** `({ML})`", inline=True)
        embed.add_field(name="發生時間:", value=""+data["earthquakeInfo"]["originTime"]+"", inline=False)
        embed.add_field(name="震央位置:", value=data["earthquakeInfo"]["epiCenter"]["location"], inline=False)
        embed.set_author(name=data["reportType"]+"(詳情請點我)",url=data["web"], icon_url=ptcolor)  # 開頭作者
        embed.set_image(url=data["reportImageURI"])#地震報告圖片
        embed.set_footer(text=f"臺灣交通部中央氣象局提供 ▪ 發布時間：{ttme}", icon_url="https://imgur.com/NKP107p.png")
        await ctx.send(embed=embed)

    @commands.command()
    async def info(self,ctx):
        embed = discord.Embed(title="nice bot", description="Nicest bot there is ever.", color=0xeee657)  # 在這裡提供關於您的信息
        embed.add_field(name="Author", value="<YOUR-USERNAME>")  # 顯示機器人所服務的數量。
        embed.add_field(name="Server count", value=f"{len(self.bot.guilds)}")  # 給用戶提供一個連結來請求機器人接入他們的伺服器
        embed.add_field(name="Invite", value="[Invite link](<insert your OAuth invitation link here>)",inline=False)
        await ctx.send(embed=embed)


def setup(bot):
    bot.add_cog(Commands(bot))
