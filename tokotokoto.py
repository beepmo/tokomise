import discord
from cards import clades

def toko(title,description,footnote=None,image=None,thumbnail=None,url=None,**fields): #house name

  if url == None:
    embed = discord.Embed(title=title,description=description,color=discord.Colour.blurple()) #house colour

  elif url != None:
    embed = discord.Embed(title=title, url=url,description=description,color=discord.Colour.blurple()) #house colour

  if footnote != None:
    embed.set_footer(text=footnote)
  
  if image != None:
    embed.set_image(url=image)
  
  if thumbnail != None:
    embed.set_thumbnail(url=thumbnail)

  for key,value in fields.items():
    if type(value)==str:
      embed.add_field(name=key,value=value)
    elif type(value)==list:
      embed.add_field(name=key,value=value[0],inline=False)

  return(embed)

make1 = toko('Make card - step 1','''
For connections to remember, moments to quote...
Anything, any form your idea may take!

:whale2:

''',
thumbnail='https://i1.wp.com/i.ytimg.com/vi/9JmD_g_qCOM/maxresdefault.jpg',
Summon_convo='''
Using the text channel :ocean:
Please type a title / description / procedure / image -
any form the idea takes !

Players might be summoned for convo.
If its mechanism works, 
rinden can add it into tokomise pushcart
''',
Template_py='''
To see about filling a card in python :droplet:

Summon a discord embed template + description with `template`

^First step!
Backup with **summon convo** anytime
'''
)

make2=toko('discord.Embed()','''
The message following this embed will be the template.
Execute it as shown in picture ( & described ) :

1. Copy and paste message text into the typing box

2. Add [ 3 x ` + py ] to form python code block

3. Add tokomise command [ douzo ] in front

4. Edit inside \"  \" , and as indicated by any comments
  (Avoid any \" inside content, even if escaped with \\ .
     Tokomin needs to do some hard-coded parsing for put in ! )

5. Close with 3 codeblock ticks as in step two, on a new line

Tokomin will then send the preview.
''',image='https://cdn.discordapp.com/attachments/867508002055127080/867544217677070356/Screen_Shot_2021-07-21_at_4.09.54_PM.png',url='https://discordpy.readthedocs.io/en/latest/api.html#embed',
Troubleshooting=['''
Tokomin's one possible error message indicates that there is a mistake in the codeblock.

For feedback and help to tokomise :whale2: , 
Tokomin's python repl is given here :
https://replit.com/@beepmo/tokomise#main.py
'''],
All_Correct=['''
If the card looks ready to go:
- Determine its house & clades
[Info can be obtained through 
`description of houses and clades`]
- Use command `put in {house}`
[See `example of put in`]
'''])

prologue = toko('Tokotokoto','''
A text-literary-adventure-forum-linguistics game!

In *The Last Samurai*  by Helen DeWitt, Ludovic had a pushcart of books with him - to enter the world around? 
This game contains a tokomise pushcart of cards - to explore the world - in the book, through the book
Two houses of cards, technical and art, are accessible without reading *The Last Samurai* .

Actions:''',
'''
or: 
advertise tokomise /
make another house of cards ...

Pushcart is flexible and (players) alive!''', 
None,
'https://i1.wp.com/i.ytimg.com/vi/9JmD_g_qCOM/maxresdefault.jpg',
Explore='''
`draw a koto`

Houses of cards:
*trouvaille
art
story
technical*

or, for example,
`draw a trouvaille`
more information:
`description of houses and clades`''',
Create='''
`make card`

Let's build Pushcart!

Ever wanted to 
- make Duolingo questions
ببتي -  
 ||yayyi, write a beautiful ya||
- share a status on discord but it would not be sufficiently elaborate
...
Add to the house of technical! :mechanical_arm:

+ info in command!''',
Climb_tree_windfall='''
`draw on {card_index}`

Pushcart is played mainly with thoughts :butterfly:
But adding thoughts to the cards is important!

order `example of drawing on card` for technical details''',
Collect='''
Collect a card via a reaction emote ! :whale2:

View your collection at
`draw collection`
'''
)
prologue.set_footer(text='''or: 
advertise tokomise /
make clades ...

Pushcart is flexible and (players) alive!''',icon_url='https://i1.wp.com/i.ytimg.com/vi/9JmD_g_qCOM/maxresdefault.jpg')

cladogram = ''
for i in clades.keys():
  cladogram += i + '\n'

houses_clades=toko('Description of Houses and Clades','''
\n
As in Hogwarts, denizens are sorted into four houses.
A player can limit browsing to a specific house.

The index displayed in the footnote of each denizen consists of its house letter and a number. 
This can be used to view or add to specific cards in command `draw on {index}` 
[details in `example of drawing on card`]

Clades are like trails that denizens may be on. Mapped by the system of clades, each denizen contributes to the cityscape of tokomise. 

In the footnote, the clades that a card belongs in can also be found, affiliating other denizens on the paths.

Names:
''',
House_of_Technical='''
Technical denizens have linguistic exercises. Clades of French, Japanese, and Greek are common.
''',
House_of_Art='''
In pursuit of many masterpieces of music and imagery referenced in text, the art denizens constitute a gallery.
''',

House_of_Trouvaille='''
Sometimes, a surprise comes in the way of discovering that something in *The Last Samurai*  had been a reference. Some whereabouts like trivia are collected in this house.
''',

House_of_Story='''
Here live pieces of character musing, plot and symmetry observation, quotes, and other windfalls from close reading.
''',
Existing_Clades=cladogram
)

drawing = toko('Drawing on a card','''
By typing `draw on {index}`, a player can summon a specific card by its index.

Adding a `:`, one can add a field to a card. 
Execute as described ( & shown in picture ) :

1. Send content in a normal message - it can be anything!

2. Begin the command message with `draw on {index} : []()`
Tokomin will take the part after `:` and make a hyperlink with the text in `[]` and the url in `()`.

3. Copy the message link from step one into `()`.

4. Please fill `[]` with an emote & a one-word description of content. :oden:

''',image='https://cdn.discordapp.com/attachments/678390654211981312/870503586394693692/Screen_Shot_2021-07-29_at_6.54.19_PM.png')

template = '''```py
import discord

embedVar = discord.Embed( #this is the only block that cannot be omitted
  title="J.S. Mill",
  description=\'\'\'found salvation in Wordsworth's poetry\'\'\', #text
  url="https://replit.com/@beepmo/tokomise", #hyperlink in title; omit line if None
  color=0x1abc9c #any 0x + hex colour is valid, but house colour will be automatically used during put in
)

embedVar.add_field( #this block can be used multiple times to add info boxes
  name="I wandered lonely as a cloud", #section header
  value=\'\'\'[poem goes here]\'\'\', #section text
  inline=False #toggle True or False for columning
)

embedVar.set_thumbnail( #for adding a thumbnail picture
  url="https://flxt.tmsimg.com/assets/p5588_p_v10_av.jpg"
)

embedVar.set_image( #for adding an image
  url="https://ndbooks.imgix.net/dewitt_last_samurai_cover_final.jpg?auto=format&ch=Width,DPR&q=98&w=500"
)
```
'''



