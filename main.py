import os
import discord
import random
from cards import art_dict, tech_dict, trouvaille_dict, story_dict, clades, art, tech, trouvaille, story
from tokotokoto import toko, prologue, make1, make2, template, houses_clades, drawing

print(clades)

whole_dict={**story_dict,**tech_dict,**trouvaille_dict,**art_dict}

story_keys = list(story_dict.keys())
trouvaille_keys = list(trouvaille_dict.keys())
art_keys = list(art_dict.keys())
tech_keys = list(tech_dict.keys())
whole_keys = list(whole_dict.keys())

client = discord.Client()

@client.event
async def on_ready():
    print("I'm in")
    print(client.user)

@client.event
async def on_message(message):

  if message.author == client.user: #no reply to self
    return

  text=None
  embed=None

  if 'help' in message.content.lower():
    embed=prologue

  elif 'draw a' in message.content.lower():
    
    if 'art' in message.content.lower():
      index = random.choice(art_keys)
    
    elif 'trouvaille' in message.content.lower():
      index = random.choice(trouvaille_keys)

    elif 'story' in message.content.lower():
      index = random.choice(story_keys)

    elif 'technical' in message.content.lower():
      index = random.choice(tech_keys)

    elif 'koto' in message.content.lower():
      index = random.choice(whole_keys)
    
    embed = whole_dict[index]

  elif 'description of houses and clades' in message.content.lower():
    embed = houses_clades
  
  elif 'make card' in message.content.lower():
    embed=make1

  elif 'template' in message.content.lower():

    text=template
    embed = make2

  elif 'douzo' in message.content:
    
    code = message.content[10:-3] #chop the first 10 characters for 'douzo```py' and last 3 characters for '```'
    d = {}
    try:
      exec(code,d) #exec does not work in function, put in dictionary
      #import discord needed in dictionary
    except:
      text='An error occurred; please check and retry.'

    embed = d['embedVar']
  
  elif 'draw on' in message.content.lower():

    if ':' in message.content:
      
      author=str(message.author)[:-5] #omit discord tag

      something=message.content.split(':',1)[1]+'\n\n'

      index=message.content.split(':',1)[0].split()[2]

      try:
        whole_dict[index].add_field(name='Something from '+author,value=something,inline=False)

        embed=whole_dict[index]

        with open('cards.py','a') as cards:
          cards.write('\n\nwhole_dict[\''+index+'\'].add_field(name=\'Something from '+author+'\',value=\'\'\''+something+'\'\'\',inline=False)')

        text = 'Field saved!'

      except:
        text='An error occurred; please check and retry'

    elif ';' not in message.content:
      index=message.content.split()[2]
      embed=whole_dict[index]

  elif 'example of drawing on card' in message.content.lower():
    embed = drawing

  elif 'put in house of ' in message.content.lower():
    level1 = message.content.split('\n',2) #gotta have clades line
  
    try:
      house = level1[0].split()[4].lower() #to avoid lowering clades and code

      clades = [] #optionals begin as default

      clades = level1[1].split()[1:] #exclude word clade
      #clade names cannot contain space
      #test tuple - does not matter
      code = level1[2]

    except:
      text='An error occurred. Recommendation: check command formatting'

    else:
      from put_in import convert_to_toko
      try:
        convert_to_toko(code)
      except:
        text='An error occurred. Recommendation: check that there are no extra changes to template, eg. new line, spaces surrounding `=`.'

      else:
        title, description, url, fields, thumbnail_url, image_url = convert_to_toko(code)
      
        try:
          if house == 'art':
            art(title,description,url,*clades,**fields) #create embed, automate footer, and update art_dict
            #don't do non-keyword argument after keyword argument: make the first arguments non-keyword
            if image_url != None:
              art_dict[art.index].set_image(url=image_url)
            if thumbnail_url != None:
              art_dict[art.index].set_thumbnail(url=thumbnail_url)   
            
            embed = art_dict[art.index] #send it
            whole_dict[art.index] = art_dict[art.index] #update whole_dict

          elif house == 'trouvaille':
            trouvaille(title,description,url,*clades,**fields) #create embed, automate footer, and update trouvaille_dict
            if image_url != None:
              trouvaille_dict[trouvaille.index].set_image(url=image_url)
            if thumbnail_url != None:
              trouvaille_dict[trouvaille.index].set_thumbnail(url=thumbnail_url)   
            
            embed = trouvaille_dict[trouvaille.index] #send it
            whole_dict[trouvaille.index] = trouvaille_dict[trouvaille.index]

          elif house == 'tech':
            tech(title,description,url,*clades,**fields) #create embed, automate footer, and update tech_dict
            if image_url != None:
              tech_dict[tech.index].set_image(url=image_url)
            if thumbnail_url != None:
              tech_dict[tech.index].set_thumbnail(url=thumbnail_url)   
            
            embed = tech_dict[tech.index] #send it
            whole_dict[tech.index] = tech_dict[tech.index]

          elif house == 'story':
            story(title,description,url,*clades,**fields) #create embed, automate footer, and update story_dict
            if image_url != None:
              story_dict[story.index].set_image(url=image_url)
            if thumbnail_url != None:
              story_dict[story.index].set_thumbnail(url=thumbnail_url)   
            
            embed = story_dict[story.index] #send it
            whole_dict[story.index] = story_dict[story.index]

        except:
          text='An error occurred. Recommendation: check that house is correctly specified.'
        else:
          from put_in import convert_to_write

          convert_to_write(house,title,description,url,thumbnail_url,image_url,clades,fields)

          text='Card saved!'

  elif 'draw collection' in message.content.lower():
      import importlib
      try:
        collection=importlib.import_module(str(message.author.id))

        title = str(message.author)[:-5]+'\'s collection'
        description = ''' '''
        for key, value in collection.d.items():
          description += '\n'+str(key)+' : '+str(value) 

        embed = toko(title,description)
        
      except:
        text='Nothing here yet. Begin building your collection by reacting to a card!'

  else:
    hear1 = ['hi ','hello','toko'] #hi with space
    say1 = ['арвуэ :watermelon:','Salut','tokotokoto ga suki desu ^-^','douzo (Sibylla\'s way, please)','tokomise - 床店 small shop - came from floor shop and had sometimes been a pushcart','namae wa Tokomin - tokomise no Tokomin desu \nname\'s Tokomin - I\'m Tokomin of tokomise','le melon d\'eau :watermelon:']

    for i in hear1:
      if i in message.content.lower():
        text=random.choice(say1)

  if embed != None:
    await message.channel.send(embed=embed)
  if text != None:
    await message.channel.send(content=str(text))

