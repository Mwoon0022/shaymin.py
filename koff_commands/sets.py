import cogs
from db import formats
import discord
import urllib
from db import koffing as koff


bot_icon = 'https://media.discordapp.net/attachments/805074788623056946/887626784873521152/New_Piskel_3.png'
default_colour = discord.Color.from_rgb(47,49,54)
error = lambda pref : f"```{pref}sets <gen no.> <pokemon>[-forme]```"  
  

def get(sets_data, data, author):


    set_format = sets_data.keys()
    formatsFinal = ' | '.join(set_format)
    baseStats = data.data()['baseStats']



    embed = discord.Embed(title = ' ឵឵  ឵឵  ឵឵  ', description = f"""
 **Formats:** {formatsFinal}

```HP  {str(baseStats['hp']).ljust(3)}  {cogs.stats(baseStats['hp'])}
ATK {str(baseStats['atk']).ljust(3)}  {cogs.stats(baseStats['atk'])}
DEF {str(baseStats['def']).ljust(3)}  {cogs.stats(baseStats['def'])}
SPA {str(baseStats['spa']).ljust(3)}  {cogs.stats(baseStats['spa'])}
SPD {str(baseStats['spd']).ljust(3)}  {cogs.stats(baseStats['spd'])}
SPE {str(baseStats['spe']).ljust(3)}  {cogs.stats(baseStats['spe'])}```
឵឵  ឵឵  ឵឵  """, color=default_colour)
    embed.set_thumbnail(url = f"https://www.smogon.com/dex/media/sprites/xy/{data.pokemon.lower().replace(' ','-')}.gif")
    embed.set_author(name=f' {data.pokemon}', icon_url=f"https://archives.bulbagarden.net/media/upload/5/55/Bag_Premier_Ball_Sprite.png")
    embed.set_footer(text = f"Shaymax │ {author}", icon_url = "https://img.pokemondb.net/sprites/black-white/anim/normal/shaymin-land.gif")

    return embed

  
# - - - - - - - - - - - - - - - - - - #



    return embed

def process(s, format_, poke, author):

  try:
    moves = s["moves"]
    moves_f = []
    if type(moves) == type('e'):
      moves_f = f'{moves}'
    else:
      for x in moves:
        x = str(x).replace(',', ' / ')
        x = x.replace("'", '')
        x = x.replace('"', '')
        x = x.replace('[', '')
        x = x.replace(']', '')
        x = x.capitalize()
        moves_f.append(f'{x}')

      moves = '\n'.join(moves_f)

  except KeyError as k: 
    moves = 'not given'

  try: 
    item = s["item"]
    itemOne = item
    if isinstance(item, list):
      itemOne = item[1]
      if isinstance(itemOne, list):
        itemOne = itemOne[1]
    if isinstance(item,list):
      item = ' / '.join(item)

  except KeyError as k: 


    item = '-'
    itemOne = 'gold-bottle-cap'

  try:
    nature = s["nature"]
    if isinstance(nature,list):
      nature = ' / '.join(nature)
  except KeyError as k: 
    nature = '-'

  try:
    ability = s["ability"]
    if isinstance(ability,list):
      ability = ' / '.join(ability)
    ability = f'\n` Ability `  {ability}'
  except KeyError as k: 
    ability = ''

  try:
    ivs = cogs.iev(s["ivs"], 'i')
    ivs = f'\n{ivs}'
  except KeyError as k: 
    ivs = ''
  
  try:
    evs = cogs.iev(s["evs"], 'e')
    evs = f'\n{evs}'
  except KeyError as k: 
    evs = ''  
    
  toptext = f"""{poke} ― {format_.replace(' ― ','  ')}"""

  embed = discord.Embed(description = f""" ឵឵  ឵឵  ឵឵
` Item    `  {item}{ability}
` Nature  `  {nature}{ivs}{evs}
 ឵឵  ឵឵  ឵឵  """, color = default_colour )

  embed.add_field(name = 'Moves', value= f"```asciidoc\n{moves}``` ឵឵  ឵឵  ឵឵  ", inline = True)

  embed.set_footer(text = f"Shaymax │ {author}", icon_url = "https://img.pokemondb.net/sprites/black-white/anim/normal/shaymin-land.gif")
  embed.set_thumbnail(url = f"https://www.smogon.com/dex/media/sprites/xy/{poke.lower().strip().replace(' ','-')}.gif")
  embed.set_author(name = toptext, icon_url = f"https://img.pokemondb.net/sprites/items/{itemOne.lower().replace(' ', '-')}.png")

  return embed







  
        