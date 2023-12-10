import os


def open_file_in_read_mode(filename):
     if os.path.exists(filename):
         try:
             f = open(filename, 'r')
             print("file opened correclty")
             return f
         except IOError:
             return None
     return None