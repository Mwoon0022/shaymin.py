import discord
import random

default_colour = discord.Color.from_rgb(47,49,54)

def get(author):
    thumbnail_pokemon = [ "shaymin","hawlucha","charizard-megax","charizard-megay","lanturn","houndoom","moltres","salamence-mega","regidrago","mawile-mega","groudon-primal","kyogre-primal","xerneas","zygarde","yveltal","beedrill-mega","blaziken-mega","ferrothorn","chansey","regirock","regieleki"]
    thumbnail = thumbnail_pokemon[random.randint(0,len(thumbnail_pokemon)]

    embed = discord.Embed(description = f""" ឵឵  ឵឵  ឵឵  
` ~sets <gen> <pokeSpecies> `
gets the smogon reccomended sets for a pokemon
                          
` ~stats <gen> <poke[-forme]> <format> `
gets the showdown statistics for a pokemon

` ~user <username> `
gets a showdown users ELO GXE and GLI in ladder
 ឵឵  ឵឵  ឵឵  """, color = default_colour )
  
    embed.set_footer(text = f"Shaymax │ {author}", icon_url = "https://img.pokemondb.net/sprites/black-white/anim/normal/shaymin-land.gif")
  
    embed.set_thumbnail(url =f"https://play.pokemonshowdown.com/sprites/afd/{thumbnail}.png")

  
    return embed
