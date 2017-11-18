import random, pickle, os, util
import discord, asyncio, globalvariables
from discord.ext import commands

des = "This is a discord bot that is specially made to use for attendance check in Rototuna High School"
bot = commands.Bot(description=des, command_prefix=globalvariables.prefix)

ClassAtt = []
PersonalAtt = ["N/A","N/A","N/A"]

@bot.event
async def on_ready():
	print("Bot Online!")
	print("Logged in as : {}".format(bot.user.name))
	print("ID: {}".format(bot.user.id))
	print("Database Version: {}".format(util.dbconcheck()))
	await bot.change_presence(game=discord.Game(name="prefix: 'r!'"))
	print("Ready to use!")

# --------------------------------------------------------- #

#Command 01 - Test Command (ping)
@bot.command(pass_context=True)
async def ping(ctx):
	print(ctx.message.author() + "has issued the command 'ping'")
	await bot.say("Pong!")

#Command 02 - Test Command (slap)
@bot.command(pass_context=True)
async def slap(ctx,args):
	print(ctx.message.author() + "has issued the command 'slap.' The recipient was '{}'".format(args))
	await bot.say("You slapped {}".format(args))

#Command 03 - Test Command (embed)
@bot.command(pass_context=True)
async def embed(ctx):
	em = discord.Embed(title='My Embed Title', description='My Embed Content.', colour=0xDEADBF)
	em.set_author(name='Someone', icon_url=bot.user.default_avatar_url)
	print(ctx.message.author() + "has issued the command 'embed'")
	await bot.send_message(ctx.message.channel, embed=em)


# ---------------------------------------------------------- #

#Command 01 - Admin Command (Ban)
#@bot.command(pass_content=True)
#async def ban(ctx,args):


# ---------------------------------------------------------- #

try:
	bot.run("MzgwOTYyNzk1MzE3MTAwNTQ2.DPAZ3A.zOhojblXlJjnlA2V_-7kikO7NFs")

except KeyboardInterrupt:
	util.dbdiscon()
	bot.logout()
	bot.close()
