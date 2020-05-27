numbers = [234, 123, 712, 98, 234]
import Utils  # Utils is another python module with pre-defined functions
from Utils import find_max

find_max(numbers)  # If we only import a specific function from another module, we dont have to prefix it with the name

Utils.find_max(numbers)  # Compare it if we import the whole module, anything must be prefix
