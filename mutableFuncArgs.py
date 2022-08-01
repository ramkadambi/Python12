#Mutable Param Functions
def modifyStudents(studentList):
	studentList.append('Jeffrey')
	return

myStudents = ['Rahul', 'Nidish', 'HariPriya']
print(myStudents)
modifyStudents(myStudents)
print(' After calling modifyStudents')
print(myStudents)
