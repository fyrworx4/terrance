import os
import subprocess
from dotenv import load_dotenv
from discord.ext import commands

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

bot = commands.Bot(command_prefix="!")


@bot.event
async def on_ready():
    print(f'{bot.user} succesfully logged in!')

@bot.event
async def on_message(message):
    # Make sure the Bot doesn't respond to it's own messages
    if message.author == bot.user: 
        return
    
    if message.content == 'hello':
        await message.channel.send(f'Hi {message.author}! Happy to hear the sound of your voice!')
    if message.content == 'bye':
        await message.channel.send(f'Goodbye {message.author}! I hope you have a good day!')
    
    if "orange" in message.content:
        await message.channel.send("LKSDFJLKDFJKLSDFJ")

    await bot.process_commands(message)

@bot.command()
async def square(ctx, arg):
    print(arg)
    await ctx.send(int(arg) ** 2)

@bot.command()
async def run(ctx, arg):
    print(arg)
    result = os.popen(str(arg.decode("utf-8"))).read()

    #result = os.system(str(arg))

    #result = subprocess.check_output(str(arg), shell=True)

    #f = open("output.txt", "w")
    #f.write(result)
    #f.close

    #await ctx.send(f.read())
    await ctx.send("```" + result + "```")

bot.run(TOKEN)