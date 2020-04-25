from array import *

initial_permutation = [58, 50, 42, 34, 26, 18, 10, 2,
                60, 52, 44, 36, 28, 20, 12, 4,
                62, 54, 46, 38, 30, 22, 14, 6,
                64, 56, 48, 40, 32, 24, 16, 8,
                57, 49, 41, 33, 25, 17, 9, 1,
                59, 51, 43, 35, 27, 19, 11, 3,
                61, 53, 45, 37, 29, 21, 13, 5,
                63, 55, 47, 39, 31, 23, 15, 7]

final_permutation = [40 ,8,48,16,56,24,64,32,
39,7,47,15,55,23,63,31,
38,6,46,14,54,22,62,30,
37,5,45,13,53,21,61,29,
36,4,44,12,52,20,60,28,
35,3,43,11,51,19,59,27,
34,2,42,10,50,18,58,26,
33,1,41,9,49,17,57,25]

expension = [32, 1 , 2 , 3 , 4 , 5 , 4 , 5,
         6 , 7 , 8 , 9 , 8 , 9 , 10, 11,
         12, 13, 12, 13, 14, 15, 16, 17,
         16, 17, 18, 19, 20, 21, 20, 21,
         22, 23, 24, 25, 24, 25, 26, 27,
         28, 29, 28, 29, 30, 31, 32, 1 ]

brut_force_subKey =['000000','000001','000010',
'000011','000100','000101','000110',
'000111','001000','001001','001010',
'001011','001100','001101','001110',
'001111','010000','010001','010010',
'010011','010100','010101','010110',
'010111','011000','011001','011010',
'011011','011100','011101','011110',
'011111','100000','100001','100010',
'100011','100100','100101','100110',
'100111','101000','101001','101010',
'101011','101100','101101','101110',
'101111','110000','110001','110010',
'110011','110100','110101','110110',
'110111','111000','111001','111010',
'111011','111100','111101','111110',
'111111']

sbox =  [[[14, 4, 13, 1, 2, 15, 11, 8, 3, 10, 6, 12, 5, 9, 0, 7],
          [ 0, 15, 7, 4, 14, 2, 13, 1, 10, 6, 12, 11, 9, 5, 3, 8],
          [ 4, 1, 14, 8, 13, 6, 2, 11, 15, 12, 9, 7, 3, 10, 5, 0],
          [15, 12, 8, 2, 4, 9, 1, 7, 5, 11, 3, 14, 10, 0, 6, 13 ]],

         [[15, 1, 8, 14, 6, 11, 3, 4, 9, 7, 2, 13, 12, 0, 5, 10],
            [3, 13, 4, 7, 15, 2, 8, 14, 12, 0, 1, 10, 6, 9, 11, 5],
            [0, 14, 7, 11, 10, 4, 13, 1, 5, 8, 12, 6, 9, 3, 2, 15],
           [13, 8, 10, 1, 3, 15, 4, 2, 11, 6, 7, 12, 0, 5, 14, 9 ]],

         [ [10, 0, 9, 14, 6, 3, 15, 5, 1, 13, 12, 7, 11, 4, 2, 8],
           [13, 7, 0, 9, 3, 4, 6, 10, 2, 8, 5, 14, 12, 11, 15, 1],
           [13, 6, 4, 9, 8, 15, 3, 0, 11, 1, 2, 12, 5, 10, 14, 7],
            [1, 10, 13, 0, 6, 9, 8, 7, 4, 15, 14, 3, 11, 5, 2, 12 ]],

          [ [7, 13, 14, 3, 0, 6, 9, 10, 1, 2, 8, 5, 11, 12, 4, 15],
           [13, 8, 11, 5, 6, 15, 0, 3, 4, 7, 2, 12, 1, 10, 14, 9],
           [10, 6, 9, 0, 12, 11, 7, 13, 15, 1, 3, 14, 5, 2, 8, 4],
            [3, 15, 0, 6, 10, 1, 13, 8, 9, 4, 5, 11, 12, 7, 2, 14] ],

          [ [2, 12, 4, 1, 7, 10, 11, 6, 8, 5, 3, 15, 13, 0, 14, 9],
           [14, 11, 2, 12, 4, 7, 13, 1, 5, 0, 15, 10, 3, 9, 8, 6],
            [4, 2, 1, 11, 10, 13, 7, 8, 15, 9, 12, 5, 6, 3, 0, 14],
           [11, 8, 12, 7, 1, 14, 2, 13, 6, 15, 0, 9, 10, 4, 5, 3 ]],

         [ [12, 1, 10, 15, 9, 2, 6, 8, 0, 13, 3, 4, 14, 7, 5, 11],
           [10, 15, 4, 2, 7, 12, 9, 5, 6, 1, 13, 14, 0, 11, 3, 8],
            [9, 14, 15, 5, 2, 8, 12, 3, 7, 0, 4, 10, 1, 13, 11, 6],
            [4, 3, 2, 12, 9, 5, 15, 10, 11, 14, 1, 7, 6, 0, 8, 13] ],

          [ [4, 11, 2, 14, 15, 0, 8, 13, 3, 12, 9, 7, 5, 10, 6, 1],
           [13, 0, 11, 7, 4, 9, 1, 10, 14, 3, 5, 12, 2, 15, 8, 6],
            [1, 4, 11, 13, 12, 3, 7, 14, 10, 15, 6, 8, 0, 5, 9, 2],
            [6, 11, 13, 8, 1, 4, 10, 7, 9, 5, 0, 15, 14, 2, 3, 12] ],

         [ [13, 2, 8, 4, 6, 15, 11, 1, 10, 9, 3, 14, 5, 0, 12, 7],
            [1, 15, 13, 8, 10, 3, 7, 4, 12, 5, 6, 11, 0, 14, 9, 2],
            [7, 11, 4, 1, 9, 12, 14, 2, 0, 6, 10, 13, 15, 3, 5, 8],
            [2, 1, 14, 7, 4, 10, 8, 13, 15, 12, 9, 0, 3, 5, 6, 11] ] ]

