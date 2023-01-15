import discord

art_dict = {}
tech_dict = {}
story_dict = {}
trouvaille_dict = {}

#clade names cannot contain space
clades = {'Leighton': ['{a5}', '{a7}', '{a19}'], 'Kurosawa': ['{t10}', '{t13}', '{s2}'], 'Structure': ['{s29}', '{t28}'], 'Appearance': ['{s11}', '{s2}', '{s14}', '{s26}'], 'Poetry': ['{r1}', '{a1}', '{a9}', '{a15}', '{a17}'], 'Piano': ['{a11}', '{a13}', '{s23}', '{s26}', '{s29}'], 'Song': ['{s11}', '{a3}', '{s14}', '{s8}'], 'Japanese': ['{t10}', '{t13}', '{t16}', '{t19}', '{t22}'], 'French+Latin': ['{t7}']
  }

def story(title,description,url=None,*tags,**fields): #house name
  
  story.index='{s'+str(story.count)+'}' #house letter + count

  if url == None:
    embed = discord.Embed(title=title,description=description+'\n',#color=discord.Colour.dark_blue()) #house colour
    color=0x83b2d6)

  elif url != None:
    embed = discord.Embed(title=title, url=url,description=description+'\n',color=0x83b2d6) #house colour

  if tags != None:
    labels = ''

    for tag in tags:
      if story.index not in clades[tag]: #dumb method - I have to print clades after edits and replace line 8 with it
        clades[tag].append(story.index) #house index
      labels += '\n' + tag +' '+ str(clades[tag])
    embed.set_footer(text=story.index+labels) #house index

  elif tags == None:
    embed.set_footer(text=story.index) #house index

  for key,value in fields.items():
    if type(value)==str:
      embed.add_field(name=key,value=value)
    elif type(value)==list:
      embed.add_field(name=key,value=value[0],inline=False)

  story_dict[story.index]=embed #house dict + index

  story.count += 3 #house count, different starting values and steps
story.count = 2

def art(title,description,url=None,*tags,**fields): #house name
  
  art.index='{a'+str(art.count)+'}' #house letter + count

  if url == None:
    embed = discord.Embed(title=title,description=description,color=0xa7c4bc) #house colour

  elif url != None:
    embed = discord.Embed(title=title, url=url,description=description,color=0xa7c4bc) #house colour

  if tags != None:
    labels = ''

    for tag in tags:
      if art.index not in clades[tag]: #dumb method - I have to print clades after edits and replace line 8 with it
        clades[tag].append(art.index) #house index
      labels += '\n' + tag +' '+ str(clades[tag])
    embed.set_footer(text=art.index+labels) #house index

  elif tags == None:
    embed.set_footer(text=art.index) #house index

  for key,value in fields.items():
    if type(value)==str:
      embed.add_field(name=key,value=value)
    elif type(value)==list:
      embed.add_field(name=key,value=value[0],inline=False)

  art_dict[art.index]=embed #house dict + index

  art.count += 2 #house count
art.count = 1

def trouvaille(title,description,url=None,*tags,**fields): #house name
  
  trouvaille.index='{r'+str(trouvaille.count)+'}' #house letter + count

  if url == None:
    embed = discord.Embed(title=title,description=description,color=0xc2b0eb) #house colour

  elif url != None:
    embed = discord.Embed(title=title, url=url,description=description,color=0xc2b0eb) #house colour

  if tags != None:
    labels = ''

    for tag in tags:
      if trouvaille.index not in clades[tag]: #dumb method - I have to print clades after edits and replace line 8 with it
        clades[tag].append(trouvaille.index) #house index
      labels += '\n' + tag +' '+ str(clades[tag])
    embed.set_footer(text=trouvaille.index+labels) #house index

  elif tags == None:
    embed.set_footer(text=trouvaille.index) #house index

  for key,value in fields.items():
    if type(value)==str:
      embed.add_field(name=key,value=value)
    elif type(value)==list:
      embed.add_field(name=key,value=value[0],inline=False)

  trouvaille_dict[trouvaille.index]=embed #house dict + index

  trouvaille.count += 1 #house count
trouvaille.count = 1

