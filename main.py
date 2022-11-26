import discord
import logging
import os
import itertools
from discord.ext import tasks
from koff_commands import sets, user, stats, help
from urllib.request import Request, urlopen
from cogs import pokemon
import cogs
import json
import db


# poetry export -f requirements.txt --without-hashes --output requirements.txt
# pip install -U git+https://github.com/Rapptz/discord.py
#‿︵‿︵‿︵‿︵‿︵‿︵‿︵‿︵‿︵‿︵


client = discord.Client(intents=discord.Intents().all())
logging.basicConfig(level=logging.INFO)
status = itertools.cycle(['Try ~help', 'e. | ~help'])

@client.event
async def on_ready():
    change_status.start()
    print("\n\n\n[?]  Bot is online")
    print(f"[?]  Logged in as {client.user} - {client.user.id}")
    print(f"[?]  Active Guilds --> ")
    activeservers = client.guilds
    for guild in activeservers:
      print("        ", guild.name)
    print("\n")

@tasks.loop(seconds=5)
async def change_status():
    await client.change_presence(activity=discord.Game(next(status)))

botPrefix = '~'





#‿︵‿︵‿︵‿︵‿︵‿︵‿︵‿︵‿︵‿︵

#‿︵‿︵‿︵‿︵‿︵‿︵‿︵‿︵‿︵‿︵





@client.event
async def on_message(msg):
    if msg.content.startswith(botPrefix) and not msg.content.startswith(botPrefix*2):

        ctx = msg.content.lower()[len(botPrefix):].strip()
        channel = msg.channel                                   


      
      

      #‿︵‿︵‿︵‿︵‿︵ HELP ‿︵‿︵‿︵‿︵‿︵


        if ctx.startswith('help'):
          await channel.send(embed=help.get(msg.author))      


          

          
       #‿︵‿︵‿︵‿︵‿︵ USER ‿︵‿︵‿︵‿︵‿︵

      

        elif ctx.startswith('user '):

          username = ctx.split(' ')[1]
          try: output = user.get(username)
          except: await channel.send("Couldnt find that user")

          #‿︵‿︵‿ DROPDOWN ‿︵‿︵‿
          
          class Dropdown(discord.ui.Select):
              def __init__(self):
                
                  options = []
                  for tier in output.keys():
                    options.append(discord.SelectOption(label=tier))
                  super().__init__(placeholder='Choose a format...', min_values=1, max_values=1, options=options[:25])

              async def callback(self, interaction: discord.Interaction):

                  embed = user.process(self.values[0],output[self.values[0]],msg.author)
                  await interaction.response.send_message(embed = embed, ephemeral = True)

          class DropdownView(discord.ui.View):
              def __init__(self):
                  super().__init__()
                  self.add_item(Dropdown())          

          view = DropdownView()
          await channel.send(embed = user.embed(username, output, msg.author) , view = view)              



          

       #‿︵‿︵‿︵‿︵‿︵ SETS ‿︵‿︵‿︵‿︵‿︵

      

        elif ctx.startswith('sets '):
          
          ctx = ctx.split(' ')
          gen = ctx[1]
          poke = ctx[2:]
          poke = ' '.join(poke)

          if poke.lower() == 'dialga': poke = 'Garbodor'
          elif poke.lower() == 'garbodor': poke = 'Dialga'

          if str(gen) not in ['1','2','3','4','5','6','7','8']:
            await channel.send("its `sets <gen> <pokemon>`, that gen is invalid, it should be a number from 1 ~ 8" )   
          
          try: 
            data = pokemon(poke,gen)
            sets_data = data.sets()
          except KeyError: await channel.send("its `sets <gen> <pokemon>`, that pokemon name isnt quite right")

          
          #‿︵‿︵‿ DROPDOWN ‿︵‿︵‿

          class Dropdown(discord.ui.Select):
              def __init__(self):
                
                  options = []
                  for key in sets_data.keys():
                    for __set__ in sets_data[key].keys():
                      options.append(discord.SelectOption(label=f"{key} ― {__set__}"))
                  super().__init__(placeholder='Choose a set...', min_values=1, max_values=1, options=options)

              async def callback(self, interaction: discord.Interaction):
                  format_ = self.values[0]
                  battle_format = format_.split(' ― ')[0]
                  set_ = format_.split(' ― ')[1]
                  s = sets_data[battle_format][set_]
                  embed = sets.process(s, format_, poke, interaction.user)

                  await interaction.response.send_message(embed = embed, ephemeral = True)

          class DropdownView(discord.ui.View):
              def __init__(self):
                  super().__init__()
                  self.add_item(Dropdown())
          
          view = DropdownView()
          await channel.send(embed = sets.get(sets_data, data, msg.author) , view = view)  


          

          
       #‿︵‿︵‿︵‿︵‿︵ STATISTICS ‿︵‿︵‿︵‿︵‿︵

      
      
        elif ctx.startswith('stats '):
       

          ctx = ctx.split(' ')
          gen = ctx[1].strip()
          poke = ctx[2:-1]
          format = ctx[-1].lower().strip()

          if str(gen) not in ['1','2','3','4','5','6','7','8']:
            await channel.send(f"its `~stats <gen> <pokemon> <format>`, gen:{gen} is invalid, it should be a number from 1 ~ 8" )   


          if str(format) not in db.formats.keys():
            await channel.send(f"its `~stats <gen> <pokemon> <format>`, format: {format} is invalid, remember it shouldnt have any spaces in it" )
          
          if isinstance(poke, list):
              poke = str(' '.join(poke))

          stats_data = pokemon(poke,gen)
          
          try:
            x = stats_data.stats(format)
          except: 
            await channel.send(f"{poke} doesnt exist in gen{gen} {format}")

          del x
          stats_ = stats.pokemonStats(format,stats_data,msg.author)
          embed = stats_.general()



          class StatisticsView(discord.ui.View):
            def __init__(self):
                super().__init__(timeout=None)
                  
            @discord.ui.button(label=' General ', style=discord.ButtonStyle.green, custom_id='statisticsview:general')
            async def general(self, interaction: discord.Interaction, button: discord.ui.Button):
                await interaction.response.edit_message(embed = stats_.general())
                  
            @discord.ui.button(label='   Sets  ', style=discord.ButtonStyle.green, custom_id='statisticsview:sets')
            async def sets(self, interaction: discord.Interaction, button: discord.ui.Button):
                await interaction.response.edit_message(embed = stats_.sets())
                  
            @discord.ui.button(label=' Relations ', style=discord.ButtonStyle.green, custom_id='statisticsview:relations')
            async def relations(self, interaction: discord.Interaction, button: discord.ui.Button):
                await interaction.response.edit_message(embed = stats_.relations())
                        
                    
          view2 = StatisticsView()
          await channel.send(embed = embed, view = view2)

          

          
#‿︵‿︵‿︵‿︵‿︵‿︵‿︵‿︵‿︵‿︵

#‿︵‿︵‿︵‿︵‿︵‿︵‿︵‿︵‿︵‿︵




client.run("ODYzNzMzNTkxODIxMzg1NzQ4.GshAz4.umtxECvHVBD__SMv0Vq7TMVF81hmDSgPyYFBH4")