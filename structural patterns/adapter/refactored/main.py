import json

from bs4 import BeautifulSoup

from experiment import Experiment

"""
Experiment is the client
Main is the client interface
"""

def main() -> None:
    with open('config.json', encoding='utf-8') as file:
        config = json.load(file)
    
    experiment = Experiment(config)
    experiment.run()

if __name__ == '__main__':
    main()
