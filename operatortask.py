#result processing
#declare
sid = None
fullname = None
sub1 = None #obtained marks
sub2 = None
sub3 = None
total = None
#input
sid = input("Enter student ID: ")
fullname = input("Enter your full name: ")
sub1 = input("Enter your marks in sub1:")
sub2 = input("Enter your marks in sub2:")
sub3 = input("Enter your marks in sub3:")

#process
#calculate total
total = input(int(sub1 + sub2 + sub3))
#calculate result
#NA
#output
print("SID : {}".format(sid))
print("FULLNAME : {}".format(fullname))
print("SUB1 : {}".format(sub1))
print("SUB2 : {}".format(sub2))
print("SUB3 : {}".format(sub3))
print("TOTAL : {}".format(total))

