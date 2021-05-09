import argparse
import yaml
import os



class myerror(Exception):
   pass 




def get_data():

    with open ('alacritty.yml','r') as f:
        data = yaml.load(f , Loader=yaml.FullLoader)
    
    return data


def get_themes(theme):
    files = os.listdir(path='themes')
    themes = []
    for i in files:
        themes.append(i.split('.')[0])
    print(themes)
    try:
        if theme in themes:
            return theme
        raise myerror('theme error')
    except:
    




def Themes(data , theme):
    path = 'themes/'+theme+'.yaml'
    #obrir tema i transformar en diccionari
    with open ( path ,'r') as f:
        theme = yaml.load(f , Loader=yaml.FullLoader)

    #intercambiar alavritty_diccionari.colors --> colors de tema
    data['colors']=theme['colors']

    new_config = yaml.dump(data, sort_keys= True)
    #tornar a escriure alacritty.yaml

    with open ('alacritty.yml','w') as f:
        f.write(new_config)

get_themes()
