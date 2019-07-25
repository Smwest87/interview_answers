import requests


class Starwars:

    def __init__(self):
        self.host = 'https://swapi.co/api'

    def return_all_people(self):
        r = requests.get(self.host + '/people/')
        return r.json()

    def return_all_films(self):
        r = requests.get(self.host + '/films/')
        return r.json()

    def return_all_starships(self):
        r = requests.get(self.host + '/starships/')
        return r.json()

    def return_all_species(self):
        r = requests.get(self.host + '/species/')
        return r.json()


    def return_person(self,id):
        r = requests.get(self.host + '/people/' + str(id))
        return r.json()

    def return_film(self,id):
        r = requests.get(self.host + '/films/' + str(id))
        return r.json() 

    def return_starships(self,id):
        r = requests.get(self.host + '/starships/' + str(id))
        return r.json()    

    def return_specie(self,id):
        r = requests.get(self.host + '/species/' + str(id))
        return r.json()