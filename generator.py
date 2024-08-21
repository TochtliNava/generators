import json
import random
import datetime

classes = ["Warrior", "Mage", "Archer", "Assassin", "Priest", "Shaman", "Paladin", "Druid", "Necromancer", "Mechanist", "Engineer", "Hunter"]
races = ["Human", "Elf", "Orc", "Dwarf", "Undead", "Troll", "Gnome", "Goblin", "Dragonkin", "Silvanian", "Teknocard", "Cilikan", "Ghoul"]
guilds = ["Knights of Light", "Dark Rangers", "Horde", "Alliance", "Shadow Brotherhood", "Emerald Order", "Arbinger's guild", "Mermaid's Hymn"]
regions = ["North", "South", "East", "West", "Central", "Asia", "Europe", "Mid West", "Africa", "Oceania", "Central America", "South America"]
skills = ["Divine Strike", "Shadow Arrow", "Earthquake", "Fireball", "Healing Touch", "Assassinate", "Wind Fury", "Improvise", "Hatred Punch"]
equipments = ["Sword of Valor", "Bow of the Fallen", "Hammer of Doom", "Staff of Wisdom", "Dagger of Shadows"]
subscription_types = ["Free", "Premium", "VIP"]

def generate_player_name():
    prefix = ''.join(random.choices('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ', k=random.randint(5,8)))
    suffix = ''.join(random.choices('0123456789', k=random.randint(2,4)))
    special_char = random.choice(['@', '#', '_'])
    return f"{prefix}{special_char}{suffix}"

ndjson_data = []
for i in range(1, 4001):
    player = {
        "player_name": generate_player_name(),
        "class": random.choice(classes),
        "level": random.randint(1, 60),
        "power": random.randint(500, 1500),
        "race": random.choice(races),
        "guild": random.choice(guilds),
        "hours_played": random.randint(10, 1000),
        "pvp_rank": random.randint(1, 10),
        "region": random.choice(regions),
        "special_skill": random.choice(skills),
        "equipment": random.choice(equipments),
        "last_login": (datetime.date.today() - datetime.timedelta(days=random.randint(0, 365))).isoformat(),
        "gold": random.randint(1000, 100000),
        "items_count": random.randint(50, 200),
        "subscription_type": random.choice(subscription_types),
        "xp": random.randint(1000, 100000),
        "join_date": (datetime.date.today() - datetime.timedelta(days=random.randint(365, 1095))).isoformat()
    }
    ndjson_data.append(player)

output_file = 'C:\\Users\\Alex\\Downloads\\players-index-2024-13.ndjson'
with open(output_file, 'w') as f:
    for entry in ndjson_data:
        f.write(json.dumps(entry) + "\n")

output_file
