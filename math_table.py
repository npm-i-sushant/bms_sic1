import sys

user_number = int(sys.argv[1])

for i in range(1, 21):
    print('%d x %02d = %3d'%(user_number, i, user_number * i))

