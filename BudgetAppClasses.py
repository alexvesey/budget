from cmd import Cmd

class BudgetItem:
  def __init__(self,price,date,category,description):
    self.price = price
    self.date = date
    self.category = category
    self.description = description 

  def dump(self):
    dump_dict = {"price":self.price, "date":self.date,"category":self.category,"description": self.description}
    return str(dump_dict) 

class CmdPrompt(Cmd):
  prompt = 'Budget>>'
  intro = "Welcome Alex"
  def do_exit(self, inp):
    print('bye')
    return True
  def help_exit(self):
    print("exit the app")

  def do_add_item(self, inp):
    print("Adding '{}'".format(inp))

