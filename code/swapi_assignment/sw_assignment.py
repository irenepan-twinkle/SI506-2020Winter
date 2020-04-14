from sw_entities import EvacuationPlan, Garrison, MilitaryBase, \
    Person, Planet, Species, Starship
import sw_utilities as utl


ENDPOINT = 'https://swapi.py4e.com/api'

def create_person(data):
    """TODO
    """

    pass

def create_planet(data):
    """TODO
    """

    pass


def create_species(data):
    """Creates a Species instance from dictionary data (a map),
    converting string values to the appropriate type whenever
    possible.

    Parameters:
        data (dict): source data

    Returns:
        species: new Species instance
    """

    species = Species(data['url'], data['name'])
    species.classification = data['classification']
    species.designation = data['designation']
    species.language = data['language']

    return species


def create_starship(data):
    """Creates a Starship instance from dictionary data (a map),
    converting string values to the appropriate type whenever
    possible. Assigning crews and passengers are considered separate
    operations.

    Parameters:
        data (dict): source data

    Returns:
        starship: a new Starship instance
    """

    pass


def main():
    """Entry point. This program will import two custom modules (sw_entities.py,
    sw_utilities.py) that provide class definitions and utility functions designed
    to interact with local file assets and the Star Wars API (SWAPI). Additional
    utility functions designed to simply the creation of object instances are
    located above.

    main() will manage the workflow required to create two Top Secret data files
    requested by Rebel Alliance Intelligence.

    - A JSON file comprising a list of uninhabited planets where a new rebel base
      could be situated if Imperial forces discover the location of Echo Base.

    - A JSON file describing the Echo Base including an evacuation plan of base
      personnel. The plan will assign Princess Leia and the protocol droid C-3PO
      to the transport Bright Hope. Upon departure the transport will be
      escorted by an X-wing starfighter piloted by Commander Luke Skywalker
      (with astromech droid R2-D2) and the light freighter Millennium Falcon
      crewed by the smugglers Han Solo and Chewbacca, the Wookiee.

    Parameters:
        None

    Returns:
        None
    """

    # Refer to SWAPI Echo Base Assignment Guide for instructions and tips.

    # Endpoints
    swapi_people_url = f"{ENDPOINT}/people/"
    swapi_planets_url = f"{ENDPOINT}/planets"
    swapi_starships_url = f"{ENDPOINT}/starships/"

    # 8.2 WARMUP: Locate uninhabited planets


    # 8.3 TEST CODE: Create an Echo Base person


    # 8.4 TEST CODE: Create an Echo Base starship


    # 8.5 Echo Base evacuation plan

    echo_base_data = None # read file
    echo_base = None # instantiate MiltaryBase instance


    # 8.5.1 echo_base MiltaryBase


    # 8.5.2 evac_plan EvacuationPlan


    # 8.5.3 gr_75_transport Starship


    # 8.5.4 x_wing Starship


    # 8.5.5 m_falcon Starship


    # 8.5.6 Evacuation arithmetic


    # 8.5.7 Complete the evacuation plan and write to file


    # WRITE TO FILE
    filepath = 'sw_echo_base-v1p1.json'
    utl.write_custom_json(filepath, echo_base)


if __name__ == '__main__':
    main()