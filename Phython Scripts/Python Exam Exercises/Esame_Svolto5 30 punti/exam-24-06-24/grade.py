# -*- coding: utf-8 -*-
import testlib
import isrecursive
import os
import sys
import tree
from testlib import my_print, COL, check_expected

############ check that you have renamed the file as program.py   ###########
if not os.path.isfile('program.py'):
    print('WARNING: Save program.empty.py as program.py\n'
          'ATTENZIONE: salvare program.vuoto.py con nome program.py')
    sys.exit(0)
#############################################################################

import program

#############################################################################
#### Use DEBUG=True to disable the recursion tests and enable the
#### stack trace: each error will produce a more verbose output
####
#### Mettete DEBUG=True per disattivare i test di ricorsione  e
#### fare debug delle funzioni più facilmente attivando stack trace
DEBUG = False
# DEBUG = False
#############################################################################

################################################################################
# ------- THE SOURCE CODE FROM THIS POINT FORWARD IS FOR TESTING ONLY -------- #

# ----- The use of the following functions in your program is forbidden ------ #
# ---------------------------------------------------------------------------- #
# --- IL CODICE SORGENTE DI SEGUITO È ESCLUSIVAMENTE PER EFFETTUARE I TEST --- #
# ------- L'uso delle funzioni seguenti nel vostro programma è vietato --------#
################################################################################

def test_personal_data_entry(run=True):
    if 'name' in program.__dict__:
        assert program.name       != 'NAME', f"{COL['YELLOW']}ERROR: Please assign the 'name' variable with YOUR NAME in program.py{COL['RST']}"
        assert program.surname    != 'SURNAME', f"{COL['YELLOW']}ERROR: Please assign the 'surname' variable with YOUR SURNAME in program.py{COL['RST']}"
        assert program.student_id != 'MATRICULATION NUMBER', f"{COL['YELLOW']}ERROR: Please assign the 'student_id' variable with YOUR MATRICULATION NUMBER in program.py{COL['RST']}"
        print(f'{COL["GREEN"]}Student info: {program.name} {program.surname} {program.student_id}{COL["RST"]}')
    else:
        assert program.nome      != 'NOME', f"{COL['YELLOW']}ERRORE: Indica il tuo NOME in program.py{COL['RST']}"
        assert program.cognome   != 'COGNOME', f"{COL['YELLOW']}ERRORE: Indica il tuo COGNOME in program.py{COL['RST']}"
        assert program.matricola != 'MATRICOLA', f"{COL['YELLOW']}ERRORE: Indica il tuo NUMERO DI MATRICOLA in program.py{COL['RST']}"
        print(f'{COL["GREEN"]}Informazioni studente: {program.nome} {program.cognome} {program.matricola}{COL["RST"]}')
    return 1e-9

def add_docstring(f, local):
    S = ''
    if 'run' in local: del local['run']
    for key, val in local.items():
        S += f'\n{key} = {val}'
    f.__doc__ = S


###############################################################################


def do_func1_tests(list_of_lists, expected):
    res = program.func1(list_of_lists)
    testlib.check_list(res, expected)
    return 0.5


def test_func1_1(run=True):
    '''
    list_of_lists = [['e', 'a', 'e'], ['b', 'c'], ['c', 'd', 'd']]
    expected = ['a', 'b', 'c', 'c']
    '''
    list_of_lists = [['e', 'a', 'e'], ['b', 'c'], ['c', 'd', 'd']]
    expected = ['a', 'b', 'c', 'c']
    return do_func1_tests(list_of_lists, expected)

def test_func1_2(run=True):
    '''
    list_of_lists = [['a', 'b', 'b', 'b', 'a'], ['z', 'y', 'x', 'w', 'v'], ['a']]
    expected = ['z', 'y', 'x', 'w', 'v', 'a']
    '''
    list_of_lists = [['a', 'b', 'b', 'b', 'a'], ['z', 'y', 'x', 'w', 'v'], ['a']]
    expected = ['z', 'y', 'x', 'w', 'v', 'a']
    return do_func1_tests(list_of_lists, expected)

def test_func1_3(run=True):
    '''
    list_of_lists = [['a', 'a', 'b', 'b', 'c', 'a', 'b', 'c', 'd']]
    expected = ['d']
    '''
    list_of_lists = [['a', 'a', 'b', 'b', 'c', 'a', 'b', 'c', 'd']]
    expected = ['d']
    return do_func1_tests(list_of_lists, expected)

def test_func1_4(run=True):
    '''
    list_of_lists = [['a', 'b', 'c', 'a', 'b', 'c'], ['z', 'y', 'x', 'x', 'z', 'y'], ['a', 'b', 'a', 'b'], ['z', 'z']]
    expected = []
    '''
    list_of_lists = [['a', 'b', 'c', 'a', 'b', 'c'], ['z', 'y', 'x', 'x', 'z', 'y'], ['a', 'b', 'a', 'b'], ['z', 'z']]
    expected = []
    return do_func1_tests(list_of_lists, expected)

def do_func2_tests(L0, L1, expected):
    res = program.func2(L0, L1)
    testlib.check_val(res, expected)
    return 0.5

def test_func2_1(run=True):
    '''
    L0 = ['ab', 'o o']
    L1 = [2, 3]
    expected = "ababo oo oo o"
    '''
    L0 = ['ab', 'o o']
    L1 = [2, 3]
    expected = "ababo oo oo o"
    return do_func2_tests(L0, L1, expected)

def test_func2_2(run=True):
    '''
    L0 = ['quick', 'brow', 'fox']
    L1 = [2, 0, 2]
    expected = "quickquickfoxfox"
    '''
    L0 = ['quick', 'brow', 'fox']
    L1 = [2, 0, 2]
    expected = "quickquickfoxfox"
    return do_func2_tests(L0, L1, expected)

def test_func2_3(run=True):
    '''
    L0 = ['h', 'e', 'l', 'o']
    L1 = [1, 1, 2, 1]
    expected = "hello"
    '''
    L0 = ['h', 'e', 'l', 'o']
    L1 = [1, 1, 2, 1]
    expected = "hello"
    return do_func2_tests(L0, L1, expected)

def test_func2_4(run=True):
    '''
    L0 = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i']
    L1 = [0, 1, 2, 3, 4, 5, 6, 7, 8]
    expected = "bccdddeeeefffffgggggghhhhhhhiiiiiiii"
    '''
    L0 = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i']
    L1 = [0, 1, 2, 3, 4, 5, 6, 7, 8]
    expected = "bccdddeeeefffffgggggghhhhhhhiiiiiiii"
    return do_func2_tests(L0, L1, expected)


def do_func3_tests(file_in, expected):
    res = program.func3(file_in)
    testlib.check_val(res, expected)
    return 1


def test_func3_1(run=True):
    '''
    file_in = "func3/in1.txt"
    expected = 14
    '''
    file_in = "func3/in1.txt"
    expected = 14
    return do_func3_tests(file_in, expected)

def test_func3_2(run=True):
    '''
    file_in = "func3/in2.txt"
    expected = -9738
    '''
    file_in = "func3/in2.txt"
    expected = -9738
    return do_func3_tests(file_in, expected)

