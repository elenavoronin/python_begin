filenames = ["1.doc", "1.report", "1.presentation"]

# new_filenames = []
#
# for file in filenames:
#     file = file.replace("1.", "1-")
#     file = file.replace(file, f"{file}.txt")
#     new_filenames.append(file)
# print(new_filenames)



filenames = [filename.replace('.', '-') + '.txt' for filename in filenames]
print(filenames)