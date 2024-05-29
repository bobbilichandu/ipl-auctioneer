import os
from re import X
from typing import Dict

import discord
from discord.ext import commands

from auction.GuildAuction import GuildAuction
from commandHelpers.addRepresentative import addRepresentative
from commandHelpers.addTeam import addTeam
from commandHelpers.start import startAuction
from commandHelpers.stop import stopAuction

intents = discord.Intents.all()
bot = commands.Bot(command_prefix='$', intents=intents)

guild_to_auction: Dict[str, GuildAuction] = {}


@bot.event
async def on_ready():
  guild_count = 0
  for guild in bot.guilds:
    print(f"- {guild.id} (name: {guild.name})")
    guild_count = guild_count + 1
  print("IPL Auctioneer is in " + str(guild_count) + " guilds.")


@bot.command()
async def ping(ctx):
  await ctx.send('pong')


@bot.command()
async def auction(ctx, *args):

  if args[0] == 'start':
    await startAuction(ctx, args, guild_to_auction)
    return

  elif args[0] == 'stop':
    await stopAuction(ctx, args, guild_to_auction)
    return

  elif args[0] == 'addTeam':
    await addTeam(ctx, args, guild_to_auction)
    return

  elif args[0] == 'addRepresentative':
    await addRepresentative(ctx, args, guild_to_auction)
    return

  else:
    await ctx.send('Please provide a valid command')


DISCORD_TOKEN = os.getenv("DISCORD_TOKEN")
if DISCORD_TOKEN:
  bot.run(DISCORD_TOKEN)
else:
  print("No discord token provided to start the bot")