def test_func3_3(run=True):
    '''
    file_in = "func3/in3.txt"
    expected = 0
    '''
    file_in = "func3/in3.txt"
    expected = 0
    return do_func3_tests(file_in, expected)

def test_func3_4(run=True):
    '''
    file_in = "func3/in4.txt"
    expected = 1011
    '''
    file_in = "func3/in4.txt"
    expected = 1011
    return do_func3_tests(file_in, expected)

def do_func4_tests(dict_in, expected):
    res = program.func4(dict_in)
    testlib.check_list(res, expected)
    return 0.5


def test_func4_1(run=True):
    '''
    dict_in = {"f":(1, 2, 3), "a":["h", "w"], "c":{"f":3, "g":[1,2]}}
    expected = [["f", (1, 2, 3)], ["a", ["h", "w"]], ["c", {"f":3, "g":[1,2]}]]
    '''
    dict_in = {"f":(1, 2, 3), "a":["h", "w"], "c":{"f":3, "g":[1,2]}}
    expected = [["f", (1, 2, 3)], ["a", ["h", "w"]], ["c", {"f":3, "g":[1,2]}]]
    return do_func4_tests(dict_in, expected)

def test_func4_2(run=True):
    '''
    dict_in = {3: {'name': 'Steve', 'age': 25, 'marks': 60}, 2: {'name': 'Anil', 'age': 23, 'marks': 75}, 1: {'name': 'Asha', 'age': 20, 'marks': 70}}
    expected = [[1, {'name': 'Asha', 'age': 20, 'marks': 70}], [2, {'name': 'Anil', 'age': 23, 'marks': 75}], [3, {'name': 'Steve', 'age': 25, 'marks': 60}]]
    '''
    dict_in = {3: {'name': 'Steve', 'age': 25, 'marks': 60}, 2: {'name': 'Anil', 'age': 23, 'marks': 75}, 1: {'name': 'Asha', 'age': 20, 'marks': 70}}
    expected = [[1, {'name': 'Asha', 'age': 20, 'marks': 70}], [2, {'name': 'Anil', 'age': 23, 'marks': 75}], [3, {'name': 'Steve', 'age': 25, 'marks': 60}]]
    return do_func4_tests(dict_in, expected)