def tech(title,description,url=None,*tags,**fields): #house name
  
  tech.index='{t'+str(tech.count)+'}' #house letter + count

  if url == None:
    embed = discord.Embed(title=title,description=description,color=0xb3a249) #house colour

  elif url != None:
    embed = discord.Embed(title=title, url=url,description=description,color=0xb3a249) #house colour

  if tags != None:
    labels = ''

    for tag in tags:
      if tech.index not in clades[tag]: #dumb method - I have to print clades after edits and replace line 8 with it
        clades[tag].append(tech.index) #house index
      labels += '\n' + tag +' '+ str(clades[tag])

    embed.set_footer(text=tech.index+labels) #house index

  elif tags == None:
    embed.set_footer(text=tech.index) #house index

  for key,value in fields.items():
    if type(value)==str:
      embed.add_field(name=key,value=value)
    elif type(value)==list:
      embed.add_field(name=key,value=value[0],inline=False)

  tech_dict[tech.index]=embed #house dict + index

  tech.count += 3 #house count
tech.count = 7

art('Rage, rage against the dying of the `night`','''

Do not go gentle into that good night     - Dylan Thomas

*Do not go gentle into that good night,
Old age should burn and rave at close of day;
Rage, rage against the dying of the light.

Though wise men at their end know dark is right,
Because their words had forked no lightning they
Do not go gentle into that good night.

Good men, the last wave by, crying how bright
Their frail deeds might have danced in a green bay,
Rage, rage against the dying of the light.

Wild men who caught and sang the sun in flight,
And learn, too late, they grieved it on its way,
Do not go gentle into that good night.

Grave men, near death, who see with blinding sight
Blind eyes could blaze like meteors and be gay,
Rage, rage against the dying of the light.

And you, my father, there on the sad height,
Curse, bless, me now with your fierce tears, I pray.
Do not go gentle into that good night.
Rage, rage against the dying of the light.*
\n
''',None,
'Poetry',
p470='''
Do you know what I said when I woke up? said Sib.

No, I said.

Rage, rage against the dying of the night. You wouldn't have wanted to hear that from your friend.

No, I said.
''',
Poem_thoughts='''
T\'was introduced by Laura as a example of a villanelle in UTP Poetry Month 2021.

[On Villanelles](https://www.poetryfoundation.org/learn/glossary-terms/villanelle)

[Of Dylan Thomas](https://www.brainpickings.org/2017/01/24/dylan-thomas-do-not-go-gentle-into-that-good-night/)
''')

art('Yesterday by The Beatles','''
Yesterday
All my troubles seemed so far away
Now it looks as though they’re here to stay
Oh I believe in yesterday

Suddenly 
I’m not half the man I used to be
There’s a shadow hanging over me
Oh yesterday
Came suddenly

Why she had to go I don’t know she wouldn’t say
I said something wrong now I long for yesterday

Yesterday
Love was such an easy game to play
I need a place to hide away
Oh I believe in yesterday

The Beatles:
https://www.youtube.com/watch?v=NrgmdOz227I
''',
'https://www.youtube.com/watch?v=NrgmdOz227I',
'Song',
p68='''
and he would say Listen to this
and he would read out a sentence which was like Yesterday with Brahmsian harmony
''')

art('Greek Girls Playing At Ball  - Lord Leighton','''
p59
||I no sooner read it than||
I saw in my mind an image of Lord Leighton's Greek Girls Playing At Ball, 
||with its irreproachable, its even masterly use of perspective in the handling of the girls, the antique landscape,||
||no sooner did I see this than I started to laugh,||
||so shallow and superficial did it seem in comparison with (say) a print by Utamaro.||

\n
''',None,'Leighton')
art_dict[art.index].set_image(url='''
https://upload.wikimedia.org/wikipedia/commons/b/b2/Greek-girls-playing-at-ball.jpg''')

art('The Syracusan Bride Leading Wild Beasts in Procession','''
p67
By Lord Leighton, of course, I don't mean the Hellenising late-Victorian painter of A Syracusan Bride Leading Wild Beasts in Procession and Greek Girls Playing at Ball, but the painterly American writer who is the spiritual heir of the artist.
''',None,'Leighton')
art_dict[art.index].set_image(url='''
https://upload.wikimedia.org/wikipedia/commons/thumb/8/81/The_Syracusan_Bride_leading_Wild_Animals_in_Procession_to_the_Temple_of_Diana_by_Lord_Frederick_Leighton.jpg/1200px-The_Syracusan_Bride_leading_Wild_Animals_in_Procession_to_the_Temple_of_Diana_by_Lord_Frederick_Leighton.jpg''')

