
import discord
from discord.ext import commands
from discord.ext.commands import Bot
import asyncio

bot =  commands.Bot(command_prefix="$")

@bot.event
async def on_ready():
    print ("Hello there stoner..")
    


@bot.command(pass_context=True)
async def hi(ctx):
    await bot.say("niegroman") 

bot.run("NDg1MTI3ODkyNDQ4MDUxMjIx.Dn-qWQ.xRgFdV_AWAL18V2BjLN8EYMo0kQ")
