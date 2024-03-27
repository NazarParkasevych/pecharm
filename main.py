from swapi import get_film, get_person
def get_films_info(film_id):
    film = get_film(film_id)
    characters = film.get_characters()
    vehicles = film.get_vehicles()
    starships = film.get_starships()
    species = film.get_species()
    print(f"Фільм: {film.title}")
    print(f"Персонажі: ")
    for index, character in enumerate(characters, 1):
        homeworld = get_person(character).get_homeworld()
        homeworld_name = homeworld.name if homeworld else "не відомо"
        print(f"{index}, {character.name} з планети {homeworld_name}")
    print(f"Транспортні засоби: ")
    for index, vehicle in enumerate(vehicles, 1):
        print(f"{index}, {vehicle.name}")
    print(f"Космічні кораблі: ")
    for index, starship in enumerate(starships, 1):
        print(f"{index}, {starship.name}")
    print(f"Види істот: ")
    for index, specie in enumerate(species, 1):
        print(f"{index}, {specie.name}")
if __name__ == '__main__':
    film_id = input('Введіть ідентифікатор фільму: ')
    get_films_info(film_id)

