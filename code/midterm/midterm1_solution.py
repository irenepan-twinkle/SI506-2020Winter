# MIDTERM CODING ASSESSMENT OPTION 1

# DATA:
#
# In this exercise, you will make use of the <medal_counts> list, which
# contains data on the number of medals won by some of the winningest nations
# during the 2018 Winter Olympics. Each element of the <medal_counts> list is
# a string of the following format:
#
#     <country name>,<total number of medals won>
#
# As an example, "Italy,10" would mean that Italy won 10 medals.
#
# YOUR TASK:
#
# You will construct a function <filter_medal_counts> as described by the
# docstring provided. Then, make a call to your <filter_medal_counts> function
# with the following arguments in the <main> function:
#
#     medal_list = medal_counts
#     minimum_medal_count = 20
#
# The returned value of your <filter_medal_counts> call (and thus the returned value of
# <main>) should include the following key/value pairs:
#
#   'Netherlands': 20
#   'Germany': 31
#   'United States': 23
#   'Canada': 29
#   'Norway': 39
#
# You may then upload this file to Gradescope as many times as you want in the
# available test time. However, be aware that Gradescope will be testing your code
# with hidden data in order to make sure your function will work in the same way with
# other datasets, so just because you produce the expected output for the data
# given here, doesn't mean that you have the answer entirely correct. Make sure your
# function is generalizable!


medal_counts = [
    "France,15",
    "Netherlands,20",
    "Germany,31",
    "United States,23",
    "Switzerland,15",
    "Canada,29",
    "Sweden,14",
    "Norway,39",
    "Austria,14",
    "South Korea,17",
]

# BEGIN CODING HERE

def filter_medal_counts(medal_list, minimum_medal_count):
    """
    This function will filter a <medal_list> of countries and their medal counts
    (e.g. <medal_counts>) by the number of medals that country won.
    If the total number of medals won by that country is greater than or
    equal to <minimum_medal_count>, then it will be included in the returned
    dictionary.

    Parameters:
        medal_list (list): A list of strings, where each string is of the
            form "<country>,<total number of medals>"
        minimum_medal_count (int): The minimum number medals that a country
            must have won in order to be included in the returned dictionary.

    Returns:
        dict: A dictionary where each key is a country name and each value is
            the integer number of medals won by the country. MAKE SURE that
            the values are integers by converting them using the int() function.
            As an example, if South Korea was included in this dictionary, its
            entry would be: {"South Korea" : 17}

    HINT: You will need to use the int() function to convert string representations
    of numbers into integers in order to compare two numbers. Also remember that the
    values of the returned dictionary should be integers as well.
    """

    filtered_countries = {}

    for country in medal_list:

        country_data = country.split(",")
        name = country_data[0]
        total_medal_count = int(country_data[1])

        if total_medal_count >= minimum_medal_count:
            filtered_countries[name] = total_medal_count

    return filtered_countries


def main():
    """
    Call <filter_medal_counts> with the arguments listed under "Your Task" above
    and save the returned value to a variable called <result>. Then, return <result>.

    Note: Feel free to introduce print statements into this function to test that
    <result> is correct. <result> should contain the following key/value pairs:

        'Netherlands': 20
        'Germany': 31
        'United States': 23
        'Canada': 29
        'Norway': 39

    Parameters:
        None

    Returns:
        dict: A returned dictionary from a call to <filter_medal_counts> with the
            arguments as described in "Your Task" above.
    """

    result = filter_medal_counts(medal_counts,20)

    print(f"\nThe result of your code:\n{result}\n")

    return result

# END CODING HERE --- DO NOT CHANGE CODE BELOW THIS LINE!
# The folowing couple lines of code will call <main> for you! So don't
# worry about making a call to <main>

if __name__ == "__main__":
    main()
