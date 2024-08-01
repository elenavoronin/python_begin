# file = open("../files/members.txt", "a")
# new_member = input("please enter a new member: ")
# file.writelines(new_member)


# filenames = ['doc.txt', 'report.txt', 'presentation.txt']
# text = "Hello"
#
# for filename in filenames:
#     file = open(f"../files/{filename}", "w")
#     file.write(text)

file = open("../files/a.txt", "r")
output = file.readline()
print(output)
file.close()

file = open("../files/b.txt", "r")
output = file.readline()
print(output)
file.close()

file = open("../files/b.txt", "r")
output = file.readline()
print(output)
file.close()
