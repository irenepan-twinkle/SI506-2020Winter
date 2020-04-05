import copy
import json
import requests

ENDPOINT = 'https://swapi.co/api'

class Entity:
    """Base representation of a resource. Instantiate with name
    and resource identifier.

    Attributes:
        name: resource name
        url: resource identifier

    Methods:
        assign_values: convenience method for loading in dict data
        jsonable: return JSON-friendly dict representation of the object
    """

    def __init__(self, name, url):
        self.name = name
        self.url = url # resource identifier


    def assign_values(self, data):
        """Bulk assign dictionary/map values. Iterate over object
        attributes (__dict__.keys()) and assign data values on matching
        keys using built-in setattr() function.

        Parameters:
            data (dict): key/value pairs to assign

        Returns:
            None
        """

        pass


    def jsonable(self):
        """Return a JSON-friendly representation of the object.
        Use a dictionary literal rather than built-in dict() to avoid
        built-in lookup costs.

        Do not simply return self.__dict__. It can be intercepted and
        mutated, adding, modifying or removing instance attributes as a
        result.

        Parameters:
            None

        Returns:
            dict: dictionary of the object's instance variables
        """

        return {'name': self.name, 'url': self.url}


    def __str__(self):
        return self.name


class Person(Entity):
    """Representation of a person.

    Attributes:
        name: person name
        url: person's resource identifier
        gender: person's gender
        birth_year: person's birth_year
        homeworld: person's home planet

    Methods:
        get_homeworld: retrieve home planet
        jsonable: return JSON-friendly dict representation of the object
    """

    def __init__(self, name, url):
        super().__init__(name, url)
        self.gender = None
        self.birth_year = None
        self.homeworld = None


    def get_homeworld(self, url):
        """Retrieve SWAPI representation of home planet.
        Convert to Planet instance and assign to person.

        Parameters:
            url (str): resource identifier

        Returns:
            None
        """

        pass


    def jsonable(self):
        """Return a JSON-friendly representation of the object.
        Use a dictionary literal rather than built-in dict() to avoid
        built-in lookup costs.

        Do not simply return self.__dict__. It can be intercepted and
        mutated, adding, modifying or removing instance attributes as a
        result.

        Parameters:
            None

        Returns:
            dict: dictionary of the object's instance variables
        """

        # return self.__dict__ # DANGEROUS
        # return copy.deepcopy(self.__dict__) # safe but slow

        return {
                'url': self.url,
                'name': self.name,
                'gender': self.gender,
                'birth_year': self.birth_year,
                'homeworld': self.homeworld
            }


    def __str__(self):
        return self.name


class Planet(Entity):
    """Representation of a planet.

    Attributes:
        gravity: gravity level
        climate: climate description
        terrain: terrain description
        population: population size

    Methods:
        jsonable: return JSON-friendly dict representation of the object
    """

    def __init__(self, name, url):
        super().__init__(name, url)
        self.gravity = None
        self.climate = None
        self.terrain = None
        self.population = None


    def jsonable(self):
        """Return a JSON-friendly representation of the object.
        Use a dictionary literal rather than built-in dict() to avoid
        built-in lookup costs.

        Do not simply return self.__dict__. It can be intercepted and
        mutated, adding, modifying or removing instance attributes as a
        result.

        Parameters:
            None

        Returns:
            dict: dictionary of the object's instance variables
        """

        # return self.__dict__ # DANGEROUS
        # return copy.deepcopy(self.__dict__) # safe but slow

        return {
                'url': self.url,
                'name': self.name,
                'gravity': self.gravity,
                'climate': self.climate,
                'terrain': self.terrain,
                'population': self.population
            }


    def __str__(self):
        return self.name


class Starship(Entity):
    """A crewed vehicle used for traveling in realspace or hyperspace.

    Attributes:
        name: starship name or nickname
        url: resource identifier
        model: manufacturer's model name
        manufacturer: starship builder
        dimensions: starship length, width, height
        max_atmosphering_speed: max sub-orbital speed
        hyperdrive_rating: lightspeed propulsion system rating
        MGLT: megalight per hour traveled
        crew: crew size
        crew_members: crew (role, name) assigned to starship
        passengers: number of passengers starship rated to carry
        cargo_capacity: cargo metric tonnage starship rated to carry
        consumables: max period in months before on-board provisions
            must be replenished
        armament: offensive and defensive weaponry

    Methods:
        assign_crew: assign crew members to starship
        jsonable: return JSON-friendly dict representation of the object
    """

    def __init__(self, name, url):
        super().__init__(name, url)
        self.starship_class = None
        self.model = None
        self.manufacturer = None
        self.dimensions = None
        self.max_atmosphering_speed = None
        self.hyperdrive_rating = None
        self.MGLT = None
        self.crew = None
        self.crew_members = {}
        self.passengers = None
        self.cargo_capacity = None
        self.consumables = None
        self.armament = []


    def assign_crew(self, crew):
        """Assign crew to crew_member dictionary.

        Parameters:
            crew (dict): key maps to role (e.g., pilot), value maps to
                         crew member name.

        Returns:
            None
        """

        pass


    def jsonable(self):
        """Return a JSON-friendly representation of the object.
        Use a dictionary literal rather than built-in dict() to avoid
        built-in lookup costs.

        Do not simply return self.__dict__. It can be intercepted and
        mutated, adding, modifying or removing instance attributes as a
        result.

        Parameters:
            None

        Returns:
            dict: dictionary of the object's instance variables
        """

        # return self.__dict__ # DANGEROUS
        # return copy.deepcopy(self.__dict__) # safe but slow

        return {
            'url': self.url,
            'name': self.name,
            'starship_class': self.starship_class,
            'model': self.model,
            'manufacturer': self.manufacturer,
            'dimensions': self.dimensions,
            'max_atmosphering_speed': self.max_atmosphering_speed,
            'hyperdrive_rating': self.hyperdrive_rating,
            'MGLT': self.MGLT,
            'crew': self.crew,
            'crew_members': self.crew_members,
            'passengers': self.passengers,
            'cargo_capacity': self.cargo_capacity,
            'consumables': self.consumables,
            'armament': self.armament
        }


    def __str__(self):
        return f"{self.starship_class} {self.model} {self.name}"


