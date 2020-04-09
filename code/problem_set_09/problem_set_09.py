import requests, json

# PROBLEM SET 09

ENDPOINT = 'https://swapi.py4e.com/api'

# INCOMING SECURE TRANSMISSION - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
"""
In this problem set, you have been levereged by the First Order to help them identify
where key Resistance members, Rey and Chewbacca, have been operating. Unfortunately,
the First Order informant network consists of all kinds of unscrupulous persons, often who
will simply report anything to get paid. Therefore, there are many records of different
people named Rey and Chewbacca in the informant reports <informants.json>. You will need
to cross-reference the informant reports with the data that already exists in the First
Order databases (i.e. SWAPI). In practice, this means that if the informant report
contains the same name, hair color, eye color, and species as the SWAPI record, you will
flag that report and update the location of that Resistance member.

The informant.json file contains records of name, hair_color, eye_color, species_name, and
location. We strongly recommend you open the file and look at it before continuing this
assignment. Look for the "TO DO" comments in this assignment to see where you need to
add code. Don't forget to fill in the proper parameters to each function and method.
Feel free to remove the placeholder <pass> statements as you write actual code.
"""
# END TRANSMISSION - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

# BEGIN ASSIGNMENT:

# TO DO: Finish get_swapi_resource.
def get_swapi_resource():
    """This function initiates an HTTP GET request to the SWAPI service in order to return a
    representation of a resource. The function defines two parameters, the resource url (str) and
    an optional params (dict) query string of key:value pairs may be provided as search terms
    (e.g., {'search': 'yoda'}). If a match is obtained from a search, be aware that the JSON object
    that is returned will include a list property named 'results' that contains the resource(s)
    matched by the search query term(s).

    HINT: You will need to use a conditional <if> statement to determine whether or not to
    include the parameters in the requests.get() function call.

    Parameters:
        resource (str): a url that specifies the resource.
        params (dict): optional dictionary of querystring arguments. This parameter should
            have a default value of None.

    Returns:
        dict: dictionary representation of the decoded JSON.
    """

    pass


# TO DO: Finish read_json
def read_json():
    """This function reads a JSON document and returns a dictionary if provided with a valid
    filepath.

    Parameters:
        filepath (str): path to file.

    Returns:
        dict: dictionary representations of the decoded JSON document.
    """

    pass


# TO DO: Finish write_json
def write_json():
    """Given a valid filepath writes data to a JSON file.

    Parameters:
        filepath (str): the path to the file.
        data (dict): the data to be encoded as JSON and written to the file.

    Returns:
        None
    """

    pass


# TO DO: Create the __init__, __str__, and evaluate_information methods to Person
class Person():
    """
    This class contains all of the information that the First Order has on a person.
    You will need to create a constructor that takes the following arguments:

        <self>
        <name>
        <hair_color>
        <eye_color>
        <species_name>

    and convert them all into instance variables. In addition, the constructor should
    create an instance variable <self.location> and set its value to "unknown" for now.
    We'll change that later in the <evaluate_information> method.

    Additionally, build a <__str__> method that returns the following string (with the
    proper instance variables in place of these placeholders):

    "<name> is a <species_name> with <hair_color> hair and <eye_color> eyes. Location: <location>"

    Instance Variables:
        name (str): Name of the person.
        hair_color (str): Hair color of the person.
        eye_color (str): Eye color of the person.
        species_name (str): Name of the species of the person.
        location (str): Current planet the person is known to be operating on.
            The location starts out as 'unknown' until we can cross-reference our
            central databases with the information from our informants. THAT'S YOUR
            JOB!
    """

    def __init__():

        pass


    def __str__(self):

        pass


    def evaluate_information():
        """
        This method will take a dictionary <information_dict> that has the following keys:

            hair_color, eye_color, species_name, location, name

        and it will check if the values to those keys are the exact same as the
        respective instance variable (e.g. <name> should be the same as <self.name>). If
        all keys are the same, then update <self.location> to be the value of the
        <information_dict> <location> key.

        Parameters:
            information_dict (dict): A dictionary of information to compare with the instance
                variables.

        Returns:
            None, but has the potential to update self.location
        """

        pass


# TO DO: Build the main() function following the cues
def main():
    """
    This function will use various utility functions, classes, and methods to determine
    the location of two Resistance members: Rey and Chewbacca. Nothing is returned from
    this function, however a file <updated_information.json> is produced.

    Parameters:
        None

    Returns:
        None
    """

    # First, call <get_swapi_resource> with the correct parameters (you'll likely want
    # to pass a parameters dictionary like so: {'search':'rey'}) to retrieve a
    # dictionary of data about Rey. Save it to <rey_data>. Make sure <rey_data> is a
    # dictionary, and not a list!
    pass

    # Now, get Rey's species name by making a request to the url that is contained in the string
    # stored in <rey_data['species'][0]>. Save the name of that species to <rey_species>.
    # <rey_species> should be a string. Then, add a new key/value pair to <rey_data>
    # which has a key of "species_name" and a value of <rey_species>.
    pass

    # Do the same thing for Chewbacca, saving the information to <chewbacca_data> and
    # <chewbacca_species>.
    pass

    # Create instances of <Person> for both Rey and Chewbacca using the data you have stored
    # in the dictionaries <rey_data>, <chewbacca_data> and strings <rey_species>, <chewbacca_species>
    pass

    # Read in the data from the informants using the <read_json> function.
    # Make a new list <rey_info> that only contains the information on rey.
    # Make a new list <chewbacca_info> that only contains the information on chewbacca.
    # If you are confused, look at the keys of the dictionary that resulted from your
    # call to <read_json>.
    pass

    # For each dictionary in <rey_info>, utilize the method <evaluate_information> from the
    # instance of <person> for Rey. Only one entry of <rey_info> should flag as True and update
    # Rey's location. Then, do the same for Chewbacca.
    pass

    # Create a new dictionary with only two key value pairs:
    #
    # {
    #   'Rey': <str representation of Rey's instance of Person>
    #   'Chewbacca': <str representation of Chewbacca's instance of Person>
    # }
    pass

    # Write out your new dictionary to <updated_information.json> using <write_json>
    pass

# END ASSIGNMENT

if __name__ == '__main__':
    main()
