courses = {150:'CSCI 150', 161:'CSCI 161', 162:'CSCI 162', 231:'CSCI 231', 241:'CSCI 241', 251:'CSCI 251', 260:'CSCI 260', 300:'CSCI 300', 303:'CSCI 303', 304:'CSCI 304', 307:'CSCI 307', 353:'CSCI 353', 385:'CSCI 385', 355:'CSCI 355', 461:'CSCI 461', 475:'CSCI 475', 480:'CSCI 480'}

courseId = 1

pastClasses = []

while (courseId):
	courseId = (int)(raw_input("Please enter a class number or 0 to quit: "))
	if courses.has_key(courseId):
		pastClasses.append(courses[courseId])
	elif courseId == 0:
		pass
	else:
		print "I don't recgonize that class."

print "You entered: "
for i in pastClasses:
	print i

print "You can take: "
for j in pastClasses:
	x = j[5:8]
	if x == "161": 
		if "CSCI 162" not in pastClasses:
			print "CSCI 162"
		if "CSCI 241" not in pastClasses:
			print "CSCI 241"
	elif x == "162": 
		if "CSCI 231" not in pastClasses:
			print "CSCI 231"
		if "CSCI 303" not in pastClasses:
			print "CSCI 303"
		if "CSCI 304" not in pastClasses:
			print "CSCI 304"
		if "CSCI 307" not in pastClasses:
			print "CSCI 307"
	elif x == "150":
		if "CSCI 260" not in pastClasses:
			print "CSCI 260"
	elif x == "231":
		if "CSCI 353" not in pastClasses:
			print "CSCI 353"
		if "CSCI 355" not in pastClasses:
			print "CSCI 355"
	elif x == "241":
		if "CSCI 300" not in pastClasses:
			print "CSCI 300"
	elif x == "353":
		if "CSCI 385" not in pastClasses:
			print "CSCI 385"
	elif x == "470":
		if "CSCI 480" not in pastClasses:
			print "CSCI 480" 


if "CSCI 161" not in pastClasses:
	print "CSCI 161"
if "CSCI 150" not in pastClasses:
	print "CSCI 150"
if "CSCI 251" not in pastClasses:
	print "CSCI 251"

if 'CSCI 303' in pastClasses:
	if 'CSCI 304' in pastClasses:
		if 'CSCI 307' in pastClasses and "CSCI 475" not in pastClasses:
			print "CSCI 475"
			if 'CSCI 231' in pastClasses and "CSCI 461" not in pastClasses:
				print "CSCI 461"
