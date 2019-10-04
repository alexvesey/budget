from BudgetAppClasses import BudgetItem

def main():
  b1 = BudgetItem( 50, "10/3/19", "food", "fish")

  print(b1.dump())


if __name__ == "__main__":
  main()

