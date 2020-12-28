# Tax Reduction REST Apis - Tools

## Import Data Tool

- Use this tool to ingest property tax related data into our database. We will be using MongoDB as a datastore so go ahead and install MongoDB.

### Steps to ingest data:

- Install dependencies for the project using the following command:
  ```sh
  $ cd TaxReduction
  $ pip3 install -r requirements.txt
  ```
- Use the -h flag to get to know about the different files to ingest:

  ```sh
  $ cd tools/
  $ python import_data.py -h
  usage: import_data.py [-h] [-p PROPERTY] [-l LAND] [-o OWNER] [-sa SALES]
                        [-se SEGMENT] [-i IMPROVEMENT]

  optional arguments:
    -h, --help            show this help message and exit
    -p PROPERTY, --property PROPERTY
                          absolute path to properties data file
    -l LAND, --land LAND  absolute path to land data file
    -o OWNER, --owner OWNER
                          absolute path to owners data file
    -sa SALES, --sales SALES
                          absolute path to sales data file
    -se SEGMENT, --segment SEGMENT
                          absolute path to segments data file
    -i IMPROVEMENT, --improvement IMPROVEMENT
                          absolute path to improvement data file
  ```

- Run the script using the following command (data files should be available in the data directory):
  ```sh
    $ python3 import_data.py -i ../data/Improvement.txt -se ../data/Segment.txt -p ../data/Property.txt -l ../data/Land.txt -o ../data/Owner.txt -sa ../data/Sales.txt
  ```
- Patiently wait for the data ingestion to complete.
