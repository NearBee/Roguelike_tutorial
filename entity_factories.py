from components.ai import HostileEnemy
from components.fighter import Fighter
from entity import Actor
from entity import Entity

player = Actor(
    char="@",
    color=(126, 222, 100),
    name="Player",
    ai_cls=HostileEnemy,
    fighter=Fighter(hp=30, defense=2, power=5),
)

orc = Actor(
    char="o",
    color=(63, 127, 63),
    name="Orc",
    ai_cls=HostileEnemy,
    fighter=Fighter(hp=10, defense=0, power=3),
)

troll = Actor(
    char="T",
    color=(62, 222, 187),
    name="Troll",
    ai_cls=HostileEnemy,
    fighter=Fighter(hp=16, defense=1, power=4),
)
