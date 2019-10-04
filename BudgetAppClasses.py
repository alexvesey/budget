from cmd import Cmd
import json

class BudgetItem:
  def __init__(self,price,date,category,description):
    self.price = price
    self.date = date
    self.category = category
    self.description = description 

  def dump(self):
    dump_dict = {"price":self.price, "date":self.date,"category":self.category,"description": self.description}
    return str(dump_dict) 

class Database:
  def __init__(self,json_data):
    self.json_data = json_data
    self.current_user = ''

  def SetCurrentUser(self, name):
    self.current_user = name

class CmdPrompt(Cmd):
  prompt = 'Budget>>'
  intro = "Start by entering 'load' <your name>"
  def do_exit(self, inp):
    print('bye')
    return True
  def help_exit(self):
    print("exit the app")

  def do_add_item(self, inp):
    

  def do_load(self, inp):
    database = LoadData(inp)
    database.SetCurrentUser(inp)
    print("welcome '{}'".format(inp))


def SaveData(json_data):
    with open('BudgetDB.json', 'w') as json_file:
      json_file.write(json.dumps(json_data, indent=2, sort_keys=True))

def LoadData(name):

  try:
    with open('BudgetDB.json', 'w') as json_file:
      db = Database(json.load(json_file))
      db.SetCurrentUser(name)
      return db
  except:
    print("No DB yet setup, creating new DB")
    db = Database({name:{}})
    return db
