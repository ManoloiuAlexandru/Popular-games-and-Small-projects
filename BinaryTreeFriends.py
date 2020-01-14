import random


class BinaryTree:
    def __init__(self, data):
        self.right = None
        self.left = None
        self.data = data

    def add_to_left(self, nod, data):
        if nod is None:
            nod = BinaryTree(data)
        elif nod.left is None:
            nod.left = BinaryTree(data)
        else:
            self.add_to_left(nod.left, data)

    def add_to_right(self, nod, data):
        if nod is None:
            nod = BinaryTree(data)
        elif nod.right is None:
            nod.right = BinaryTree(data)
        else:
            self.add_to_right(nod.right, data)

    def get_person_to_talk_to(self, person_who_talks):
        nod = person_who_talks
        person_to_talk_to = []
        while nod.left is not None:
            person_to_talk_to.append(nod.left.data)
            nod = nod.left
        return person_to_talk_to

    def get_person_that_talked(self, person_who_talks):
        nod = person_who_talks
        person_to_talk_to = []
        while nod.right is not None:
            person_to_talk_to.append(nod.right.data)
            nod = nod.right
        return person_to_talk_to

    def talk(self, person_who_talks):
        person_to_talk_to = self.get_person_to_talk_to(person_who_talks)
        person_talked_to = self.get_person_that_talked(person_who_talks)
        person_to_talk = random.choice(person_to_talk_to)
        print(person_who_talks.data, " will talk to ", person_to_talk)
        nod = BinaryTree(person_who_talks.data)

        for person in person_talked_to:
            nod.add_to_right(nod,person)
        for person in person_to_talk_to:
            if person == person_to_talk:
                nod.add_to_right(nod, person)
            else:
                nod.add_to_left(nod, person)
        return nod


if __name__ == '__main__':
    data_base = ["John", "Marie", "Andrew", "Michael", "Alexander"]
    binary_tree_of_data_base = []
    for data in range(0, len(data_base)):
        root = BinaryTree(data_base[data])
        for rest_of_data in range(0, len(data_base)):
            if data_base[rest_of_data] == data_base[data]:
                pass
            else:
                root.add_to_left(root, data_base[rest_of_data])
        binary_tree_of_data_base.append(root)

    for nr in range(0, len(binary_tree_of_data_base)):
        person = binary_tree_of_data_base[nr]
        print("------------------------")
        while len(person.get_person_to_talk_to(person)) > 0:
            person = person.talk(person)
        print("------------------------")
