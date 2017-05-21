"""funciton to run if user choose to make a report on donor information"""


donors_info = {'Sam Wippy': [100000], 'Willy Wonka': [12, 13, 14], 'Garth Brooks': [1]}


def create_report():
"""making a list for each column from dict data then populate row data into a table"""
    title_row = ["Donor_Name", "Total_Donation", "Number_of_Donation", "Average_Donation"]
    donor_name = donors_info.keys()
    donation = donors_info.values()
    num_of_donation = [str(len(a)) for a in donation]
    total_donation = [str(sum(a)) for a in donation]
    average_donation = [str(sum(a)/len(a)) for a in donation]
    for row in zip(donor_name, total_donation, num_of_donation, average_donation):
        print ', '.join(row)