def test_func4_3(run=True):
    '''
    dict_in = {'A': {'Augusta', 'Arvada', 'Aurora', 'Albany', 'Arlington', 'Atlantic City', 'Allentown', 'Asheville', 'Atlanta', 'Akron', 'Alexandria', 'Antioch', 'Abilene', 'Anaheim', 'Ann Arbor', 'Athens', 'Appleton', 'Amarillo', 'Apple Valley', 'Aberdeen', 'Austin', 'Albuquerque', 'Anchorage'}, 'B': {'Baton Rouge', 'Boise City', 'Berkeley', 'Billings', 'Brighton', 'Beaumont', 'Bradenton', 'Burlington', 'Bel Air', 'Burbank', 'Birmingham', 'Bonita Springs', 'Barnstable', 'Baltimore', 'Buffalo', 'Brownsville', 'Boise', 'Boston', 'Bremerton', 'Bakersfield', 'Bethlehem', 'Bloomington', 'Boulder', 'Bridgeport', 'Bellevue', 'Bryan'}, 'C': {'Clearwater', 'Carrollton', 'Corona', 'Cambridge', 'Clarke County', 'Clarksville', 'Champaign', 'Chesapeake', 'Chula Vista', 'Charleston', 'Columbus', 'Corpus Christi', 'Cape Coral', 'Colorado Springs', 'Canton', 'Chandler', 'Chicago', 'Columbia', 'Cathedral City', 'Costa Mesa', 'Cleveland', 'Cincinnati', 'Concord', 'Coral Springs', 'Charlotte', 'Chattanooga', 'Cedar Rapids', 'College Station', 'Cary'}, 'D': {'Downey', 'Davidson County', 'Dayton', 'Dallas', 'Daly City', 'Davenport', 'Durham', 'Des Moines', 'Duluth', 'Detroit', 'Danbury', 'Deltona', 'Daytona Beach', 'Denver', 'Denton'}, 'E': {'Evansville', 'Erie', 'Escondido', 'El Monte', 'Elizabeth', 'El Paso', 'Elk Grove', 'Eugene', 'Elkhart'}, 'F': {'Fargo', 'Fort Wayne', 'Frederick', 'Fairfield', 'Fresno', 'Fontana', 'Fort Collins', 'Fitchburg', 'Fort Walton Beach', 'Fort Worth', 'Flint', 'Fort Smith', 'Fayetteville', 'Fort Lauderdale', 'Fullerton', 'Fremont'}, 'G': {'Green Bay', 'Grayslake', 'Gainesville', 'Garden Grove', 'Glendale', 'Grand Prairie', 'Grand Rapids', 'Gastonia', 'GreenBay', 'Greensboro', 'Greenville', 'Gilbert', 'Gulfport-Biloxi', 'Garland'}, 'H': {'Havre de Grace', 'Henderson', 'Hartford', 'Honolulu', 'Hemet', 'Hollywood', 'Hagerstown', 'Harrisburg', 'Houma', 'Hampton', 'Huntington Beach', 'High Point', 'Hayward', 'Hickory', 'Huntsville', 'Huntington', 'Howell', 'Hesperia', 'Harlingen', 'Houston', 'Hialeah'}, 'I': {'Irvine', 'Irving', 'Indianapolis', 'Independence', 'Inglewood'}, 'J': {'Jersey City', 'Jacksonville', 'Jefferson', 'Johnson City', 'Joliet', 'Jackson'}, 'K': {'Knoxville', 'Killeen', 'Kailua', 'Kalamazoo', 'Kaneohe', 'Kenosha', 'Kansas City', 'Kissimmee', 'Kennewick'}, 'L': {'Lafayette', 'Little Rock', 'Las Vegas', 'Long Beach', 'Laredo', 'Lacey', 'Lincoln', 'Lancaster', 'Lakeland', 'Lansing', 'Lubbock', 'Leominster', 'Lorain', 'Las Cruces', 'Lowell', 'Lakewood', 'Lexington', 'Louisville', 'Los Angeles', 'Lewisville', 'Layton', 'Lake Charles'}, 'M': {'Minneapolis', 'Merced', 'McAllen', 'Myrtle Beach', 'Manchester', 'Murrieta', 'Monroe', 'Macon', 'Miami', 'Medford', 'Madison', 'Mesquite', 'Memphis', 'Muskegon', 'Melbourne', 'Murfreesboro', 'Marina', 'Marysville', 'Montgomery', 'Mesa', 'McHenry', 'Milwaukee', 'Modesto', 'Monterey', 'Mission Viejo', 'Moreno Valley', 'Mobile', 'Miramar'}, 'N': {'New Haven', 'New Orleans', 'New London', 'Norwich', 'Newport News', 'Newburgh', 'North Las Vegas', 'North Charleston', 'New York', 'Naperville', 'Nashua', 'North Port', 'Nashville', 'Naples', 'Norwalk', 'Newark', 'New Bedford', 'New York City', 'Norman', 'Normal', 'Norfolk'}, 'O': {'Olathe', 'Ocala', 'Overland Park', 'Oceanside', 'Olympia', 'Odessa', 'Oxnard', 'Orange', 'Orem', 'Omaha', 'Orlando', 'Ontario', 'Ogden', 'Oakland', 'Oklahoma City'}, 'P': {'Panama City', 'Palm Springs', 'Port Arthur', 'Poughkeepsie', 'Portsmouth', 'Port Orange', 'Peoria', 'Pensacola', 'Palm Bay', 'Providence', 'Philadelphia', 'Plano', 'Pomona', 'Pueblo', 'Pembroke Pines', 'Phoenix', 'Provo', 'Punta Gorda', 'Pompano Beach', 'Pasadena', 'Paterson', 'Palmdale', 'Portland', 'Port Saint Lucie', 'Pittsburgh', 'Port St. Lucie'}, 'R': {'Richmond', 'Rockford', 'Raleigh', 'Richland', 'Redding', 'Reading', 'Reno', 'Riverside', 'Roseville', 'Roanoke', 'Round Lake Beach', 'Rancho Cucamonga', 'Rochester', 'Racine', 'Richmond County'}, 'S': {'Santa Barbara', 'Sterling Heights', 'Saint Petersburg', 'San Jose', 'Sioux Falls', 'Shreveport', 'Springdale', 'Santa Cruz', 'Salem', 'St. Petersburg', 'Seattle', 'St. Paul', 'Santa Maria', 'Simi Valley', 'Syracuse', 'Saginaw', 'Saint Paul', 'Sioux City', 'San Francisco', 'Spokane', 'Santa Rosa', 'San Diego', 'Sebastian', 'Springfield', 'Santa Clara', 'San Buenaventura', 'Stamford', 'Sacramento', 'Stockton', 'Sunnyvale', 'San Bernardino', 'Santa Clarita', 'Saint Louis', 'Spartanburg', 'San Antonio', 'St. Louis', 'Scranton', 'South Lyon', 'Salt Lake City', 'Sarasota', 'Savannah', 'Salinas', 'Santa Ana', 'South Bend', 'Scottsdale', 'Seaside'}, 'T': {'Tuscaloosa', 'Tacoma', 'Thousand Oaks', 'Topeka', 'Tucson', 'Temecula', 'Tampa', 'Thornton', 'Tallahassee', 'Tyler', 'Tulsa', 'Trenton', 'Tempe', 'Toledo', 'Torrance'}, 'U': {'Utica'}, 'V': {'Vallejo', 'Virginia Beach', 'Vero Beach', 'Vancouver', 'Visalia', 'Victorville'}, 'W': {'Waco', 'Waterbury', 'Warren', 'Washington', 'Worcester', 'Winston', 'Westminster', 'West Valley City', 'West Covina', 'Wilmington', 'Waterloo', 'Wichita', 'Winter Haven'}, 'Y': {'York', 'Yakima', 'Yonkers', 'Youngstown'}}
    expected = [['S', {'San Bernardino', 'Santa Ana', 'Springfield', 'Sioux City', 'South Lyon', 'Saginaw', 'Saint Paul', 'Seattle', 'Saint Louis', 'Scottsdale', 'Santa Rosa', 'Salem', 'Sacramento', 'Salinas', 'Shreveport', 'Salt Lake City', 'Sebastian', 'South Bend', 'St. Petersburg', 'San Diego', 'San Buenaventura', 'San Francisco', 'Sioux Falls', 'Santa Barbara', 'Savannah', 'Saint Petersburg', 'Spokane', 'Santa Clarita', 'San Jose', 'Santa Cruz', 'Santa Maria', 'San Antonio', 'Springdale', 'St. Louis', 'Stockton', 'Sunnyvale', 'Sarasota', 'Sterling Heights', 'Syracuse', 'Spartanburg', 'Stamford', 'Simi Valley', 'Scranton', 'St. Paul', 'Santa Clara', 'Seaside'}], ['C', {'Carrollton', 'Clarke County', 'Chandler', 'Cincinnati', 'Cedar Rapids', 'Cary', 'Cleveland', 'Columbia', 'Corpus Christi', 'Charlotte', 'Clearwater', 'Cambridge', 'Chattanooga', 'Clarksville', 'Chicago', 'College Station', 'Charleston', 'Chula Vista', 'Chesapeake', 'Canton', 'Colorado Springs', 'Costa Mesa', 'Cape Coral', 'Champaign', 'Coral Springs', 'Concord', 'Columbus', 'Corona', 'Cathedral City'}], ['M', {'Murfreesboro', 'Manchester', 'Merced', 'Mission Viejo', 'Montgomery', 'Murrieta', 'Miami', 'McAllen', 'Myrtle Beach', 'McHenry', 'Muskegon', 'Madison', 'Miramar', 'Minneapolis', 'Mobile', 'Milwaukee', 'Marina', 'Medford', 'Mesquite', 'Marysville', 'Monroe', 'Memphis', 'Monterey', 'Modesto', 'Melbourne', 'Macon', 'Moreno Valley', 'Mesa'}], ['B', {'Billings', 'Burbank', 'Bryan', 'Boise City', 'Bonita Springs', 'Brownsville', 'Beaumont', 'Baton Rouge', 'Bellevue', 'Burlington', 'Bremerton', 'Bridgeport', 'Brighton', 'Buffalo', 'Bloomington', 'Bakersfield', 'Berkeley', 'Baltimore', 'Boulder', 'Birmingham', 'Bradenton', 'Bethlehem', 'Boise', 'Boston', 'Bel Air', 'Barnstable'}], ['P', {'Port St. Lucie', 'Paterson', 'Pensacola', 'Port Saint Lucie', 'Plano', 'Port Orange', 'Panama City', 'Pueblo', 'Portland', 'Provo', 'Poughkeepsie', 'Palmdale', 'Pittsburgh', 'Peoria', 'Pomona', 'Port Arthur', 'Punta Gorda', 'Providence', 'Pompano Beach', 'Phoenix', 'Palm Bay', 'Philadelphia', 'Portsmouth', 'Palm Springs', 'Pembroke Pines', 'Pasadena'}], ['A', {'Antioch', 'Atlanta', 'Alexandria', 'Aurora', 'Albuquerque', 'Ann Arbor', 'Apple Valley', 'Athens', 'Abilene', 'Arvada', 'Akron', 'Allentown', 'Atlantic City', 'Arlington', 'Asheville', 'Anaheim', 'Austin', 'Aberdeen', 'Anchorage', 'Augusta', 'Appleton', 'Amarillo', 'Albany'}], ['L', {'Leominster', 'Lexington', 'Las Vegas', 'Louisville', 'Lewisville', 'Little Rock', 'Lowell', 'Lincoln', 'Lubbock', 'Laredo', 'Lakeland', 'Lorain', 'Lake Charles', 'Long Beach', 'Las Cruces', 'Lakewood', 'Lacey', 'Layton', 'Los Angeles', 'Lafayette', 'Lansing', 'Lancaster'}], ['H', {'Hickory', 'Harrisburg', 'Harlingen', 'Henderson', 'Hartford', 'Hialeah', 'Havre de Grace', 'Hayward', 'Huntington Beach', 'Honolulu', 'Hagerstown', 'Hampton', 'Hesperia', 'Houma', 'Houston', 'High Point', 'Huntington', 'Huntsville', 'Howell', 'Hemet', 'Hollywood'}], ['N', {'Nashua', 'New Bedford', 'New Haven', 'Nashville', 'Newark', 'North Charleston', 'New York City', 'Newport News', 'New York', 'Norwich', 'Norfolk', 'Norman', 'Naperville', 'New London', 'North Port', 'Norwalk', 'Normal', 'New Orleans', 'North Las Vegas', 'Naples', 'Newburgh'}], ['F', {'Fort Walton Beach', 'Fayetteville', 'Fairfield', 'Fremont', 'Fargo', 'Fort Smith', 'Frederick', 'Fort Collins', 'Flint', 'Fort Worth', 'Fitchburg', 'Fort Lauderdale', 'Fresno', 'Fullerton', 'Fontana', 'Fort Wayne'}], ['D', {'Daly City', 'Durham', 'Davenport', 'Dayton', 'Downey', 'Daytona Beach', 'Denton', 'Denver', 'Davidson County', 'Deltona', 'Danbury', 'Des Moines', 'Dallas', 'Detroit', 'Duluth'}], ['O', {'Oceanside', 'Orem', 'Ocala', 'Overland Park', 'Ogden', 'Omaha', 'Orange', 'Oakland', 'Oklahoma City', 'Oxnard', 'Odessa', 'Orlando', 'Olathe', 'Ontario', 'Olympia'}], ['R', {'Richland', 'Riverside', 'Rancho Cucamonga', 'Redding', 'Rochester', 'Round Lake Beach', 'Richmond County', 'Reading', 'Rockford', 'Roanoke', 'Richmond', 'Raleigh', 'Racine', 'Reno', 'Roseville'}], ['T', {'Tampa', 'Tucson', 'Tallahassee', 'Tyler', 'Trenton', 'Torrance', 'Tuscaloosa', 'Thornton', 'Temecula', 'Tacoma', 'Thousand Oaks', 'Tulsa', 'Toledo', 'Tempe', 'Topeka'}], ['G', {'Grand Prairie', 'Gulfport-Biloxi', 'Green Bay', 'Glendale', 'Gilbert', 'Gastonia', 'Garden Grove', 'GreenBay', 'Gainesville', 'Grayslake', 'Greenville', 'Garland', 'Grand Rapids', 'Greensboro'}], ['W', {'Waterbury', 'Waterloo', 'Waco', 'Warren', 'Worcester', 'Washington', 'Winston', 'Winter Haven', 'Wichita', 'Wilmington', 'Westminster', 'West Valley City', 'West Covina'}], ['E', {'El Paso', 'Escondido', 'Evansville', 'Elk Grove', 'Erie', 'El Monte', 'Elizabeth', 'Elkhart', 'Eugene'}], ['K', {'Knoxville', 'Kenosha', 'Kissimmee', 'Killeen', 'Kansas City', 'Kaneohe', 'Kalamazoo', 'Kailua', 'Kennewick'}], ['J', {'Joliet', 'Jacksonville', 'Jersey City', 'Jefferson', 'Jackson', 'Johnson City'}], ['V', {'Visalia', 'Victorville', 'Vallejo', 'Virginia Beach', 'Vancouver', 'Vero Beach'}], ['I', {'Irving', 'Independence', 'Irvine', 'Indianapolis', 'Inglewood'}], ['Y', {'Youngstown', 'York', 'Yonkers', 'Yakima'}], ['U', {'Utica'}]]
    '''
    cities = ["Aberdeen", "Abilene", "Akron", "Albany", "Albuquerque", "Alexandria", "Allentown", "Amarillo", "Anaheim", "Anchorage", "Ann Arbor", "Antioch", "Apple Valley", "Appleton", "Arlington", "Arvada", "Asheville", "Athens", "Atlanta", "Atlantic City", "Augusta", "Aurora", "Austin", "Bakersfield", "Baltimore", "Barnstable", "Baton Rouge", "Beaumont", "Bel Air", "Bellevue", "Berkeley", "Bethlehem", "Billings", "Birmingham", "Bloomington", "Boise", "Boise City", "Bonita Springs", "Boston", "Boulder", "Bradenton", "Bremerton", "Bridgeport", "Brighton", "Brownsville", "Bryan", "Buffalo", "Burbank", "Burlington", "Cambridge", "Canton", "Cape Coral", "Carrollton", "Cary", "Cathedral City", "Cedar Rapids", "Champaign", "Chandler", "Charleston", "Charlotte", "Chattanooga", "Chesapeake", "Chicago", "Chula Vista", "Cincinnati", "Clarke County", "Clarksville", "Clearwater", "Cleveland", "College Station", "Colorado Springs", "Columbia", "Columbus", "Concord", "Coral Springs", "Corona", "Corpus Christi", "Costa Mesa", "Dallas", "Daly City", "Danbury", "Davenport", "Davidson County", "Dayton", "Daytona Beach", "Deltona", "Denton", "Denver", "Des Moines", "Detroit", "Downey", "Duluth", "Durham", "El Monte", "El Paso", "Elizabeth", "Elk Grove", "Elkhart", "Erie", "Escondido", "Eugene", "Evansville", "Fairfield", "Fargo", "Fayetteville", "Fitchburg", "Flint", "Fontana", "Fort Collins", "Fort Lauderdale", "Fort Smith", "Fort Walton Beach", "Fort Wayne", "Fort Worth", "Frederick", "Fremont", "Fresno", "Fullerton", "Gainesville", "Garden Grove", "Garland", "Gastonia", "Gilbert", "Glendale", "Grand Prairie", "Grand Rapids", "Grayslake", "Green Bay", "GreenBay", "Greensboro", "Greenville", "Gulfport-Biloxi", "Hagerstown", "Hampton", "Harlingen", "Harrisburg", "Hartford", "Havre de Grace", "Hayward", "Hemet", "Henderson", "Hesperia", "Hialeah", "Hickory", "High Point", "Hollywood", "Honolulu", "Houma", "Houston", "Howell", "Huntington", "Huntington Beach", "Huntsville", "Independence", "Indianapolis", "Inglewood", "Irvine", "Irving", "Jackson", "Jacksonville", "Jefferson", "Jersey City", "Johnson City", "Joliet", "Kailua", "Kalamazoo", "Kaneohe", "Kansas City", "Kennewick", "Kenosha", "Killeen", "Kissimmee", "Knoxville", "Lacey", "Lafayette", "Lake Charles", "Lakeland", "Lakewood", "Lancaster", "Lansing", "Laredo", "Las Cruces", "Las Vegas", "Layton", "Leominster", "Lewisville", "Lexington", "Lincoln", "Little Rock", "Long Beach", "Lorain", "Los Angeles", "Louisville", "Lowell", "Lubbock", "Macon", "Madison", "Manchester", "Marina", "Marysville", "McAllen", "McHenry", "Medford", "Melbourne", "Memphis", "Merced", "Mesa", "Mesquite", "Miami", "Milwaukee", "Minneapolis", "Miramar", "Mission Viejo", "Mobile", "Modesto", "Monroe", "Monterey", "Montgomery", "Moreno Valley", "Murfreesboro", "Murrieta", "Muskegon", "Myrtle Beach", "Naperville", "Naples", "Nashua", "Nashville", "New Bedford", "New Haven", "New London", "New Orleans", "New York", "New York City", "Newark", "Newburgh", "Newport News", "Norfolk", "Normal", "Norman", "North Charleston", "North Las Vegas", "North Port", "Norwalk", "Norwich", "Oakland", "Ocala", "Oceanside", "Odessa", "Ogden", "Oklahoma City", "Olathe", "Olympia", "Omaha", "Ontario", "Orange", "Orem", "Orlando", "Overland Park", "Oxnard", "Palm Bay", "Palm Springs", "Palmdale", "Panama City", "Pasadena", "Paterson", "Pembroke Pines", "Pensacola", "Peoria", "Philadelphia", "Phoenix", "Pittsburgh", "Plano", "Pomona", "Pompano Beach", "Port Arthur", "Port Orange", "Port Saint Lucie", "Port St. Lucie", "Portland", "Portsmouth", "Poughkeepsie", "Providence", "Provo", "Pueblo", "Punta Gorda", "Racine", "Raleigh", "Rancho Cucamonga", "Reading", "Redding", "Reno", "Richland", "Richmond", "Richmond County", "Riverside", "Roanoke", "Rochester", "Rockford", "Roseville", "Round Lake Beach", "Sacramento", "Saginaw", "Saint Louis", "Saint Paul", "Saint Petersburg", "Salem", "Salinas", "Salt Lake City", "San Antonio", "San Bernardino", "San Buenaventura", "San Diego", "San Francisco", "San Jose", "Santa Ana", "Santa Barbara", "Santa Clara", "Santa Clarita", "Santa Cruz", "Santa Maria", "Santa Rosa", "Sarasota", "Savannah", "Scottsdale", "Scranton", "Seaside", "Seattle", "Sebastian", "Shreveport", "Simi Valley", "Sioux City", "Sioux Falls", "South Bend", "South Lyon", "Spartanburg", "Spokane", "Springdale", "Springfield", "St. Louis", "St. Paul", "St. Petersburg", "Stamford", "Sterling Heights", "Stockton", "Sunnyvale", "Syracuse", "Tacoma", "Tallahassee", "Tampa", "Temecula", "Tempe", "Thornton", "Thousand Oaks", "Toledo", "Topeka", "Torrance", "Trenton", "Tucson", "Tulsa", "Tuscaloosa", "Tyler", "Utica", "Vallejo", "Vancouver", "Vero Beach", "Victorville", "Virginia Beach", "Visalia", "Waco", "Warren", "Washington", "Waterbury", "Waterloo", "West Covina", "West Valley City", "Westminster", "Wichita", "Wilmington", "Winston", "Winter Haven", "Worcester", "Yakima", "Yonkers", "York", "Youngstown"]
    dict_in = {char: {city for city in cities if city.startswith(char)} for char in 'ABCDEFGHIJKLMNOPRSTUVWY'}
    expected = [['S', {'San Bernardino', 'Santa Ana', 'Springfield', 'Sioux City', 'South Lyon', 'Saginaw', 'Saint Paul', 'Seattle', 'Saint Louis', 'Scottsdale', 'Santa Rosa', 'Salem', 'Sacramento', 'Salinas', 'Shreveport', 'Salt Lake City', 'Sebastian', 'South Bend', 'St. Petersburg', 'San Diego', 'San Buenaventura', 'San Francisco', 'Sioux Falls', 'Santa Barbara', 'Savannah', 'Saint Petersburg', 'Spokane', 'Santa Clarita', 'San Jose', 'Santa Cruz', 'Santa Maria', 'San Antonio', 'Springdale', 'St. Louis', 'Stockton', 'Sunnyvale', 'Sarasota', 'Sterling Heights', 'Syracuse', 'Spartanburg', 'Stamford', 'Simi Valley', 'Scranton', 'St. Paul', 'Santa Clara', 'Seaside'}], ['C', {'Carrollton', 'Clarke County', 'Chandler', 'Cincinnati', 'Cedar Rapids', 'Cary', 'Cleveland', 'Columbia', 'Corpus Christi', 'Charlotte', 'Clearwater', 'Cambridge', 'Chattanooga', 'Clarksville', 'Chicago', 'College Station', 'Charleston', 'Chula Vista', 'Chesapeake', 'Canton', 'Colorado Springs', 'Costa Mesa', 'Cape Coral', 'Champaign', 'Coral Springs', 'Concord', 'Columbus', 'Corona', 'Cathedral City'}], ['M', {'Murfreesboro', 'Manchester', 'Merced', 'Mission Viejo', 'Montgomery', 'Murrieta', 'Miami', 'McAllen', 'Myrtle Beach', 'McHenry', 'Muskegon', 'Madison', 'Miramar', 'Minneapolis', 'Mobile', 'Milwaukee', 'Marina', 'Medford', 'Mesquite', 'Marysville', 'Monroe', 'Memphis', 'Monterey', 'Modesto', 'Melbourne', 'Macon', 'Moreno Valley', 'Mesa'}], ['B', {'Billings', 'Burbank', 'Bryan', 'Boise City', 'Bonita Springs', 'Brownsville', 'Beaumont', 'Baton Rouge', 'Bellevue', 'Burlington', 'Bremerton', 'Bridgeport', 'Brighton', 'Buffalo', 'Bloomington', 'Bakersfield', 'Berkeley', 'Baltimore', 'Boulder', 'Birmingham', 'Bradenton', 'Bethlehem', 'Boise', 'Boston', 'Bel Air', 'Barnstable'}], ['P', {'Port St. Lucie', 'Paterson', 'Pensacola', 'Port Saint Lucie', 'Plano', 'Port Orange', 'Panama City', 'Pueblo', 'Portland', 'Provo', 'Poughkeepsie', 'Palmdale', 'Pittsburgh', 'Peoria', 'Pomona', 'Port Arthur', 'Punta Gorda', 'Providence', 'Pompano Beach', 'Phoenix', 'Palm Bay', 'Philadelphia', 'Portsmouth', 'Palm Springs', 'Pembroke Pines', 'Pasadena'}], ['A', {'Antioch', 'Atlanta', 'Alexandria', 'Aurora', 'Albuquerque', 'Ann Arbor', 'Apple Valley', 'Athens', 'Abilene', 'Arvada', 'Akron', 'Allentown', 'Atlantic City', 'Arlington', 'Asheville', 'Anaheim', 'Austin', 'Aberdeen', 'Anchorage', 'Augusta', 'Appleton', 'Amarillo', 'Albany'}], ['L', {'Leominster', 'Lexington', 'Las Vegas', 'Louisville', 'Lewisville', 'Little Rock', 'Lowell', 'Lincoln', 'Lubbock', 'Laredo', 'Lakeland', 'Lorain', 'Lake Charles', 'Long Beach', 'Las Cruces', 'Lakewood', 'Lacey', 'Layton', 'Los Angeles', 'Lafayette', 'Lansing', 'Lancaster'}], ['H', {'Hickory', 'Harrisburg', 'Harlingen', 'Henderson', 'Hartford', 'Hialeah', 'Havre de Grace', 'Hayward', 'Huntington Beach', 'Honolulu', 'Hagerstown', 'Hampton', 'Hesperia', 'Houma', 'Houston', 'High Point', 'Huntington', 'Huntsville', 'Howell', 'Hemet', 'Hollywood'}], ['N', {'Nashua', 'New Bedford', 'New Haven', 'Nashville', 'Newark', 'North Charleston', 'New York City', 'Newport News', 'New York', 'Norwich', 'Norfolk', 'Norman', 'Naperville', 'New London', 'North Port', 'Norwalk', 'Normal', 'New Orleans', 'North Las Vegas', 'Naples', 'Newburgh'}], ['F', {'Fort Walton Beach', 'Fayetteville', 'Fairfield', 'Fremont', 'Fargo', 'Fort Smith', 'Frederick', 'Fort Collins', 'Flint', 'Fort Worth', 'Fitchburg', 'Fort Lauderdale', 'Fresno', 'Fullerton', 'Fontana', 'Fort Wayne'}], ['D', {'Daly City', 'Durham', 'Davenport', 'Dayton', 'Downey', 'Daytona Beach', 'Denton', 'Denver', 'Davidson County', 'Deltona', 'Danbury', 'Des Moines', 'Dallas', 'Detroit', 'Duluth'}], ['O', {'Oceanside', 'Orem', 'Ocala', 'Overland Park', 'Ogden', 'Omaha', 'Orange', 'Oakland', 'Oklahoma City', 'Oxnard', 'Odessa', 'Orlando', 'Olathe', 'Ontario', 'Olympia'}], ['R', {'Richland', 'Riverside', 'Rancho Cucamonga', 'Redding', 'Rochester', 'Round Lake Beach', 'Richmond County', 'Reading', 'Rockford', 'Roanoke', 'Richmond', 'Raleigh', 'Racine', 'Reno', 'Roseville'}], ['T', {'Tampa', 'Tucson', 'Tallahassee', 'Tyler', 'Trenton', 'Torrance', 'Tuscaloosa', 'Thornton', 'Temecula', 'Tacoma', 'Thousand Oaks', 'Tulsa', 'Toledo', 'Tempe', 'Topeka'}], ['G', {'Grand Prairie', 'Gulfport-Biloxi', 'Green Bay', 'Glendale', 'Gilbert', 'Gastonia', 'Garden Grove', 'GreenBay', 'Gainesville', 'Grayslake', 'Greenville', 'Garland', 'Grand Rapids', 'Greensboro'}], ['W', {'Waterbury', 'Waterloo', 'Waco', 'Warren', 'Worcester', 'Washington', 'Winston', 'Winter Haven', 'Wichita', 'Wilmington', 'Westminster', 'West Valley City', 'West Covina'}], ['E', {'El Paso', 'Escondido', 'Evansville', 'Elk Grove', 'Erie', 'El Monte', 'Elizabeth', 'Elkhart', 'Eugene'}], ['K', {'Knoxville', 'Kenosha', 'Kissimmee', 'Killeen', 'Kansas City', 'Kaneohe', 'Kalamazoo', 'Kailua', 'Kennewick'}], ['J', {'Joliet', 'Jacksonville', 'Jersey City', 'Jefferson', 'Jackson', 'Johnson City'}], ['V', {'Visalia', 'Victorville', 'Vallejo', 'Virginia Beach', 'Vancouver', 'Vero Beach'}], ['I', {'Irving', 'Independence', 'Irvine', 'Indianapolis', 'Inglewood'}], ['Y', {'Youngstown', 'York', 'Yonkers', 'Yakima'}], ['U', {'Utica'}]]
    return do_func4_tests(dict_in, expected)

