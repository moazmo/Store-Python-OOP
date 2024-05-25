store_items = [
    ['iphone 13', 900, 60],
    ['iphone 14', 1000, 60],
    ['Macbook Air', 1500, 25],
    ['Macbook Pro', 2000, 35],
    ['Airpods Pro', 950, 22],
    ['Ipad Pro', 1100, 15],
    ['Apple Watch S7', 600, 33]]

massage = """Available Items:
1.View Available Items
2.View Chart
3.Clear Cart
4.Quit
"""

class Online_store:
    item_number = 1
    def __init__(self, name, price, quantity):
        self.number = Online_store.item_number
        self.name = name
        self.price = price
        self.quantity = quantity
        Online_store.item_number += 1
    def __str__(self):
        return f"{self.number}: {self.name} {self.price}$ ... {self.quantity} unit"
    def item_details(self):
        return f"you picked {self.name}\nthe price : {self.price}$\nonly {self.quantity} unit available"

class Store:
    def __init__(self):
        self.items = [Online_store(store_items[i][0], store_items[i][1], store_items[i][2]) for i in range(len(store_items))]
        self.massage = massage
        self.chart = []
    def check(self, my_input, my_list):
        try:
            if int(my_input) in my_list:
                return input
            else:
                print("Wrong number", "try again", "_"*20, sep="\n")
        except:
            print("must be number", "try again", "_"*20, sep="\n")
    def check_quantity(self, my_input, my_list):
        try:
            if int(my_input) in my_list:
                return input
            else:
                print("not enough amount", "try again", "_"*20, sep="\n")
        except:
            print("must be number", "try again", "_"*20, sep="\n")
    def main_windows(self):
        while True:
            print("-"*40)
            print(self.massage, "-"*30, sep="\n")
            main_choice = input("Enter the number of your choice :")
            if self.check(main_choice, [1, 2, 3, 4]):
                if main_choice == "1":
                    self.my_items_list()
                if main_choice == "2":
                    self.view_chart()
                if main_choice == "3":
                    self.chart.clear()
                    print("your chart successfully cleared")
                if main_choice == "4":
                    print("thanks your for your visit","we wish see you soon",sep="\n")
                    break
    def my_items_list(self):
        while True :
            print("_"*30)
            for item in self.items:
                print(item.__str__())
            print("_" * 30)
            choice = input(" press number of item to buy.....press 0 to back :")
            if self.check(choice, [0, 1, 2, 3, 4, 5, 6, 7]):
                if choice == "0":
                    self.main_windows()
                else:
                    self.check_quantity_confirm(choice)
    def check_quantity_confirm(self, choice):
        while True:
            for item in self.items:
                if item.number == int(choice):
                    print(item.item_details())
                    print("press 0 to back")
                    quantity = input("enter quantity :")
                    if quantity == "0":
                        self.my_items_list()
                    if self.check_quantity(quantity,range(1,item.quantity+1)):
                        self.add_to_chart(choice,quantity,item.name)
                    else:
                        self.my_items_list()
    def add_to_chart(self,items_no, quantity,item_name):
        chart_items = [items_name[0] for items_name in self.chart]
        for item in self.items:
            if item.number == int(items_no):
                if item.name not in chart_items:
                    item.quantity -= int(quantity)
                    self.chart.append([item.name,int(quantity),int(item.price)])
                    print(f"{item_name} successfully added to your chart ")
                    self.my_items_list()
                else:
                    for item in self.chart:
                        if item[0] == item_name:
                            item[1] += int(quantity)
                            print(f"{item_name} add again successfully")
                            self.my_items_list()
    def view_chart(self):
        if self.chart:
            print(". . . . .chart. . . . . .")
            print("unite name        ","units","          price")
            total_chart_price = []
            for no, item in enumerate(self.chart,1):
                total = item[1]*item[2]
                total_chart_price.append(total)
                print(f"{no}.{item[0]} ...{item[1]}/unit....{item[2]}$/unit...total {total}$   ")
            print("\n")
            print(f"TOTAL CHART PRICE :   {sum(total_chart_price)}$")
        else:
            print("SORRY...yours chart is empty")
mystore = Store()
mystore.main_windows()