@client.event
async def on_reaction_add(reaction,user):

  embeds_list = reaction.message.embeds
  try: #will except for non-collectibles
    card = embeds_list[0]
    #type(card) == <class 'discord.embeds.Embed'>

    print(card.footer)
    #EmbedProxy(text="{t16}\nJapanese ['{t10}', '{t13}', '{t16}']") if footer exits, else EmbedProxy()

    if '{' in str(card.footer): #no random footers containing '{' please

      try: #EmbedProxy gives random '' or ""
        footer_text=str(card.footer).split('"',2)[1]
      except:
        footer_text=str(card.footer).split("'",2)[1]
      print(footer_text)
      index = footer_text.split('\\n')[0]
      print(index)

      reacters = await reaction.users().flatten()

      import importlib

      for i in reacters:
        i = str(i.id)
        try: #user has collection

          collection = importlib.import_module(i)
          if reaction.emoji in collection.d.keys():
            collection.d[reaction.emoji].append(index)
          else:
            collection.d[reaction.emoji]=index

          with open(i+'.py','w') as collection_file: #save to file
            collection_file.write('d='+str(collection.d))

        except: #user needs new collection
          with open(i+'.py','w') as new_collection:
            new_collection.write("d={}\nd[\'"+str(reaction.emoji)+"\']=[\'"+index+"\']")
  except:
    pass

import keep_alive
token = os.environ['TOKEN']
client.run(token)


