# ipl-auctioneer [WIP]

Discord bot that can conduct auctions


# Done

- `$auction start` -> to start the auction.
- `$auction stop` -> to stop the auction.
- `$auction addTeam <team_name> <budget>` to add a team.
  - Also updates the budget
- `$auction addRepresentative <team_name> <@tagged_user>` to add a representative to an added team.
- `$auction removeTeam <team_name>` to remove a team and representatives.
- `$auction removeRepresentative <@tagged_user>` to remove a representative.
- Update nickname for reps

# TODO

- [x] Add remove team
- [x] Add remove representative
- [x] Add list teams
- [x] Add list representatives
- [ ] Get list of players in CSV format (atleast 350 players)
  - [ ] Tier splitting
  - [ ] list players
      - [ ] retain player option
- [ ] Bidding using discord public threads
  - [ ] $bid command

