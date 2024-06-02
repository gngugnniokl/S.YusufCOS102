from abc import ABC, abstractmethod

class ClubGenie(ABC):
    @abstractmethod
    def fan_page(self):
        pass

class FC_Gronk(ClubGenie):
    def fan_page(self):
        print("Welcome to FC Gronk!")

class Madiba_FC(ClubGenie):
    def fan_page(self):
        print("Welcome to Madiba FC!")

class Blue_Army_FC(ClubGenie):
    def fan_page(self):
        print("Welcome to Blue Army FC!")

class TSG_Walker_FC(ClubGenie):
    def fan_page(self):
        print("Welcome to TSG Walker FC!")

def create_club_instance(club_name):
    clubs = {
        'FC Gronk': FC_Gronk,
        'Madiba FC': Madiba_FC,
        'Blue Army FC': Blue_Army_FC,
        'TSG Walker FC': TSG_Walker_FC
    }
    if club_name in clubs:
        club_instance = clubs[club_name]()  # Fix here
        club_instance.fan_page()
    else:
        print(f"No club found with the name: {club_name}")

club_name = input("Enter the name of the club you support: ")
create_club_instance(club_name)
