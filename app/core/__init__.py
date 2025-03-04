import os

from ..common.utils import read_properties_file

sql_scripts = read_properties_file(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'mysql/sql.properties'))

from .mysql import *
