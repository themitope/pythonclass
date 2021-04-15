# balance = 0
# new_balance = 0
class Budget:
    def __init__(self, categories):
        self.categories = categories

    def deposit(self, category, amount):
        self.categories[category]["balance"] += amount
        # new_balance += amount
        print("You have successfully deposited %d for %s \n Your new balance is %d" % (amount, category, self.categories[category]["balance"]))

    def withdraw(self, category, amount):
        if(amount > self.categories[category]["balance"]):
            print("Insufficient Balance! Please make a deposit and try again")
        else:
            self.categories[category]["balance"] -= amount
            print("You have successfully withdrawn %d from %s \n Your new balance is %d" % (amount, category, self.categories[category]["balance"]))

    def compute_balance(self, category):
        print("Your balance is %d " % self.categories[category]["balance"])
    
    def transfer_amount(self, transfer_from, transfer_to, amount):
        if(self.categories[transfer_from]["balance"] < amount):
            print("You do not have enough balance for this transaction")
        else:
            if (transfer_to in self.categories):
                self.categories[transfer_from]["balance"]-= amount
                self.categories[transfer_to]["balance"] += amount
                print("You have successfully transfered %d from %s to %s" % (amount, transfer_from, transfer_to))
            else:
               print("Category you are transfering to does not exist") 


new_budget = Budget({
    "Food": {
        "balance": 0
    }, 
    "Clothing": {
        "balance": 0
    }, 
    "Entertainment": {
        "balance": 0
    },
})
new_budget.deposit("Food", 5000)
new_budget.deposit("Clothing", 10000)
new_budget.deposit("Entertainment", 15000)
new_budget.withdraw("Food", 3000)
new_budget.withdraw("Clothing", 5000)
new_budget.withdraw("Entertainment", 10000)
new_budget.compute_balance("Food")
new_budget.compute_balance("Clothing")
new_budget.compute_balance("Entertainment")
new_budget.transfer_amount("Food", "Clothing", 1000)