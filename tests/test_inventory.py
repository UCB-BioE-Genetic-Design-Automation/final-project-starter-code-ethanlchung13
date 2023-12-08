from composition.Inventory import Inventory


class TestInventory:

    inventory = Inventory()

    # Tests that the read in data is as what is expected from the TSV file inputted
    def test_read_csv(self):
        file_path = "/Users/ethanchung/Desktop/BioE134/final-project-starter-code-ethanlchung13/tests/Box_Lyc7.txt"
        self.inventory.read_tsv(file_path)

        box = self.inventory.get_box("Box_Lyc7")

        labels_data = [
            ["PF3b uM100", "odxs1 uM100", "ojpsDF1 uM100", "oispG1 dil20x", "64 dil20x", "slyc11 dil20x", "oBcaGF dil20x", "15U1 uM10", "slyc7 uM10"],
            ["PF3b uM100", "odx2 uM100", "ojpdDF2 uM100", "oispG2 dil20x", "106 dil20x", "oBcaGF dil20x", "oBmGF dil20x", "15L2 uM11", "15L2 uM11"],
            ["15b uM100", "odsx3 uM100", "ojpsDF3 uM100", "oispG3 dil20x", "111 dil20x", "oBmGF dil20x", "oPfGF dil20x", "15S1 uM12", "olyc6 uM12"],
            ["xB uM100", "odxs4 uM100", "ojpsDF4 uM100", "oispG4 dil20x", "dxs dil20x", "oPfGF dil20x", "oispG5 dil20x", "15O1 uM13", "olyc7 uM13"],
            ["xC uM100", "slyc11 uM100", "slyc12 uM100", "slyc13 dil20x", "DF dil20x", "oispG5 dil20x", "oBcaGR dil20x", "15M1 uM14", "olyc8 uM14"],
            ["dfA uM100", "x uM100", "df uM100", "g dil20x", "G dil20x", "oBcaGR dil20x", "oBmGR dil20x", "b112 uM15", "55F uM15"],
            ["dfC uM100", "olyc9 uM100", "olyc11 uM100", "olyc13 dil20x", "dxs2 dil20x", "oBmGR dil20x", "oPfGR dil20x", "olyc9 uM16", "olyc12 uM16"],
            ["gA uM100", "olyc10 uM100", "olyc12 uM100", "olyc14 dil20x", "DF1 dil20x", "oPfGR dil20x", "oPfGR dil20x", "olyc9 uM17", "olyc13 uM17"],
            ["55F uM100", "olyc6 uM100", "olyc7 uM100", "olyc8 dil20x", "1C dil20x", "p20N80 dil20x", "oPfGR dil20x", "olyc11 uM18", "olyc14 uM18"]
        ]

        side_label_data = [
            ["PF3b", "odxs1", "ojpsDF1", "oispG1", "64", "slyc11", "oBcaGF", "15U1", "slyc7"],
            ["PF3b", "odx2", "ojpdDF2", "oispG2", "106", "oBcaGF", "oBmGF", "15L2", "15L2"],
            ["15b", "odsx3", "ojpsDF3", "oispG3", "111", "oBmGF", "oPfGF", "15S1", "olyc6"],
            ["xB", "odxs4", "ojpsDF4", "oispG4", "dxs", "oPfGF", "oispG5", "15O1", "olyc7"],
            ["xC", "slyc11", "slyc12", "slyc13", "DF", "oispG5", "oBcaGR", "15M1", "olyc8"],
            ["dfA", "x", "df", "g", "G", "oBcaGR", "oBmGR", "b112", "55F"],
            ["dfC", "olyc9", "olyc11", "olyc13", "dxs2", "oBmGR", "oPfGR", "olyc9", "olyc12"],
            ["gA", "olyc10", "olyc12", "olyc14", "DF1", "oPfGR", "oPfGR", "olyc9", "olyc13"],
            ["55F", "olyc6", "olyc7", "olyc8", "1C", "p20N80", "oPfGR", "olyc11", "olyc14"]
        ]

        construct_data = [
            ["PF3b", "odxs1", "ojpsDF1", "oispG1", "64", "slyc11", "oBcaGF", "15U1", "slyc7"],
            ["PF3b", "odx2", "ojpdDF2", "oispG2", "106", "oBcaGF", "oBmGF", "15L2", "15L2"],
            ["15b", "odsx3", "ojpsDF3", "oispG3", "111", "oBmGF", "oPfGF", "15S1", "olyc6"],
            ["xB", "odxs4", "ojpsDF4", "oispG4", "dxs", "oPfGF", "oispG5", "15O1", "olyc7"],
            ["xC", "slyc11", "slyc12", "slyc13", "DF", "oispG5", "oBcaGR", "15M1", "olyc8"],
            ["dfA", "x", "df", "g", "G", "oBcaGR", "oBmGR", "b112", "55F"],
            ["dfC", "olyc9", "olyc11", "olyc13", "dxs2", "oBmGR", "oPfGR", "olyc9", "olyc12"],
            ["gA", "olyc10", "olyc12", "olyc14", "DF1", "oPfGR", "oPfGR", "olyc9", "olyc13"],
            ["55F", "olyc6", "olyc7", "olyc8", "1C", "p20N80", "oPfGR", "olyc11", "olyc14"]
        ]

        concentration_data = [
            ["uM100", "uM100", "uM100", "dil20x", "dil20x", "dil20x", "dil20x", "uM10", "uM10"],
            ["uM100", "uM100", "uM100", "dil20x", "dil20x", "dil20x", "dil20x", "uM11", "uM11"],
            ["uM100", "uM100", "uM100", "dil20x", "dil20x", "dil20x", "dil20x", "uM12", "uM12"],
            ["uM100", "uM100", "uM100", "dil20x", "dil20x", "dil20x", "dil20x", "uM13", "uM13"],
            ["uM100", "uM100", "uM100", "dil20x", "dil20x", "dil20x", "dil20x", "uM14", "uM14"],
            ["uM100", "uM100", "uM100", "dil20x", "dil20x", "dil20x", "dil20x", "uM15", "uM15"],
            ["uM100", "uM100", "uM100", "dil20x", "dil20x", "dil20x", "dil20x", "uM16", "uM16"],
            ["uM100", "uM100", "uM100", "dil20x", "dil20x", "dil20x", "dil20x", "uM17", "uM17"],
            ["uM100", "uM100", "uM100", "dil20x", "dil20x", "dil20x", "dil20x", "uM18", "uM18"]
        ]

        culture_data = [
            ["primary", "primary", "primary", "primary", "primary", "primary", "primary", "primary", "primary"],
            ["primary", "primary", "primary", "primary", "primary", "primary", "primary", "primary", "primary"],
            ["primary", "primary", "primary", "primary", "primary", "primary", "primary", "primary", "primary"],
            ["primary", "primary", "primary", "primary", "primary", "primary", "primary", "primary", "primary"],
            ["primary", "primary", "primary", "primary", "primary", "primary", "primary", "primary", "primary"],
            ["primary", "primary", "primary", "primary", "primary", "primary", "primary", "primary", "primary"],
            ["primary", "primary", "primary", "primary", "primary", "primary", "primary", "primary", "primary"],
            ["primary", "primary", "primary", "primary", "primary", "primary", "primary", "primary", "primary"],
            ["primary", "primary", "primary", "primary", "primary", "primary", "primary", "primary", "primary"]
        ]

        for s in box.samples.values():
            assert any(s.label in sublist for sublist in labels_data), "Label is not in expected set"
            assert any(s.side_label in sublist for sublist in side_label_data), "Side Label is not in expected set"
            assert any(s.construct in sublist for sublist in construct_data), "Construct is not in expected set"
            assert any(s.concentration in sublist for sublist in concentration_data), "Concentration is not in expected set"
            assert any(s.culture in sublist for sublist in culture_data), "Culture is not in expected set"

        self.inventory.create_tsv(self.inventory.get_box("Box_Lyc7"), "output_file.tsv")


testInventory = TestInventory()
testInventory.test_read_csv()
