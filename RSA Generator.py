from CUST_LIB import *


def generateRSAKeys():
    #Doesnt exist yet, program in CUST_LIB
    P=generatePrimes()#Add number here
    Q=generatePrimes()#Add number here
    N=P*Q
    T=(P-1)*(Q-1)
    E=int(input("Public Key.\nMust be prime\nMust be less than totient ("+str(T)+")\nMust NOT be a factor of totient"))#Prompt for public key
    #Note on D: (D*E)/T must have remainder 1
