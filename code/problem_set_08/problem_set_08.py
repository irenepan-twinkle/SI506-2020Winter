# In this homework, you'll work and code as a Software Engineer of a game company.
# You are asked to construct objects for those heroes in the game and also simulate the game

# <heroes> is a list of dictionary. Each dictionary describes the attributes of a hero at level 0 in the game

heroes = [
    {
        "name": "Axe",
        "main_attribute": "strength",
        "base_hp": 625,
        "base_mp": 234,
        "base_damage": 52,
        "strength_growth_per_level": 3.6,
        "agility_growth_per_level": 2.2,
        "intelligence_growth_per_level": 1.6
    },
    {
        "name": "Monkey King",
        "main_attribute": "agility",
        "base_hp": 511,
        "base_mp": 260,
        "base_damage": 51,
        "strength_growth_per_level": 2.8,
        "agility_growth_per_level": 3.7,
        "intelligence_growth_per_level": 1.8
    },
    {
        "name": "Invoker",
        "main_attribute": "intelligence",
        "base_hp": 492,
        "base_mp": 195,
        "base_damage": 42,
        "strength_growth_per_level": 2.4,
        "agility_growth_per_level": 1.9,
        "intelligence_growth_per_level": 4.6
    }
]

# There are 39 strength heroes, 37 agility heroes and 43 intelligence heroes in the game.
# Strength heroes, agility heroes and intelligence heroes they are different types of heroes

# THIS PART WOULD NOT BE GRADED
# How would you design the classes to describe those heroes?
# What is parent class?
# What are child classes?
# What are the differences between those child classes?
# Just think about those questions. You don't need to write down anything

# First, let's create the parent class for all heroes
class Hero():
    """
    This is a class that contains information on Hero.

    Attributes:
        name (str): The name of the hero.
        hp (float): The health points of the hero.
        mp (float): The magic points of the hero.
        level (int): The level of the hero.
        damage (float): The damage of the hero.
        strength_growth (float): The strength gain per level of the hero.
        agility_growth (float): The agility gain per level of the hero.
        intelligence_growth (float): The intelligence gain per level of the hero.
    """

    def __init__(self):
        """
        TO DO:
        The constructor of the <Hero> class. Here you will need to create
        the attributes ("instance variables") that were described in the <Hero>
        docstring. Note that some of the attributes are defined by parameters passed
        to this constructor method, but others are not. In this case, the <level> should be 0.

        Parameters:
            name (str): The name of the hero.
            hp (float): The health points of the hero.
            mp (float): The magic points of the hero.
            damage (float): The damage of the hero.
            strength_growth (float): The strength gain per level of the hero.
            agility_growth (float): The agility gain per level of the hero.
            intelligence_growth (float): The intelligence gain per level of the hero.

        Returns:
            None
        """
    
    def __str__(self):
        """
        TO DO:
        This is the string method for the <Hero> class, describing the infomation of the hero in the format
        "<name>, level <level>, hp <hp>, mp <mp>, damage <damage>". 

        Parameters:
            None

        Returns:
            str: A string that describes this instance of <Hero>

        """

    
    def attack(self):
        """
        TO DO:
        This method allows current hero to attack the other hero.
        Attack means that other hero's hp would be reduced by current hero's damage

        Parameters:
            other (obj): other is an instance of hero 

        Returns:
            None
        """

    def is_dead(self):
        """
        TO DO:
        This method examines whether the hero is dead or not.
        Dead means <hp> is equal or less than 0.

        Parameters:
            None

        Returns:
            dead (bool): True if the hero is dead. False if the hero is alive
        """

    

# Second, let's create the child classes for different types of heroes
class StrengthHero(Hero):
    def __init__(self):
        """
        TO DO:
        The constructor of the <StrengthHero> class.
        Use super() to initialize the attributes of the parent class.
        Add a new attribute <main_attribute>.
        The <main_attribute> of strength hero should be "strength"

        Parameters:
            name (str): The name of the hero.
            hp (float): The health points of the hero.
            mp (float): The magic points of the hero.
            damage (float): The damage of the hero.
            strength_growth (float): The strength gain per level of the hero.
            agility_growth (float): The agility gain per level of the hero.
            intelligence_growth (float): The intelligence gain per level of the hero.

        Returns:
            None
        """

    
    def level_up(self):
        """
        TO DO:
        This method would level a hero up
        1. increase <level> by 1
        2. increase <hp> by 20 * <strength_growth>
        3. increase <mp> by 5 * <intelligence_growth>
        4. increase <damage> by 1 * main_attribute growth


        Parameters:
            None

        Returns:
            None
        """
    
    def ability(self):
        """
        TO DO:
        This method would double hero's hp at the cost of 200 mp
        If the hero's mp is less than 200, this method should print "<name> doesn't have enough mp"
        If the hero's mp is equal or greater tan 200, this method would double its hp, reduce its mp by 200
        and print "<name> now has <hp> hp"

        Parameters:
            None

        Returns:
            None
        """

