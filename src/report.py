"""funciton to run if user choose to make a report on donor information"""

import os
import sys


# def clear_screen():
#     """Taken from the Treehouse shopping_list exercise."""
#     os.system("cls" if os.name == "nt" else "clear")


donors_info = {'Sam Wippy': [100000], 'Willy Wonka': [12, 13, 14], 'Garth Brooks': [1]}


def create_report():
"""function to make a table out of our dictionary by making a list for each row first"""
    title_row = ["Donor_Name", "Total_Donation", "Number_of_Donation", "Average_Donation"]
    donor_name = donor_info.keys()
    donation = donors_info.values()
    num_of_donation = [len(a) for a in donation]
    total_donation = [sum(a) for a in donation]
    average_donation = [sum(a)/len(a) for a in donation]


