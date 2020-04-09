import requests, json

# PROBLEM SET 10
# BEGIN ASSIGNMENT:

# TO DO: Implement the __init__ method to Entity
# Entity is the parent class
class Entity():
    """
    Base representation of a resource.

    Attributes:
        url: resource identifier

    """
    def __init__(self):
        pass


# TO DO: Implement the __init__, jsonable methods to Film
# Film is the child class of Entity
class Film():
    PROPERTIES = ("title", "episode_id", "url")
    def __init__(self, property_dict):
        # Here we use a property_dict to wrap all the PROPERTIES of the object
        # Use property in PROPERTIES as key to access the value in property_dict and assign it to the instance attribute
        # For example, "url" is in PROPERTIES and you should use super().__init__ in this way:
        super().__init__(property_dict["url"])
        # For example, since "title" is in PROPERTIES, you should assign the instance variale in this way:
        self.title = property_dict["title"]

        # Assign value to the rest properties
        
        pass

    def jsonable(self):
        """
        Return a JSON-friendly representation of the object.
        Use a dictionary literal - {} rather than built-in dict() to avoid
        built-in lookup costs.

        The key should be the name of instance variable and value should be the corresponding value.
        For example, self.title should be converted in this way:
        {"title": self.title}

        Parameters:
            None
        Returns:
            dict: dictionary of the object's instance variables
        """
        
        pass

# TO DO: Implement the __init__, jsonable methods to Person
# Planet is the child class of Entity
class Planet(Entity):
    PROPERTIES = ("name", "climate", "terrain", "url")
    def __init__(self, property_dict):
        # Similar to Film.__init__()
        
        pass
    
    def jsonable(self):
        """
        Return a JSON-friendly representation of the object.
        Use a dictionary literal - {} rather than built-in dict() to avoid
        built-in lookup costs.

        The key should be the name of instance variable and value should be the corresponding value.
        For example, self.name should be converted in this way:
        {"name": self.name}

        Parameters:
            None
        Returns:
            dict: dictionary of the object's instance variables
        """
        
        pass

# TO DO: Implement the __init__, update_homeworld, update_films, jsonable methods to Person
# Please understand <convert_resource_to_obj> first. You need to utilize it 
# in update_homeworld, update_films, jsonable methods
# Person is the child class of Entity
class Person():
    PROPERTIES = ("name", "height", "mass", "homeworld", "films", "url")
    def __init__(self, property_dict):
        # Similar to Film.__init__()
        
        pass
    
    def update_homeworld(self):
        """
        self.homeworld is a url so far
        Replace it with corresponding Planet object
        
        HINT: You should call the functions <get_swapi_resource>,<convert_resource_to_obj> 
        to generate the object

        Parameters:
            None
        Returns:
            None, but self.homeworld has been updated
        """
        pass

    def update_films(self):
        """
        self.films is a list of urls so far
        Replace it with a list of corresponding Film objects
        You should use list comprehension to generate the list of objects
        
        HINT: You should call the functions <get_swapi_resource>,<convert_resource_to_obj> 
        to generate the object

        Parameters:
            None
        Returns:
            None, but self.films has been updated
        """
        pass

    def jsonable(self):
        """
        Return a JSON-friendly representation of the object.
        Use a dictionary literal - {} rather than built-in dict() to avoid
        built-in lookup costs.
        The key should be the name of instance variable and value should be the corresponding value.
        For example, self.url should be converted in this way:
        {"url": self.url}

        Notice that now self.homeworld is a Planet object and self.films is a list of Film objects.
        You need to convert Planet / Film objects using their .jsonable() methods to corresponding JSON-friendly representations.
        You should use list comprehension to generate the list of JSON-friendly representations for self.films

        Parameters:
            None
        Returns:
            dict: dictionary of the object's instance variables
        """
        pass

