from cmd import Cmd
import json
#---------------------------------------------------------------------------------------------------------------
class BudgetItem:
  def __init__(self,price,date,category,description):
    self.price = price
    self.date = date
    self.category = category
    self.description = description 

  def dump(self):
    dump_dict = {"price":self.price, "date":self.date,"category":self.category,"description": self.description}
    return str(dump_dict) 

#---------------------------------------------------------------------------------------------------------------
class Database:
  def __init__(self,json_data):
    self.json_data = json_data
  
  def SaveData(self):
    with open('BudgetDB.json', 'w') as json_file:
      json_file.write(json.dumps(self.json_data, indent=2, sort_keys=True))

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

  def SaveItem(self,item, current_user):
    current_num_items = len(self.json_data[current_user].keys())
    next_item_num = current_num_items+1

    pair_key = 'item'+ next_item_num
    self.json_data[current_user][pair_key] = item
#----------------------------------------------------------------------------------------------------------------
class CmdPrompt(Cmd):
  def __init__(self):
    Cmd.__init__(self)
    self.database = Database({})
    self.current_user = ''
  prompt = 'Budget>>'
  intro = "Start by entering 'load' <your name>"


  def do_exit(self, inp):
    self.database.SaveData()
    print('Goodbye!')
    return True

  def help_exit(self):
    print("exit the app")

  def do_add_item(self, inp):
    inp = inp.split()

    item = {"name": inp[0], "date": inp[1], "category":inp[2], "decription":inp[3]}   

    self.database.AddItem(item, current_user) 
  
  def do_load(self, inp):
    self.database= Database.LoadData(inp)
    self.current_user = inp 
    print("welcome '{}'".format(inp))

#-----------------------------------------------------------------------------------------------------------------


