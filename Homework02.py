courses = {150:'CSCI 150', 161:'CSCI 161', 162:'CSCI 162', 231:'CSCI 231', 241:'CSCI 241', 251:'CSCI 251', 260:'CSCI 260', 300:'CSCI 300', 303:'CSCI 303', 304:'CSCI 304', 307:'CSCI 307', 353:'CSCI 353', 385:'CSCI 385', 355:'CSCI 355', 461:'CSCI 461', 475:'CSCI 475', 480:'CSCI 480'}

prereq = {'CSCI 161':'CSCI 162 and CSCI 241', 'CSCI 162':'CSCI 231, 304, and 307', 'CSCI 150':'CSCI 260', 'CSCI 241':'CSCI 300', 'CSCI 231':'CSCI 353 and CSCI 355', 'CSCI 353':'CSCI 385', 'CSCI 470':'CSCI 480'}

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
	if prereq.has_key(j):
		print prereq[j]

if 'CSCI 303' in pastClasses:
	if 'CSCI 304' in pastClasses:
		if 'CSCI 307' in pastClasses:
			print "CSCI 475"
			if 'CSCI 231' in pastClasses:
				print "CSCI 461"
