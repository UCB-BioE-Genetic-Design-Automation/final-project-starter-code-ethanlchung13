from composition.model.Box import Box
from composition.model.Sample import Sample


class Inventory:

    def __init__(self):
        self.boxes = {}

    # Creates a new box and adds it to the inventories list of boxes
    def add_new_box(self, name: str, description: str, room: str):
        box = Box(name, description, room)
        self.boxes[name] = box

    # Remove a box from the inventory
    def remove_box(self, name: str):
        del self.boxes[name]

    # Returns the box with the specified name from the inventory
    def get_box(self, name: str):
        box = self.boxes[name]
        return box

    # Returns the samples of the specified box
    def get_box_samples(self, name: str):
        box = self.boxes[name]
        return box.samples

    # Returns the description of the specified box
    def get_box_description(self, name: str):
        box = self.boxes[name]
        return box.description

    # Returns the location of the specified box
    def get_box_location(self, name: str):
        box = self.boxes[name]
        return box.location

    # Changes the description of the specified box
    def change_box_description(self, name: str, desc: str):
        box = self.boxes[name]
        box.description = desc

    # Changes the room location of the specified box
    def change_box_location(self, name: str, loc: str):
        box = self.boxes[name]
        box.location = loc

    # Reads in a tab separated file/text file and creates a Box object with Samples that are created from the data
    def read_tsv(self, file_path: str):

        with open(file_path, 'r') as tsv_file:
            lines = tsv_file.readlines()

        # Extract box information from the first three lines
        box_name = lines[0].split('\t')[1].strip()
        box_description = lines[1].split('\t')[1].strip()
        box_room = lines[2].split('\t')[1].strip()

        self.add_new_box(name=box_name, description=box_description, room=box_room)
        new_box = self.get_box(box_name)

        # Create 2D arrays to store the data from the file
        constructs = [[None for _ in range(9)] for _ in range(9)]
        concentrations = [[None for _ in range(9)] for _ in range(9)]
        culture = [[None for _ in range(9)] for _ in range(9)]

        # Iterate through and store the constructs data
        for i in range(9):
            row = lines[27 + i].split('\t')
            row = row[1:len(row) + 1]
            for r in range(9):
                if '\n' in row[r]:
                    row[r] = row[r][:len(row[r]) - 1]
                constructs[i][r] = row[r]

        # Iterate through and store the concentrations data
        for i in range(9):
            row = lines[38 + i].split('\t')
            row = row[1:len(row) + 1]
            for r in range(9):
                if '\n' in row[r]:
                    row[r] = row[r][:len(row[r]) - 1]
                concentrations[i][r] = row[r]

        # Iterate through and store the culture data
        for i in range(9):
            row = lines[49 + i].split('\t')
            row = row[1:len(row) + 1]
            for r in range(9):
                if '\n' in row[r]:
                    row[r] = row[r][:len(row[r]) - 1]
                culture[i][r] = row[r]

        # Create a sample using the corresponding data from constructs, concentrations, and culture
        # Store each of the samples in the box at the index it was found
        alphabet = {1: "A", 2: "B", 3: "C", 4: "D", 5: "E", 6: "F", 7: "G", 8: "H", 9: "I"}
        for i in range(9):
            for j in range(9):
                new_box.add_sample(Sample(constructs[j][i], concentrations[j][i], culture[j][i]), alphabet[i + 1], j)

    # Creates a tsv file for each box in the inventory
    # Main functionality of creating a tsv file is in the box object
    def create_tsv(self):
        for b in self.boxes:
            b.create_tsv(b.name)

