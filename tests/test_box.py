from composition.model.Box import Box
from composition.model.Sample import Sample


class TestBox:

    # Create a box instance with a name, description, and room
    box = Box("box1", "Example box being used for testing of box class functions.", "room1")

    # Create sample instances that will go on in the box for testing inputting a construct, concentration, and culture
    sample1 = Sample("plasmid1", "dil20x", "primary")

    # Test get_descritpion, which should return the description written when the box was instantiated
    def test_get_description(self):
        description = self.box.get_description()
        assert description == "Example box being used for testing of box class functions.", "get_description does not work"

    # Test get_room, which should return the room written when the box was instantiated
    def test_get_room(self):
        description = self.box.get_room()
        assert description == "room1", "get_room does not work"

    # Test add_sample function, which adds a sample at a specified index in the box
    # Takes in a Sample, row string, and column integer
    def test_add_sample(self):
        self.box.add_sample(self.sample1, "A", 5)
        assert self.box.samples is not {}, "add_sample does not work"

    # Test get_sample function
    # Should return the sample at a requested index
    def test_get_sample(self):
        sample = self.box.get_sample("A", 5)
        assert sample is not None, "get_sample does not work"
        assert sample.construct == "plasmid1", "get_sample construct does not work"
        assert sample.concentration == "dil20x", "get_sample concentration does not work"

    # Test move_sample function
    # Should move the sample to the desired location
    # Remove the memory of previous location and update the sample's metadata with the new location info
    def test_move_sample(self):
        self.box.move_sample("A5", "A", 3)
        assert self.box.get_sample("A", 3) is not None, "sample is not in specified location"
        assert self.box.get_sample("A", 5) == "There is no sample at index A5 in box box1",\
            "old location is not correctly updated"
        assert len(self.box.samples) == 1, "the size of the dictionary changed"
        assert self.box.get_sample("A", 3).location == "room1/box1/A3", "incorrect location metadata of sample"

    # Test add_sample_orderly
    # Function should add samples in a pattern of down then right
    # Thus, when there are 10 existing samples, column A should be complete and the next added should be B1
    def test_add_sample_orderly(self):
        sample2 = Sample("plasmid2", "uM10", "primary")
        sample3 = Sample("plasmid3", "uM10", "primary")
        sample4 = Sample("plasmid4", "uM10", "primary")
        sample5 = Sample("plasmid5", "uM10", "primary")
        sample6 = Sample("plasmid6", "uM10", "primary")
        sample7 = Sample("plasmid7", "uM10", "primary")
        sample8 = Sample("plasmid8", "uM10", "primary")
        sample9 = Sample("plasmid9", "uM10", "primary")
        sample10 = Sample("plasmid10", "uM10", "primary")

        samples = [sample2, sample3, sample4, sample5, sample6, sample7, sample8, sample9, sample10]
        for s in samples:
            self.box.add_sample_orderly(s)

        indices = self.box.samples.keys()
        expected_indices = ['A1', 'A2', 'A3', 'A4', 'A5', 'A6', 'A7', 'A8', 'A9', 'B1']
        for i in expected_indices:
            assert i in indices, "add_sample_orderly did not add in expected pattern of down then over"

    # Test remove_sample
    # Should remove a sample at a specified location
    # The sample should be removed from the box samples and the sample's location metadata should be reset
    def test_remove_sample(self):
        sample = self.box.get_sample("B", 1)
        self.box.remove_sample("B1")
        assert len(self.box.samples) == 9, "no sample has been removed"
        assert self.box.get_sample("B", 1) == "There is no sample at index B1 in box box1",\
            "function did not remove sample at specified location"
        assert sample.location is None, "sample's location is not updated when removed"

    # Test create_tsv
    # Converts a box to a TSV file
    # this function creates a tsv with the current box size and tests again with a larger box size
    # Correct output can be checked by viewing files output_tsv_1 and output_tsv_2
    def test_create_tsv(self):
        self.box.create_tsv("output_tsv_1")

        samples_11_to_42 = [
            Sample(f"plasmid{i}", "uM10", "primary") for i in range(11, 43)
        ]

        for s in samples_11_to_42:
            self.box.add_sample_orderly(s)

        self.box.create_tsv("output_tsv_2")


testBox = TestBox()
testBox.test_get_description()
testBox.test_get_room()
testBox.test_add_sample()
testBox.test_get_sample()
testBox.test_move_sample()
testBox.test_add_sample_orderly()
testBox.test_remove_sample()
testBox.test_create_tsv()