class BudgetItem:
  def __init__(self,price,date,category,description):
    self.price = price
    self.date = date
    self.category = category
    self.description = description 

  def dump(self):
    dump_dict = {"price":self.price, "date":self.date,"category":self.category,"description": self.description}
    return str(dump_dict) 
