import discord
from discord.ext import commands
# from itertools import cycle
import asyncio
import platform
import time
import colorsys
import random
prefix = "§"
bot = commands.Bot(command_prefix=prefix)
bot.remove_command('help')
BOT_OWNER_ROLE="owner" #change which role you need!



@bot.event
async def on_ready():
    print('Online')
    print("Created by ✞☬Attitude boy☬✞")
    print("𝑸𝑼𝑰𝒁 𝚝𝚒𝚖𝚎")
    print("https://discord.gg/Wt6uDbb")
    print("Everything's all ready to go~")
    while True:
    	await bot.change_presence(activity=discord.Activity(type=1,name="with Hêårt håçk!"))
    	await asyncio.sleep(5)
    	
    	await bot.change_presence(activity=discord.Activity(type=1,name="with Created by ✞☬Attitude boy☬✞"))
    	await asyncio.sleep(5)
	
    	await bot.change_presence(activity=discord.Activity(type=1,name="with My server"))
    	await asyncio.sleep(5)
    	
    	await bot.change_presence(activity=discord.Activity(type=1,name="with All Users"))
    	await asyncio.sleep(5)
    	
    	await bot.change_presence(activity=discord.Activity(type=1,name="with Happy moment"))
    	await asyncio.sleep(5)
    	
    	await bot.change_presence(activity=discord.Activity(type=1,name="with Love"))
    	await asyncio.sleep(5)
    	
    	await bot.change_presence(activity=discord.Activity(type=1,name="With Animals"))
    	await asyncio.sleep(5)
    	
    	await bot.change_presence(activity=discord.Activity(type=1,name="with Kings"))
    	await asyncio.sleep(5)
	
    	await bot.change_presence(activity=discord.Activity(type=1,name="with your Love😍!"))
    	await asyncio.sleep(5)
	
    	await bot.change_presence(activity=discord.Activity(type=1,name="with All cmds!"))
    	await asyncio.sleep(5)
	
    	await bot.change_presence(activity=discord.Activity(type=2,name="with req.owner role"))
    	await asyncio.sleep(5)
	
    	await bot.change_presence(activity=discord.Activity(type=1,name="with  members!"))
    	await asyncio.sleep(5)
    	
    	await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name=f'''{len(bot.guilds)} servers'''))
    	await asyncio.sleep(5)

@bot.command(name="hi")
async def ping(ctx):
    '''
    This text will be shown in the help command
    '''

    # Get the latency of the bot
    latency = bot.latency  # Included in the Discord.py library
    # Send it to the user
    await ctx.send(latency)
    
bot.run("NjU4NzIxMDQ3NzI5NjY4MTE2.XujV2w.aYbbwI0wdsXpTRohdmUBVl9B2Zw",bot=False)
