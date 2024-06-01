import datetime
import discord
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

    guild_to_auction[guild_id] = GuildAuction(guild_id, uuid.uuid4(),
                                              ctx.channel.id,
                                              datetime.datetime.now(),
                                              ctx.author.id)
    embed = discord.Embed(title="Auction Started!!",
                          color=discord.Color.dark_teal())
    embed.add_field(name="",
                    value="Auction ID: " +
                    str(guild_to_auction[guild_id].auction_id) + "\n",
                    inline=False)
    embed.add_field(name="",
                    value="Auction Owner: <@" +
                    str(guild_to_auction[guild_id].auction_owner) + ">\n",
                    inline=False)
    embed.add_field(
        name="",
        value="Please add teams and base prices using addTeam command\n" +
        "\nusage: \n\n > $auction addTeam <team_name> <base_price>\n",
        inline=False)
    embed.add_field(
        name="",
        value=
        "Please add representatives for the teams using addRepresentative command\n"
        +
        "\nusage: \n\n > $auction addRepresentative <team_name> <team_representative_name",
        inline=False)
    await ctx.send(embed=embed)
    return