class CustomEncoder(json.JSONEncoder):
    """Extends the json module's JSONEncoder class in order to serialize
     composite class instances.

     Note: include the pylint disable comment as Windows users have
     reported issues when the default() method is called.

     Methods:
        default: overrides default method
     """

    def default(self, obj): # pylint: disable=E0202
        """Check object is provisioned with a jsonable method that is
        callable. If yes override default serialization handling.

        Parameters:
            obj (object): class instance

        Returns:
            dict: dictionary representation of the object
        """

        if hasattr(obj, 'jsonable') and callable(obj.jsonable):
            return obj.jsonable()
        else:
            return json.JSONEncoder.default(self, obj)


def get_swapi_resource(url, params=None, timeout=20):
    """Description removed. For you to write.

    Parameters:
        url (str): a url that specifies the resource.
        params (dict): optional dictionary of querystring arguments.
        timeout (int): timeout value in seconds

    Returns:
        dict: dictionary representation of the decoded JSON.
    """

    pass


def read_json(filepath):
    """Description removed. For you to write.

    Parameters:
        filepath (str): path to file.

    Returns:
        dict: dictionary representations of the decoded JSON document.
    """

    with open(filepath, 'r', encoding='utf-8') as file_obj:
        data = json.load(file_obj)

    return data


def write_json(filepath, data):
    """Serializes basic objects (e.g., dictionaries and lists)
    as JSON using default encoder. Writes content to the provided filepath.

    Parameters:
        filepath (str): the path to the file.
        data (dict): the data to be encoded as JSON and written to the file.

    Returns:
        None
    """

    with open(filepath, 'w', encoding='utf-8') as file_obj:
        json.dump(data, file_obj, ensure_ascii=False, indent=2)


def write_custom_json(filepath, obj):
    """Serializes complex objects (e.g., composite class instances) as JSON
    by adding a CustomEncoder to the json.dump() call. Writes content to the
    provided filepath.

    Parameters:
        filepath (str): the path to the file.
        data (dict): the data to be encoded as JSON and written to the file.

    Returns:
        None
    """

    with open(filepath, 'w', encoding='utf-8') as file_obj:
        json.dump(obj, file_obj, cls=CustomEncoder, ensure_ascii=False, indent=2)


def main():
    """Entry point for program. Orchestrates workflow involving
    reading in local data, issuing GET requests to retrieve remote data,
    instantiating class instances, and writing out data as JSON to a file.
    """

    # 1.0 DATA PREP

    # 1.1 Retrieve SWAPI representation of the Millenium Falcon (base)
    url = f"{ENDPOINT}/starships"
    params = {'search': 'falcon'}
    swapi_m_falcon = None

    # print(f"\nSWAPI = {swapi_m_falcon}\n")

    # 1.2 Read in additional Millenium Falcon data
    filepath = 'wookiee_m_falcon.json'
    wookiee_m_falcon = None

    # print(f"\nLocal = {wookiee_m_falcon}\n")

    # 1.3 Combine starship data dicts
    # Note: local vals replace swapi vals on matching keys

    # swapi_m_falcon. ????? # FIX ME in-place (no assignment)

    # print(f"\nCombined = {swapi_m_falcon}\n")


    # 2.0 WORK WITH CLASS INSTANCES

    # 2.1 Create Starship instance
    m_falcon = None

    # 2.2 Bulk assign dictionary values to instance variables
    # assign_values() acts as a filter
    # Downside: overwrites init values

    # UNCOMMENT
    # m_falcon.assign_values(swapi_m_falcon)

    # print(f"\nm_falcon.armament = {m_falcon.armament}\n")

    # 3.0 ASSIGN CREW TO STARSHIP
    url = f"{ENDPOINT}/people"

    # 3.1 Get SWAPI Han Solo (Corellian smuggler, pilot)
    params = {'search': 'solo'}
    swapi_solo = None

    # print(f"\nswapi_solo = {swapi_solo}\n")

    # Add instance variable values the conventional way)
    solo = None

    # UNCOMMENT AND FIX
    # solo.gender = None
    # solo.birth_year = None
    # solo.get_homeworld(None) # fetch homeworld dict


    # 3.2 Get SWAPI Chewbacca (Wookiee, co-pilot)
    params = {'search': 'chewbacca'}
    swapi_chewie = None

    # print(f"\nswapi_chewie = {swapi_chewie}\n")

    chewie = None

    # UNCOMMENT AND FIX
    # chewie.assign_values(None) # bulk assign
    # chewie.get_homeworld(None) # fetch homeworld dicts

    # 3.3 Assign crew
    crew = {}
    m_falcon.assign_crew(crew)


    # 4.0 WRITE TO FILE
    filepath = 'si506_m_falcon.json'

    # UNCOMMENT
    # write_json(filepath, m_falcon) # raises TypeError exception

    # Serialize composite class instances (a complex object)
    # Implement CustomEncoder(); reference in json.dump()
    # write_custom_json(filepath, m_falcon)


if __name__ == '__main__':
    main()
