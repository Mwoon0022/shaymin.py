import cogs
import discord


#‿︵‿︵‿︵‿︵‿︵‿︵‿︵‿︵‿︵‿︵


bot_icon = 'https://media.discordapp.net/attachments/805074788623056946/887626784873521152/New_Piskel_3.png'
default_colour = discord.Color.from_rgb(47,49,54)
error = lambda pref : f"```{pref}sets <gen no.> <pokemon>[-forme]```"
  

#‿︵‿︵‿︵‿︵‿︵‿︵‿︵‿︵‿︵‿︵

def fix(dict):
  output = []
  for x in dict.keys():
    if int(dict[x]*100) > 2:
      output.append(f'`{str(int(cogs.percentage(dict[x]))).rjust(3,"0")}%` ━ {x}'.replace(':',' '))
    else: break  
  return '\n'.join(output[:12])

def fixCounters(dict):
  if dict.keys():
    newline = '\n'
    output = []
    for x in dict.keys():
      output.append(f'`{str(int(cogs.percentage(dict[x][1]))).rjust(3,"0")} ~ {str(int(cogs.percentage(dict[x][2]))).rjust(3,"0")}%` ━ {x}'.replace(':',' '))

    return f"""{newline}__Counters__:

> ko'd ~ switched in
                          
{newline.join(output[:12])}"""

  else: 
    return " "

def get(formats, gen, mon, author):


    
    formatsFinal = ' | '.join(formats)
    baseStats = cogs.pokemon(mon,gen)
    baseStats = baseStats.data()['baseStats']



    embed = discord.Embed(title = ' ឵឵  ឵឵  ឵឵  ', description = f"""
 **Formats:** {formatsFinal}

```HP  {str(baseStats['hp']).ljust(3)}  {cogs.stats(baseStats['hp'])}
ATK {str(baseStats['atk']).ljust(3)}  {cogs.stats(baseStats['atk'])}
DEF {str(baseStats['def']).ljust(3)}  {cogs.stats(baseStats['def'])}
SPA {str(baseStats['spa']).ljust(3)}  {cogs.stats(baseStats['spa'])}
SPD {str(baseStats['spd']).ljust(3)}  {cogs.stats(baseStats['spd'])}
SPE {str(baseStats['spe']).ljust(3)}  {cogs.stats(baseStats['spe'])}```
឵឵  ឵឵  ឵឵  """, color=default_colour)
    embed.set_thumbnail(url = f"https://www.smogon.com/dex/media/sprites/xy/{mon.lower().replace(' ','-')}.gif")
    embed.set_author(name=f' {mon}', icon_url=f"https://archives.bulbagarden.net/media/upload/5/55/Bag_Premier_Ball_Sprite.png")
    embed.set_footer(text = f"Shaymax │ {author}", icon_url = "https://img.pokemondb.net/sprites/black-white/anim/normal/shaymin-land.gif")

    return embed

  
#‿︵‿︵‿︵‿︵‿︵‿︵‿︵‿︵‿︵‿︵

class pokemonStats:

  def __init__(self, format_, data, author):
    
    self.author = author
    self.poke = data.pokemon
    self.data = data.stats(format_)
    self.lead = self.data["lead"]
    self.usage = self.data["usage"]
    self.weight = self.data["weight"]
    self.viability = self.data["viability"][0]
    self.abilities = self.data["abilities"]
    self.items = self.data["items"]
    self.spreads = self.data["spreads"]
    self.moves = self.data["moves"]
    self.teammates = self.data["teammates"]
    self.counters = self.data["counters"]

  
  def general(self):

    lead = self.lead["weighted"]
    used = self.usage["weighted"]
    weight = self.weight
    viable = round(self.viability/10)

    embed = discord.Embed(description = f""" ឵឵  ឵឵  ឵឵  ឵឵  ឵឵  ឵឵  ឵឵  ឵឵  ឵឵  ឵឵  ឵឵  ឵឵  ឵឵  ឵឵  ឵឵  ឵឵ 
`lead  ` ━ {str(cogs.percentage(lead)).rjust(5,'0')}%
`used  ` ━ {str(cogs.percentage(used)).rjust(5,'0')}%
`weight` ━ {str(cogs.percentage(weight)).rjust(5,'0')}%
`viabil` ━ {viable}
឵឵  ឵឵  ឵឵
""", color = default_colour )
    embed.set_footer(text = f"Shaymax │ {self.author}", icon_url = "https://img.pokemondb.net/sprites/black-white/anim/normal/shaymin-land.gif")
    embed.set_thumbnail(url = f"https://www.smogon.com/dex/media/sprites/xy/{self.poke.lower().strip().replace(' ','-')}.gif")
    embed.set_author(name = self.poke, icon_url = "https://archives.bulbagarden.net/media/upload/5/55/Bag_Premier_Ball_Sprite.png")
  
    return embed 
  
  
  def sets(self):


    
    items = fix(self.items)
    spreads = fix(self.spreads)
    moves = fix(self.moves)
    abilities = fix(self.abilities)
    
    embed = discord.Embed(description = f""" ឵឵  ឵឵  ឵឵  ឵឵  ឵឵ 
__Items__:

{items}                     

__Abilities__:

{abilities}
                        
__Moves__:
                          
{moves}               
                          
__Spreads__:
                          
{spreads}
឵឵ ឵឵ ឵឵ ឵឵ ឵឵""", color = default_colour )
    embed.set_footer(text = f"Shaymax │ {self.author}", icon_url = "https://img.pokemondb.net/sprites/black-white/anim/normal/shaymin-land.gif")
    embed.set_thumbnail(url = f"https://www.smogon.com/dex/media/sprites/xy/{self.poke.lower().strip().replace(' ','-')}.gif")
    embed.set_author(name = self.poke, icon_url = "https://archives.bulbagarden.net/media/upload/5/55/Bag_Premier_Ball_Sprite.png")
  
    return embed 
  
  
  def relations(self):

    teammates = fix(self.teammates)
    counters = fixCounters(self.counters)
    embed = discord.Embed(description = f""" ឵឵  ឵឵  ឵឵  ឵឵  ឵឵ 
__Teammates__:

{teammates}                                     
{counters} ឵឵ ឵឵ ឵឵ ឵឵ ឵឵""", color = default_colour )
    embed.set_footer(text = f"Shaymax │ {self.author}", icon_url = "https://img.pokemondb.net/sprites/black-white/anim/normal/shaymin-land.gif")
    embed.set_thumbnail(url = f"https://www.smogon.com/dex/media/sprites/xy/{self.poke.lower().strip().replace(' ','-')}.gif")
    embed.set_author(name = self.poke, icon_url = "https://archives.bulbagarden.net/media/upload/5/55/Bag_Premier_Ball_Sprite.png")
  
    return embed 

