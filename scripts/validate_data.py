""" Python script to validate data

Run as:

    python3 scripts/validata_data.py data
"""

import os.path as op
import sys
import hashlib

MY_DIR = op.dirname(__file__)
DATA_DIR = op.join(MY_DIR,'../data')
MAIN_DIR = op.join(MY_DIR,'..')
sys.path.append(DATA_DIR)
sys.path.append(MAIN_DIR)

def file_hash(filename):
    """ Get byte contents of file `filename`, return SHA1 hash

    Parameters
    ----------
    filename : str
        Name of file to read

    Returns
    -------
    hash : str
        SHA1 hexadecimal hash string for contents of `filename`.
    """
    # Open the file, read contents as bytes.
    # Calculate, return SHA1 has on the bytes from the file.

    # add the path to data back into the filename - there must be a better way of doing this
    fullfilename = "data/" + filename

    with open(fullfilename, 'rb') as fobj:  # 'rb' means Read Bytes.
        byte_contents = fobj.read()
        hash = hashlib.sha1(byte_contents).hexdigest()
    return hash
    #raise NotImplementedError('This is just a template -- you are expected to code this.')


def validate_data(data_directory):
    """ Read ``hash_list.txt`` file in ``data_directory``, check hashes
    
    An example file ``data_hashes.txt`` is found in the baseline version
    of the repository template for your reference.

    Parameters
    ----------
    data_directory : str
        Directory containing data and ``hash_list.txt`` file.

    Returns
    -------
    None

    Raises
    ------
    ValueError:
        If hash value for any file is different from hash value recorded in
        ``hash_list.txt`` file.
    """
    # Read lines from ``hash_list.txt`` file.
    # Split into SHA1 hash and filename
    # Calculate actual hash for given filename.
    # If hash for filename is not the same as the one in the file, raise
    # ValueErrorfilename
    filename = op.join(data_directory,'hash_list.txt')

    with open(filename) as fobj:
        lines = fobj.readlines()
    for i in range(len(lines)): 
        ishash,filename = str.split(lines[i])
        ctlhash = file_hash(filename)
        if ishash != ctlhash:
            raise NotImplementedError('Error with hash code for file', filename)


def main():
    # This function (main) called when this file run as a script.
    #
    # Get the data directory from the command line arguments
    if len(sys.argv) < 2:
        raise RuntimeError("Please give data directory on "
                           "command line")
    data_directory = sys.argv[1]
    print(sys.argv[0])
    print(sys.argv[1])

    # Call function to validate data in data directory
    validate_data(data_directory)


if __name__ == '__main__':
    # Python is running this file as a script, not importing it.
    
    main()
