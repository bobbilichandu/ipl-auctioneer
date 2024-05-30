async def removeRepresentative(ctx, args, guild_to_auction):
  if len(args) != 2:
    await ctx.send(
        'Please provide a valid command. Command **removeRepresentative** only takes 1 value'
        + 'user tagged' + '\n' +
        'Example: \n > $auction removeRepresentative @user_id')
    return

  guild_id = ctx.guild.id
  if guild_id not in guild_to_auction:
    await ctx.send(
        'No Auction in progress. Start a new auction using start command.')
    return

  if ctx.channel.id != guild_to_auction[guild_id].channel_id:
    await ctx.send('This is not the channel where the auction is running.')
    return

  if ctx.author.id != guild_to_auction[guild_id].auction_owner:
    await ctx.send('You are not the owner of the auction.')
    return

  rep = args[1]

  if not rep.startswith('<@'):
    await ctx.send('Representative should be a user tagged, eg: @user_')
    return

  team = ''
  for team_acronym in guild_to_auction[guild_id].team_representatives:
    if rep in guild_to_auction[guild_id].team_representatives[team_acronym]:
      team = team_acronym
      break

  if team == '':
    await ctx.send('Representative not found.')
    return

  guild_to_auction[guild_id].team_representatives[team].remove(rep)
  await ctx.send('Removed representative: ' + rep + ' from team: ' + team +
                 '.\n' +
                 getRepresentativesMessage(guild_to_auction, team, guild_id))
  return


def getRepresentativesMessage(guild_to_auction, team_acronym, guild_id):
  if len(guild_to_auction[guild_id].team_representatives[team_acronym]) == 0:
    return ''
  message = "Representatives for the team: " + team_acronym + "are: "
  for rep in guild_to_auction[guild_id].team_representatives[team_acronym]:
    message += rep + " "
  return message
