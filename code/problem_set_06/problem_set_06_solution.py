# PROBLEM SET 6

# Importing some required libraries:
import csv # You'll use this one!
import operator # Don't worry about this one.

# PROBLEM STATEMENT
#
# You have been asked to determine which US state has the largest area of national parks, given
# a CSV file ("parks.csv") that contains information on all of the national parks in the US.
# Build a python script that will create an output file ("parkarea.csv") that contains rows
# in the following format:
#
#     <state two-letter identifier>,<area of national parks in km^2 contained in that state>
#
# As an example, the output file should contain the following rows:
"""
MI,2287.16
TN,2085.96
CO,1575.536
"""
# To accomplish this task, build out the following stubbed functions. We have provided one
# function for you <sort_dictionary_by_value>. PLEASE DON'T CHANGE ANY CODE IN THIS FUNCTION,
# however, please read the docstring to understand how it works and what it is doing!


def sort_dictionary_by_value(dictionary):
    """
    DON'T CHANGE THIS FUNCTION. This function sorts a dictionary by its values in a
    descending fashion.

    Parameters:
        dictionary (dict): A dictionary to be sorted.

    Returns:
        dict: The sorted dictionary.
    """

    desc_dictionary = dict(sorted(dictionary.items(), key=operator.itemgetter(1), reverse=True))

    return desc_dictionary


def read_csv_file(input_filepath):
    """
    This function reads a .csv file and parses it into a list of dictionaries,
    where each dictionary is formed from the data on one line of the .csv file.
    This function takes one argument <input_filepath>, which is the path of the file
    to be read. You will need to use the "csv" module in this function.

    The format of the returned list of dictionaries is as follows:

        [
            { <column 1 header>: <row 1 column 1 value>,
              <column 2 header>: <row 1 column 2 value>,
              <column 3 header>: <row 1 column 3 value>,
              ...etc
            },

            { <column 1 header>: <row 2 column 1 value>,
              <column 2 header>: <row 2 column 2 value>,
              <column 3 header>: <row 2 column 3 value>,
              ...etc
            },

            ...etc
        ]

    As an example, if the input file is structured as the following:

    Name,Age,Animal Type
    Lex,5,Dog
    Luke,7,Cat

    Then the returned list would be:

    [
        {
            "Name": "Lex",
            "Age": "5",
            "Animal Type": "Dog"
        },
        {
            "Name": "Luke",
            "Age": "7",
            "Animal Type": "Cat"
        }
    ]

    As a final example, if your input file was structured like so:

    Park Code,Park Name,State,Acres,Latitude,Longitude
    ACAD,Acadia National Park,ME,47390,44.35,-68.21

    Then the returned list should be:

    [
        {
            "Park Code": "ACAD",
            "Park Name": "Acadia National Park",
            "State": "ME",
            "Acres": "47390",
            "Latitude": "44.35",
            "Longitude": "-68.21"
        }
    ]


    HINT: This is the most challenging part of this problem. You may want to consider
    using nested loops with enumerate statements. Don't worry about converting any
    strings to other types here; you can handle that later.

    Parameters:
        input_filepath (str): The location of the file to read and parse.

    Returns:
        list: A list of dictionaries, where each dictionary is one row from the
            input file.
    """

    out_list = []

    with open(input_filepath, 'r') as f:
        reader = csv.reader(f)
        for i,row in enumerate(reader):
            if i == 0:
                labels = row
            else:
                park_dict = {}
                for j,value in enumerate(row):
                    park_dict[labels[j]] = value
                out_list.append(park_dict)

    return out_list


def write_csv_file(output_filepath, dict_to_write, header):
    """
    Writes a .csv file using the "csv" module. The file will contain the information
    from <dict_to_write>, where each row of the new .csv file is one of the key/value
    pairs. In other words, the output file should have two columns. Don't forget to
    include the header to each column, which is given to this function in the parameter
    <header>. The resultant file should be structured in the following way:

        <header[0]>,<header[1]>
        key1,value1
        key2,value2
        key3,value3
        ...etc

    Parameters:
        output_filepath (str): The file path to the new file being created.
        dict_to_write (dict): The information to include in the file being created.
        header (list): A list of two elements that correspond to the headers of the
            two columns in the new file.

    Returns:
        None
    """

    with open(output_filepath,'w') as f:
        writer = csv.writer(f)
        writer.writerow(header)
        for k,v in dict_to_write.items():
            writer.writerow([k,v])


def acres_to_km2(acres):
    """
    Converts a value in acres to a value in kilometers squared. The conversion
    is as follows:

        1 acre is approximately 0.004 km^2

    Parameters:
        acres (float): A number in acres

    Returns:
        float: A number in km^2
    """

    return acres * 0.004


def km2_by_state(list_of_park_dicts):
    """
    This function takes a list of national park data (e.g. the returned value from
    <read_csv_file>), and returns a new dictionary that contains the summed
    area (in kilometers squared) of national parks in each state. The output
    dictionary should have the format:

    {<state two-letter identifier>: <float of total area of parks in that state in km^2>}

    Parameters:
        list_of_park_dicts (list): A list of dictionaries, where each dictionary contains the
            information on a specific park.

    Returns:
        dict: A dictionary where the keys are the two-letter state identifiers and the values
            are the sum total area of national parks in that state (in km^2).

    NOTE: Don't worry about states that don't have any national parks in the dataset we
    have provided. Your returned dictionary should only include the states that are present
    in the data.

    HINT: You'll need to use an accumulator pattern here to build a new dictionary. You
    will also need to call <acres_to_km2> to convert the park areas into km^2.
    """

    park_area_by_state = {}

    for park in list_of_park_dicts:

        state = park["State"]
        area_in_acres = float(park['Acres'])
        area_in_km2 = acres_to_km2(area_in_acres)

        if state not in park_area_by_state:
            park_area_by_state[state] = area_in_km2
        else:
            park_area_by_state[state] += area_in_km2

    return park_area_by_state


def main():
    """
    Read in the data from "parks.csv". Then, parse that data and determine
    how much national park area is in each state using your <km2_by_state> function.
    Then, sort the resultant dictionary. Finally, write the sorted dictionary to a
    new file "parkarea.csv". Don't forget to include headers into the "parkarea.csv"
    file!

    Parameters:
        None

    Returns:
        None

    HINT: You will need to call each of the functions in this script to complete this
    task.
    """

    data = read_csv_file('parks.csv')
    park_area = km2_by_state(data)
    park_area = sort_dictionary_by_value(park_area)
    write_csv_file("parkarea.csv", park_area, ['State','Area'])


# END CODING HERE - - - - - - - - - - - - - - - - - - - - - - - - - - - -

if __name__ == '__main__':
    main()
