import discord, time
from discord.ext import commands

select_game = "Game name here"
token = "Account token here"

bot = commands.Bot("$", self_bot = True)
bot.remove_command('help')

@bot.event
async def on_ready():
    await bot.change_presence(status=discord.Status.dnd, activity=discord.Game(name=select_game))
    print("Your status is set online!")

bot.run(token, bot=False)
