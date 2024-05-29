async def addRepresentative(ctx, args, guild_to_auction):
  if len(args) != 3:
    await ctx.send(
        'Please provide a valid command. Command **addRepresentative** only takes 2 values'
        + 'Team acronyms and user tagged' + '\n' +
        'Example: \n > addTeam CSK @user_id')
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

  team_acronym = args[1]
  rep = args[2]

  if not team_acronym.isalnum():
    await ctx.send('Team acronym should be alphanumeric, eg: CSK')
    return

  if not rep.startswith('<@'):
    await ctx.send('Representative should be a user tagged, eg: @user_')
    return

  if isRepresentative(guild_to_auction, rep, guild_id):
    await ctx.send('The tagged user is already a representative of a team.')
    return

  if team_acronym not in guild_to_auction[guild_id].teams:
    await ctx.send('Team does not exist.')
    return

  if team_acronym not in guild_to_auction[guild_id].team_representatives:
    guild_to_auction[guild_id].team_representatives[team_acronym] = []
  guild_to_auction[guild_id].team_representatives[team_acronym].append(rep)
  await ctx.send(
      getRepresentativesMessage(guild_to_auction, team_acronym, guild_id))


def getRepresentativesMessage(guild_to_auction, team_acronym, guild_id):
  message = "Representatives for the team: " + team_acronym + "are: "
  for rep in guild_to_auction[guild_id].team_representatives[team_acronym]:
    message += rep + " "
  return message


def isRepresentative(guild_to_auction, rep, guild_id):
  team_reps = guild_to_auction[guild_id].team_representatives
  return any(rep in team_reps[team] for team in team_reps)
