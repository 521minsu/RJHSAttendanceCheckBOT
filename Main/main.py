import random, pickle, os
import discord, asyncio, globalvariables
from discord.ext import commands

client = discord.Client()
des = "This is a discord bot that is specially made to use for attendance check in Rototuna High School"

client = commands.Bot(description=des, command_prefix=globalvariables.prefix)

@client.event
async def on_ready():
	print("Bot Online!")
	print("Logged in as : {}".format(client.user.name))
	print("ID: {}".format(client.user.id))
	await client.change_presence(game=discord.Game(name="prefix: 'r!'"))
	print("Ready to use")

#Command 01 - Test Command (ping)
@client.command(pass_context=True)
async def ping(ctx):
	await client.say("Pong!")

#Command 02 - Test Command (slap)
@client.command(pass_context=True)
async def slap(ctx,args):
	print(args)
	await client.say("You slapped {}".format(args))

#Command 03 - Test Command (add quote) - save to a file test
@client.command(pass_context=True)
async def addquote(ctx,args):
	if not os.path.isfile("quote_file,pk1"):
		quote_list = []
	else:
		with open("quote_file.pk1", "rb") as quote_file:
			quote_list = pickle.load(quotefile)
	quote_list.append(args)
	with open("quote_file.pk1", "wb") as quote_file:
		pickle.dump(quote_list,quote_file)

#Command 04 - Test Command (showquote) - show the quote saved
@client.command(pass_context=False)
async def showquote():
	with open("quote_file.pk1", "rb") as quote_file:
		quote_list = pickle.load(quote_file)
	await client.say(random.choice(quote_list))

client.run("MzgwOTYyNzk1MzE3MTAwNTQ2.DPAZ3A.zOhojblXlJjnlA2V_-7kikO7NFs")
