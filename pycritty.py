import argparse
import yaml

def get_data():

    with open ('alacritty.yml','r') as f:
        config = yaml.load(f , Loader=yaml.FullLoader)
    
    return config