def test_func4_4(run=True):
    '''
    dict_in = {'hp': {'name': ' Folio Elitebook 9470M', 'brand': 'HewlettPackard Laptop', 'price':30000},
            'lenovo': {'name': 'Camera 8989', 'brand': 'Lenovo Laptop', 'price':40000},
            'dell': {'name': 'Dell Inspiron', 'brand': 'Dell Laptop', 'price':200}}
    expected = [['dell', {'name': 'Dell Inspiron', 'brand': 'Dell Laptop', 'price': 200}], ['hp', {'name': ' Folio Elitebook 9470M', 'brand': 'HewlettPackard Laptop', 'price': 30000}], ['lenovo', {'name': 'Camera 8989', 'brand': 'Lenovo Laptop', 'price': 40000}]]
    '''
    dict_in = {'hp': {'name': ' Folio Elitebook 9470M', 'brand': 'HewlettPackard Laptop', 'price':30000},
            'lenovo': {'name': 'Camera 8989', 'brand': 'Lenovo Laptop', 'price':40000},
            'dell': {'name': 'Dell Inspiron', 'brand': 'Dell Laptop', 'price':200}}
    expected = [['dell', {'name': 'Dell Inspiron', 'brand': 'Dell Laptop', 'price': 200}], ['hp', {'name': ' Folio Elitebook 9470M', 'brand': 'HewlettPackard Laptop', 'price': 30000}], ['lenovo', {'name': 'Camera 8989', 'brand': 'Lenovo Laptop', 'price': 40000}]]
    return do_func4_tests(dict_in, expected)