art('Eyes Blazing','''
p331
I could see Sibylla's thoughts circling her mind like goldfish in a bowl. At last she spoke.


To be or not to be, that is the question

Whether t'is nobler in the mind to suffer

The strings and arrows of outrageous fortune

Or to take arms against a sea of troubles

And, by opposing, end them. To die, to sleep -

No more and by a sleep to say we end

The heartache, the thousand natural shocks

That flesh is heir to; 'tis a consummation


The woman glanced aghast at the small fat crew and was at once relieved, for it was clear enough that they had not understood a word of this.
Well, of course we all have our cross to bear, she said cheerily.
Sibylla gazed down, eyes blazing, at a can of baked beans.
\n
''',None,
'Poetry'
)

art('The Well-Tempered Clavier  - Glenn Gould','''
p123
I am not really capable of replaying a fugue in my head so I listened to his queer performance of the [C minor prelude, Book I](https://www.youtube.com/watch?v=1CVlBSgj0bk&list=PLDriozYVKPiFbf6hwHW63v3TzyspILprU&index=1),
which begins with each note staccato, 
and then two-thirds of the way down the first page the notes suddenly run very smoothly and softly

''',None,
'Piano',
Reference='''
The Well-Tempered Clavier  - Kimiko Ishizaka
[C minor prelude, Book I
(BWV 846)](https://www.youtube.com/watch?v=nPHIZw7HZq4&t=279s)
''')

art('The Well-Tempered Clavier  - Glenn Gould','''
p123
and then I listened to [Prelude No. 22 in B flat minor](https://www.youtube.com/watch?v=IBkYpqGk-bI&list=PLDriozYVKPiFbf6hwHW63v3TzyspILprU&index=43) 
which I could never play without the pedal.
I think that though perhaps it should not be played with the pedal it should at least be played legato,
and yet the harsh coldness with which Gould plays this piece displaced
with its coldness, its lack of ease, 
the wilful expression with which Liberace wearies the heart.

''',None,
'Piano',
Reference='''
The Well-Tempered Clavier  - Kimiko Ishizaka
[Prelude No. 22 in B flat minor
(BWV 867)](https://www.youtube.com/watch?v=nPHIZw7HZq4&t=5399s)
''')

art('De Dumty','''
p126
Come across the poem of Keats on looking onto Chapman's Homer

would probably be interested and surprised to see that this was what Chapman had written:


De dumty dumty dumty dumty dum Iove saw their heavy chair

And (pitying them) spake to his minde; Poor wretched beasts (said he)

Why gave we you t'a mortall king? De dumty dumty

De dumty dumty dumty dum de dumty dumty dum?

De dumty dumty dumty dum de dumty dumty dum?

Of all the miserable'st things that breathe and creepe on earth,

No one more wretched is then man. And for your deathless birth,

Hector must faile to make you prise de dumty dumty dum

''',None,
'Poetry')

art('The Shield of Achilles','''
[by W. H. Auden - 1907-1973](https://poets.org/poem/shield-achilles) 
which Sibylla had been reading

Read with Iliad and [contemporary](https://harpers.org/2010/01/auden-the-shield-of-achilles/) context

Image source : https://theshieldofachilles.net/appearance/creation/
''',
'https://en.wikipedia.org/wiki/Shield_of_Achilles',
'Poetry',
p401='''
I said: They are quanta of lattice vibrational energy.
They died as men before their bodies died, said Sibylla.
''')
art_dict[art.index].set_image(url='https://achillesshieldblog.files.wordpress.com/2017/01/kathleen-vail-copyright-achilles-shield-epicenter-creation-1200x500-feature-image.png?w=705&h=435&crop=1')

art('Portrait of May Sartoris','''
''',None,'Leighton')
art_dict[art.index].set_image(url='''
https://upload.wikimedia.org/wikipedia/commons/d/db/Frederic_Leighton_-_Portrait_of_May_Sartoris_-_Google_Art_Project.jpg''')

