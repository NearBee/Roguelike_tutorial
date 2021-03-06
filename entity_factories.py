from components.ai import BossEnemy, HostileEnemy
from components import consumable, equippable
from components.equipment import Equipment
from components.fighter import Fighter
from components.inventory import Inventory
from components.level import Level
from entity import Actor, Item
from entity import Entity

player = Actor(
    char="○",
    color=(126, 222, 100),
    name="Player",
    ai_cls=HostileEnemy,
    equipment=Equipment(),
    fighter=Fighter(hp=30, base_defense=1, base_power=2),
    inventory=Inventory(capacity=26),
    level=Level(level_up_base=200),
)

orc = Actor(
    char="¡",
    color=(63, 127, 63),
    name="Orc",
    ai_cls=HostileEnemy,
    equipment=Equipment(),
    fighter=Fighter(hp=10, base_defense=0, base_power=3),
    inventory=Inventory(capacity=0),
    level=Level(xp_given=35),
)

troll = Actor(
    char="¡",
    color=(62, 222, 187),
    name="Troll",
    ai_cls=HostileEnemy,
    equipment=Equipment(),
    fighter=Fighter(hp=16, base_defense=1, base_power=4),
    inventory=Inventory(capacity=0),
    level=Level(xp_given=100),
)

abomination = Actor(
    char="§",
    color=(119, 170, 119),
    name="Abomination",
    ai_cls=BossEnemy,
    equipment=Equipment(),
    fighter=Fighter(hp=30, base_defense=3, base_power=10),
    inventory=Inventory(capacity=0),
    level=Level(xp_given=100),
)

confusion_scroll = Item(
    char="ß",
    color=(207, 63, 255),
    name="Confusion Scroll",
    consumable=consumable.ConfusionConsumable(number_of_turns=10),
)

fireball_scroll = Item(
    char="Σ",
    color=(0, 0, 255),
    name="Fireball Scroll",
    consumable=consumable.FireballDamageConsumeable(damage=12, radius=3),
)

health_potion = Item(
    char="¿",
    color=(255, 68, 102),
    name="Health Potion",
    consumable=consumable.HealingConsumable(amount=4),
)

lighting_scroll = Item(
    char="Θ",
    color=(255, 255, 0),
    name="Lighting Scroll",
    consumable=consumable.LightningDamageConsumable(damage=20, maximum_range=5),
)

dagger = Item(
    char="/", color=(0, 191, 255), name="Dagger", equippable=equippable.Dagger()
)

sword = Item(char="/", color=(0, 191, 255), name="Sword", equippable=equippable.Sword())

leather_armor = Item(
    char="[",
    color=(139, 69, 19),
    name="Leather Armor",
    equippable=equippable.LeatherArmor(),
)

chain_mail = Item(
    char="[", color=(139, 69, 19), name="Chain Mail", equippable=equippable.ChainMail()
)
