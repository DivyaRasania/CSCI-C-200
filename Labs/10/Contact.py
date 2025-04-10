class Contact:
    def __init__(self, nameList, phoneNumber, email, birthday):
        """
        Variables Sent:
            Name, Phone number, Email, Birthdate

        Create Instance variables:
            - First Name:   first
            - Middle Name:  middle
            - Last Name:    last
            - Phone Number: mobile
            - Email:        email
            - BirthDate:    birthdate
        """
        if len(nameList) == 3:
            self.firstName = nameList[0]
            self.middleName = nameList[1]
            self.lastName = nameList[2]
        elif len(nameList) == 2:
            self.firstName = nameList[0]
            self.middleName = ""
            self.lastName = nameList[1]
        else:
            self.firstName = ""
            self.middleName = ""
            self.lastName = ""
        self.phoneNumber = phoneNumber
        self.email = email
        self.birthday = birthday
        self.fullName = ""

    def getName(self):
        """
        Return the name as a string like this "first middle last"
        The middle name might not exist
        """
        if self.middleName:
            self.fullName = f"{self.firstName} {self.middleName} {self.lastName}"
        else:
            self.fullName = f"{self.firstName} {self.lastName}"
        
        return self.fullName

    def __str__(self):
        """
        Returns a string representing the contact:
        > Contact: Josh Baker - 3178675309
        """
        return f"Contact: {self.fullName} - ({self.phoneNumber})"

    def __repr__(self):
        """
        Provided: 
        - Feel free to read more about it here: https://stackoverflow.com/questions/1436703/difference-between-str-and-repr
        """
        return self.__str__() # This is provided. Helps with something printing a list of contact items.

    def call(self):
        """
        Print "Dialing ..." and then when they dont pick up
        the user should be prompted to input a message and then it should
        be printed
        """
        print(f"Dialing {self.firstName} ...")

    '''
    # Code from lab
    def sendText(self, message):
        """
        Given a message a text to the person
        """
        print(f'To {self.firstName}: "\t" {message}')

    def sendBirthdayText(self):
        """
        There should be a premade birthday text that uses the name 
        and then prints it out when this is called
        """
        self.sendText(f"Happy Birthday: {self.firstName}")
    '''

    def sendBirthdayText(self):
        """
        There should be a premade birthday text that uses the name 
        and then prints it out when this is called
        """
        print(f"To {self.firstName}:")
        print(f"\tHappy Birthday {self.firstName}!")
    
    def sendText(self, message):
        """
        Given a message a text to the person
        """
        print(f"You: {message}")

    def updateNumber(self, phoneNumber):
        """
        Take in a new phone number and replace the user's current phone number
        """
        self.phoneNumber = phoneNumber
        return self.phoneNumber