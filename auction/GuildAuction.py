from typing import List

from auction.Player import Player


class GuildAuction:

  def __init__(self, guild_id, auction_id, channel_id, start_time,
               auction_owner):
    self.guild_id = guild_id
    self.auction_id = auction_id
    self.channel_id = channel_id
    self.start_time = start_time

    self.teams = {}
    self.team_representatives = {}
    self.team_to_players = {}
    self.auction_owner = auction_owner

    self.players = []
    self.bidding_player_id = 0

    self.is_bidding_on = False
    self.sold_players = {}
    self.unsold_players = {}

  def addPlayers(self, players: List[Player]):
    self.players = players
