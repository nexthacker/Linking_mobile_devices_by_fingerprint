
def text_processing(num_coletas):
    values = []
    for x in range(1,num_coletas):
        arquivo = []
        working = False

        try:
            arq = open("coletas/coleta_{}.txt".format(x))
            arquivo = arq.readlines()
            arq.close()
            print("coleta_{} is default".format(x))
            working = True
        except:
            print("coleta_{} not default".format(x))

        if not working:

            try:
                encoding = "unicode"
                arq = open("coletas/coleta_{}.txt".format(x), encoding=encoding)
                arquivo = arq.readlines()
                arq.close()
                print("coleta_{} is unicode".format(x))
                working = True
            except:
                print("coleta_{} not unicode".format(x))

            if not working:
                try:
                    encoding = "utf-8"
                    arq = open("coletas/coleta_{}.txt".format(x), encoding=encoding)
                    arquivo = arq.readlines()
                    arq.close()
                    print("coleta_{} is utf-8".format(x))
                    working = True
                except:
                    print("coleta_{} not utf-8".format(x))

                if not working:
                    try:
                        encoding = 'ascii'
                        arq = open("coletas/coleta_{}.txt".format(x), encoding=encoding)
                        arquivo = arq.readlines()
                        arq.close()
                        print("coleta_{} is ascii".format(x))
                    except:
                        print("coleta_{} not ascii".format(x))

        for line in arquivo:
            line = line.split()
            if len(line) < 10:
                pass
            else:
                output = (line[6], line[-1])
                if line[-1] != " " :
                    values.append(output)

        try:
            new_file = open("coletas/nova_coleta_{}.txt".format(x), "w")
            for value in values:
                new_file.write("{} {} \n".format(value[0], value[1]))

            new_file.close()
        except:
            pass