#INSERT ART HERE

tech('Comment vivre sans inconnu devant soi',
'''
(p470)
Do you know what Boulez says somewhere? she said.
No, what does Boulez say somewhere? I said.
Comment vivre sans inconnu devant soi. Not everyone can.
Fine, I said. 
\n
''',None,'French+Latin',
l_indice='''
le sens de "comment vivre sans toi" en [une chanson](https://www.youtube.com/watch?v=ogJTCGAgmIk)
''',
le_lexique=['''
inconnu ||n. unknown||
comment ||how||
vivre to ||live||
devant ||before||
sans ||without||
soi ||one||
''']
)

tech('Yai ! Kisama','''
やい！
Yai !
貴様！
Kisama !
よく　も　俺の　事　を 
yokumo oreno koto wo
侍　か 
samurai ka
なんて
nante
吐かしやがって。。。
nukasushagatte
巫山戯る な！
fuzukeru na！
''',None,'Kurosawa','Japanese',
Kisama='''
貴様 = derogatory \"you\"
< 貴 'lordly' + 様 'sama' ''',
Fuzakeru='''
巫山戯る = deride
< 巫 'witch' + 山 'mountain' + 戯 'war' ''',
p240=['''
Asking me 'Are you a samurai?' like that – how dare you!'''])
tech_dict[tech.index].set_thumbnail(url='''
https://cdn11.bigcommerce.com/s-yzgoj/images/stencil/1280x1280/products/1387738/3021025/EVCMBDSESAEC003H__74840__86732.1551747501.jpg?c=2''')

tech('i - 05:47','''

利吉 Rikichi :
野伏せり nobuseri (bandits) 突っ tsu (stab) 殺す kkorosu (kill) だ da
みんな minna (all) 突っ  殺す  だ !
二度と nidoto (never again) 来ねえ kunee (come) ように youni (in order for)
みんな  突っ  殺す  だ

写平 Yohei :
おらあ oraa (I) 嫌 iya (detest) だ da

满足 Manzo :
できねえ dekinee (undoable) 相談 sounan (talk) だ 
そんな sonna (such) こたあ kotaa (thing)
\n
''',None,'Kurosawa','Japanese',
p13='''
\n
The version there:

Let’s make bamboo spears! Let’s kill all the bandits!
You can’t.
That’s impossible.
'''
)

tech('Doh ka na?','''
I said Nothing and she said Doh ka na? very sceptically. Doh ka na? means Really? in Japanese. (p182)

chottomattekudasai - what is Doh ka na?
Questioning how 'h' appears in romaji... A guess:
"どうか　な？
douka na?"
どうか = adv.1. somehow
            2. please

etto... why does Sibylla say so, sceptically, when Ludo is trying to hide that anything is wrong so as to not upset her?
''',None,'Japanese')

tech('What\'s Penguin?','''
p31
It's what English translators translate into.abs
Merely had a lot of fighting experience!
Determined to follow you!

p168
He said he knew Tadaima and Ohaiyogozaimasu and Konnichiwa and Sayonara and Tada kassen ni wa zuiben deta ga.

''',None,'Japanese',
只今='''
今「ima」now
只、唯「tada」just
||exp. I'm home||
||tada ima||
''',
お早う='''
早い「hayai」early, brisk
早く「hayaku」early, briskly
;exp. hurry.
Ludo said 1 extra "i"
||exp. Good morning||
||ohayou||
''',
御座います='''
御「go」royal
- 御免 sorry
; 免「men」pardon.
- 御主人　husband
; 主 main 人 person
; 主人「shujin」master
座「za」seat
います「imasu」to be
- 有難う御座います
「arigatougozaimasu」thanks
||exp. to be||
||gozaimasu||
''',
左様なら='''
左様「sayou」like so
なら「nara」if so
||adieu||
||sayounara||
''',
只合戦には随分出たが='''
合戦「kassen」battle
随分「zuibun」a lot
出た「deta」past. 出る「deru」go

Syntax:「合戦には随分出た」= object
||Merely had a lot of fighting experience||
'''
)

