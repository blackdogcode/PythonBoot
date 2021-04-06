import random

if __name__ == "__main__":
    people = 'Angela, Ben, Jenny, Michael, Chloe'
    people = people.split(", ")
    random.shuffle(people)
    person = people[0]
    print(f'{person} is going to buy the meal today!')

