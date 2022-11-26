import bs4 as bs
import urllib
import discord

colour = discord.Color.from_rgb(47,49,54)

def process(format, info, author):
    elo = info[0]
    if len(info) < 3:
      embed=discord.Embed(description=f"""

` ELO ` ━ {elo}
` G‌‌‌XE ` ━ (more games needed)
` GLI ` ━ (more games needed)
                          """, color=colour)
    else:
      gxe = info[1]
      gli = info[2]
      embed=discord.Embed(description=f"""
` ELO ` ━ {elo}
` G‌‌‌XE ` ━ {gxe}
` GLI ` ━ {gli}                
""", color=colour)   
    embed.set_author(name=format,icon_url="https://pokemonshowdown.com/images/icon.png")
    embed.set_footer(text=f"Shaymax │ requested by {author}", icon_url="https://img.pokemondb.net/sprites/black-white/anim/normal/shaymin-land.gif")
    return embed



def get(username_sd):


        req = urllib.request.Request(
            f'https://pokemonshowdown.com/users/{username_sd}',
            headers={'User-Agent': 'Mozilla/5.0'})

        try:
            source = urllib.request.urlopen(req).read()
        except urllib.error.HTTPError:
            raise Exception("Couldnt find that user")
        soup = bs.BeautifulSoup(source)
        table = soup.find('table')
        try:
            table_rows = table.find_all('tr')
        except AttributeError:
            raise Exception("Couldnt find that user")

        output = {}
        for tr in table_rows:
            td = tr.find_all('td')
            row = [i.text for i in td]
            try:
              output[row[0]] = row[1:]
            except:
              pass



        return output

def embed (username, output, author):
    formats = ' | '.join(output.keys())

    embed = discord.Embed(description=f"""឵឵  ឵឵  ឵឵      
**Formats:** {formats}
  ឵឵  ឵឵      """,color=colour)
    embed.set_footer(text=f"Shaymax │ requested by {author}", icon_url="https://img.pokemondb.net/sprites/black-white/anim/normal/shaymin-land.gif")
    embed.set_author( name=username,icon_url="https://pokemonshowdown.com/images/icon.png")
  
    return embed