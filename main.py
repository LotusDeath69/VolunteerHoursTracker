import discord
from discord.ext import commands
from dotenv import load_dotenv
import os 

load_dotenv()


#Varibles
prefix = '?'
token = os.environ['TOKEN']
client = commands.Bot(command_prefix=prefix, help_command=None)


def createEmbed(ign, title, value):
    embed = discord.Embed(
    title = title,
    colour = discord.Colour.blue()
  )
    embed.add_field(name=ign, value=value)
    embed.set_footer(text='Created by ThatBananaking')
    return embed 


@client.event
async def on_ready():
  await client.change_presence(status=discord.Status.online, activity=discord.Activity(
    type=discord.ActivityType.listening, name='change this to total hours'
  ))
  print('logged in')


@client.command()
async def add(ctx, date, hours):

    
    
client.run(token)

