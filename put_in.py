def convert_to_toko(content):

  #optionals begin as default
  url = None
  image_url = None
  thumbnail_url = None
  fields = {}


  l1 = content.split('embedVar')

  #print(l1)

  object_block_lines = l1[1].split('\n')

  for line in object_block_lines:
    if 'title="' in line:
      title = line.split('"',2)[1]
    elif 'description=\'\'\'' in line:
      description = line.split("'''",2)[1]
    elif 'url="' in line:
      url = line.split('"',2)[1]


  addon_blocks = l1[2:] #get rid of import discord and title

  for block in addon_blocks:
    
    line = block.split('\n')

    if '.add_field(' in line[0]:

      for i in line:
        name = ''
        value = ''
        if 'name="' in i:
          name = i.split('"',2)[1]
        elif 'value=\'\'\'' in i:
          value = i.split('\'\'\'',2)[1]
        elif 'inline=' in i:
          code = i.split('#')[0] #get rid of comment
          if 'False' in code:
            list_for_value = []
            list_for_value.append(value)
            value = list_for_value
      
      fields[name] = value

    elif '.set_thumbnail(' in line[0]:
      thumbnail_url = line[1].split('"',2)[1]

    elif '.set_image(' in line[0]:
      image_url = line[1].split('"',2)[1]

  return title, description, url, fields, thumbnail_url,image_url

def convert_to_write(house,title,description,url,thumbnail_url,image_url,clades,fields):

  write_title=title.replace("'","") #delete the issue of ' by killing
  write_description=description.replace("'","")

  if len(clades) > 0:
    cladogram=""
    for i in range(len(clades)-1):
      cladogram+=clades[i]+","
    cladogram+=clades[-1]

  if len(fields) == 0:

    if len(clades) > 0:

      with open("cards.py","a") as cards:
        cards.write("\n\n"+house+"('"+write_title+"','"+write_description+"','"+str(url)+"','"+cladogram+"')")
        #no dictionary

    elif len(clades)== 0:

      with open("cards.py","a") as cards:
        cards.write("\n\n"+house+"('"+write_title+"','"+write_description+"','"+str(url)+"')")
      #no dictionary,no clades

  elif len(fields) > 0:

    fields_list=[]
    fields_string=''

    print(fields)
    for key,value in fields.items():
      #print('key,value',key,value)
      write_key=str(key).replace(' ','_').replace("'",'')
      write_value=str(value).replace("'",'')
      entry = write_key +'='+"'"+write_value+"'"
      fields_list.append(entry)

    for i in range(len(fields_list)-1):
      fields_string+=fields_list[i]+','
    fields_string+=fields_list[-1]

    #print(fields_string)

    if len(clades) == 0:
      with open("cards.py","a") as cards:
        cards.write("\n\n"+house+"('"+write_title+"','"+write_description+"','"+str(url)+"',"+fields_string+")")

    elif len(clades) > 0:
      with open("cards.py","a") as cards:
        cards.write("\n\n"+house+"('"+write_title+"','"+write_description+"','"+str(url)+"','"+cladogram+"',"+fields_string+")")

  if thumbnail_url != None:
      with open("cards.py","a") as cards:
        cards.write("\n"+house+"_dict["+house+".index]"+".set_thumbnail(url='"+thumbnail_url+"')")
      
  if image_url != None:
      with open("cards.py","a") as cards:
        cards.write("\n"+house+"_dict["+house+".index]"+".set_image(url='"+image_url+"')")
  
  with open("cards.py","a") as cards:
    cards.write('\nwhole_dict['+house+'.index]='+house+'_dict['+house+'.index]')