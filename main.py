from swapi.api import Swapi

# Ініціалізуємо клієнт SWAPI
swapi = Swapi()

def get_film_details(film_id):
    # Отримуємо дані про фільм
    film = swapi.get_film(film_id)

    # Виводимо назву фільму
    print(f"Фільм: {film.title}")

    # Виводимо персонажів та їх планети
    print("Персонажі:")
    for character_url in film.characters:
        character = swapi.get_person(character_url)
        homeworld = swapi.get_planet(character.homeworld)
        print(f"{character.name} з планети {homeworld.name}")

    # Виводимо транспортні засоби
    print("Транспортні засоби:")
    for vehicle_url in film.vehicles:
        vehicle = swapi.get_vehicle(vehicle_url)
        print(vehicle.name)

    # Виводимо космічні кораблі
    print("Космічні кораблі:")
    for starship_url in film.starships:
        starship = swapi.get_starship(starship_url)
        print(starship.name)

    # Виводимо види істот
    print("Види істот:")
    for species_url in film.species:
        species = swapi.get_species(species_url)
        print(species.name)


if __name__ == "__main__":
    film_id = input("Введіть ідентифікатор фільму: ")
    get_film_details(film_id)