def do_test_func5(ID, expected):
    img_in = f'func5/img{ID}_in.png'
    img_out = f'func5/img{ID}_out.png'
    img_exp = f'func5/img{ID}_exp.png'
    # remove the previous image each time if it is there
    if os.path.exists(img_out):
        os.remove(img_out)
    # now run

    res = program.func5(img_in, img_out)
    testlib.check_val(res, expected, f'''{'*'*50}\n[ERROR] Il numero di X e diamanti è sbagliato! / The number of Xs and diamonds is incorrect.\nReturned={res}, expected={expected}.\n{'*'*50}''')
    testlib.check_img_file(img_out, img_exp)
    return 2


def test_func5_1(run=True):
    '''
    imagefile = func5/img0_in.png
    output_imagefile = func5/img0_out.png
    '''
    ID = 0
    expected = (2, 3)
    return do_test_func5(ID, expected)


def test_func5_2(run=True):
    '''
    imagefile = func5/img1_in.png
    output_imagefile = func5/img1_out.png
    '''
    ID = 1
    expected = (2812, 2813)
    return do_test_func5(ID, expected)


def test_func5_3(run=True):
    '''
    imagefile = func5/img2_in.png
    output_imagefile = func5/img2_out.png
    '''
    ID = 2
    expected = (0, 22)
    return do_test_func5(ID, expected)


