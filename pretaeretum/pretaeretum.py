import pandas
import random
import math 



def das_pretäretum_von(verben,times=10):

    for _ in range(times):

        index = random.choice(range(len(verben)))

        print(f"Was ist das präteritum von ({verben['Infinitiv'][index]})? Konjugire mit ich.")

        antwort = input()

        print(f"Antwort: {antwort}")

        if math.isnan(float(verben['Präteritum_ich*'][index])):
            print(f"Die richtige Antwort: {verben['Präteritum_ich'][index]}")
        else: 
            print(f"Die richtige Antwort: {verben['Präteritum_ich'][index]}/{verben['Präteritum_ich*'][index]}")

        print("----------------------------------------------------------------------------------------------------")



if __name__ == "__main__":
    verben = pandas.read_csv("verben/top-german-verbs.csv")
    das_pretäretum_von(verben=verben,times=10)
