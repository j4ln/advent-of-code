#!/usr/bin/python3

with open("d07.input") as file:
    input = file.read().splitlines()

working_dir = ""
directories = set()
directory_files = []

for line in enumerate(input):
    index = line[0]
    line = line[1]

    # Parse command
    if line.find("$") != -1:
        command = line.split(" ")

        # cd command, track working directory, and seen directories
        if command[1] == "cd":
            match command[2]:
                case "/":
                    working_dir = "/"
                case "..":
                    last_dir = working_dir[:-1].rfind("/")
                    working_dir = working_dir[:last_dir] + "/"
                case _:
                    working_dir += f"{command[2]}/"
            directories.add(working_dir)

        # ls command, get files in the directory as a list of dicts
        elif command[1] == "ls":
            files = []
            for ls_line in input[index + 1 :]:
                if ls_line.find("$") != -1:
                    break
                output = ls_line.split(" ")
                if output[0] != "dir":
                    files.append({"file": output[1], "size": int(output[0])})
            # Append the list of directory files as a dict to a list
            directory_files.append({"name": working_dir, "files": files})

# Work out the total size of each directory
for dir_dict in directory_files:
    total_size = 0
    for file in dir_dict["files"]:
        total_size += file["size"]
    dir_dict["total_size"] = total_size

# Work out the true total size for each directory we saw
# Takes into account a directories inner directory size
total_dir_sizes = []
for dir in directories:
    total_size = 0
    for dir_dict in directory_files:
        if dir_dict["name"].find(dir) != -1:
            total_size += dir_dict["total_size"]
    total_dir_sizes.append(total_size)

# Part 1
sum_of = 0
for dir_size in total_dir_sizes:
    if dir_size <= 100000:
        sum_of += dir_size
print(sum_of)

# Part 2
total_space = 70000000
required_space = 30000000

total_dir_sizes.sort()
unused_space = total_space - total_dir_sizes[-1]
missing_space = required_space - unused_space

for dir_size in total_dir_sizes:
    if dir_size > missing_space:
        print(dir_size)
        break
