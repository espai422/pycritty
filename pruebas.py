import yaml

def Themes(data , theme):
#obrir alavritty.yaml i transformar a diccionari
    with open ('alacritty.yml','r') as f:
    config = yaml.load(f , Loader=yaml.FullLoader)

#obrir tema i transformar en diccionari
    with open ('themes/onedark.yaml','r') as f:
    theme = yaml.load(f , Loader=yaml.FullLoader)

#intercambiar alavritty_diccionari.colors --> colors de tema
    config['colors']=theme['colors']

    new_config = yaml.dump(config, sort_keys= True)
#tornar a escriure alacritty.yaml

    with open ('alacritty.yml','w') as f:
    f.write(new_config)

