#!/bin/python3
import yaml
import os
def DATA():
#obrir alavritty.yaml i transformar a diccionari
    with open ('alacritty.yml','r') as f:
        config = yaml.load(f , Loader=yaml.FullLoader)
    return config


def Themes(theme):
    global config
    theme = 'themes/'+theme+'.yaml'
#obrir tema i transformar en diccionari
    with open (theme,'r') as f:
        theme = yaml.load(f , Loader=yaml.FullLoader)

    config['colors']=theme['colors']

def get_fonts():
        with open ('fonts.yaml','r') as f:
            DC_fonts = yaml.load(f , Loader=yaml.FullLoader)
            print(DC_fonts)
        return DC_fonts

def font(font):
    global config
    fonts = get_fonts()
    endfont = fonts['fonts'][font]

    config['font']['bold']['family'] = endfont
    config['font']['italic']['family'] = endfont
    config['font']['normal']['family'] = endfont

def fontsize(size):
    global config
    config['font']['size'] = size


def opacity(val):
    global config
    config['background_opacity'] = val

def padding(val):
    global config
    config['window']['padding']['x']= val

def cursor(val):
    global config
    config['cursor']['style'] = val 


config = DATA()
config = yaml.dump(config, sort_keys= True)
print(config)