# TO DO: Finish get_swapi_resource.
# Below is an updated version of the function <get_swapi_resource> you have implemented in PS9
def get_swapi_resource():
    """
    This function initiates an HTTP GET request to the SWAPI service in order to return a
    representation of a resource.

    If <params> is None, you don't need to include <params> when you make the GET request.

    Once you get the response from the request, check its status code
    If status code is equal to 200, which means the GET request succeeded, convert the response to python dict
    Else print "<status code> something wrong happened" and return None

    Parameters:
        resource (str): a url that specifies the resource.
        params (dict): optional dictionary of querystring arguments. The default value is None.
        timeout (int): timeout value in seconds. The default value is 5

    Returns:
        dict: dictionary representation of the decoded JSON.
    """

    pass

# TO DO: Finish convert_resource_to_obj().
# You may notice that in the JSON returned by SWAPI, some information are represented by other urls
# For example, in Luke.json, the value of "films" is a list of urls, where each url represents a film
# that Luke Skywalker was in.
# <convert_resource_to_obj> would convert JSONs represented by those urls to meaningful objects.
def convert_resource_to_obj():
    """
    <resource_dict> should be a dictionary returned by <get_swapi_resource> or <read_json>.
    Use dictionary comprehension to generate property dict
        Loop over the key-value pair in resource dict
            If the key is in obj_class.PROPERTIES, add the key-value pair into the property dict
    Use property dict to initiate an instance of the <obj_class>

    Parameters:
        resource (str): a url that specifies the resource.
        obj_class (cls): a class that initiates the instance

    Returns:
        instance (obj): an instance generated by <obj_class>.
    """

    pass

# We have provided write_json for you
def write_json(filepath, data):
    with open(filepath, 'w', encoding='utf-8') as file_obj:
        json.dump(data, file_obj, ensure_ascii=False, indent=2)

# We have provided read_json for you
def read_json(filepath):
    with open(filepath, 'r', encoding='utf-8') as file_obj:
        data = json.load(file_obj)

    return data

def main():
    # Pass three tests below first before you start working on <main>

    # BEGIN TEST FOR <get_swapi_resource> (Uncomment me when you're ready!)
    # get_swapi_resource('http://google.com/max') # should print 404 something wrong happened
    # END TEST FOR <get_swapi_resource>

    # BEGIN TEST FOR <Entity> (Uncomment me when you're ready!)
    # entity = Entity("https://swapi.co/api/people")
    # print(entity.url == "https://swapi.co/api/people")# should print True
    # END TEST FOR <Entity>

    # BEGIN TEST FOR <Film> (Uncomment me when you're ready!)
    # film_property_dict = {"title": "max", "episode_id": 1, "url": "www.max.com"}
    # film = Film(film_property_dict)
    # print(film.url == "www.max.com") # should print True
    # print(film.jsonable() == film_property_dict) # should print True
    # END TEST FOR <Film>

    # Now you can work on main :)
    # We have provided other tests for you
    # Call the function <read_json> to read <Luke.json> get the resource dict
    # Call the function <convert_resource_to_obj> to create a Person instance <luke>


    # BEGIN TEST FOR <convert_resource_to_obj> (Uncomment me when you're ready!)
    # print(isinstance(luke, Person)) # should print True
    # print(luke.name == "Luke Skywalker") # should print True
    # print(luke.url == "https://swapi.py4e.com/api/people/1/") # should print True
    # END TEST FOR <convert_resource_to_obj>

    # So far luke.homeworld is still a url. Let's replace it with a Planet object


    # BEGIN TEST FOR <update_homeworld> (Uncomment me when you're ready!)
    # print(isinstance(luke.homeworld, Planet)) # should print True
    # END TEST FOR <update_homeworld>

    # So far luke.films is still a list of urls. Let's replace it with a list of Film objects


    # BEGIN TEST FOR <update_films> (Uncomment me when you're ready!)
    print(isinstance(luke.films[0], Film)) # should print True
    # END TEST FOR <update_films>

    # BEGIN TEST FOR <jsonable> (Uncomment me when you're ready!)
    # print(luke.jsonable()["homeworld"]["name"] == "Tatooine") # should print True
    # print(luke.jsonable()["films"][0]["title"] == "A New Hope") # should print True
    # END TEST FOR <jsonable>

    # Now write luke.jsonable() into the file <luke_updated.json>





# END ASSIGNMENT

if __name__ == '__main__':
    main()