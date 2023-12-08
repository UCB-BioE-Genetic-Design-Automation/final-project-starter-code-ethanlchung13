from composition.model.Box import Box
from composition.model.Sample import Sample


class TestSample:

    # Create sample instance inputting a construct, concentration, and culture
    sample = Sample("plasmid1", "dil20x", "primary")

    def test_get_construct(self):
        assert self.sample.get_construct() == "plasmid1", "get_construct not working"

    def test_get_concentration(self):
        assert self.sample.get_concentration() == "dil20x", "get_concentration not working"

    def test_get_label(self):
        assert self.sample.get_label() == "plasmid1 dil20x", "get_label not working"

    def test_get_side_label(self):
        assert self.sample.get_side_label() == "plasmid1", "get_side_label not working"

    def test_get_culture(self):
        assert self.sample.get_culture() == "primary", "get_culture not working"

    def test_get_location(self):
        assert self.sample.get_location() is None, "get_location not working upon initialization"

    def test_get_location_after_added(self):
        box = Box("box1", "Example box being used for testing of box class functions.", "room1")
        box.add_sample(self.sample, "A", 1)
        assert self.sample.get_location() == "room1/box1/A1", "get_location not working after sample is added to a box"

testSample = TestSample()
testSample.test_get_construct()
testSample.test_get_concentration()
testSample.test_get_label()
testSample.test_get_side_label()
testSample.test_get_culture()
testSample.test_get_location()
testSample.test_get_location_after_added()