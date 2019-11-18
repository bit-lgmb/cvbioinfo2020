lista = "/home/breno/PycharmProjects/cvbioinfo2020/contactform/Seleção - Selecionados.csv"
form = open("forma", "w")
with open(lista) as fi:
    for i in fi:
        infos = i.split(",")
        line = """<tr>\n\t<td>""" + infos[0] + """</td>\n\t<td>""" + infos[-1].strip()+"""</td>\n</tr> \n"""

        form.write(line)


form.close()