tech('Douzo, jinsai','''
p186

if she picked 火「hi/ka  fire」

and I picked 炎「en  flame」

and we bore in mind the fact that 巛 was the radical marigawa for river

we would understand in an intuitive way why 災「sai／wazawa」meant natural calamity/disaster

and we would then see why 人災 「jinsai」was a manmade calamity

and 火災 「kasai」was fire or conflagration

''',None,'Japanese',
Chinese1='''
灾 = 災
= house radical + 火
''',
Chinese2='''
Inconsistencies:
災 main radical 巛 or 火
巛 stroke number 3 or 6
''',
Chinese3='''
the only other common character with 巛 main radical:
巢 nest
''',
Douzo='''
どうぞ by all means, please
''',
p186p187p201=['''
An indispensible euphemism for a small child.
Douzo, jinsai.
Not to my knowledge, jinsai.
'''])

tech('子','''
「ko」small
''',
子猫='''
猫「neko」cat
||kitten||
''',
子犬='''
犬「inu」dog
||puppy||
''',
子供='''
供「tomo」follower
||child||
''',
p408=['''The silence stretched out, for my mother was debating inwardly the right of one rational being to exercise arbitrary authority over another rational being on the ground of seniority. 
Or rather she was not debating this, for she did not believe in such a right, but she was resisting the temptation to exercise such power sanctioned only by the custom of the day. 
At last she said: Well then I’ll see you tomorrow.'''])

tech('Ludere','''
p131. When I got home it was obvious that his name was actually Ludovic so I called him that having really no choice in the matter.''',None,
'Structure','French+Latin',
Ludere='''Ludes = you play
Ludet = he/she/it/they play
Ludemus = we play
Ludetis = y'all play
Ludent = they play
`Ludo` = I play''')

tech('Kanji  様 「sama」','''
Coming from Chinese, 様 means likeness.
Another pronounciation is「you」and 様 is the kanji for the expressions 「youni」, in order for / like ; and 「douyouni」, similarly
As a suffix, 様 「sama」 is an honourific title like -san, added in address to a person, and much more!
''',None,'Japanese',animate='''
神様　「kami-sama」god
皆様　「minna-sama」everyone
高橋様　「takahashi-sama」honourific person Takahashi
お主様　「onushi-sama」(guardian) spirit
ご主人　「goshujin-sama」master
貴様　「kisama」(derogatory) you
お客様　「okyaku-sama」customer
お子様 　「okosama」child
母様　「kaasama」mother
御父様　「omousama」father''',celestrial='''
お日様　「ohi-sama」sun
お星様　「ohoshi-sama」stars
お月様　「otsuki-sama」moon
''',conceptual=['''
ご苦労様　「thank you for your hard work」
お疲れ様　「thank you for hard work / you must be fatigued」

- after a meal,
ご馳走様　「feast / thank you for the feast」
- much formally,
お粗末様　「crude rice (fare) 'twas」
'''])
print(tech.index)
#INSERT TECH HERE

trouvaille('J. S. Mill found salvation in Wordsworth\'s poetry','''
Discovering, at last, the salvation of Wordsworth’s poetry, Mill felt himself reconnected to natural beauty, and to “the common feelings and common destiny of human beings.”

(New Yorker article - read with moderation!)
\n
''',
'https://www.newyorker.com/magazine/2018/06/04/helen-dewitt-has-your-number','Poetry',A_poem='''

I wandered lonely as a cloud

I wandered lonely as a cloud 
That floats on high o'er vales and hills,
When all at once I saw a crowd,
A host, of golden daffodils;
Beside the lake, beneath the trees,
Fluttering and dancing in the breeze.

Continuous as the stars that shine
And twinkle on the milky way,
They stretched in never-ending line
Along the margin of a bay:
Ten thousand saw I at a glance,
Tossing their heads in sprightly dance.

The waves beside them danced; but they
Out-did the sparkling waves in glee:
A poet could not but be gay,
In such a jocund company:
I gazed—and gazed—but little thought
What wealth the show to me had brought:

For oft, when on my couch I lie
In vacant or in pensive mood,
They flash upon that inward eye
Which is the bliss of solitude;
And then my heart with pleasure fills,
And dances with the daffodils.
''')

trouvaille('Sorabji','''Richard Sorabji co-edits the Ancient Commentators series of translations with Prof Griffin.''',
Evidence='written under \"Research\" - https://philosophy.ubc.ca/profile/michael-griffin/')

