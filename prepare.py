import os
for f in os.listdir(os.getcwd()):
    if ".gjf" in f:
        file_old = open(os.path.join(os.getcwd(), f), 'r')
        lines = file_old.readlines()
        file_old.close()
        os.remove(file_old.name)
        file_new = open(os.path.join(os.getcwd(), file_old.name), 'w')
        file_new.write("%nprocshare = 12\n%mem = 24Gb\n#p opt=(vtight) b3lyp/6-311++g** nosymm\n\n======\n\n0 1\n")
        for i in range(5, len(lines)-1):
            columns = lines[i].split(" ")
            del columns[1]
            for col in columns:
                file_new.write(col)
                file_new.write(" ")
        file_new.close()


