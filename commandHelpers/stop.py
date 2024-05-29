async def stopAuction(ctx, args, guild_to_auction):
  if len(args) != 1:
    await ctx.send(
        'Please provide a valid command. Command **stop** does not take any arguments'
    )
    return

  guild_id = ctx.guild.id
  if guild_id not in guild_to_auction:
    await ctx.send(
        'No Auction in progress. Start a new auction using start command.')
    return

  if ctx.channel.id != guild_to_auction[guild_id].channel_id:
    await ctx.send('This is not the channel where the auction is running.')
    return

  auction_id = guild_to_auction[guild_id].auction_id
  del guild_to_auction[guild_id]
  await ctx.send('Stopping auction...')
  await ctx.send('All auction data will be cleaned up. Auction ID: ' +
                 str(auction_id))

  # send auction report

  return
