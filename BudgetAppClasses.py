from cmd import Cmd
import pandas as pd
import pdb
#---------------------------------------------------------------------------------------------------------------
class BudgetItem:
  def __init__(self,):
    self.user = ''
    self.item_name = ''
    self.price = ''
    self.date = ''
    self.category = ''
    self.description = ''

  def to_str(self):
    dump_str = self.user+" "+self.item_name+" "+self.price+" "+self.date +" "+self.category+" "+self.description
    return dump_str

  def from_str(self,string_in):
    split = string_in.split(',')
    self.item_name = split[0]
    self.price = split[1]
    self.date = split[2]
    self.category = split[3]
    self.description = split[4]
    self.user = split[5]

#---------------------------------------------------------------------------------------------------------------
class Database:
  def __init__(self):
    self.data_frame = pd.DataFrame()
  
  def SaveToFile(self):
    with open('BudgetDB.csv', 'w') as out_file:
      self.data_frame.to_csv(out_file, index= False)

  def LoadFromFile(self):
    try:
        self.data_frame = pd.read_csv('BudgetDB.csv') 
        return self.data_frame
    except:
      print("No DB yet setup, creating new DB")
      col_names = ["User","Item Name","Price","Date of Purchase","Budget Category","Description"]
      self.data_frame = pd.DataFrame(columns= col_names)
      return self.data_frame

  def SaveItem(self,bi):
    self.data_frame = self.data_frame.append({'User': bi.user, 'Item Name':bi.item_name, 'Price': \
                                              bi.price, 'Date of Purchace': bi.date, 'Budget Category': \
                                              bi.category, 'Description': bi.description}, ignore_index = True)
#----------------------------------------------------------------------------------------------------------------
class CmdPrompt(Cmd):
  def __init__(self):
    Cmd.__init__(self)
    self.database = Database()
    self.current_user = ''
  prompt = 'Budget>>'
  intro = "Start by entering 'load' <your name>"

  def do_exit(self, inp):
    self.database.SaveToFile()
    print('Goodbye!')
    return True

  def do_load(self, inp):
    self.database= Database()
    self.database.LoadFromFile()
    self.current_user = inp 
    print("welcome '{}'".format(inp))

  def do_add(self, inp):
    budget_item = BudgetItem()
    inp = inp+","+self.current_user
    budget_item.from_str(inp)
    self.database.SaveItem(budget_item)
#-----------------------------------------------------------------------------------------------------------------


