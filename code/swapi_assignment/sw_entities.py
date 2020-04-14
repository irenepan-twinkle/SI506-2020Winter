class Entity:
    """Minimal representation of a thing or entity.

    Attributes:
        url: resource identifier
        name: common name

    Methods:
        jsonable: return JSON-friendly dict representation of the object
    """

    def __init__(self, url, name):

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
            dict: dictionary of the object's instance variable values
        """

        # return self.__dict__ # DANGEROUS
        # return copy.deepcopy(self.__dict__) # safe but slow

        pass

    def __str__(self):
        """Human-readable string representation of the object."""

        return f"{self.name} ({self.url})"


class EvacuationPlan(Entity):
    """Rebel Alliance evacuation plan. Classified as Top Secret. In the event
    that Imperial forces discover a Rebel Alliance base, provides for removal of
    garrison in a single lift if sufficient transport assets are available.
    If necessary, cargo space will be converted to passenger space. Document
    also lists crew assignments for both transports and escorts as well as
    passenger assignments.

    Attributes:
        url (str): resource identifier
        name (str): common name
        classification (str): document classification (e.g., Top Secret)
        year_era (str): year suffixed by galatic era (e.g., 3 ABY)
        description (str): short description
        garrison_personnel_count (int): garrison size
        num_available_transports (int): number of available transports
        passenger_overload_multiplier (int): transport passenger overload
            multiplier
        max_passenger_overload_capacity (int): maximum number of passengers
            available transports can carry if cargo space is converted to
            passengar space (transports * seating * overload multiplier)
        transport_assignments (list): transports assigned to operation
        transport_escorts (list): starship escorts assigned to guard
            transports after departure.

    Methods:
        jsonable: return JSON-friendly dict representation of the object
    """

    def __init__(self, url, name):

        pass

    def jsonable(self):
        """Return a JSON-friendly representation of the object.
        Use a dictionary literal rather than built-in dict() to avoid
        built-in lookup costs.

        Parameters:
            None

        Returns:
            dict: dictionary of the object's instance variable values
        """

        pass

    def __str__(self):
        """Human-readable string representation of the object."""

        return f"{self.name} ({self.url})"


class Garrison(Entity):
    """Military garrison assigned to a military base.

    Attributes:
        url (str): resource identifier
        name (str): common name
        commander (Person): base commander
        personnel (dict): personnel count inclusive of military forces,
            medical staff, and droids.

    Methods:
        jsonable: return JSON-friendly dict representation of the object
    """

    def __init__(self, url, name):
        super().__init__(url, name)
        self.commander = None
        self.personnel = {}

    def jsonable(self):
        """Return a JSON-friendly representation of the object.
        Use a dictionary literal rather than built-in dict() to avoid
        built-in lookup costs.

        Parameters:
            None

        Returns:
            dict: dictionary of the object's instance variable values
        """

        return {
            'url': self.url,
            'name': self.name,
            'commander': self.commander,
            'personnel': self.personnel
            }

    def __str__(self):
        """Human-readable string representation of the object."""

        return f"{self.name} ({self.url})"


class MilitaryBase(Entity):
    """A military base.

    Attributes:
        url (str): resource identifier
        name (str): common name
        operational_status (str): under construction, active, abandoned, destroyed
        location (Planet): planet on which location is based
        facilities (list): base facilities
        garrison (Garrison): assigned military forces, medical personnel, and droids
        fixed_defenses (list): summary of defensive assets and fixed fortifications
        air_space_assets (list): air and space craft assigned to base
        evacuation_plan (EvacuationPlan): emergency withdrawal plan

    Methods:
        jsonable: return JSON-friendly dict representation of the object
    """

    def __init__(self, url, name):

        pass

    def jsonable(self):
        """Return a JSON-friendly representation of the object.
        Use a dictionary literal rather than built-in dict() to avoid
        built-in lookup costs.

        Parameters:
            None

        Returns:
            dict: dictionary of the object's instance variable values
        """

        pass

    def __str__(self):
        """Human-readable string representation of the object."""

        return f"{self.name} ({self.url})"


class Person(Entity):
    """A sentient being designated as a person.

    Attributes:
        url (str): resource identifier
        name (str): common name
        birth_year (str): year of birth suffixed with the galatic era
            BBY or ABY (before Battle of Yavin / after Battle of Yavin)
        height (float): height in centimeters
        mass (float): weight in kilograms
        homeworld (Planet): home planet
        species (Species): the species to which the person is assigned

    Methods:
        get_homeworld: retrieve home planet
        get_species: retrieve species
        jsonable: return JSON-friendly dict representation of the object
    """

    def __init__(self, url, name):

        pass

    def jsonable(self):
        """Return a JSON-friendly representation of the object.
        Use a dictionary literal rather than built-in dict() to avoid
        built-in lookup costs.

        Parameters:
            None

        Returns:
            dict: dictionary of the object's instance variable values
        """

        pass

    def __str__(self):
        """Human-readable string representation of the object."""

        return f"{self.name} ({self.url})"


class Planet(Entity):
    """A planet.

    Attributes:
        url (str): resource identifier
        name (str): common name
        gravity (str): number denoting the gravity of this planet. The value
            '1' is normal or 1 standard G, '2' is twice or 2 standard Gs,
            '0.5' is half or 0.5 standard Gs
        climate (list): climate description
        terrain (list): terrain description
        surface_water (int): percentage of the planet surface covered by bodies
            of water
        population (int): population estimate of sentient beings inhabiting planet

    Methods:
        jsonable: return JSON-friendly dict representation of the object
    """

    def __init__(self, url, name):

        pass

    def jsonable(self):
        """Return a JSON-friendly representation of the object.
        Use a dictionary literal rather than built-in dict() to avoid
        built-in lookup costs.

        Parameters:
            None

        Returns:
            dict: dictionary of the object's instance variable values
        """

        pass

    def __str__(self):
        """Human-readable string representation of the object."""

        return f"{self.name} ({self.url})"


class Species(Entity):
    """A unit of biodiversity.

    Attributes:
        url (str): resource identifier
        name (str): common name
        classification (str): classifier, e.g., 'mammal', 'reptile'
        designation (str): designation, e.g., 'sentient'
        language (str): language commonly spoken by species

    Methods:
        jsonable: return JSON-friendly dict representation of the object.
    """

    def __init__(self, url, name):

        pass

    def jsonable(self):
        """Return a JSON-friendly representation of the object.
        Use a dictionary literal rather than built-in dict() to avoid
        built-in lookup costs.

        Parameters:
            None

        Returns:
            dict: dictionary of the object's instance variable values
        """

        pass

    def __str__(self):
        """Human-readable string representation of the object."""

        return f"{self.name} ({self.url})"


class Starship(Entity):
    """A crewed transport craft used for inter-planetary travel in
    'realspace' or 'hyperspace'.

    Attributes:
        url (str): resource identifier
        name (str): common name, e.g., 'X-wing'
        model (str): official name, e.g., 'T-65 X-wing'
        starship_class (str): starship type, e.g., 'Starfighter'
        length (float): length in meters
        max_atmosphering_speed (float): maximum speed of atmospheric flight
        hyperdrive_rating (float): lightspeed propulsion system rating
        MGLT (int): megalight per hour traveled
        armament (list): weapon system(s) installed, if any
        crew (int): maximum crew size
        passengers (int): maximum number of passengers craft is rated to carry
        consumables (str): maximum length of time craft can sustain crew
            and passengers without having to resupply provisions
        cargo_capacity (int): maximum weight of cargo in kilograms craft is
            rated to carry
        crew_members (dict): assigned crew member(s)
        passenger_manifest (list): assigned passenger(s)

    Methods:
        assign_crew: assign crew member(s) to starship.
        assign_passengers: assign passenger(s) to starship.
        jsonable: return JSON-friendly dict representation of the object.
    """

    def __init__(self, url, name, model, starship_class):

        pass

    def assign_crew(self, crew):
        """Assign crew member(s) by role to a starship or a vehicle.

        Parameters:
            crew (dict): crew assignment(s) {<role>: <Person>},
                         e.g., {'Pilot': <Luke Skywalker>}

        Returns:
           None
        """

        pass

    def assign_passengers(self, manifest):
        """Add passenger(s) to the passenger manifest.

        Parameters:
            manifest (list): passenger list [<Person>]

        Returns:
            None

        """

        pass

    def jsonable(self):
        """Return a JSON-friendly representation of the object.
        Use a dictionary literal rather than built-in dict() to avoid
        built-in lookup costs.

        Parameters:
            None

        Returns:
            dict: dictionary of the object's instance variable values
        """

        pass

    def __str__(self):
        """Human-readable string representation of the object."""

        return f"{self.name} ({self.url})"
