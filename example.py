from steam_community_market.prices import Prices

market = Prices('USD')

items = ['Prisma Case', 'Danger Zone Case', 'Supermega Case']
item = market.get_prices(items, 730)

print(item)
