class Category:
   
    def __init__(self, category):
        self.category = category
        self.ledger = []
        

    def __str__(self):
        # Using a formatted string to center the category name within a 30-character line
        output_string = f'{self.category:*^30}\n'
        total = 0

        for item in self.ledger:
            # Properly format each line with description and amount
            description = item["description"][:23]
            amount = item["amount"]
            output_string += f'{description:<23}{amount:>7.2f}\n'
            total += amount
                
        output_string += f'Total: {total:.2f}'
        return output_string
    #method deposit    
    def deposit(self, amount, description = ""):
        ledger = self.ledger
        ledger.append({'amount': amount, 'description': description})
       
    #method withdraw
    def withdraw(self, amount, description = ""):
        ledger = self.ledger
        if self.check_funds(amount): 
            ledger.append({'amount': -1 * amount, 'description': description})
            return True
        else:
            return False

    #method get spent money
    def get_spent(self):
        ledger = self.ledger
        spend = sum (
                items['amount'] for items in ledger if items['amount'] < 0
            )
        
        return round(spend * -1, 2)
    #method get balance
    def get_balance(self):
        ledger= self.ledger
        total =0
        for items in ledger:
            total += items['amount']
        return total
    #method transfer
    def transfer(self, amount, aim_category):
        ledger = self.ledger
        category= aim_category.category
        
        if self.check_funds(amount):
            ledger.append({'amount': -1 * amount, 'description': f'Transfer to {category}'}) 
            aim_category.deposit(amount, f'Transfer from {self.category}')
            return True
        else:
            return False
            


    def check_funds(self, amount):
        
        if amount <= self.get_balance():
            return True
        else:
            return False


def create_spend_chart(categories):
   
    total_spent = sum(category.get_spent() for category in categories)
    percentages = [category.get_spent() / total_spent * 100 for category in categories]


    chart = "Percentage spent by category\n"


    for i in range(100, -1, -10):
        chart += f"{i:>3}| "
        for percentage in percentages:
            chart += "o  " if percentage >= i else "   "
        chart += "\n"

   
    chart += "    " + "-" * (3 * len(categories) + 1) + "\n"

    
    max_len = max(len(category.category) for category in categories)

    
    for i in range(max_len):
        chart += "     "
        for category in categories:
            if i < len(category.category):
                chart += category.category[i] + "  "
            else:
                chart += "   "
        chart += "\n"

    # Return the completed chart, stripping the last newline
    return chart.rstrip("\n")
       
    




# food = Category('Food')
# food.deposit(1000, 'deposit')
# food.withdraw(10.15, 'groceries')
# food.withdraw(15.89, 'restaurant and more food for dessert')
# clothing = Category('Clothing')
# food.transfer(50, clothing)
# clothing.withdraw(10.15, 'skirt')
# auto = Category('Auto')
# auto.withdraw(18.15, 'car')
# print(food)

# print(clothing)
# print(create_spend_chart([food, clothing, auto]))







    



