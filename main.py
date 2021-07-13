import discord
from discord.ext import commands, tasks
from dotenv import load_dotenv
from discord.errors import DiscordException
import os 
from database import *
from datetime import timedelta
from openpyxl import Workbook
load_dotenv()


#Varibles
prefix = '?'
token = os.environ['TOKEN']
excel_path = os.environ['EXCEL_PATH']
db_path = os.environ['DB_PATH']
client = commands.Bot(command_prefix=prefix, help_command=None)


def addData(data):
  wb = Workbook()
  ws = wb.active
  ws['A1'] = 'Date'
  ws['B1'] = 'Minutes'
  ws['C1'] = 'Total Minutes'
  for i in data:
    row = list(i)
    del row[2]
    ws.append(row)
  wb.save("volunteerHours.xlsx")


@client.event
async def on_ready():
  await client.change_presence(status=discord.Status.online, activity=discord.Activity(
    type=discord.ActivityType.listening, name=f'{divmod(int(logRetrive()[::-1][0][3]), 60)[0]}/100 hours'
  ))
  print('logged in')


@client.command()
async def add(ctx, *args):
  if ctx.author.id != 466042357553430539:
    await ctx.reply('You cannot use this bot! L')
    return
  if len(args) > 2:
    await ctx.reply('Requires only `date, hours` input.')
  elif len(args) == 1:
    await ctx.reply('Requires the `hours` variable as well.')
  
  else:
    if ':' in args[1]:
      time = args[1].split(':')
      time = int(time[0]) * 60 + int(time[1])
    else:
      time = int(args[1]) * 60

    try:
      total_hours = int(logRetrive()[::-1][0][3]) + time
    except IndexError:
      total_hours = time
    logAdd(args[0], str(time), str(total_hours))
    await ctx.reply(f'Congratulations! You now have {divmod(total_hours, 60)[0]}/100 hours.')


@client.command()
async def total(ctx):
  await ctx.reply(f"You have {divmod(int(logRetrive()[::-1][0][3]), 60)[0]}/100 hours.")


@client.command()
async def excel(ctx):
  addData(logRetrive())
  await ctx.send(content="Excel File:", file=discord.File(excel_path))


@client.command()
async def database(ctx):
  await ctx.send(content="Database File:", file=discord.File(db_path))
client.run(token)



