async def addTeam(ctx, args, guild_to_auction):
  if len(args) != 3:
    await ctx.send(
        'Please provide a valid command. Command **addTeam** only takes 2 values'
        + 'Team acronyms and the overall budget in crores' + '\n' +
        'Example: \n > addTeam CSK 100')
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
  budget = args[2]

  if not team_acronym.isalnum():
    await ctx.send('Team acronym should be alphanumeric, eg: CSK')
    return

  if not budget.isnumeric():
    print(budget)
    await ctx.send('Budget should be a number, eg: 100')
    return

  if team_acronym in guild_to_auction[guild_id].teams:
    guild_to_auction[guild_id].teams[team_acronym] = float(budget)
    await ctx.send('Updating limit for the team: ' + team_acronym +
                   "'s budget to " + budget)
  else:
    guild_to_auction[guild_id].teams[team_acronym] = float(budget)
    await ctx.send('Team added with name: ' + team_acronym + ' and budget: ' +
                   budget)
  return
