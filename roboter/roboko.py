"""
Roboko is a restaurant recommendation ROBOT
She can learn what kind of restaurant is popular
"""
import pandas as pd
import os
import pathlib
import csv

FILE_PATH = "recommend.csv"
FIELD_NAMES = ["NAME", "COUNT"]

def talk(func):
    def wrapper(*args, **kwargs):
        print("=" * 50)
        print("ROBOKO:")
        func(*args, **kwargs)
        print("-" * 50)
    return wrapper 

def input_customer():
    return input("Please input your answer : ")

class Roboko(object):
    @talk
    def __init__(self):
        print("Hello. My name is Roboko")
        if not os.path.exists(FILE_PATH):
            print('I\'m sorry, I have no data')
            pathlib.Path(FILE_PATH).touch()
            with open(FILE_PATH, "w", newline="") as recommend_file:
                writer = csv.DictWriter(recommend_file, fieldnames=FIELD_NAMES)
                writer.writeheader()
        self.restaurant_list = pd.read_csv(FILE_PATH)
        self.restaurant_list = self.restaurant_list.loc[:, ["NAME", "COUNT"]]
        self.restaurant_list.sort_values("COUNT")
        print(f"init : {self.restaurant_list}")

    @talk
    def customer_name_check(self):
        print("What is your name?")
        self.customer_name = input_customer()
        if self.customer_name == "":
            self.customer_name = "anonymous"

    @talk
    def say_goodbye(self):
        print("Thank you for your cooperation!")
        print(f"Good bye {self.customer_name}!!")
        print(f"current statistics result: ")
        print(self.restaurant_list)
        self.restaurant_list.to_csv(FILE_PATH)

    @talk
    def recommend(self):
        print(f"I have recommendation for you")
        for i in range(len(self.restaurant_list)):
            print(f'Do you like {self.restaurant_list["NAME"].iloc[i]}')
            answer = input_customer()
            if answer in ["y", "yes", "Yes"]:
                print("Good!")
                print(f"I remember you like {self.restaurant_list['NAME'].iloc[i]}!!")
                self.restaurant_list["COUNT"].iloc[i] += 1
                break

    @talk
    def hearing(self):
        print("So, do you have any recommendations?")
        restaurant_name = input_customer().capitalize()
        temp_restaurant = pd.Series([restaurant_name, 1], index=["NAME", "COUNT"], name=len(self.restaurant_list))
        self.restaurant_list = self.restaurant_list.append(temp_restaurant)
        print(self.restaurant_list)