
# Inventory

Inventory is a Python project that involves the implementation of a sample management system for biological research. The system defines classes for Boxes and Samples, enabling the organization, storage, and retrieval of biological samples within specific containers. The program facilitates the reading and creation of tab-separated value (TSV) files, allowing seamless integration with external data sources and the efficient management of experimental data in a laboratory setting.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites

You need Python installed on your machine. If you don't have Python, let's install it first.

#### Installing Python

1. Download Python from the official [Python website](https://www.python.org/downloads/).
2. Run the installer and follow the on-screen instructions. Make sure to check the box that says "Add Python to PATH" before you click "Install Now".

### Goal and Utilization of the Project

The goal of this project is to develop a sample management system tailored for biological research, providing researchers with a flexible and efficient tool for organizing and tracking biological samples within laboratory boxes. The system aims to simplify the handling of experimental data by enabling the creation, retrieval, and manipulation of samples, as well as the import and export of data through tab-separated value (TSV) files. 

An Inventory object should be able to store a list of boxes. Each box should have metadata of a name, description, and room. Boxes can store up to 9x9 samples. Samples store metadata for construct, concentration, label, side label, culture, and location. 

By offering robust functionality, the project aims to enhance the overall efficiency of sample management in biological laboratories.

To see the execution of this project, see the test files which walk through the creation of an inventory, boxes, and samples (next section).

### Running the Tests

This project uses testing files as the testing framework. To run tests, follow these steps:

1. Navigate to the tests directory if you're not already there.

2. Run the test files:

   - test_inventory.py
   - test_box.py
   - test_sample.py
   
   When testing read_tsv, sample tsv files "Box_Lyc7.txt" and "Box_Lyc15.txt" are used, which can both be found in the tests directory.
   
3. Each respective test file walks through the creation of an instance of the object at hand. Each of the functionalities of the objects is tested in a unique function, with assert statements to check the expected result. At the end of the file, you will see that each test function has been called, meaning that if there are any errors there will be no assert messages.

### Results of the Tests

As aforementioned, the results of the tests is shown through  assert statements of each test function in the test files. Each of the files have no returns when run, meaning that each of the objects that make up the storage system function correctly in accordance with expectations.

From the testing of create_tsv, we see that two tsv files are successfully created from box information. They are labeled as output_tsv_1 and output_tsv_2 and can be found in the tests directory. 

## Author

* **Ethan Chung** - *EC* - [ethanlchung13](https://github.com/ethanlchung13)
