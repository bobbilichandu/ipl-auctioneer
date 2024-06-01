import discord
from table2ascii import Alignment, table2ascii, PresetStyle


async def listTeams(ctx, args, guild_to_auction):

  if len(args) != 1:
    await ctx.send(
        'Please provide a valid command. Command **listTeams** take no values'
        + '\n' + 'Example: \n > $auction listTeams')
    return

  guild_id = ctx.guild.id
  if guild_id not in guild_to_auction:
    await ctx.send(
        'No Auction in progress. Start a new auction using start command.')
    return

  if ctx.channel.id != guild_to_auction[guild_id].channel_id:
    await ctx.send('This is not the channel where the auction is running.')
    return

  if ctx.author.id != guild_to_auction[
      guild_id].auction_owner and not isRepresentative(
          guild_to_auction, ctx.author.id, guild_id):
    await ctx.send(
        'You are neither the owner nor a representative in the auction.')
    return

  teams = guild_to_auction[ctx.guild.id].teams
  embed = discord.Embed(title="List of teams", color=discord.Color.dark_gold())
  table = []
  header = ["#", "Team", "Budget"]

  for team in teams:
    table.append(["#", team, str(teams[team])])

  table_content = table2ascii(
      header=header,
      body=table,
      style=PresetStyle.thin_compact_rounded,
      alignments=[Alignment.CENTER, Alignment.CENTER, Alignment.CENTER],
      column_widths=[12, 12, 12],
  )
  embed.add_field(name="", value=f"```\n{table_content}\n```", inline=False)

  await ctx.send(embed=embed)


def isRepresentative(guild_to_auction, rep, guild_id):
  team_reps = guild_to_auction[guild_id].team_representatives
  return any("<@" + str(rep) + ">" in team_reps[team] for team in team_reps)
