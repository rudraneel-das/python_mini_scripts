"""
This is a skeleton script for generating a comma separated data file from a concrete
data block. This script can be modified by the user as deemed fit.

This script needs a list of lengths af each column in the exact order they are to be
sliced in.

Ths script optionally takes a list of header names of the columns, if present.

One can also put in desired separator, but it is optional. If no separator is provided
the script will consider comma (,) as the default separator.

Example 1 (headers=None, separator=None):
------------------------------------------------------------------------------------
aaaa00158kkyeb  hhjytd       lengths=[4,5,5,2,6]      aaaa,00158,kkyeb,  ,hhjytd
hhhh12358   jk  poiuyt     ---------------------->    hhhh,12358,   jk,  ,poiuyt
llll00000yykiy  hhrtygf                               llll,00000,yykiy,  ,hhrtygf


Example 2 (separator=None)
------------------------------------------------------------------------------------
aaaa00158kkyeb  hhjytd       lengths=[4,5,5,2,6]      colA,colB,colC,colD,colE
hhhh12358   jk  poiuyt     ---------------------->    aaaa,00158,kkyeb,  ,hhjytd
llll00000yykiy  hhrtygf    headers=['colA','colB',    hhhh,12358,   jk,  ,poiuyt
                             'colC','colD','colE']    llll,00000,yykiy,  ,hhrtygf


Example 3
------------------------------------------------------------------------------------
aaaa00158kkyeb  hhjytd       lengths=[4,5,5,2,6]      colA|colB|colC|colD|colE
hhhh12358   jk  poiuyt     ---------------------->    aaaa|00158|kkyeb|  |hhjytd
llll00000yykiy  hhrtygf    headers=['colA','colB',    hhhh|12358|   jk|  |poiuyt
                             'colC','colD','colE']    llll|00000|yykiy|  |hhrtygf
                                separator='|'

"""

import os
from typing import List


def _get_location_and_name_of_file_to_be_separated() -> tuple[str, str]:
    """Returns a tuple of the location of the data file and the name
    of the data file WITH ITS EXTENSION"""
    return r'', ''


def _get_the_desired_file_name_with_extension(file: str) -> str:
    """This function is supposed to return the desired output file name and format.
    As of now for a data file named 'name.txt' we get output file name 'csv_name.txt'"""
    return 'csv_' + file


def _get_the_list_of_header_names() -> List[str] | None:
    """Returns a list of header names or None if no headers are present"""
    return ['colA', 'colB', 'colC', 'colD', 'colE']


def _get_the_list_of_length_of_each_column() -> List[int]:
    """Returns a list of lengths of each column in the order they appear"""
    return [4, 5, 5, 2, 6]


def _get_the_lines_of_the_file_as_a_list(path, file_name) -> List[str]:
    """Reads all the lines from the required file which has the concrete
    block of data and returns a list, where each item in the list is one
    whole line of the file"""
    with open(os.path.join(path, file_name), 'r') as file:
        lines = file.read()

    lines = lines.split('\n')

    return lines


def _separate_the_lines(list_of_lines: List[str],
                        list_of_lengths: List[int],
                        list_oh_headers: List[str] | None = None,
                        separator: str | None = None) -> List[str]:
    """
    Takes each line and slices it as per the lengths present in the parameter
    list_of_lengths and in the exact order in which they are mentioned.

    list_of_lines: It is a list where every item of the list represents one entire
                   row/ line of data from the file which needs to be separated.
    list_of_lengths: It is a list where every item of the list represents the number
                     of characters the data of that column is supposed to be.
    list_oh_headers: It is a list of header names for the separated file. This
                     parameter is optional, for cases when header names are not
                     present or unimportant.
    separator: It is a string character which is supposed to separate data of
               column(i) from that of column(i-1) and/or column(i+1). This
               parameter is optional. If left out, then the default separator is
               comma (,)
    """
    if separator is None:
        separator = ','  # Default separator, is comma

    separated_lines = []
    for line in list_of_lines:  # Processing one line at a time
        if len(line) == 0:  # If a line is blank, then no need to separate it
            continue
        else:
            column_wise_data = []
            for length in list_of_lengths[:-1]:
                # The reason for not considering the length of the last column is
                # done for a small reason that sometimes the data file could have
                # wrong data format for a line. Look at Example 1 above. Observe
                # how the last column was to be of 6 characters, but line 3 had last
                # column of length 7. Reason for why this happened could vary.
                column_wise_data.append(line[:length])
                line = line[length:]

            # Since we do not slice the last column,
            # we keep all that's left of the line in the last column
            column_wise_data.append(line)

            # Each item of the separated_lines is one whole SEPARATED row/ line
            # of the data file in str format
            separated_lines.append(separator.join(column_wise_data))

    if list_oh_headers is not None:  # If headers are present then add them
        separated_lines = [separator.join(list_oh_headers)] + separated_lines

    return separated_lines


def _generate_the_required_separated_file(data, path, file_name):
    """This function is supposed to crate the required file with the file name
    provided in the file_name parameter and in the location provided in the path
    parameter """
    with open(os.path.join(path, file_name), 'w') as file:
        file.write('\n'.join(data))
        file.write('\n')


def main():
    location, file_name = _get_location_and_name_of_file_to_be_separated()
    desired_file_name = _get_the_desired_file_name_with_extension(file_name)
    headers = _get_the_list_of_header_names()
    lengths = _get_the_list_of_length_of_each_column()
    lines_from_file = _get_the_lines_of_the_file_as_a_list(path=location,
                                                           file_name=file_name)
    separated_lines = _separate_the_lines(list_of_lines=lines_from_file,
                                          list_of_lengths=lengths,
                                          list_oh_headers=headers,
                                          separator=',')
    _generate_the_required_separated_file(data=separated_lines,
                                          path=location,
                                          file_name=desired_file_name)


main()
