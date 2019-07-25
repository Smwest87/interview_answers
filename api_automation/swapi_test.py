import pytest
import requests
from swapi import Starwars

#all requests are defined in the swapi.py file
swapi_class = Starwars()

class Test_Class():
    
    
    def test_obi_wan(self):
        film = swapi_class.return_film(1)
        #confirm that film id 1 = New Hope
        assert film['title'] == 'A New Hope'
        people = film['characters']
        #confirm that Obi Wan's url is in the characters array
        assert 'https://swapi.co/api/people/10/' in people
        obi_wan = swapi_class.return_person(10)
        #confirm that character id 10 is Obi Wan
        assert obi_wan['name'] == 'Obi-Wan Kenobi' 

    def test_enterprise(self):
        ship_names = []
        #intial request to acquire total_ships['count']
        ships = swapi_class.return_all_starships()
        total_ships = ships['count']
        #counter will increase with each page
        ship_counter = 0
        #storing initial next url ----- May need if then statment if ships['next'] is null
        next_url = ships['next']
        for ship in ships['results']:
            #append names to ship_name
            ship_names.append(ship['name'])
        #increase ship_counter by length of results
        ship_counter += len(ship_names)
        
        #the rest can be handled in a loop after the intial request. Can no longer use the functioons built in swapi.py though -- may need to rewrite for readability
        while ship_counter < total_ships:
            r = requests.get(next_url)
            r = r.json()
            for ship in r['results']:
                ship_names.append(ship['name'])
            ship_counter += len(ship_names)
        #this is expected to fail - I do think a try except would be useful here for a better error message 
        assert "Enterprise" in ship_names



    def test_chewi(self):
        # we know that chewi's character id is 13. However we could test the search functionality of the API here as well
        chewi = swapi_class.return_person(13)
        assert chewi['name'] == 'Chewbacca'
        # chewi['species'] is a list, but only contains one entry. I'm assuming other characters could have multiple species
        chewi_species = chewi['species'][0]
        r = requests.get(chewi_species)
        r = r.json()
        #confirm chewi_species is in fact Wookiee
        assert r['name'] == 'Wookiee'

    def test_starship_response(self):
        #my thought is that asserting ship['field'] == True will determine if the field exists unless the field is 0 or null
        #but even if it is null the field could still exist -- maybe I need to check for a NoneType in the field 
        ship = swapi_class.return_starships(10)
        #if ship['field'] == true OR if type(ship['field']) == None:
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
        
    def test_starship_count(self):
        #initial request to get the count of total_ships
        ships = swapi_class.return_all_starships()
        total_ships = ships['count']
        #ship_counter will increase by the length of each ships['results']
        ship_counter = 0
        ship_counter += len(ships['results'])
        #store the initial next url
        next_url = ships['next']

        while ship_counter < total_ships:
            r = requests.get(next_url)
            r = r.json()
            ship_counter += len(r['results'])
            next_url = r['next']

        assert ship_counter == total_ships


