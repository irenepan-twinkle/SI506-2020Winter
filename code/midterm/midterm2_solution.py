# MIDTERM CODING ASSESSMENT OPTION 2

# DATA:
#
# In this exercise, you will make use of the <planets> dictionary, which
# contains data about each planet: its categorization as an "inner" planet or
# "outer" planet and the number of known natural satellites (moons). The dictionary
# <planets ist structured in the following format:
#
#     {<planet name> : [<category>, <number of natural satellites>]}
#
# As an example, {"Earth" : ['inner', 1]} means that Earth is an inner planet with
# one natural satellite. Note that the values of <planets> are lists.
#
# YOUR TASK:
#
# You will construct a function <satellite_count> that will count the total number of
# natural satellites of planets in one cateogry or another. To do so, follow the
# specifications outlined in the given docstring. Then, you will call your
# <satellite_count> function with the following arguments in the <main> function:
#
#     planet_dict = planets
#     planet_type = 'outer'
#
# The returned value from your call to <satellite_count> (and thus the returned value
# of <main>) should return an integer value of
#
#   202
#
# You may then upload this file to Gradescope as many times as you want in the
# available test time. However, be aware that Gradescope will be testing your code
# with hidden data in order to make sure your function will work in the same way with
# other datasets, so just because you produce the expected output for the data
# given here, doesn't mean that you have the answer entirely correct. Make sure your
# function is generalizable!

planets = {
    "Mercury" : ['inner', 0],
    "Venus" : ['inner', 0],
    "Earth" : ['inner', 1],
    "Mars" : ['inner', 2],
    "Jupiter" : ['outer', 79],
    "Saturn" : ['outer', 82],
    "Uranus" : ['outer', 27],
    "Neptune" : ['outer', 14]
}

# BEGIN CODING HERE

def satellite_count(planet_dict, planet_type):
    """
    This function will take a dictionary <planet_dict> and a <planet_type> designation
    as parameters and return the total number of natural satellites of all the planets
    with the <planet_type> designation.

    Parameters:
        planet_dict (dict): A dictionary, where each element has a planet name as the key
            and a list as the value. The value list has two elements: the first element
            is a string of the planet's category (either "inner" or "outer") and the second
            element is an integer representing the number of natural satellites of that
            planet.
        planet_type (str): A string describing the category of planet to be included in the
            sum of natural satellites (which is the returned value of this function).

    Returns:
        (int): The total number of natural satellites of the planets with <planet_type>
            designation.
    """

    total_moons = 0

    for key,val in planet_dict.items():
        type = val[0]
        moons = val[1]
        if type == planet_type:
            total_moons += moons

    return total_moons


def main():
    """
    Call <satellite_count> with the arguments listed under "Your Task" above
    and save the returned value to a variable called <result>. Then, return <result>.

    Note: Feel free to introduce print statements into this function to test that
    <result> is correct. <result> should be the following integer:

        202

    Parameters:
        None

    Returns:
        int: A returned integer from a call to <satellite_count> with the
            arguments as described in "Your Task" above.
    """

    result = satellite_count(planets,'outer')

    print(f"\nThe result of your code:\n{result}\n")

    return result

# END CODING HERE --- DO NOT CHANGE CODE BELOW THIS LINE!
# The folowing couple lines of code will call <main> for you! So don't
# worry about making a call to <main>

if __name__ == '__main__':

    main()
