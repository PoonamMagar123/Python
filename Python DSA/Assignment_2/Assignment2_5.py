
# 5. Define a class Team with instance object variable a list of team member names. 
# Provide methods to input member names and display member names.

class Team:
    def __init__(self):
        self.members = []  # Initialize an empty list to store team member names
    
    def inputMembers(self):
        # Method to input member names into the team
        num_members = int(input("Enter the number of team members: "))
        for _ in range(num_members):
            member_name = input("Enter team member name: ")
            self.members.append(member_name)
    
    def displayMembers(self):
        # Method to display member names in the team
        print("Team Members: ")
        for member in self.members:
            print(member)

def main():
    # Creating a Team object
    team1 = Team()
    
    # Inputting and displaying team member names
    team1.inputMembers()
    team1.displayMembers()

if __name__ == "__main__":
    main()

# The Team class has an instance variable members initialized as an empty list in the constructor.
# The inputMembers method allows you to input member names into the team.
# It asks for the number of team members and then prompts for each member's name, adding them to the members list.
# The displayMembers method displays the member names stored in the members list.