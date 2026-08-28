Tecate 2026 Draft Companion v9

Run server.py in Pythonista, then use the Safari page it opens.

Tabs:
1. League Inputs
2. Scoring Inputs
3. Lineup Builder
4. Value Board

The ranking engine is ported from Tecate 2026.xlsx:
- position fantasy points
- RANK.EQ positional ranking
- Flex/Superflex eligibility
- dynamic flex allocation
- replacement rank and VOS
- overall VOS ranking
- historical cost by current positional rank
- league allocatable premium
- calculated auction value
- whole-dollar app rounding
- Value = rounded Calculated - rounded Historical

The embedded offensive player pool contains 522 players.

v10 DEF/K RULE
- Every DEF slot is fixed at exactly $1.
- Every K slot is fixed at exactly $1.
- DEF/K cost does not change when Minimum Bid changes.
- Allocatable Premium reserves offensive Minimum Bid for QB/RB/WR/TE/Bench players and $1 for every DEF/K.
- Max Bid reserves offensive Minimum Bid for other unfilled offensive slots and exactly $1 for each DEF/K slot.
