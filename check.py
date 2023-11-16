import os
homo = 0.0
lumo = 0.0
if os.path.isfile(os.path.join(os.getcwd(), "check.txt")):
    os.remove(os.path.join(os.getcwd(), "check.txt"))
for f in os.listdir(os.getcwd()):
    lumo_found = False
    homo_found = False
    if ".out" in f:
        file = open(os.path.join(os.getcwd(), f), 'r')
        lines = file.readlines()
        test_split = lines[len(lines)-1].split()
        if test_split[0] == "Normal" and test_split[1] == "termination":
            for i in range(len(lines)-1, 0, -1):
                split_lines_1 = lines[i].split()
                split_lines_2 = lines[i-1].split()
                if len(split_lines_1) > 2 and len(split_lines_2) > 2:
                    if split_lines_1[1] == "virt." and split_lines_2[1] == "occ." and not lumo_found:
                        lumo_str = split_lines_1[4]
                        lumo_found = True
                        lumo = float(lumo_str)
                if len(split_lines_1) > 2:
                    if split_lines_1[1] == "occ." and not homo_found:
                        homo_str = split_lines_1[len(split_lines_1)-1]
                        homo_found = True
                        homo = float(homo_str)
                if homo_found and lumo_found:
                    homo = homo * 27.2114
                    lumo = lumo * 27.2114
                    homo_str = "%.4f" % homo
                    lumo_str = "%.4f" % lumo
                    homo_str_f = "HOMO: " + homo_str + " eV\n"
                    lumo_str_f = "LUMO: " + lumo_str + " eV\n"
                    output = open(os.path.join(os.getcwd(), "check.txt"), 'a')
                    output.write(f)
                    output.write(": calculation finished\n")
                    output.write(homo_str_f)
                    output.write(lumo_str_f)
                    output.write("---------------\n")
                    output.close()
                    break
        else:
            output = open(os.path.join(os.getcwd(), "check.txt"), 'a')
            output.write(f)
            output.write(": calculation is either still in progress or failed.\n")
            output.write("---------------\n")
            output.close()
