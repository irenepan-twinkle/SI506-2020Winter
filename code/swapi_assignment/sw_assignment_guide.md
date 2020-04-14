# SI 506 SWAPI Echo Base Assignment

## Release Date: Tuesday, 14 April, 10:00 AM

## Due Date: Thursday, 30 April, by 11:59 PM

## 1.0 The mission

Rebel Alliance Intelligence has detected the presence of Imperial probe
[droids](https://starwars.fandom.com/wiki/Probe_droid/Legends) in the Hoth system. The secret Rebel
Alliance base codenamed _Echo_ is located on the ice planet Hoth. If Imperial probes
discover the location of the base an Imperial assault is likely to be initiated. Your job is to
write a Python program capable of producing two JSON documents that contain enriched data sourced
from local files (provided) and the [Star Wars API](https://swapi.py4e.com/).

The Python program you write will be capable of producing two JSON files:

1. a document comprising a list of uninhabited planets on which a new based can be located.
2. an updated and enriched Echo Base document that includes an evacuation plan for base personnel.

Each document will be produced to a specified format.  You will submit your Python program files
to a site (codename: Gradescope) for evaluation on or before the appointed due date.

Good luck and may the Force be with you.

## 2.0 General assignment outline

Perform the following steps:

- Read this document.
- Review template files
  - `sw_assignment.py`
  - `sw_entities.py`
  - `sw_utilities.py`
- Review data files
  - `sw_planets-v1p0.json`
  - `sw_echo_base-v1p0.json`
  - `sw_echo_base_transport_craft.csv`
  - `sw_bright_hope_crew.json`
- Review JSON solution files
  - `test_uninhabited_planets.json`
  - `test_sw_echo_base-v1p1.json`
- Implement classes and class methods in `sw_entities.py`.
- Implement utility functions in `sw_utilities.py`.
- Implement create object functions in `sw_assignment.py`.
- Implement `main()` in `sw_assignment.py` to manage workflow necessary to produce two JSON files that match the two associated solution files line for line.
- Issue HTTP GET requests to the SWAPI endpoint in order to retrieve JSON representations of people, planets, species, and starships. Decode JSON to Python dictionaries and lists (of dictionaries).
- Read local CSV and JSON files, returning dictionaries or lists of dictionaries that represent "enriched" collections of key-value pairs. Combine data with "default" SWAPI data.
- When appropriate convert SWAPI string values to `float`, `int`, `list`.
- Instantiate class instances and assign "enriched" data to instance variables.
- Identify uninhabited planets, serialize filtered planet objects to JSON using a provided `json` module custom encoder class, and write to a file.
- Build an Echo Base evacuation plan, serialize the object model to JSON using a provided `json` module custom encoder class, and write to a file.
- submit updated `sw_assignment.py`, `sw_entities.py`, and `sw_utilities.py` to the Rebel Alliance Intelligence drop site (codename Gradescope).

## 3.0 Constraints

Consider this an open book, open notes, open network take home final. You may submit partial
or completed solutions to Gradescope as many times as is necessary prior to the deadline.

That said, certain constraints exist regarding this assignment to which you _must_ comply:

- All submitted work _must_ be your own original work. Write this program on your own without any
assistance from others including fellow classmates, other individuals, study groups, forums, or
tutors. Abide by the rules regarding plagiarism as defined in the syllabus.
- If you have questions regarding the SWAPI Echo Base assignment post them on Piazza.
- Submit your three Python files to Gradescope for auto grading on or before Thursday,
30 April, 2020, at 11:59 PM Eastern. __Late submissions will _not_ be accepted__.
- Extensions for late assignments will _not_ be granted unless exceptional circumstances arise that prevent you from completing the assignment on time.
- Do not install the Python SWAPI module. Your script must do all the work itself.

## 4.0 Custom modules, data files, and JSON solutions files

Rebel Alliance Intelligence will provide you with three stubbed out Python files (the templates) that provide a skeletal implementation of the program that you will complete.

You will also receive four data files and two JSON solution files. Use the latter two files to
perform "diffs" on the JSON files you produce in order to measure progress. When your JSON files
match the test files submit your three Python files to Gradescope to receive full credit.

:warning: do not change the file names. The auto grader will raise a runtime exception if it encounters different names.

| File | Purpose | Notes |
| :--- | :------ | :---- |
| `sw_assignment.py` | Python script | Includes `main()`. |
| `sw_entities.py` | Python module | Class definitions. Imported by `sw_assignment.py`. |
| `sw_utilities.py` | Python module | Utility functions. Imported by `sw_assignment.py`. |
| `sw_planets-v1p0.json` | List of SWAPI planet objects | Data source. |
| `sw_echo_base-v1p0.json` | Default Echo Base representation | Data source. |
| `sw_echo_base_transport_craft.csv` | Enriched Transport craft data | Add/overwrite SWAPI data. |
| `sw_bright_hope_crew.json` | GR-75 Transport crew | Data source. |
| `test_uninhabited_planets.json` | Testing file | Compare to uninhabited planets JSON file you produce. Match line for line. |
| `test_sw_echo_base-v1p1.json` | Testing file | Compare to the Echo Base v1p1 (i.e., version 1.1) JSON file you produce. Match line for line. |

## 5.0 Scoring (1500 points)

The SWAPI Echo Base assignment is worth 1500 points. Points are distributed across seventeen (17) auto graded tests that assess your submitted work. You earn points whenever you pass a test. You may submit your files to Gradescope as many times as is needed before the assignment closing date.

## 6.0 Classes

Each entity described below is defined as a `class` in the module `sw_entities.py`.
Complete the implementation of these classes, adding Docstrings as necessary,
per the table information below.

:bulb: Class initialization for `Entity` and its subtypes is deliberately lightweight. All that is required is a resource identifer string in the form of a URL and a name string.  Other instance variables can be set after the object is created.

:bulb: Descriptions of each instance variable can be found in the pre-populated class Docstrings.

### 6.1 CustomEncoder(json.JSONEncoder)

module: `sw_utilities.py`

:exclamation: The `CustomEncoder` class has been implemented for you. Do _not_ modify
the class.

`CustomEncoder` handles the encoding of custom composite objects as JSON.
Invoked by the `json.dump()` method when called inside the function
`write_custom_json(filepath, data)`. See the Lecture 21 [Millennium Falcon
exercise walk through](https://zoom.us/rec/play/v8B4fuqppm83TtzDsASDAPQsW9TvLPis1CMeqfoEzky9UiRXN1XwYrdEa7OBs0d8bcMz-FCkvVH4pDLz?startTime=1586112032000) recording for implementation details.

| method | implement | add Docstring | notes |
| :----- | :-------- | :------------ | :---- |
| `default(self, obj)` | No | No | __Implemented__. Do not modify|

### 6.2 Entity

module: `sw_entities.py`

data source(s): supertype initialized by subtypes

| order | instance variable | type | notes |
| ----: | :---------------- | :--: | :---- |
| 1 | url | str | |
| 2 | name | str | |

| method | implement | add Docstring | notes |
| :----- | :-------- | :------------ | :---- |
| `__init__(self, url, name)` | Yes | No | |
| `jsonable(self)` | Yes | No | |
| `__str__(self)` | No | No | |

### 6.3 EvacuationPlan(Entity)

module: `sw_entities.py`

data source(s): `sw_echo_base-v1p0.json`, SWAPI (transport passenger seating count)

| order | instance variable | type | notes |
| ----: | :---------------- | :--: | :---- |
| 1 | url | str | |
| 2 | name | str | |
| 3 | classification | str | |
| 4 | year_era | str | |
| 5 | description | str | |
| 6 | garrison_personnel_count | int | |
| 7 | num_available_transports | int | |
| 8 | passenger_overload_multiplier | int | |
| 9 | max_passenger_overload_capacity | int | |
| 10 | transport_assignments | list | `[<Starship>]` |
| 11 | transport_escorts | list | `[<Starship>, <Starship>]` |

| method | implement | add Docstring | notes |
| :----- | :-------- | :------------ | :---- |
| `__init__(self, url, name)` | Yes | No | |
| `jsonable(self)` | Yes | No | |
| `__str__(self)` | No | No | |

### 6.4 Garrison(Entity)

module: `sw_entities.py`

data source(s): `sw_echo_base-v1p0.json`, SWAPI (Garrison Commander homeworld and species)

| order | instance variable | type | notes |
| ----: | :---------------- | :--: | :---- |
| 1 | url | str | |
| 2 | name | str | |
| 3 | commander | Person | |
| 4 | personnel | dict | |

| method | implement | add Docstring | notes |
| :----- | :-------- | :------------ | :---- |
| `__init__(self, url, name)` | No | No | Implemented as an example. |
| `jsonable(self)` | No | No | Implemented as an example. |
| `__str__(self)` | No | No | Implemented as an example. |

### 6.5 MiltaryBase(Entity)

module: `sw_entities.py`.

data source(s): `sw_echo_base-v1p0.json`

| order | instance variable | type | notes |
| ----: | :---------------- | :--: | :---- |
| 1 | url | str | |
| 2 | name | str | |
| 3 | operational_status | str | |
| 4 | location | Planet | |
| 5 | facilities | list | |
| 6 | garrison | Garrison | |
| 7 | fixed_defenses | list | |
| 8 | air_space_assets | list | |
| 9 | facilities | EvacuationPlan | |

| method | implement | add Docstring | notes |
| :----- | :-------- | :------------ | :---- |
| `__init__(self, url, name)` | Yes | No | |
| `jsonable(self)` | Yes | No | |
| `__str__(self)` | No | No | |

### 6.6 Person(Entity)

module: `sw_entities.py`.

source(s): SWAPI, `swapi-echo_base-v1p0.json`, `sw_bright_hope_crew.json`.

The Echo Base `swapi-echo_base-v1p0.json` file contains default data on the
base commander General
[Carlist Rieekan](https://starwars.fandom.com/wiki/Carlist_Rieekan/Legends)
His data must be enriched with `homeworld` and `species` data
retrieved from SWAPI.

Data on other leading Rebel Alliance members including
Princess [Leia Organa](https://starwars.fandom.com/wiki/Leia_Organa_Solo),
Commander [Luke Skywalker](https://starwars.fandom.com/wiki/Luke_Skywalker/Legends),
the smugglers [Han Solo](https://starwars.fandom.com/wiki/Han_Solo/Legends) and
[Chewbacca](https://starwars.fandom.com/wiki/Chewbacca/Legends), and the droids
[C-3PO](https://starwars.fandom.com/wiki/C-3PO/Legends),
[R2-D2](https://starwars.fandom.com/wiki/R2-D2/Legends), as well as three
crew members of the GR-75 medium transport 'Bright Hope': Araly Denau, Teckla Lerga,
and Rego Syko listed in `sw_bright_hope_crew.json`.

| order | instance variable | type | notes |
| ----: | :---------------- | :--: | :---- |
| 1 | url | str | |
| 2 | name | str | SWAPI search field. |
| 3 | birth_year | str | |
| 4 | height | float | |
| 5 | mass | float | | |
| 9 | homeworld | Planet | Retrieve planet data from SWAPI. |
| 10 | species | Species | Retrieve species data from SWAPI. |

| method | implement | add Docstring | notes |
| :----- | :-------- | :------------ | :---- |
| `__init__(self, url, name)` | Yes | No | |
| `jsonable(self)` | Yes | No | |
| `__str__(self)` | No | No | |

### 6.7 Planet(Entity)

module: `sw_entities.py`.

source(s): SWAPI endpoint: `sw-echo_base-v1p0.json1`.

| order | instance variable | type | notes |
| ----: | :---------------- | :--: | :---- |
| 1 | url | str | |
| 2 | name | str | SWAPI search field |
| 8 | gravity | str | |
| 7 | climate | list | |
| 9 | terrain | list | |
| 10 | surface_water | int | |
| 11 | population | int | |

| method | implement | add Docstring | notes |
| :----- | :-------- | :------------ | :---- |
| `__init__(self, url, name)` | Yes | No | |
| `jsonable(self)` | Yes | No | |
| `__str__(self)` | No | No | |

### 6.8 Species(Entity)

module: `sw_entities.py`.

data source(s): SWAPI endpoint.

| order | instance variable | type | notes |
| ----: | :---------------- | :--: | :---- |
| 1 | url | str | |
| 2 | name | str | SWAPI search field. |
| 3 | classification | str | |
| 4 | designation | str | |
| 5 | language | str | |

| method | implement | add Docstring | notes |
| :----- | :-------- | :------------ | :---- |
| `__init__(self, url, name)` | Yes | No | |
| `jsonable(self)` | Yes | No | |
| `__str__(self)` | No | No | |

### 6.9 Starship(Entity)

module: `sw_entities.py`.

data source(s): SWAPI endpoint, `swapi_echo_base_transport_craft.csv`.

The Echo Base `swapi_echo_base_transport_craft.csv` file contains information on
the following transport craft:

- [T-65 X-wing starfighter](https://starwars.fandom.com/wiki/T-65B_X-wing_starfighter/Legends)
- [BTL Y-wing assault starfighter](https://starwars.fandom.com/wiki/BTL_Y-wing_starfighter/Legends)
- [t-47 airspeeder](https://starwars.fandom.com/wiki/T-47_airspeeder/Legends)
- [GR-75 medium transport](https://starwars.fandom.com/wiki/GR-75_medium_transport/Legends)
- [Millennium Falcon](https://starwars.fandom.com/wiki/Millennium_Falcon/Legends) light freighter.

:bulb: `swapi_echo_base_transport_craft.csv` contains data (e.g., fields and values) not found in SWAPI.

| order | instance variable | type | notes |
| ----: | :---------------- | :--: | :---- |
| 1 | url | str | |
| 2 | name | str | SWAPI search field. |
| 3 | model | str | SWAPI search field. |
| 4 | starship_class | str | |
| 5 | length | float | |
| 6 | max_atmosphering_speed | float | |
| 7 | hyperdrive_rating | float | |
| 8 | MGLT | int | |
| 9 | armament | list | Non-SWAPI property. |
| 10 | crew | int | |
| 11 | passengers | int | |
| 12 | consumables | str | |
| 13 | cargo_capacity | int | |
| 14 | crew_members | dict | Non-SWAPI property. `{'<role>': <Person>}` |
| 15 | passenger_manifest | list | Non-SWAPI property. `[<Person>]` |

| method | implement | add Docstring | notes |
| :----- | :-------- | :------------ | :---- |
| `__init__(self, url, name, model, starship_class)` | Yes | No | |
| `assign_crew(self, crew)` | Yes | No | Each `crew` key defines a role (e.g., `pilot`, `co-pilot`,
`astromech_droid`) while the associated value is an instance of a Person (e.g., Luke Skywalker). |
| `assign_passengers(self, manifest)` | Yes | List of Person instances assigned to the starship's passenger manifest. | |
| `jsonable(self)` | Yes | No | |
| `__str__(self)` | No | No | |

## 7.0 Functions

Tasks that must be repeated will be assigned to functions or class methods.

:exclamation: The modules you write you will write _must_ implement the following listed functions. Each function must be include a Docstring. You are free to write other functions to help accomplish the assignment objectives but you __must__ implement all the functions described below that are not already implemented for you to earn points.

### 7.1 `sw_assignment.py` module

The four `create_*(data)` functions in `sw_assignment.py` help eliminate the code duplication that would inevitably occur in `main()` due to the need to create multiple class instances of the same type, particularly people and starships. You will write Docstrings and statement blocks for each of these stubbed out functions.

These functions should also handle the conversion of string values sourced from SWAPI to floats, ints, and lists whenever appropriate. When assigning instance variable values each `create_*(data)` function needs to call the appropriate `convert_str_to_*(data)` function to convert the string value. The class tables below list the correct type for each instance variable specified.

The module _must_ include a `main()` function that serves as the program's entry point. Design the program to interact with local file assets and the Star Wars API to create two data files required by Rebel Alliance Intelligence. Delegate sub-tasks to other functions. Call these ancillary functions from `main()` or, when appropriate, from other functions as needed.

The code you write in `main()` will orchestrate the creation of the following two
files:

- `sw_uninhabited_planets.json`, a JSON file comprising a list of uninhabited planets where a new rebel base could be situated if Imperial forces discover the location of Echo Base.

- `sw_echo_base-v1p1.json1`, A JSON file describing the Echo Base including an evacuation plan of base personnel. The plan will also assign Princess Leia and the protocol droid C-3PO to the transport Bright Hope. Upon departure the transport will be escorted by an X-wing starfighter piloted by Commander Luke Skywalker (with astromech droid R2-D2) and the light freighter Millennium Falcon crewed by the smugglers Han Solo and Chewbacca, the Wookiee.

| function | implement | add Docstring | notes |
| :------- | :-------- | :------------ | :---- |
| `main()` | Yes | Yes | Entry point for the program. |
| `create_Person(data)` | Yes | Yes | Calls string conversion methods, `create_Planet(data)`, and `create_Species(data)` |
| `create_Planet(data)` | Yes | Yes | Calls string conversion methods. |
| `create_Species(data)` | No | No | Implemented as an example. |
| `create_Starship(data)` | Yes | No | Calls string conversion methods. |

### 7.2 `sw_utilities.py` module

The functions that comprise `sw_utilities.py` are a set of utility functions that arguably could be used by other programs. All Docstrings have been written for these functions. Read the function documentation to better understand their behavior, parameters and return values.

Two functions have been implemented: `read_csv_as_dict(path, delimiter=',')` and `write_custom_json(filepath, obj)`. Other functions were introduced during lecture or in a couple of the problem sets. Free free to borrow the code and implement it in this assignment to jump-start your work, though don't assume that a cut-and-paste job will always meet your needs.

| function | implement | add Docstring | notes |
| :------- | :-------- | :------------ | :---- |
| `combine_data(default_data, override_data)` | Yes | No | copy.deepcopy() implemented. You implement remainder of function. |
| `convert_str_to_float(value)` | Yes | No | Implement using try / except blocks. |
| `convert_str_to_int(value)` | Yes | No | Implement using try / except blocks. |
| `convert_str_to_list(value)` | Yes | No | Implement using try / except blocks. |
| `get_swapi_resource(url, params=None, timeout=20)` | Yes | Yes | SWAPI data is serialized as JSON.  The `requests` module decodes the response by calling its `.json()` and returns a list or dictionary. |
| `is_unknown(value)` | Yes | No | Implement a _case-insensitive_ membership test of the passed in value against the tuple items (`unknown`, `n/a`). Return `True` if a match is obtained. Use try / except blocks. |
| `read_csv_as_dict(path, delimiter=',')` | No | No | __Implemented__. Do _not_ modify. |
| `read_json(filepath)` | No | Yes | __Implemented__. Write Docstring only. |
| `write_custom_json(filepath, obj)` | No | No | __Implemented__. Do _not_ modify. |

## 8.0 Implementation notes

I recommend adopting an iterative approach when writing your code. First, focus on generating the
`sw_uninhabited_planets.json` file. The classes and functions you must implement should be tackled in groups. Follow the steps below before attempting to produce the more complex
`sw_echo_base-v1p1.json` file.

### 8.1 Module imports

All required import statements are provided. Note that `sw_assignment.py` imports objects from both the modules `sw_entities.py` (the model classes) and `sw_utilities.py` (utility functions).

`sw_assignment.py`

```python
from sw_entities import EvacuationPlan, Garrison, MilitaryBase, \
    Person, Planet, Species, Starship
import sw_utilities as utl
```

`sw_utilities.py`

```python
import copy
import csv
import json
import requests
```

To reference a utility function `sw_assignment.py` prefix the function name with `utl`, as in

```python
filepath = 'sw_planets-v1p0.json'
swapi_planets = utl.read_json(filepath)
```

### 8.2 Locate uninhabited planets

You will work with local file resources initially, not SWAPI. Review the following files:

- input: `sw_planets-v1p0.json`
- output: `sw_uninhabited_planets.json` (see provided test solution file)

then implement the following classes and functions noting their locations and where in `sw_assignment.py` the class is instantiated or the function is called.

:exclamation: Start with `Entity` first. It's only partially implemented and its missing instance
variables introduce errors in all its subtypes that attempt to initialize it using `super()`.

| Object | location| instantiate / call from | notes |
| :----- | :------ | :-------------------- | ----- |
| `Entity` | `sw_entities` | `Planet` | Supertype |
| `Planet` | `sw_entities` | `create_planet(data)` | Subtype |
| `create_planet(data)` | `sw_assignment` | `main()` | |
| `convert_str_to_int(value)` | `sw_utilities` | `create_planet(data)` | |
| `convert_str_to_list(value)` | `sw_utilities` | `create_planet(data)` | |
| `read_json(filepath)` | `sw_utilities` | `main()` | read `sw_planets-v1p0.json` |
| `is_unknown(value)` | `sw_utilities` | `main()` | for loop / list comprehension conditional statement |
| `write_custom_json(filepath, obj)` `sw_utilities` | `main()` | Write uninhabited planet objects to file as JSON. Function already implemented. |

Then perform the following operations in `main()`:

1. Read `sw_planets-v1p0.json` and return a list of planet dictionaries.
2. Create an empty list in `main()` to hold uninhabited planet objects.
3. Iterate over the list of planet dictionaries.
   1. Call `is_unknown()` and perform a _case-insensitive_ truth value test on each planet's _population_ value.
   2. If the value is an 'unknown' (e.g., unknown or n/a) create a `Planet` instance
   3. Append the planet object to a (growing) list of uninhabited planet objects.
4. Once all the uninhabited planets have been appended to the list of uninhabited planets,
   serialize the planet objects as JSON and write to a file named `sw_uninhabited_planets.json`.
5. Compare your file to the uninhabited planets solution file (do this in VS Code). When the two files match line for line, submit your three Python modules to Gradescope and earn points.

Do this work first before doing anything else. This will introduce you to all three modules and how the objects work with one another. Look for the patterns in the implementation (which you will repeat).

:bulb: compare the file you are generating with the test solution file regularly in order
to gauge your process. This is called "diffing" your files. For VS Code users see Gérald Barré's
blog post ["Comparing files using Visual Studio Code"](https://www.meziantou.net/comparing-files-using-visual-studio-code.htm)
(Mar 2018) on how to compare two files using the VS Code user interface.

### 8.3 Create an Echo Base person

Next implement the Species and Person classes, related helper and string conversion functions, and `get_swapi_resource()`.

| Object | location| instantiate / call from | notes |
| :----- | :------ | :-------------------- | ----- |
| `Species` | `sw_entities` | `create_person(data)` | |
| `create_species(data)` | `sw_assignment` | `main()` | Implemented as an example.|
| `Person` | `sw_entities` | `create_person(data)` | |
| `create_person(data)` | `sw_assignment` | `main()` | calls `create_planet(data)`, `create_species(data)`, `convert_str_to_float(value)` |
| `convert_str_to_float(value)` | `sw_utilities` | `create_person(data)` | |
| `get_swapi_resource(filepath, params=None, timeout=20)` | `sw_utilities` | `main()` | |

Implement the Species and Planet classes (review the Docstrings for required attributes and methods).  Note how `create_species(data)` is implemented. Adopt the same approach for `create_person(data)` although creating a Person instance involves more work. First, call `convert_str_to_float(value)` when assigning string values that can be converted to `float`. Second, call the SWAPI service to retrieve the person's homeworld data. Call `create_planet(data)` to create the Planet instance and assign it to the `person.homeworld` instance variable. Third, call the SWAPI service to retrieve the person's species data. Call `create_species(data)` to create the Species instance and assign it to the `person.species` instance variable.

In `main()` write some test code.  Call SWAPI and retrieve a JSON representation of Princess Leia Organa decoded into a dictionary. Then call `create_person(data)` to instantiate a `Person` and populate the object with Leia data. Finally call `write_custom_json(filepath, data)` and write the Leia object to a file as JSON (e.g.,`test_leia.json`).

Your intermediate goal is to confirm that your implementation work can convert SWAPI JSON to "Echo Base" JSON (see below). Make liberal use of `print()` statements to track your work.

:bulb: The site [jsoncompare.com](https://jsoncompare.com/#!/simple/) provides a browser-based
GUI for inspecting and reformatting JSON documents.

### SWAPI Leia Organa (JSON)

```json
{
  "name": "Leia Organa",
  "height": "150",
  "mass": "49",
  "hair_color": "brown",
  "skin_color": "light",
  "eye_color": "brown",
  "birth_year": "19BBY",
  "gender": "female",
  "homeworld": "https://swapi.py4e.com/api/planets/2/",
  "films": [
    "https://swapi.py4e.com/api/films/1/",
    "https://swapi.py4e.com/api/films/2/",
    "https://swapi.py4e.com/api/films/3/",
    "https://swapi.py4e.com/api/films/6/",
    "https://swapi.py4e.com/api/films/7/"
  ],
  "species": [
    "https://swapi.py4e.com/api/species/1/"
  ],
  "vehicles": [
    "https://swapi.py4e.com/api/vehicles/30/"
  ],
  "starships": [],
  "created": "2014-12-10T15:20:09.791000Z",
  "edited": "2014-12-20T21:17:50.315000Z",
  "url": "https://swapi.py4e.com/api/people/5/"
}
```

### Echo Base Leia Organa (JSON)

```json
{
  "url": "https://swapi.py4e.com/api/people/5/",
  "name": "Leia Organa",
  "birth_year": "19BBY",
  "height": 150.0,
  "mass": 150.0,
  "homeworld": {
    "url": "https://swapi.py4e.com/api/planets/2/",
    "name": "Alderaan",
    "gravity": "1 standard",
    "climate": [
      "temperate"
    ],
    "terrain": [
      "grasslands",
      "mountains"
    ],
    "surface_water": 40,
    "population": 2000000000
  },
  "species": {
    "url": "https://swapi.py4e.com/api/species/1/",
    "name": "Human",
    "classification": "mammal",
    "designation": "sentient",
    "language": "Galactic Basic"
  }
}
```

When your output matches the "Echo Base" Leia Organa, declare victory, comment out your test code and continue on to the next step.

### 8.4 Create an Echo Base starship

Next implement the Starship class, related helper function `create_starship(data)`, and `combine_data(default_data, override_data)`, and `read_csv_as_dict(path, delimiter=',')`.

| Object | location| instantiate / call from | notes |
| :----- | :------ | :-------------------- | ----- |
| `Starship` | `sw_entities` | `create_starship(data)` | |
| `create_starship(data)` | `sw_assignment` | `main()` | |
| `combine_data(default_data, override_data)` | `sw_utilities` | `main()` | |
| `read_csv_as_dict(path, delimiter=',')` | `sw_utilities` | `main()` | |

Implement the Starship classe (review the Docstrings for required attributes and methods).  Next implement the `create_starship(data)` function.  Many SWAPI starship string values can be converted to `float`, `int`, or `list` so be sure to call the convert string functions as necessary. Next, implement `combine_data(default_data, override_data)`. You will need it to "enrich" the SWAPI-sourced data with data from `sw_echo_base_transport_craft.csv`.

In `main()` write some test code.  Call SWAPI and retrieve a JSON representation of the T-65 X-wing starfighter decoded into a dictionary. Next, call `read_csv_as_dict(path, delimiter=',')` passing in the filepath "sw_echo_base_transport_craft.csv" and return a list of dictionaries (remember to choose the right delimiter value). Pull out the T-65 X-wing dictionary and combine it with the SWAPI data. Call `combine_data(default_data, override_data)` passing in the SWAPI dictionary as the "default" and the CSV-sourced X-wing data as the "override".  Assign the return value to a new `x_wing_combined` dictionary (or choose your own variable name).

Pass the new `x_wing_combined` dictionary to `create_starship(data)` to instantiate a Starship object. Then call `write_custom_json(filepath, data)` and write the X-win object to a file as JSON (e.g.,`test_x_wing.json`). Again, make liberal use of `print()` statements to track your work.

Your second intermediate goal is to create an "Echo Base" X-wing starfighter expressed as JSON. If your JSON file matches the object below, declare victory, comment out your test code, and continue on to the next step.

:bulb: note that the JSON does not include crew member assignments. That is a task for later.

```json
{
  "url": "https://swapi.py4e.com/api/starships/12/",
  "name": "X-wing",
  "model": "T-65 X-wing",
  "starship_class": "Starfighter",
  "length": 12.5,
  "max_atmosphering_speed": 1050.0,
  "hyperdrive_rating": 1.0,
  "MGLT": 100,
  "armament": [
    "4 x Taim & Bak KX9 or IX4 laser cannons",
    "2 x Krupx MG7 proton torpedo launchers (3 torpedoes each)"
  ],
  "crew": 1,
  "passengers": 0,
  "consumables": "1 week",
  "cargo_capacity": 110,
  "crew_members": {},
  "passenger_manifest": []
}
```

### 8.5 Echo Base evacuation plan

Now it is time to begin to implement the Echo Base implementation plan.  First, implement the `EvacuationPlan`, `MiltaryBase` and `Garrison` classes along with the `read_json(filepath)` function.

| Object | location| instantiate / call from | notes |
| :----- | :------ | :-------------------- | ----- |
| `EvacuationPlan` | `sw_entities` | `main()` | |
| `MiltaryBase` | `sw_entities` | `main()` | |
| `Garrison` | `sw_assignment` | `main()` | |
| `read_json(filepath)` | `sw_utilities` | `main()` | read `echo_base-v1p0.json` and `sw_bright_hope_crew.json`. |

Then return to `main()`. At a minimum `main()` now features code written to find and write to file a list of "uninhabited planets". It may also include (commented out) test code written to create people and starships and write those objects to file.

At this point I could tell you to study the structure of both the `echo_base-v1p0.json` file and the enriched `test_echo_base-v1p1.json` file and write your code to produce the latter file. The entities defined in `sw_entities.py` are discernable as JSON objects (i.e., denoted by curly brackets {}) in `test_echo_base-v1p1.json`. The object structure is roughly as follows:

```
MiltaryBase (Echo Base)
  Planet (location)
  Garrison
    Person (Base Commander)
      Planet (homeworld)
      Species
  EvacuationPlan
    transport_assignments []
      Starship
        crew_members {}
          Person
            Planet (homeworld)
            Species
          Person
            Planet (homeworld)
            Species
          Person
            Planet (homeworld)
            Species
        passenger_manifest []
          Person
            Planet (homeworld)
            Species
          Person
            Planet (homeworld)
            Species
    transport_escorts []
      Starship
        crew_members {}
          Person
            Planet (homeworld)
            Species
          Person
            Planet (homeworld)
            Species
        passenger_manifest []
      Starship
        crew_members {}
          Person
            Planet (homeworld)
            Species
          Person
            Planet (homeworld)
            Species
        passenger_manifest []
```

If you have implemented the previous steps successfully, you can write to file most of the entities contained in the above graph (e.g., Person, Planet, Species, and Starship). What remains is to define a workflow that retrieves data from local and remote sources, combines "linked" data, converts string data to more appropriate types whenever possible, creates class instances to hold the data, and when complete serializes the object model as JSON and writes it to a `sw_echo_base-v1p1.json`.

The following `main()` coding tasks should get the job done:

#### 8.5.1 Echo Base "fact sheet"

1. Read the `sw_echo_base-v1p0.json`.
2. Create a `MiltaryBase` instance to hold Echo Base data.
3. Create a `Planet` instance to hold location-related data.
4. Create a `Garrison` instance to hold garrison-related data.
5. Create a `Person` instance for the base commander and add to the garrison instance.
6. Read `sw_echo_base_transport_craft.csv` and update the base `air_space_assets` `model` property.

#### 8.5.2 Evacuation plan

1. Create an `EvacuationPlan` instance to hold evacuation plan data. Add the data sourced from `sw_echo_base-v1p0.json`.

#### 8.5.3 GR-75 medium transport

1. Create a `Starship` instance representing a GR-75 medium transport.
2. Combine data on the transport from SWAPI and `sw_echo_base_transport_craft.csv`.
3. Rename the transport 'Bright Hope.'
4. Create `Person` instances for the crew members. Get crew data from `sw_bright_hope_crew.json1`.
5. Assign crew members to the transport.
6. Create `Person` instances for the passengers. Check the JSON solutions file for who should be assigned as passengers. Get crew data from SWAPI.
7. Assign passengers to the transport manifest.
8. Add the transport to the evacuation plan's transport_passenger_assignments list. Suspend disbelief and pretend that you perform these steps another 29 times for each available transport and the thousands of base personnel to be evacuated.

#### 8.5.4 X-wing

1. Create a `Starship` instance representing an X-wing starfighter
2. Combine data on the X-wing from SWAPI and `sw_echo_base_transport_craft.csv`.
3. Create `Person` instances for the crew members. Check the JSON solutions file for who should be assigned to the X-wing. Get crew data from SWAPI.
4. Assign crew members to the X-wing.
5. Add the X-wing to the evacuation plan's transport escort list. Suspend disbelief and pretend that you assign two X-wing or Y-wing starfighters as escorts for each Echo Base transport.

#### 8.5.5 Millennium Falcon

1. Create a `Starship` instance representing the Millennium Falcon.
2. Combine data on the Millennium Falcon from SWAPI and `sw_echo_base_transport_craft.csv`..
3. Create `Person` instances for the crew members. Check the JSON solutions file for who should be assigned to the Millennium Falcon. Get crew data from SWAPI.
4. Assign crew members to the Millennium Falcon.
5. Add the Millennium Falcon to the evacuation plan's transport escort list. The light frieghter is suprisingly fast and nimble and can assist in escort duties if the pilot agrees.

#### 8.5.6 Evacuation arithmetic

1. From the garrison instance add up the total number of base personnel. Assign the computed value to the Evacuation Plan's `garrison_personnel_count` property.
2. Locate a count of the Echo Base transport fleet and assign it to `num_available_transports`.
3. Multiply the number of Echo Base transports by the number of passengers each transport is rated to carry. The sum of this calculation represents the standard passenger carrying capacity of the Echo Base transport fleet. Assume that in an emergency each transport can carry three (3) times the number of passengers in a single lift by trading cargo space for passenger use. Multiply the standard passenger carrying capacity of the Echo Base transport fleet by the `passenger_overload_multiplier` and assign the result to `max_passenger_overload_capacity`. This number (available transports x passenger seating per transport x overload multiplier) represents the total number of base personnel that can be evacuated in a single lift prior to an Imperial assault on the base.

#### 8.5.7 Complete the evacuation plan and write to file

Update the Echo Base instance `evacuation_plan` instance variable with the evacuation plan object.

Finally, write the enriched Echo Base instance to a file named `sw_echo_base-v1p1.json`.

Perform a diff on the file against the test solution file. If differences exist debug as necessary.
If the files match, submit your `sw_assignment.py`, `sw_entities.py`, and `sw_utilities.py` files to Rebel Alliance Intelligence (code name: Gradescope) for evaluation. You may resubmit your files as many times as is necessary to earn maximum points prior to the deadline.

## Appendix A. Docstrings

Each function _must_ include a "Docstring" that describes the function, parameters (including optional parameter default values), and return value, if any. Utilize the following `Docstring` format to document your functions:

- Function description (~1-3 sentences).
- Parameters:
  - arg_1 (type): argument 1 description.
  - arg_2 (type): argument 2 description.
- Returns:
  - type: return value description

When describing parameters and return value (if any) use the following data type abbreviations:

| Data type | Abbreviation |
|:--------- | :----------- |
| Boolean | bool |
| Complex number | complex |
| Dictionary | dict |
| Float | float |
| Integer | int |
| List | list |
| String | str |
| Tuple | tuple |
| Class | Class name |

### A.1 Docstring examples

```python
def read_csv_as_dict(path, delimiter=','):
    """Accepts a path, creates a file object, and returns a list of
    dictionaries that represent the row values.

    Parameters:
        path (str): path to file
        delimiter (str): delimiter that overrides the default delimiter

    Returns:
        list: nested dictionaries representing the file contents
     """

    pass
```

```python
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
      crewed by the smugglers Han Solo and Chewbacca.

    Parameters:
        None

    Returns:
        None
    """

    # START WORK HERE.
```

## Appendix B. Auto Grader Tests

Below is a list of the unit tests that the auto grader runs. The auto grader test module will import the three modules (`sw_assignment.py`, `sw_entities.py`, `sw_utilities.py`) that you submit in order to instantiate class instances, call class methods, and call functions. All three files _must_ be submitted each time you want Gradescope to test your code.

:exclamation: For a test to succeed, you _must_ implement all functions required by the test as well as write any required Docstrings.

| test | functions called |
| :--  | :--------------- |
| `test_01_read_json` | `read_json(filepath)` |
| `test_02_read_csv_as_dict` | `read_csv_as_dict(path, delimiter=',')` |
| `test_03_get_swapi_resource` | `get_swapi_resource(url, params=None, timeout=20)` |
| `test_04_write_custom_json` | `write_custom_json(filepath, obj)`, `read_json(filepath)`, `Person.jsonable(self)`, `create_person(data)`, `Planet.jsonable(self)`, `create_planet(data)`, `Species.jsonable(self)`, `create_species(data)`, `convert_str_to_float(value)`, `convert_str_to_int(value)`, `convert_str_to_list(value, delimiter)` |
| `test_05_combine_data` | `combine_data(default_data, override_data)`, `read_csv_as_dict(path, delimiter=',')`, `read_json(filepath)` |
| `test_06_is_unknown` | `is_unknown(value)` |
| `test_07_convert_str_to_float` | `convert_str_to_float(value)` |
| `test_08_convert_str_to_int` | `convert_str_to_int(value)` |
| `test_09_convert_str_to_list` | `convert_str_to_list(value, delimiter=',')` |
| `test_10_create_planet` | `Planet.jsonable(self)`, `create_planet(data)`, `convert_str_to_int(value)`, `convert_str_to_list(value, delimiter)`, `read_json(filepath)` `write_custom_json(filepath, obj)` |
| `test_11_create_species` | `Species.jsonable(self)`, `create_species(data)`, `read_json(filepath)` `write_custom_json(filepath, obj)` |
| `test_12_create_person` | `Person.jsonable(self)`, `create_person(data)`, `Planet.jsonable(self)`, `create_planet(data)`, `Species.jsonable(self)`, `create_species(data)`, `convert_str_to_float(value)`, `convert_str_to_int(value)`, `convert_str_to_list(value, delimiter)`, `read_json(filepath)`, `write_custom_json(filepath, obj)` |
| `test_13_create_starship` | `Starship.jsonable(self)`, `create_starship(data)`, `convert_str_to_float(value)`, `convert_str_to_int(value)`, `convert_str_to_list(value, delimiter)`, `read_csv_as_dict(path, delimiter=',')`, `read_json(filepath)`, `write_custom_json(filepath, obj)` |
| `test_14_assign_crew` | `Starship.jsonable(self)`, `Starship.assign_crew(self, crew)`, `create_starship(data)`, `Person.jsonable(self)`, `create_person(data)`, `combine_data(default_data, override_data)`, `convert_str_to_float(value)`, `convert_str_to_int(value)`, `convert_str_to_list(value, delimiter)`, `read_csv_as_dict(path, delimiter=',')`, `read_json(filepath)`, `write_custom_json(filepath, obj)` |
| `test_15_assign_passengers` | `Starship.jsonable(self)`, `Starship.assign_passengers(self, manifest)`, `create_starship(data)`, `Person.jsonable(self)`, `create_person(data)`, `combine_data(default_data, override_data)`, `convert_str_to_float(value)`, `convert_str_to_int(value)`, `convert_str_to_list(value, delimiter)`, `read_csv_as_dict(path, delimiter=',')`, `read_json(filepath)`, `write_custom_json(filepath, obj)` |
| `test_16_write_uninhabited_planets_json_file` | `main()`, `is_unknown(value)`, `Person.jsonable(self)`, `create_planet(data)`, `convert_str_to_int(value)`, `convert_str_to_list(value, delimiter)`, `read_json(filepath)` `write_custom_json(filepath, obj)` |
| `test_17_generate_echo_base_json_file` | `main()` plus all required classes, class methods, and functions. |
