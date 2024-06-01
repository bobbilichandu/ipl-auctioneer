from auction.enums.PlayerRole import PlayerRole
from auction.enums.Tier import Tier


class Player:

  def __init__(self, name: str, tier: Tier, role: PlayerRole, base_price: int):
    self.name = name
    self.tier = tier
    self.role = role
    self.base_price = base_price
