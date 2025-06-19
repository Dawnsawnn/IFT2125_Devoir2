# CE FICHIER NE SERT QU'A APPELER ET TESTER VOTRE CODE.
# VOUS NE DEVRIEZ PAS AVOIR BESOIN DE LE MODIFIER, SAUF POUR
# AJOUTER VOUS-MÊME D'AUTRES TESTS SI VOUS LE VOULEZ.
# NE PAS REMETTRE SUR STUDIUM. REMETTEZ SEULEMENT poissons.py

# THIS FILE IS ONLY USED TO CALL AND TEST YOUR CODE.
# YOU SHOULD NOT HAVE TO MODIFY IT, EXCEPT FOR ADDING
# NEW CUSTOM TESTS IF YOU WISH TO DO SO.
# DO NOT SUBMIT ON STUDIUM. ONLY SUBMIT poissons.py

import poissons
import time
import traceback

def read(input_file):
    file = open(input_file, "r")
    lines = file.readlines()
    file.close()
    return lines

def verifyAns(studentOutputFile, inputFile, expectedAnswer):
    studentOutput = read(studentOutputFile)
    
    if(len(studentOutput) != 1):
        raise Exception("Output file doesn't have only 1 line")
    if(studentOutput[0].rstrip('\r\n') != expectedAnswer):
        raise Exception("Wrong answer, got " + studentOutput[0].rstrip('\r\n') + ", expected " + expectedAnswer)
    
if __name__ == '__main__':
    nbTests = 15
    answers = ["4","0","10","0","11","33","1143","136848","12090143","12347329","990526764","1246420600","125185325914","500488580510","999999000000"]
    for i in range(1,nbTests+1):
        start = time.time()
        try:
            input_file = "input" + str(i) + ".txt"
            output_file = "output" + str(i) + ".txt"

            poissons.main([input_file, output_file])
            
            verifyAns(output_file, input_file, answers[i-1])
            print("Test " + str(i) + " OK, took " + str(time.time()-start) + " seconds\n")
        except Exception as e: 
            print("Test " + str(i) + " Fail, took " + str(time.time()-start) + " seconds")
            print(e)
            #print(traceback.format_exc())
            print()
        
