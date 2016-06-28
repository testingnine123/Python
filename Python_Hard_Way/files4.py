from sys import argv

script, file_name = argv

def print_all (f):
	print f.read ()

current_file = open (file_name)

print_all (current_file)

def rewind (f):
	print f.seek (0)

rewind (current_file)	

def print_a_line (line_count, f):
	print line_count, f.readline ()

line_count = 1

print_a_line (line_count, current_file);
