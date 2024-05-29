from typing import List
from auction.Player import Player


class GuildAuction:

  def __init__(self, guild_id, auction_id, channel_id, start_time):
    self.guild_id = guild_id
    self.auction_id = auction_id
    self.channe_id = channel_id
    self.start_time = start_time

  def addPlayers(self, players: List[Player]):
    self.players = players
