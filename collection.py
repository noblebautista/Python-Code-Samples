#Program Name: collection.py
# Purpose of a program:
# Create a collection of authors and the years they died using a dictionary.
# Print the collection in the following format:

# Charles Dickens, 1870
# William Thackeray, 1863
# Anthony Trollope, 1882
# Gerard Manley Hopkins, 1889
########################################################################################
# Noble Bautista = Editor

authors = {
    "Charles Dickens": "1870",
    "William Thackeray": "1863",
    "Anthony Trollope": "1882",
    "Gerard Manley Hopkins": "1889"
} #list of all the authors, with their death years listed as seperate items.
for author, date in authors.items():
    print('{}, {}'.format(author, date)) #prints authors names as well as their death dates in the format listed within the print statement.

