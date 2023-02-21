#!/usr/bin/python3
"""Text indentation"""


def text_indentation(text):
    if type(text) is not str:
        raise TypeError("text must be a string")
    str1 = ""
    strD = []
    for i in text:
        if i in ".:?":
            str1 += i
            strD.append(str1)
            str1 = ""
        else:
            str1 += i
    strD.append(str1)
    for i in range(len(strD)):
        if i == len(strD) - 1:
            print(strD[i].strip())
        else:
            print(strD[i].strip())
            print()
text_indentation("""Lorem ipsum dolor sit amet, consectetur adipiscing elit. \
Quonam modo? Utrum igitur tibi litteram videor an totas paginas commovere? \
Non autem hoc: igitur ne illud quidem. Fortasse id optimum, sed ubi illud: \
Plus semper voluptatis? Teneo, inquit, finem illi videri nihil dolere. \
Transfer idem ad modestiam vel temperantiam, quae est moderatio cupiditatum \
rationi oboediens. Si id dicis, vicimus. Inde sermone vario sex illa a Dipylo \
stadia confecimus. Sin aliud quid voles, postea. Quae animi affectio suum \
cuique tribuens atque hanc, quam dico. Utinam quidem dicerent alium alio \
beatiorem! Iam ruinas videres""")