per = [ 16,  7, 20, 21,
        29, 12, 28, 17,
         1, 15, 23, 26,
         5, 18, 31, 10,
         2,  8, 24, 14,
        32, 27,  3,  9,
        19, 13, 30,  6,
        22, 11,  4, 25 ]

inv_per = [9,17,23,31,
            13, 28,2,18,
            24,16,30,6,
            26,20,10,1,
            8,14,25,3,
            4,29,11,19,
            32,12,22,7,
            5,27,15,21]
#inverse de PC2
inv_PC_2 = [5,24,7,16,6,10,20,
          18,49,12,3,15,23,1,
          9,19,2,50,14,22,11,
          51,13,4,52,17,21,8,
          47,31,27,48,35,41,53,
          46,28,54,39,32,25,44,
          55,37,34,43,29,36,38,
          45,33,26,42,56,30,40]

#inverse de PC1
inv_PC_1 = [8,16,24,56,52,44,36,57,
          7,15,23,55,51,43,35,58,
          6,14,22,54,50,42,34,59,
          5,13,21,53,49,41,33,60,
          4,12,20,28,48,40,32,61,
          3,11,19,27,47,39,31,62,
          2,10,18,26,46,38,30,63,
          1,9,17,25,45,37,29,64]

PC_1 = [57, 49, 41, 33, 25, 17, 9,
        1, 58, 50, 42, 34, 26, 18,
        10, 2, 59, 51, 43, 35, 27,
        19, 11, 3, 60, 52, 44, 36,
        63, 55, 47, 39, 31, 23, 15,
        7, 62, 54, 46, 38, 30, 22,
        14, 6, 61, 53, 45, 37, 29,
        21, 13, 5, 28, 20, 12, 4 ]

PC_2 = [14, 17, 11, 24, 1, 5,
            3, 28, 15, 6, 21, 10,
            23, 19, 12, 4, 26, 8,
            16, 7, 27, 20, 13, 2,
            41, 52, 31, 37, 47, 55,
            30, 40, 51, 45, 33, 48,
            44, 49, 39, 56, 34, 53,
            46, 42, 50, 36, 29, 32 ]

shift_table = [1, 1, 2, 2,
                2, 2, 2, 2,
                1, 2, 2, 2,
                2, 2, 2, 1 ]

#permet d'effectuer un permutation sur toChange
#en utilisant la table p_table
def permutation(toChange, p_table,n):
    output = ""
    for i in range(0,n):
        output = output+ toChange[p_table[i]-1]
    return output

#découpe en deux un binaire de taille 64
def slipt(binaryinput):
    return binaryinput[:32],binaryinput[32:]

def xor(a,b):
    ans= ""
    for i in range(len(a)):
            if a[i] == b[i]:
                ans+= "0"
            else :
                ans += "1"
    return ans

#effectue la lecture du fichier ayant les chiffrés fauté, le chiffré juste
#et le message
def readKey():
    f= open("key.txt","r")
    msg = f.readline()
    msg = msg[:len(msg)-1]
    correctOut = f.readline()
    correctOut = correctOut[:len(correctOut)-1]
    dfaOutput = []
    tmp = ''
    while True:
        tmp = f.readline()
        if tmp == '':
            break
        dfaOutput.append(tmp[:len(tmp)-1])
    f.close()
    return msg,correctOut,dfaOutput

