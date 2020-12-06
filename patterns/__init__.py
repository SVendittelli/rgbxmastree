import os
import importlib

__globals = globals()

pattern_file_suffix = '_pattern.py'
suffix_length = len(pattern_file_suffix)
patterns = []

for file in os.listdir(os.path.dirname(__file__)):
    if file.endswith(pattern_file_suffix):
        mod_name = file[:-3]   # strip .py at the end
        __globals[mod_name] = importlib.import_module('.' + mod_name, package=__name__)
        patterns.append(file[:-suffix_length])

patterns.sort()
