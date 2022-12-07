"""

"""
f = open("..\sample_input.txt", "r")
# f = open("day-7-2022-input.txt", "r")
f_list = f.readlines()
cmds = [x.strip() for x in f_list]
# print(cmds)
# ['$ cd /', '$ ls', 'dir a', '14848514 b.txt',
#  '8504156 c.dat', 'dir d', '$ cd a', '$ ls',
# 'dir e', '29116 f', '2557 g', '62596 h.lst', '$ cd e',
# '$ ls', '584 i', '$ cd ..', '$ cd ..', '$ cd d', '$ ls',
# '4060174 j', '8033020 d.log', '5626152 d.ext', '7214296 k']

prev_2_dir = ""
prev_dir = "file_system"
dir = "/"  # key
file_system = {
    "/": {},
}


def kv_generator(k, v, _dir):
    _dir[k] = v


for i in range(len(cmds)):
    cmd = cmds[i]
    print(i)
    _cmd = cmd.split(" ")
    print("_cmd:", _cmd)
    # print(_cmd)

    if _cmd[0] == "$":
        command = _cmd[1]
        # print(command)

        if command == "cd":
            arg = _cmd[2]
            # print("prev_2_dir:", prev_2_dir)
            # print("prev_dir:", prev_dir)
            # print("dir:", dir)
            # print()
            if arg == "/":
                dir = "/"
                prev_dir = ""
                prev_2_dir = ""
                print("prev_2_dir:", prev_2_dir)
                print("prev_dir:", prev_dir)
                print("dir:", dir)
                print()
            elif arg.isalpha():
                prev_2_dir = prev_dir
                prev_dir = dir
                dir = arg
                print("prev_2_dir:", prev_2_dir)
                print("prev_dir:", prev_dir)
                print("dir:", dir)
                print()
            elif arg == "..":
                dir = prev_dir
                prev_dir = prev_2_dir
                prev_2_dir = ""
                print("prev_2_dir:", prev_2_dir)
                print("prev_dir:", prev_dir)
                print("dir:", dir)
                print()
        elif command == "ls":
            # prev_2_dir = prev_dir
            # prev_dir = dir
            # prev_dir and dir will be similar

            print("prev_2_dir:", prev_2_dir)
            print("prev_dir:", prev_dir)
            print("dir:", dir)
            print()

    elif _cmd[0] == "dir":
        # Add files in this dir up till next
        # line with $
        # dir = _cmd[0]
        # dir = prev_dir
        # prev_dir = prev_2_dir
        # prev_2_dir = ""
        _dir = dir
        _prev = prev_dir
        _prev_2 = prev_2_dir

        prev_2_dir = prev_dir
        prev_dir = dir
        dir = _cmd[1]
        value = {}
        print("prev_2_dir:", prev_2_dir)
        print("type(prev_2_dir):", type(prev_2_dir))
        print("prev_dir:", prev_dir)
        print("type(prev_dir):", type(prev_dir))
        print("dir:", dir)
        print("type(dir):", type(dir))
        if prev_dir:
            if prev_2_dir:
                file_system[prev_2_dir][prev_dir] = value
            else:
                file_system[prev_dir][dir] = value
        else:
            file_system[dir] = value

        dir = _dir
        prev_dir = _prev
        prev_2_dir = _prev_2

    elif _cmd[0].isdigit():
        value = int(_cmd[0])
        print("prev_2_dir:", prev_2_dir)
        print("prev_dir:", prev_dir)
        print("dir:", dir)
        print("value:", value)
        if prev_dir:
            if prev_2_dir:
                file_system[prev_2_dir][prev_dir] = value
                print("file_system[prev_2_dir][prev_dir] = value", value)
            else:
                file_system[prev_dir][dir] = value
                print("file_system[prev_dir][dir] = value", value)
        else:
            file_system[dir] = value
            print("file_system[dir] = value", value)

print("File System:", file_system)
