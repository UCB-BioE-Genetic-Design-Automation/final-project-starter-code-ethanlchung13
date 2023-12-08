from composition.model.Sample import Sample


class Box:

    def __init__(self, name: str, description: str, room: str):
        self.name = name
        self.description = description
        self.room = room
        self.samples = {}

    # Returns description of box instance
    def get_description(self):
        return self.description

    # Returns room location where the box instance is stored
    def get_room(self):
        return self.room

    # Adds a specified sample object to the box at a user specified row and column
    # Rows are represented by letters A-I, and Columns are represented by numbers 1-9
    def add_sample(self, sample: Sample, row: str, col: int):
        if row.upper() not in "ABCDEFGHI" or col not in range(1, 10):
            return "Invalid row or column values."

        index = f"{row.upper()}{col}"
        self.samples[index] = sample
        sample.location = self.room + "/" + self.name + "/" + index

    # Adds a specified sample object without a specified row and column
    # If the user prefers to array samples moving down and then right, they can use this function
    def add_sample_orderly(self, sample: Sample):
        for row in "ABCDEFGHI":
            for col in range(1, 10):
                index = f"{row}{col}"
                if index not in self.samples.keys():
                    self.samples[index] = sample
                    sample.location = self.room + "/" + self.name + "/" + index
                    return
        return "This box is already full."

    # Returns the sample at a given row and column
    def get_sample(self, row: str, col: int):
        index = f"{row.upper()}{col}"
        if index not in self.samples.keys():
            return "There is no sample at index " + index + " in box " + self.name
        return self.samples[index]

    # Moves a sample at a specified index to a new row and column location
    # Updates the location metadata of the sample
    def move_sample(self, index: str, new_row: str, new_col: int):
        if index not in self.samples.keys():
            return "Sample is not in this box."

        sample = self.samples[index]
        new_index = f"{new_row.upper()}{new_col}"
        if new_index not in self.samples.keys():
            self.samples[new_index] = sample
            del self.samples[index]
            sample.location = self.room + "/" + self.name + "/" + new_index
        else:
            return "New location is already occupied."

    # Removes the sample from a given index
    def remove_sample(self, index: str):
        if index not in self.samples.keys():
            return "No sample is at this index."
        self.samples[index].location = None
        del self.samples[index]
        return

    # Creates a tsv file from the box data
    def create_tsv(self, file_name: str):
        with open(file_name, 'w') as tsv_file:
            # Write box information
            tsv_file.write(f"name\t{self.name}\n")
            tsv_file.write(f"description\t{self.description}\n")
            tsv_file.write(f"room\t{self.room}\n\n")

            # Write headers for the samples
            tsv_file.write("label\t1\t2\t3\t4\t5\t6\t7\t8\t9\n")

            # Write sample data
            for row in "ABCDEFGHI":
                tsv_file.write(row + "\t")
                for col in range(1, 10):
                    index = f"{row}{col}"
                    if index in self.samples:
                        sample = self.samples[index]
                        tsv_file.write(f"{sample.label} {sample.concentration}\t")
                    else:
                        tsv_file.write("\t")
                tsv_file.write("\n")

            tsv_file.write("\n")

            # Write headers for side labels
            tsv_file.write("side_label\t1\t2\t3\t4\t5\t6\t7\t8\t9\n")

            # Write side label data
            for row in "ABCDEFGHI":
                tsv_file.write(row + "\t")
                for col in range(1, 10):
                    index = f"{row}{col}"
                    if index in self.samples:
                        sample = self.samples[index]
                        tsv_file.write(f"{sample.side_label}\t")
                    else:
                        tsv_file.write("\t")
                tsv_file.write("\n")

            tsv_file.write("\n")

            # Write headers for construct
            tsv_file.write("construct\t1\t2\t3\t4\t5\t6\t7\t8\t9\n")

            # Write construct data
            for row in "ABCDEFGHI":
                tsv_file.write(row + "\t")
                for col in range(1, 10):
                    index = f"{row}{col}"
                    if index in self.samples:
                        sample = self.samples[index]
                        tsv_file.write(f"{sample.construct}\t")
                    else:
                        tsv_file.write("\t")
                tsv_file.write("\n")

            tsv_file.write("\n")

            # Write headers for concentration
            tsv_file.write("concentration\t1\t2\t3\t4\t5\t6\t7\t8\t9\n")

            # Write concentration data
            for row in "ABCDEFGHI":
                tsv_file.write(row + "\t")
                for col in range(1, 10):
                    index = f"{row}{col}"
                    if index in self.samples:
                        sample = self.samples[index]
                        tsv_file.write(f"{sample.concentration}\t")
                    else:
                        tsv_file.write("\t")
                tsv_file.write("\n")

            tsv_file.write("\n")

            # Write headers for culture
            tsv_file.write("culture\t1\t2\t3\t4\t5\t6\t7\t8\t9\n")

            # Write culture data
            for row in "ABCDEFGHI":
                tsv_file.write(row + "\t")
                for col in range(1, 10):
                    index = f"{row}{col}"
                    if index in self.samples:
                        sample = self.samples[index]
                        tsv_file.write(f"{sample.culture}\t")
                    else:
                        tsv_file.write("\t")
                tsv_file.write("\n")