def test_func5_4(run=True):
    '''
    imagefile = func5/img3_in.png
    output_imagefile = func5/img3_out.png
    '''
    ID = 3
    expected = (1650, 289)
    return do_test_func5(ID, expected)

# ----------------------------------- EX.1 ----------------------------------- #
def do_test_ex1(L0, expected):
    if not DEBUG:
        try:
            isrecursive.decorate_module(program)
            program.ex1(L0)
        except isrecursive.RecursionDetectedError:
            pass
        else:
            raise Exception("The program does not employ recursion / Il programma non adotta un approccio ricorsivo")
        finally:
            isrecursive.undecorate_module(program)

    res = program.ex1(L0)
    testlib.check_list(res, expected)
    return 2

def test_ex1_1(run=True):
    '''
    L0 = [['0', '1'], ['0', '1'], ['0', '1'], ['0', '1']]
    expected = ['0000', '0001', '0010', '0011', '0100', '0101', '0110', '0111', '1000', '1001', '1010', '1011', '1100', '1101', '1110', '1111']
    '''
    L0 = [['0', '1'], ['0', '1'], ['0', '1'], ['0', '1']]
    expected = ['0000', '0001', '0010', '0011', '0100', '0101', '0110', '0111', '1000', '1001', '1010', '1011', '1100', '1101', '1110', '1111']
    return do_test_ex1(L0, expected)

