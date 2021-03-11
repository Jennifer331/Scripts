import configparser
import ast

config =configparser.ConfigParser()
config.read('config.txt')

epc = tuple(ast.literal_eval(config.get('SHOW', 'epc')))
f = ast.literal_eval(config.get('SHOW', 'f'))
print(type(epc))
print(epc, f)
