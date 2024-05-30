import datetime
import uuid
from typing import Dict

from auction.GuildAuction import GuildAuction


async def startAuction(ctx, args, guild_to_auction: Dict[str, GuildAuction]):
    if len(args) != 1:
        await ctx.send(
            'Please provide a valid command. Command **start** does not take any arguments'
        )
        return

    guild_id = ctx.guild.id
    if guild_id in guild_to_auction:
        await ctx.send(
            'Auction already in progress. Finish the current auction to start a new one.'
        )
        return
    await ctx.send("Starting Auction.....")

    guild_to_auction[guild_id] = GuildAuction(guild_id, uuid.uuid4(),
                                              ctx.channel.id,
                                              datetime.datetime.now(),
                                              ctx.author.id)
    await ctx.send(
        "Started an auction with Auction ID: " +
        str(guild_to_auction[guild_id].auction_id) + '\n' +
        "Owner of the auction is: " + "<@" +
        str(guild_to_auction[guild_id].auction_owner) + ">\n" +
        "Please add teams and base prices using addTeam command\n" +
        "usage: \n > $auction addTeam <team_name> <base_price>" +
        "You can also add team representatives using addRepresentative command\n"
        +
        "usage: \n > $auction addRepresentative <team_name> <team_representative_name"
    )
    return
