async def removeTeam(ctx, args, guild_to_auction):
  if len(args) != 2:
    await ctx.send(
        'Please provide a valid command. Command **addTeam** only takes 1 value'
        + 'Team acronyms and the overall budget in crores' + '\n' +
        'Example: \n > $auction removeTeam CSK')
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

  if not team_acronym.isalnum():
    await ctx.send('Team acronym should be alphanumeric, eg: CSK')
    return

  if team_acronym not in guild_to_auction[guild_id].teams:
    await ctx.send('Team does not exist.')
    return

  del guild_to_auction[guild_id].teams[team_acronym]
  if team_acronym in guild_to_auction[guild_id].team_representatives:
    del guild_to_auction[guild_id].team_representatives[team_acronym]

  await ctx.send('Removed the team and team representatives for the team: ' +
                 team_acronym)
  return
