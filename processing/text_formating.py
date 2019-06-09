def text_processing(num_coletas):
    values = []
    for x in range(1,num_coletas):
        arq = open("coletas/coleta_{}.txt".format(x))
        arquivo = arq.readlines()
        for line in arquivo:
            line = line.split()
            if len(line) < 10:
                pass
            else:
                output = (line[6], line[-1])
                if line[-1] != " " :
                    values.append(output)

        arq.close()
        new_file = open("coletas/nova_coleta_{}.txt".format(x), "w")
        for value in values:
            new_file.write("{} {} \n".format(value[0], value[1]))
        
        new_file.close()
