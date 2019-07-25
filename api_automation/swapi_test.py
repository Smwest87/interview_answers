import pytest
import requests
from swapi import Starwars

swapi_class = Starwars()

ships = ships = swapi_class.return_all_starships()

class Test_Class():
    
    
    def test_one(self):
        film = swapi_class.return_film(1)
        assert film['title'] == 'A New Hope'
        people = film['characters']
        assert 'https://swapi.co/api/people/10/' in people
        obi_wan = swapi_class.return_person(10)
        assert obi_wan['name'] == 'Obi-Wan Kenobi' 

    def test_two(self):
        ships = swapi_class.return_all_starships()
        ship_names = []
        for ship in ships['results']:
            ship_names.append(ship['name'])
        assert "Enterprise" in ship_names


    def test_three(self):
        chewi = swapi_class.return_person(13)
        chewi_species = chewi['species'][0]
        r = requests.get(chewi_species)
        r = r.json()
        assert r['name'] == 'Wookiee'

    def test_four(self):
        ship = swapi_class.return_starships(10)
        assert ship['name']
        assert ship['model']
        assert ship['manufacturer']
        assert ship['cost_in_credits']
        assert ship['length']
        assert ship['max_atmosphering_speed']
        assert ship['crew']
        assert ship['passengers']
        assert ship['cargo_capacity']
        assert ship['consumables']
        assert ship['hyperdrive_rating']
        assert ship['MGLT']
        assert ship['starship_class']
        assert ship['films']
        assert ship['created']
        assert ship['edited']
        assert ship['url']
        assert ship['pilots']
        
    def test_five(self):
        ships = swapi_class.return_all_starships()
        count = ships['count']
        counter = 0
        counter += len(ships['results'])
        next_url = ships['next']

        while counter < count:
            r = requests.get(next_url)
            r = r.json()
            counter += len(r['results'])
            next_url = r['next']

        assert counter == count