#effectue la lecture et le stockage et 2⁸ possibilités
def readPossibleKey():
    f = open("possible_2_8.txt","r")
    table = []
    tmp = ''
    while True:
        tmp = f.readline()
        if tmp == '':
            break
        table.append(tmp[:len(tmp)-1])
    f.close()
    return table

#ajoute des 0 à gauche de l'entrée binaire pour avec un binaire de taille 4 bit
def addZero(input):
    while len(input) < 4 :
         input = "0"+input
    return input

#effectue un brut force pour trouver les 6 bit de la sous clé
def findSubKey(bL,bR,L16,num):
    for i in range(0,64):
        compteur = 0
        key = brut_force_subKey[i]
        correct = xor(L16,key)
        lignecorret = int(correct[0]+correct[5],2)
        colcorrect = int(correct[1]+correct[2]+correct[3]+correct[4],2)
        s_correct = sbox[num][lignecorret][colcorrect]
        s_correct = bin(s_correct)
        s_correct = s_correct[2:]
        s_correct = addZero(s_correct)
        #on vérifie les 6 bit possible si elle correspond à tout les
        #les messages fauté ayant une faute dans le même bloc
        for j in range(0,len(bL)):
            dfa  = bL[j]
            dfa = xor(dfa,key)
            lignedfa = int(dfa[0]+dfa[5],2)
            coldfa = int(dfa[1]+dfa[2]+dfa[3]+dfa[4],2)
            s_dfa = sbox[num][lignedfa][coldfa]
            s_dfa = bin(s_dfa)
            s_dfa = s_dfa[2:]
            s_dfa = addZero(s_dfa)
            droite = xor(s_dfa,s_correct)
            if xor(bR[j],droite) == "0000":
                compteur = compteur+1
        #lorsque les 6 bit ont fonctionner pour tous les message fauté
        #ayant une faute dans le même bloc on retourne les 6 bit de K
        if compteur == len(bL):
            return key

#Permet de mettre les bon bit de parité à la clé K
def parityBit(input):
    output =''
    tmp =''
    cpt = 0
    for i in range(0,8):
        cpt = 0
        tmp = input[i*8:i*8+7]
        for k in range(0,7):
            if tmp[k] == '1':
                cpt = cpt +1
        if cpt%2 == 0:
            tmp += '0'
        else:
            tmp += '1'

        output += tmp
    return output


# fonction F du DES 
def f_function(R,K):
    R = permutation(R,expension,48)
    R= xor(K,R)
    out = ""
    for i in range(0,8):
        ligne = int(R[i*6]+R[i*6+5],2)
        col = int(R[i*6+1]+R[i*6+2]+R[i*6+3]+R[i*6+4],2)
        exit_sbox= sbox[i][ligne][col]
        exit_sbox = bin(exit_sbox)
        exit_sbox = exit_sbox[2:]
        exit_sbox= addZero(exit_sbox)
        out += exit_sbox

    return(permutation(out,per,32))

####################################
####################################
#
#         DEBUT DU PROGRAMME
#
######################################
####################################


#Lecture du fichier d'entrée
#Attribution à msg le message d'entrée
#correctOutHex le chiffré correct
#listOutput contient la liste de tous les chiffrés fauté
msg,correctOutHex,listOutput = readKey()
correctOutBin = bin(int(correctOutHex,16))
correctOutBin = correctOutBin[2:]
correctOutBin  = permutation(correctOutBin,initial_permutation,64)
R16,L16 = slipt(correctOutBin)
L16 = permutation(L16,expension,48)

#Chaque bloc représente un bloc de l'information qu'on lui donne
#on va socker dans les blocLX les bloc fauté se trouvant au découpage X
#après expension
blocL0 = []
blocL1 = []
blocL2 = []
blocL3 = []
blocL4 = []
blocL5 = []
blocL6 = []
blocL7 = []

#on va stocker dans les blocRX la xor du chiffré juste R16 xor R'16 le tout après permutation
#on stocker les 6 bit se trouvant à la même position que le bloc fauté L15 xor L'15
blocR0 = []
blocR1 = []
blocR2 = []
blocR3 = []
blocR4 = []
blocR5 = []
blocR6 = []
blocR7 = []


