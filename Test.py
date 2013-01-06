d = {}
#someList = []

class Person:
    def __init__(self, day, loc, time1, time2, name, course, livgroup, phone, email):
        self.day = day
        self.loc = loc
        self.time1 = time1
        self.time2 = time2
        self.name = name
        self.course = course
        self.livgroup = livgroup
        self.phone = phone
        self.email = email
        #someList.append(self)

        if (day,loc) in d:
            matchTime(self)
            d[(day,loc)].append((self))
        else:
            print "No match!"
            d[(day,loc)] = [self]

        #print f(someList)

    def __str__(self):
        return "A person named " + str(self.name)
    
    def display(self):
        print "Your name is " + str(self.name) + "and your phone is " + str(self.phone)

def matchTime(a):
    firstPrint = True
    match = False
    counter = 0
    for index,value in enumerate(d[(a.day,a.loc)]):
        if a.day == value.day:
            if (a.time1 < value.time1 and value.time1 < a.time2) or (a.time1 > value.time1 and a.time1 < value.time2):
                counter += 1
                match = True
                if firstPrint == True:
                    print "You're matched with: "
                print str(value.name) + ", Email: " + str(value.email) + ", Phone: " + str(value.phone) + ", Course: " + str(value.course) + ", Living Group: " + str(value.livgroup)
                firstPrint = False
    if match == True:
        print "You have " + str(counter) + " matche(s)!"
    else:
        print "No matches!"

"""
def f(a):
    userIndex = len(someList) - 1
    match = False
    for index, value in enumerate(someList):
        if index < userIndex:
            if value.day == someList[userIndex].day:
                if value.loc == someList[userIndex].loc:
                    print "You're matched with: " + str(value.name) + ", Email: " + str(value.email) + ", Phone: " + str(value.phone) + ", Course: " + str(value.course) + ", Living Group: " + str(value.livgroup)
                    match = True
        elif match == False:
            return "No match!"
        else:
            return ""
"""

def newUser():
    name = raw_input("Name: ")
    day = input("Day (in mmddyy): ")
    loc = raw_input("Location: ")
    time1 = input("Time from (in hhmm): ")
    time2 = input("Time to: ")
    course = raw_input("Course: ")
    livgroup = raw_input("Living Group: ")
    phone = raw_input("Phone: ")
    email = raw_input("Email: ")
    person = Person(day, loc, time1, time2, name, course, livgroup, phone, email)
    newMatch()
    
def newMatch():
    newUser()

newMatch()
