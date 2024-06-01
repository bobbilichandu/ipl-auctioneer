import discord
from table2ascii import table2ascii, PresetStyle, Alignment


async def listRepresentatives(ctx, args, guild_to_auction, bot):

    if len(args) != 1:
        await ctx.send(
            'Please provide a valid command. Command **listRepresentatives** take no values'
            + '\n' + 'Example: \n > $auction listRepresentatives')
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

    team_representatives = guild_to_auction[guild_id].team_representatives
    embed = discord.Embed(title="List of Representatives",
                          color=discord.Color.brand_green())
    table = []
    table_header = ["#", "Team", "Representatives"]
    for team in team_representatives:
        table.append([
            "#", team, ', '.join(
                getNamesFromRepresentativeTags(team_representatives[team],
                                               bot))
        ])
    table_content = table2ascii(
        header=table_header,
        body=table,
        style=PresetStyle.thin_compact_rounded,
        alignments=[Alignment.CENTER, Alignment.CENTER, Alignment.LEFT])
    embed.add_field(name="", value=f"```\n{table_content}\n```", inline=False)

    await ctx.send(embed=embed)


def getNamesFromRepresentativeTags(tags, bot):
    names = []
    for tag in tags:
        user = bot.get_user(int(tag[2:-1]))
        names.append(user.name)
    return names


def isRepresentative(guild_to_auction, rep, guild_id):
    team_reps = guild_to_auction[guild_id].team_representatives
    return any("<@" + str(rep) + ">" in team_reps[team] for team in team_reps)
