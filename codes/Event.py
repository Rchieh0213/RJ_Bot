import discord
from discord.ext import commands
import json
import random
import datetime as dt


class Event(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    # @commands.Cog.listener()
    # async def on_member_join(self,member):  # 成員加入觸發
    #     print(f"{member} join!")
    #     channel = self.bot.get_channel(742460237830946849)  # 設定機器人 文字頻道
    #     await channel.send(f"{member} join!")  # 輸出文字

    # @commands.Cog.listener()
    # async def on_member_remove(self,member):  # 成員離開觸發
    #     print(f"{member} leave!")
    #     channel = self.bot.get_channel(742460237830946849)  # 設定機器人 文字頻道
    #     await channel.send(f"{member} leave!")  # 輸出文字

    @commands.Cog.listener()
    async def on_message(self, msg:str):
        if msg.content.find('你們打') >= 0 and msg.author != self.bot.user:
            await msg.channel.send(f"馬的又我們打 都我們打就好啦!")
        if msg.content.find('你們先打') >= 0 and msg.author != self.bot.user:
            await msg.channel.send(f"等等最好給我上線喔!")
        if msg.content.find('我不打') >= 0 and msg.author != self.bot.user:
            await msg.channel.send(f"好扯喔!")
        if msg.content.find('西瓜') >= 0 and msg.author != self.bot.user:
            await msg.channel.send(file=discord.File("D:\\code\\Python\\github\\RJ_Bot\\image\\JPEG_20200714_235934.jpg"))

    # @commands.Cog.listener()
    # async def on_message(self, msg: str):
    #     if msg.content.find('西瓜') >= 0 and msg.author != self.bot.user:
    #         await msg.channel.send(file=discord.File("D:\\code\\Python\\github\\RJ_Bot\\image\\JPEG_20200714_235934.jpg"))

def setup(bot):
    bot.add_cog(Event(bot))


