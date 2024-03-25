courses = ['CSC101', 'CSC102', 'CSC103', 'NET110', 'COM241']

room_number = {'CSC101' : 3004,
            'CSC102' : 4501,
            'CSC103' : 6755,
            'NET110' : 1244,
            'COM241' : 1411}
instructors = {'CSC101' : 'Haynes',
            'CSC102' : 'Alvarado',
            'CSC103' : 'Rich',
            'NET110' : 'Burke',
            'COM241' : 'Lee'}
meeting_time = {'CSC101' : '8:00 a.m.',
            'CSC102' : '9:00 a.m.',
            'CSC103' : '10:00 a.m.',
            'NET110' : '11:00 a.m.',
            'COM241' : '1:00 p.m.'}
course_number = ''
count = 1
while True:
    if course_number not in courses:
        if count > 1:
            print('That is not a valid course number. Please try again.')
        course_number = input('What is the course number: ')
        count +=1
    else:
        break
    

print('Room Number: ', room_number[course_number])

print('Instructor: ', instructors[course_number])

print('Meeting Time: ', meeting_time[course_number])