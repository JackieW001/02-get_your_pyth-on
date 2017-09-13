import random

CLASSES = {
    7: [ 'Helen', 'Shakil', 'Eric', 'Jennifer Y', 'Jennifer Z', 'Arif', 'Queenie', 'Jawadul', 'Shaina', 'Vivien', 'Brian', 'Naotaka', 'Bayan', 'Adam', 'Caleb', 'Terry', 'Jason', 'Alessandro', 'Samantha', 'Carol', 'Joyce', 'Shannon', 'Charles', 'Taylor', 'Kelly', 'Leo', 'Khyber', 'Ibnul', 'Eugene', 'Yuyang', 'Karina', 'Tiffany', 'Holden', 'Michael'],
    8: ['Masha', 'Adrian', 'David', 'Eric', 'Josh', 'Jerome', 'Henry', 'Jackie', 'Giorgio', 'Karen', 'Sonal', 'Xavier', 'Bermet', 'Alex', 'Iris', 'Manahal', 'Donia', 'Md', 'Connie', 'Lisa', 'Xing', 'Angelica', 'Angel', 'Augie', 'Dimitriy', 'Yiduo', 'Gordon', 'Tiffany', 'Clive', 'Jonathan', 'Sasha', 'Daniel'],
    9: [ 'Yu Qi', 'Michela', 'Kristin', 'Fabiha', 'Maxim', 'Marcus', 'Ish', 'James', 'Ryan', 'Edward', 'Adeeb', 'Jake', 'Cynthia', 'Kevin', 'Levi', 'Edmond', 'Kyle', 'Andrew', 'Max', 'Jenny', 'Philip', 'Shan', 'Mansour', 'Ray', 'Jake', 'Ida', 'Kerry', 'Stanley', 'Jackie', 'William', 'Tina', 'Michael']
}


def choose(class_period):
    class_list = CLASSES[class_period]
    length = len(class_list)
    index = random.randint(0, length-1)
    return str(class_period) + ": " + class_list[index] + "\n"

def chooseRandom():
    period = random.randint(7,9)
    return "random person - " + choose(period) + "\n"

def fightWinner():
    people = [choose(7), choose(8), choose(9)]
    ans = "your contestants are:\n"
    for x in people:
        ans += x + "\n"
    person = random.randint(0,2)
    return ans + "Your new champion out of the three periods is " + people[person] + "!!!"
    


print choose(7)
print choose(8)
print choose(9)

print chooseRandom()

print fightWinner()

i = 0
while i < 10:
    print chooseRandom()
    i+=1