story('Rikichi of burning eyes','''
is so addressed by Sibylla on p173, 
referring to his scene on [ p13 = part i of book 1 = 05:47 of movie ]

There had also been a mention on p76 :
Rikichi glared from the screen with burning eyes; his pale face glowed in the cold dark room.
''',None,
'Kurosawa','Appearance')
story_dict[story.index].set_image(url='''
https://cdn.discordapp.com/attachments/678390654211981312/869054562248560700/Screen_Shot_2021-07-25_at_8.12.15_PM.png''')

trouvaille('Sibyl','''
The English word sibyl (/ˈsɪbəl/ or /ˈsɪbɪl/) comes — via the Old French *sibile* and the Latin *sibylla* — from the ancient Greek Σίβυλλα (Sibylla).
Varro derived the name from *theobule* ("divine counsel"), but modern philologists mostly propose an Old Italic or alternatively a Semitic etymology''','https://en.wikipedia.org/wiki/Sibyl#History',
First_known_mention='''
Heraclitus, 5th century BC:

The Sibyl, with frenzied mouth uttering things not to be laughed at, unadorned and unperfumed, yet reaches to a thousand years with her voice by aid of the god.
''')

#INSERT TROUVAILLE HERE

story('Surrounded by a desert','''
p88
If there was this desert of technical work to be crossed before you could play the piano, maybe every other instrument and maybe the voice was also surrounded by a desert.
\n
''')

story('Sound of Music','''
Sibylla liked to listen to The hills are alive (A-a-a-ah), although she criticized Mr. Konisberg for reenacting the Goddamned Sound of Music in the home of her mother.
\n
''',None,
'Song',
p106='''
& I dont’t know about you but I am about ready for The hills are alive (A-a-a-ah).

heptakaihebdomekontapus
[Ah. Forget it]
''',
p90='''
Well, if you want to ruin people’s lives, fine.
If you want to reenact the Goddamned Sound of Music in the home, fine.
But you don’t have to blame it on Hitler.
''')
story('Name','Ludovic and Sibylla both addressed their mothers by first name.')

story('What Buddy looked like',
'''
p5
He looked a lot like Buddy Holly, and in fact people called him Buddy (he preferred it to Werner).
''',
'https://www.youtube.com/watch?v=M4TfFTmITLo',
'Song','Appearance')
story_dict[story.index].set_image(url='''
http://www.famoussingers.org/images/buddy-holly.jpg''')

story('Wake','''
p123
; how cruel that we must
||wake each time to answer to the same name,||
||revive the same memories,||
||take up the same habits and stupidities that we shouldered the day before and lay down to sleep.||

I did not want to watch him wake to go on as he had begun.
''')

story('Doom. Doom. Doom.','''
In the interlude and proglogue
\n
''',
p10='''
Linda plunged down to the bass and hammered three bitter low notes. 

Doom. Doom. Doom.
''',
p79='''
Linda had seen four before her do something that was not so terrible and already there was something about them, their whole lives ahead of them and the best things cut off, as if something that might have been a Heifetz had been walled up inside an accountant and left to die.

Doom. Doom. Doom.
''')

story('used to go away and think',
'''
p90
I `used to` think that things might have been different. 
||Gieseking never played a scale and Glenn Gould hardly ever practiced at all, they would just look at a scale and think and think and think.
If the homely man just said to `go away and think` this would have been every bit as revolutionary a concept for a Konigsberg.||
||Perhaps he even thought that you had to think.||
||But you can't show someone how to think in an hour; you can give someone an exercise to take away.||
||My grandfather would not have been troubled by silent thought;||
||he would not have kindly commanded my mother to enjoy her music and thus driven her out of the house;
and everything mighht have been different.||
''',None,
'Piano')

