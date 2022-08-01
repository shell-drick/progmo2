from lib.world import World
from lib import api

for x in range(10):
    World.create_block(x, x)

print(World.dump())