def test_ex1_2(run=True):
    '''
    L0 = [['0', '1', '2', '3', '4', '5', '6', '7', '8', '9'], ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']]
    expected = ['00', '01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23', '24', '25', '26', '27', '28', '29', '30', '31', '32', '33', '34', '35', '36', '37', '38', '39', '40', '41', '42', '43', '44', '45', '46', '47', '48', '49', '50', '51', '52', '53', '54', '55', '56', '57', '58', '59', '60', '61', '62', '63', '64', '65', '66', '67', '68', '69', '70', '71', '72', '73', '74', '75', '76', '77', '78', '79', '80', '81', '82', '83', '84', '85', '86', '87', '88', '89', '90', '91', '92', '93', '94', '95', '96', '97', '98', '99']
    '''
    L0 = [['0', '1', '2', '3', '4', '5', '6', '7', '8', '9'], ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']]
    expected = ['00', '01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23', '24', '25', '26', '27', '28', '29', '30', '31', '32', '33', '34', '35', '36', '37', '38', '39', '40', '41', '42', '43', '44', '45', '46', '47', '48', '49', '50', '51', '52', '53', '54', '55', '56', '57', '58', '59', '60', '61', '62', '63', '64', '65', '66', '67', '68', '69', '70', '71', '72', '73', '74', '75', '76', '77', '78', '79', '80', '81', '82', '83', '84', '85', '86', '87', '88', '89', '90', '91', '92', '93', '94', '95', '96', '97', '98', '99']
    return do_test_ex1(L0, expected)


def test_ex1_3(run=True):
    '''
    L0 = [['0', '1', '2'], ['a', 'b', 'c'], ['0', '1', '2'], ['x', 'y', 'z']]
    expected = ['0a0x', '0a0y', '0a0z', '0a1x', '0a1y', '0a1z', '0a2x', '0a2y', '0a2z', '0b0x', '0b0y', '0b0z', '0b1x', '0b1y', '0b1z', '0b2x', '0b2y', '0b2z', '0c0x', '0c0y', '0c0z', '0c1x', '0c1y', '0c1z', '0c2x', '0c2y', '0c2z', '1a0x', '1a0y', '1a0z', '1a1x', '1a1y', '1a1z', '1a2x', '1a2y', '1a2z', '1b0x', '1b0y', '1b0z', '1b1x', '1b1y', '1b1z', '1b2x', '1b2y', '1b2z', '1c0x', '1c0y', '1c0z', '1c1x', '1c1y', '1c1z', '1c2x', '1c2y', '1c2z', '2a0x', '2a0y', '2a0z', '2a1x', '2a1y', '2a1z', '2a2x', '2a2y', '2a2z', '2b0x', '2b0y', '2b0z', '2b1x', '2b1y', '2b1z', '2b2x', '2b2y', '2b2z', '2c0x', '2c0y', '2c0z', '2c1x', '2c1y', '2c1z', '2c2x', '2c2y', '2c2z']
    '''
    L0 = [['0', '1', '2'], ['a', 'b', 'c'], ['0', '1', '2'], ['x', 'y', 'z']]
    expected = ['0a0x', '0a0y', '0a0z', '0a1x', '0a1y', '0a1z', '0a2x', '0a2y', '0a2z', '0b0x', '0b0y', '0b0z', '0b1x', '0b1y', '0b1z', '0b2x', '0b2y', '0b2z', '0c0x', '0c0y', '0c0z', '0c1x', '0c1y', '0c1z', '0c2x', '0c2y', '0c2z', '1a0x', '1a0y', '1a0z', '1a1x', '1a1y', '1a1z', '1a2x', '1a2y', '1a2z', '1b0x', '1b0y', '1b0z', '1b1x', '1b1y', '1b1z', '1b2x', '1b2y', '1b2z', '1c0x', '1c0y', '1c0z', '1c1x', '1c1y', '1c1z', '1c2x', '1c2y', '1c2z', '2a0x', '2a0y', '2a0z', '2a1x', '2a1y', '2a1z', '2a2x', '2a2y', '2a2z', '2b0x', '2b0y', '2b0z', '2b1x', '2b1y', '2b1z', '2b2x', '2b2y', '2b2z', '2c0x', '2c0y', '2c0z', '2c1x', '2c1y', '2c1z', '2c2x', '2c2y', '2c2z']
    return do_test_ex1(L0, expected)

# ----------------------------------- EX. 2----------------------------------- #


def do_ex2_test(root, expected, expected_tree):
    if not DEBUG:
        try:
            isrecursive.decorate_module(program)
            program.ex2(root)
        except isrecursive.RecursionDetectedError:
            pass
        else:
            raise Exception("The program does not employ recursion / Il programma non adotta un approccio ricorsivo")
        finally:
            isrecursive.undecorate_module(program)

    res = program.ex2(root)
    if res != expected:
        my_print(f'''{'*'*50}\n[ERROR]Il valore ritornato non è corretto! / The returned value is incorrect!!\nReturned={res}, expected={expected}''')
        return 0
    if root != expected_tree:
        my_print(f'''{'*'*50}\n[ERROR]L'albero non è corretto! / The tree is incorrect!!\nReturned={tree}, expected={expected_tree}''')
        return 0
    return 2


def test_ex2_1(run=True):
    '''
    root = tree.BinaryTree.fromList([1, [2, [4, None, None], None], [3, [5, [7, None, None], None], [6, None, None]]])
    expected = (4, 3)
    '''
    root = tree.BinaryTree.fromList([1, [2, [4, None, None], None], [3, [5, [7, None, None], None], [6, None, None]]])
    expected = (4, 3)
    expected_tree = tree.BinaryTree.fromList([28, [6, [4, None, None], None], [21, [12, [7, None, None], None], [6, None, None]]])
    return do_ex2_test(root, expected, expected_tree)

def test_ex2_2(run=True):
    '''
    root = tree.BinaryTree.fromList([4, [5, [18, [10, [5, None, None], None], [14, None, None]], [-10, [15, [15, None, None], None], [25, None, None]]], [14, None, [14, None, [26, None, None]]]])
    expected = (5, 8)
    '''
    root = tree.BinaryTree.fromList([4, [5, [18, [10, [5, None, None], None], [14, None, None]], [-10, [15, [15, None, None], None], [25, None, None]]], [14, None, [14, None, [26, None, None]]]])
    expected = (5, 8)
    expected_tree = tree.BinaryTree.fromList([155, [97, [47, [15, [5, None, None], None], [14, None, None]], [45, [30, [15, None, None], None], [25, None, None]]], [54, None, [40, None, [26, None, None]]]])
    return do_ex2_test(root, expected, expected_tree)


def test_ex2_3(run=True):
    '''
    root = tree.BinaryTree.fromList([-8, [23, [-8, [20, None, None], [-5, None, None]], [17, None, [-6, None, [-2, None, None]]]], [10, [14, None, None], [6, [4, None, [14, [30, None, None], None]], [19, None, None]]]])
    expected = (4, 11)
    '''
    root = tree.BinaryTree.fromList([-8, [23, [-8, [20, None, None], [-5, None, None]], [17, None, [-6, None, [-2, None, None]]]], [10, [14, None, None], [6, [4, None, [14, [30, None, None], None]], [19, None, None]]]])
    expected = (4, 11)
    expected_tree = tree.BinaryTree.fromList([128, [39, [7, [20, None, None], [-5, None, None]], [9, None, [-8, None, [-2, None, None]]]], [97, [14, None, None], [73, [48, None, [44, [30, None, None], None]], [19, None, None]]]])
    return do_ex2_test(root, expected, expected_tree)

def test_ex2_4(run=True):
    '''
    root = tree.BinaryTree.fromList([-1, [22, [1, [-6, [6, [-1, [-8, [16, None, None], [14, None, None]], None], [21, [8, None, [8, None, None]], [7, [20, None, None], [-9, None, None]]]], [1, [-6, [30, [16, None, None], [-3, None, None]], [29, None, [3, None, None]]], [-10, [4, None, [-4, None, None]], [-7, [6, None, None], [14, [30, [15, None, None], [22, None, None]], None]]]]], [-4, None, [-5, [1, [-4, None, None], [19, [10, None, None], None]], [-6, [15, None, [22, None, None]], [3, None, None]]]]], [14, [27, [10, [-2, [-1, [17, None, None], [-8, None, None]], None], [24, None, [28, [-1, [28, None, None], [29, [6, None, None], None]], [-9, [12, None, None], [2, None, None]]]]], [1, [0, [24, None, [20, None, None]], [0, [-10, [27, None, None], None], [-8, None, [14, None, None]]]], [-3, [25, [21, None, [-10, None, None]], [10, None, [17, [28, None, [17, None, None]], [-9, [1, None, None], None]]]], [-5, [23, [-3, None, None], None], None]]]], None]], None])
    expected = (35, 44)
    '''
    root = tree.BinaryTree.fromList([-1, [22, [1, [-6, [6, [-1, [-8, [16, None, None], [14, None, None]], None], [21, [8, None, [8, None, None]], [7, [20, None, None], [-9, None, None]]]], [1, [-6, [30, [16, None, None], [-3, None, None]], [29, None, [3, None, None]]], [-10, [4, None, [-4, None, None]], [-7, [6, None, None], [14, [30, [15, None, None], [22, None, None]], None]]]]], [-4, None, [-5, [1, [-4, None, None], [19, [10, None, None], None]], [-6, [15, None, [22, None, None]], [3, None, None]]]]], [14, [27, [10, [-2, [-1, [17, None, None], [-8, None, None]], None], [24, None, [28, [-1, [28, None, None], [29, [6, None, None], None]], [-9, [12, None, None], [2, None, None]]]]], [1, [0, [24, None, [20, None, None]], [0, [-10, [27, None, None], None], [-8, None, [14, None, None]]]], [-3, [25, [21, None, [-10, None, None]], [10, None, [17, [28, None, [17, None, None]], [-9, [1, None, None], None]]]], [-5, [23, [-3, None, None], None], None]]]], None]], None])
    expected = (35, 44)
    expected_tree = tree.BinaryTree.fromList([645, [646, [268, [216, [82, [21, [22, [16, None, None], [14, None, None]], None], [55, [16, None, [8, None, None]], [18, [20, None, None], [-9, None, None]]]], [140, [69, [43, [16, None, None], [-3, None, None]], [32, None, [3, None, None]]], [70, [0, None, [-4, None, None]], [80, [6, None, None], [81, [67, [15, None, None], [22, None, None]], None]]]]], [51, None, [55, [26, [-4, None, None], [29, [10, None, None], None]], [34, [37, None, [22, None, None]], [3, None, None]]]]], [356, [342, [135, [6, [8, [17, None, None], [-8, None, None]], None], [119, None, [95, [62, [28, None, None], [35, [6, None, None], None]], [5, [12, None, None], [2, None, None]]]]], [180, [67, [44, None, [20, None, None]], [23, [17, [27, None, None], None], [6, None, [14, None, None]]]], [112, [100, [11, None, [-10, None, None]], [64, None, [54, [45, None, [17, None, None]], [-8, [1, None, None], None]]]], [15, [20, [-3, None, None], None], None]]]], None]], None])
    return do_ex2_test(root, expected, expected_tree)


################################################################################

tests = [
    # TO RUN ONLY SOME OF THE TESTS, comment any of the following entries
    # PER DISATTIVARE ALCUNI TEST, commentare gli elementi seguenti
    test_func1_1, test_func1_2, test_func1_3, test_func1_4,
    test_func2_1, test_func2_2, test_func2_3, test_func2_4,
    test_func3_1, test_func3_2, test_func3_3, test_func3_4,
    test_func4_1, test_func4_2, test_func4_3, test_func4_4,
    test_func5_1, test_func5_2, test_func5_3, test_func5_4,
    test_ex1_1, test_ex1_2, test_ex1_3,
    test_ex2_1, test_ex2_2, test_ex2_3, test_ex2_4,
    test_personal_data_entry,
]


if __name__ == '__main__':
    if test_personal_data_entry() < 0:
        print(f"{COL['RED']}PERSONAL INFO MISSING. PLEASE FILL THE INITIAL VARS WITH YOUR NAME SURNAME AND STUDENT_ID{COL['RST']}")
        sys.exit()
    check_expected()
    testlib.runtests(   tests,
                        verbose=True,
                        logfile='grade.csv',
                        stack_trace=DEBUG)
    testlib.check_exam_constraints()
    if 'matricola' in program.__dict__:
        print(f"{COL['GREEN']}Nome: {program.nome}\nCognome: {program.cognome}\nMatricola: {program.matricola}{COL['RST']}")
    elif 'student_id' in program.__dict__:
        print(f"{COL['GREEN']}Name: {program.name}\nSurname: {program.surname}\nStudentID: {program.student_id}{COL['RST']}")
    else:
        print('we should not arrive here the  matricola/student ID variable is not present in program.py')
################################################################################