story('Linda','''
p10
To the front room followed by Buddy to argue for his POV -
In the front room was a 17-year-old girl with fierce black hair, fierce black eyes & ferocious red lipstick.

She did not look up because she was halfway through her 41st consecutive rendition of Chopin's Prelude No.24 in D minor.

[Chopin Prelude op. 28 n°24 in D minor `The Storm`](https://www.youtube.com/watch?v=nIsCvQPOdcM)
\n
''',None,
'Appearance','Piano',
p469=['''
rucking the sleeves up to her elbows in the what-this-old-thing way she and her friends always wore cashmere sweaters.
'''],
p79='''
Five years you studied the violin his father said and did you practice five minutes? Five years piano.
''',
p84='''
& she said vivaciously: Might as well be hung for a sheep as a lamb!
I'm a little pressed for time, said the man, but he went back and sat with one leg crossed over one knee.
My mother went to the piano and sat down. She had not practiced, but in the last week she had played Chopin's Prelude No.24 in D minor 217 times.
''')

story('Straight No Chaser - Done','''
Tracking the streak of one song through the story, 
intertwined with
the act of deal - to Sibylla from Ludo -
and "Seven Samurai".
''',None,
'Piano','Structure',
One_p33 = '''
& he can play Straight No Chaser which he learned by listening to the tape & trying to copy it about 500 times -
it is wonderful ... 
yet trying to type 62 years
... can be hard to feel a proper
''',
Three_p130='''
I kept thinking of appealing names such as Hasdrubal and Isambard Kingdom and Thelonius, and Rabindranath, 
and Darius Xerxes (Darius X.) and Amédée and Fabius Cunctator ...

Thelonius Monk was a jazz pianist of genius 
''',
Jazz_pianist_of_genius=['''
Thelonius Monk's Straight, No Chaser (1966)
(which gave name to the band which played The Twelve Days of Christmas) :
https://www.youtube.com/watch?v=7naC7TF9OU0

Biographer :
> the same kind of percussive techniques you use on the drums, an uncanny ability to play different dynamics in different fingers.
> bipolar disorder and devastating prescription
> deliberate, very thought-out. It was hard for Monk to play Monk

https://www.theatlantic.com/entertainment/archive/2010/03/the-secret-life-of-thelonious-monk/38128/
'''],
Two_p35='''
You're missing a masterpiece of modern cinema. Finish the *Odyssey* and I'll teach you the hiragana, yes?

Done.

Emma offered me a work permit & a job.

I said: Done.
''',
Four_p482='''
Make this CD and I'll teach you to play Straight No Chaser.

He said: Done.
''',
More_music=['''
Kaleidoscope by Uehara Hiromi, jazz pianist of genius who played at the 2021 Tokyo Olympics :
https://www.youtube.com/watch?v=QU2893TnTbU

Chance duets "take the adventurous list set - including tunes by Monk - to an ethereal new level" (1996) :
https://chickcorea.com/discography/duet-2/

[Album] Monk's Dream :
https://www.youtube.com/watch?v=icFRHJ9VZaw
'''])

story('scholarly charm','''
p75
この世界の教科書
ような笑顔で
a smile like textbook (albeit the textbook of this world)
''')
print(story.index)

#INSERT STORY HERE

whole_dict={**story_dict,**tech_dict,**trouvaille_dict,**art_dict}
#following are appends
#whole_dict will be redefined as sum of houses dicts in main

whole_dict['{s11}'].add_field(name='Something from beepcmo',value= '''[ 🛡️ father](https://discord.com/channels/701628890585497680/772184271413837885/870484036475289671)''',inline=False)

whole_dict['{t7}'].add_field(name='Something from beepcmo',value=''' [ 🧐  confused ](https://discord.com/channels/701628890585497680/772184271413837885/870017190471032872)

''',inline=False)

whole_dict['{r2}'].add_field(name='Something from beepcmo',value=''' [ 🦋 support ! ](https://discord.com/channels/701628890585497680/772184271413837885/870020051607113788)

''',inline=False)




whole_dict['{t28}'].add_field(name='Something from 🜋 🜋 🜋',value=''' [Lude mus is what you would say to order a mouse to play (a lot of we conjugations in Latin are imperatives to a mouse, funnily enough.) Ludo is the dative of ludus (a game), used when something is being given to it or something is being done for it. For instance, *the athlete prepared for the game* in Latin is *athleta se paravit ludo.* Ludi funebres are funeral games. This is a Roman custom (which they in turn probably took from the Greeks) in which someone's death would be commemorated with athletic contests.]

''',inline=False)

whole_dict['{t28}'].add_field(name='Something from beepcmo',value=''' In *The Last Samurai* , part II chapter 3 is *ludi funebres*

''',inline=False)