class AgilityHero(Hero):
    def __init__(self):
        """
        TO DO:
        The constructor of the <StrengthHero> class.
        Use super() to initialize the attributes of the parent class.
        Add a new attribute <main_attribute>.
        The <main_attribute> of agility hero should be "agility"

        Parameters:
            name (str): The name of the hero.
            hp (float): The health points of the hero.
            mp (float): The magic points of the hero.
            damage (float): The damage of the hero.
            strength_growth (float): The strength gain per level of the hero.
            agility_growth (float): The agility gain per level of the hero.
            intelligence_growth (float): The intelligence gain per level of the hero.

        Returns:
            None
        """
    
    def level_up(self):
        """
        TO DO:
        This method would level a hero up
        1. increase <level> by 1
        2. increase <hp> by 10 * <strength_growth>
        3. increase <mp> by 10 * <intelligence_growth>
        4. increase <damage> by 1 * main_attribute growth


        Parameters:
            None

        Returns:
            None
        """
    
    def ability(self):
        """
        TO DO:
        This method would double hero's damage at the cost of 300 mp
        If the hero's mp is less than 300, this method should print "<name> doesn't have enough mp"
        If the hero's mp is equal or greater tan 300, this method would double its damage, reduce its mp by 300
        and print "<name> now has <damage> damage"

        Parameters:
            None

        Returns:
            None
        """

class IntelligenceHero(Hero):
    def __init__(self):
        """
        TO DO:
        The constructor of the <StrengthHero> class.
        Use super() to initialize the attributes of the parent class.
        Add a new attribute <main_attribute>.
        The <main_attribute> of intelligence hero should be "intelligence"

        Parameters:
            name (str): The name of the hero.
            hp (float): The health points of the hero.
            mp (float): The magic points of the hero.
            damage (float): The damage of the hero.
            strength_growth (float): The strength gain per level of the hero.
            agility_growth (float): The agility gain per level of the hero.
            intelligence_growth (float): The intelligence gain per level of the hero.

        Returns:
            None
        """
    
    def level_up(self):
        """
        TO DO:
        This method would level a hero up
        1. increase <level> by 1
        2. increase <hp> by 5 * <strength_growth>
        3. increase <mp> by 20 * <intelligence_growth>
        4. increase <damage> by 1 * main_attribute growth


        Parameters:
            None

        Returns:
            None
        """
    
    def ability(self):
        """
        TO DO:
        This method would transform 50% of mp into hp and the rest of mp into damage.
        After transformation, mp should be 0.
        Then print "<name> now has <hp> hp and <damage> damage"

        Parameters:
            None

        Returns:
            None
        """

# Now let's simulate the game
def main(heroes):
    """
    In this function, you will create instances of heroes. You'll make heroes level up, 
    use their abilities, and attack each other.

    Parameters:
        heroes (list): A list of dictionary. Each dictionary describes the attributes of a hero.

    Returns:
        winners (list): A list of objects who survive after the fight.
    """

    # TO DO:
    # Initialize hero instances
    # Loop over <heroes>, for each dictionary, create correspoding hero instance
    # Use conditional statements to check hero's main attribute
    # If a hero's main attribute is "strength", it should be an instance of StrengthHero
    # If a hero's main attribute is "agility", it should be an instance of AgilityHero
    # If a hero's main attribute is "intelligence", it should be an instance of IntelligenceHero
    # Then add the key-value pair <name> : hero instance into a new dictionary <all_heroes>
    all_heroes = {}

    

    # TO DO:
    # Level up your heroes
    # Loop over <all_heroes>, for each key-value pair, level up the value (which is an instance of hero) to 25
    # which means you need to call the method <level_up> 25 times for each instance of hero
    # HINT: You can use range() to help repeat function/method several times


    
    # Print the information of your heroes
    # Uncomment the for loop below when you finish those TO DOs above
    # for v in all_heroes.values():
        # print(v)
    # Your output of print should be the same as below
    # Axe, level 25, hp 2425.0, mp 434.0, damage 141.9999999999999
    # Monkey King, level 25, hp 1211.0, mp 710.0, damage 143.5
    # Invoker, level 25, hp 792.0, mp 2495.0, damage 156.9999999999999
    
    # TO DO:
    # Let your heroes fight with each other with following rules:
    # If there are A,B,C,D 4 heroes
    # A would use its ability and then attack B,C,D
    # Then B would use its ability and then attack A,C,D
    # Then C, then D...

    # Below are the steps you can simulate the fight
    # Step 1: Loop over all of the key/value pairs in all_heroes. 
    # Recall that the key is the hero name and the value is the class instance representing that hero. 
    # This loop will determine whose turn it is to act in the fight!
    # Step 2: Have the hero use their ability. 
    # Remember that the ability is a method of the class instance. 
    # Your code for this should look something like this: .ability()
    # Step 3: Inside for loop, make another loop through the key/value pairs of all_heroes, 
    # but this time, use different variables to capture the individual keys and values than the outer loop. 
    # This loop will let the hero whose turn it is to attack the other heroes.
    # Step 4: Have the hero from the outer loop attack each of the other heroes. 
    # Make sure the hero doesn't attack itself! 
    # HINT: Use a conditional statement to ensure that the hero from the inner loop is different from the hero in the outer loop. 
    # ANOTHER HINT: You will want to use the .attack() method here!



    # TO DO:
    # Find winners!
    # Loop over <all_heroes> and use the method <is_dead> to check whether the hero is dead or not.
    # If the hero is not dead, add it into the list <winners>
    winners = []

    
    return winners


# Now let's do a recap of this Problem Set
# Why we need class <Hero>?
# Those heroes have the same attributes and same basic methods, like <attack>
# Why we need class <StrengthHero>, <AgilityHero>, <IntelligenceHero>
# Different heroes have different ways of leveling up and different abilities
# We actually implemented three versions of <ability> and <level_up>

# That's the power of inheritance and overriding 
# We use a parent class to manage those common attributes and methods
# We use child classes to manage those distinct methods and methods with the same name but act in different ways

# I have simplified the simulation for you
# In real world game, there are a lot more attributes, methods to manage
# That's why we need OOP to better organize our code


if __name__ == '__main__':
    main(heroes)