for k in range(0,len(listOutput)):
    L = []
    L_ = []
    DFAoutHex = listOutput[k]
    DFAoutBin = bin(int(DFAoutHex,16))
    DFAoutBin = DFAoutBin[2:]
    DFAoutBin = permutation(DFAoutBin,initial_permutation,64)

    R_16,L_16 = slipt(DFAoutBin)

    L_16 = permutation(L_16,expension,48)
    R_16 = xor(R_16,R16)
    R_16 = permutation(R_16,inv_per,32)

    for i in range(0,8):
        if xor(L16[i*6:i*6+6],L_16[i*6:i*6+6]) != brut_force_subKey[0]:
            #lorsqu'on trouve une faute dans un bloc on ajoute
            #le bloc faute dans la liste des blocs
            if i == 0:
                blocL0.append(L_16[i*6:i*6+6])
                blocR0.append(R_16[i*4:i*4+4])
            if i == 1:
                blocL1.append(L_16[i*6:i*6+6])
                blocR1.append(R_16[i*4:i*4+4])
            if i == 2:
                blocL2.append(L_16[i*6:i*6+6])
                blocR2.append(R_16[i*4:i*4+4])
            if i == 3:
                blocL3.append(L_16[i*6:i*6+6])
                blocR3.append(R_16[i*4:i*4+4])
            if i == 4:
                blocL4.append(L_16[i*6:i*6+6])
                blocR4.append(R_16[i*4:i*4+4])
            if i == 5:
                blocL5.append(L_16[i*6:i*6+6])
                blocR5.append(R_16[i*4:i*4+4])
            if i == 6:
                blocL6.append(L_16[i*6:i*6+6])
                blocR6.append(R_16[i*4:i*4+4])
            if i == 7:
                blocL7.append(L_16[i*6:i*6+6])
                blocR7.append(R_16[i*4:i*4+4])
# dans un bloc ont à tous les bloc fauté

subKey = ""
#findSubKey fait un brut force des 6 bit de la sous clé
#pour chacun des blocs
subKey +=findSubKey(blocL0,blocR0,L16[0:6],0)
subKey +=findSubKey(blocL1,blocR1,L16[6:12],1)
subKey +=findSubKey(blocL2,blocR2,L16[12:18],2)
subKey +=findSubKey(blocL3,blocR3,L16[18:24],3)
subKey +=findSubKey(blocL4,blocR4,L16[24:30],4)
subKey +=findSubKey(blocL5,blocR5,L16[30:36],5)
subKey +=findSubKey(blocL6,blocR6,L16[36:42],6)
subKey +=findSubKey(blocL7,blocR7,L16[42:48],7)

#ici on a la sous clé qui est correct
#print(subKey)




######################
#retrouver K à partir de K16
#######################

#contient 2⁸ valeurs possible que peuvent avoir 8 bit manquant
allKeyPossiblility = []
allKeyPossiblility = readPossibleKey()

#on récupère la sortie non fauté donné
correctOutBin = bin(int(correctOutHex,16))
correctOutBin = correctOutBin[2:]

#on récupère le message d'entrée
msg = bin(int(msg,16))
msg = msg[2:]

#on le découpe en deux
L,R = slipt(msg)

#on test pour les 2⁸ possibilités de 8 bit manquant
for k in range(0,len(allKeyPossiblility)):
    #on ajoute les 8 bit manquant à la fin de notre sous clé correct
    toTest = subKey + allKeyPossiblility[k]

    #on effectue l'inverse de PC2
    toTest = permutation(toTest,inv_PC_2,56)

    #ajout des bit de parité
    toTest += '00000000'
    #on effectue l'inverse de PC1
    toTest = permutation(toTest,inv_PC_1,64)
    #on met à jour les 8 bit de parité
    toTest = parityBit(toTest)

    #Vérification de cette propostion de clé

    #on applique PC1 sur notre clé potentiel
    toTest_P = permutation(toTest,PC_1,56)
    subkeyToTest = ""
    #on applique la Initial permutation sur le message
    msg =permutation(msg,initial_permutation,64)
    L,R = slipt(msg)
    C = toTest_P[0:28]
    D = toTest_P[28:]

    #on refait tout le DES
    for tour in range(0,16):
        #shift des moitié de clé selon le tour
        for rotate in range(0,shift_table[tour]):
            C= C[1:]+C[0]
            D = D[1:] +D[0]
        subkeyToTest = C+D
        #on applique PC2
        subkeyToTest = permutation(subkeyToTest,PC_2,48)
        tmp= R
        #passage de la sous clé dans la fonction F avec R
        R= f_function(R,subkeyToTest)
        R = xor(R,L)
        L = tmp
    #fin du DES on relie R16 avec L16
    verif = R +L
    # on effectue la permutation inverse
    verif = permutation(verif,final_permutation,64)
    #Vérification du chiffré obtenu avec le chiffré correct donné
    if xor(correctOutBin,verif) == '0000000000000000000000000000000000000000000000000000000000000000':
        print("La clé est : ")
        print(hex(int(toTest,2)))
        break
