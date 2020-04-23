from array import *

iptable = [40 ,8,48,16,56,24,64,32,
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

s_box =['000000','000001','000010',
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

initial_perm = [58, 50, 42, 34, 26, 18, 10, 2,
                60, 52, 44, 36, 28, 20, 12, 4,
                62, 54, 46, 38, 30, 22, 14, 6,
                64, 56, 48, 40, 32, 24, 16, 8,
                57, 49, 41, 33, 25, 17, 9, 1,
                59, 51, 43, 35, 27, 19, 11, 3,
                61, 53, 45, 37, 29, 21, 13, 5,
                63, 55, 47, 39, 31, 23, 15, 7]

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

def permutation(toChange, p_table,n):
    output = ""
    for i in range(0,n):
        output = output+ toChange[p_table[i]-1]
    return output

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

def printTheArray(arr,n):
    for i in range(n):
        print(arr[i],end='')

    print ()

def generateBinaryString(n,arr,i):
    if i ==n:
        printTheArray(arr,n)
        return arr
    arr[i]=0
    generateBinaryString(n,arr,i+1)

    arr[i] = 1
    generateBinaryString(n,arr,i+1)

def bin2dec(binary):
    decimal, i, n = 0, 0, 0
    while(binary != 0):
        dec = binary % 10
        decimal = decimal + dec * pow(2, i)
        binary = binary//10
        i += 1
    return decimal


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

def addZero(input):
    while len(input) < 4 :
         input = "0"+input
    return input

def mediumBloc(bloc):
    a = 0
    resu =""
    for j in range(0,6):
        a=0

        for i in range(0,len(bloc)):
            a = a+int(bloc[i][j],2)
        a = a/len(bloc)
        if a > 0.5 :
            resu += "1"
        else :
            resu += "0"
    return resu

def findSubKey(bL,bR,L16,num):
    for i in range(0,64):
        compteur = 0
        key = s_box[i]
        correct = xor(L16,key)
        lignecorret = bin2dec(int(correct[0]+correct[5]))
        colcorrect = bin2dec(int(correct[1]+correct[2]+correct[3]+correct[4]))
        s_correct = sbox[num][lignecorret][colcorrect]
        s_correct = bin(s_correct)
        s_correct = s_correct[2:]
        s_correct = addZero(s_correct)
        for j in range(0,len(bL)):
            dfa  = bL[j]
            dfa = xor(dfa,key)
            lignedfa = bin2dec(int(dfa[0]+dfa[5]))
            coldfa = bin2dec(int(dfa[1]+dfa[2]+dfa[3]+dfa[4]))
            s_dfa = sbox[num][lignedfa][coldfa]
            s_dfa = bin(s_dfa)
            s_dfa = s_dfa[2:]
            s_dfa = addZero(s_dfa)
            droite = xor(s_dfa,s_correct)
            if xor(bR[j],droite) == "0000":
                compteur = compteur+1
        if compteur == len(bL):
            return key


msg,correctOutHex,listOutput = readKey()
correctOutBin = bin(int(correctOutHex,16))
correctOutBin = correctOutBin[2:]
correctOutBin  = permutation(correctOutBin,initial_perm,64)
R16,L16 = slipt(correctOutBin)
L16 = permutation(L16,expension,48)

blocL0 = []
blocL1 = []
blocL2 = []
blocL3 = []
blocL4 = []
blocL5 = []
blocL6 = []
blocL7 = []

blocR0 = []
blocR1 = []
blocR2 = []
blocR3 = []
blocR4 = []
blocR5 = []
blocR6 = []
blocR7 = []
a=0

#len(listOutput)
for k in range(0,len(listOutput)):
    L = []
    L_ = []
    DFAoutHex = listOutput[k]
    DFAoutBin = bin(int(DFAoutHex,16))
    DFAoutBin = DFAoutBin[2:]
    DFAoutBin = permutation(DFAoutBin,initial_perm,64)
    #print(DFAoutBin )
    R_16,L_16 = slipt(DFAoutBin)
    #print(R_16+ " R_16")
    L_16 = permutation(L_16,expension,48)
#    print("-----------------------------")
#    print(L_16+ " L_16")
    R_16 = xor(R_16,R16)
    R_16 = permutation(R_16,inv_per,32)

    # permet d'avoir la liste des blocs fauté
    listOfSelectedBlock = []
    #print(R_16 +" xor(R16,R_16)")
    #print(xor(L16,L_16)+ " xor(L16,L-16)")
    #print(L_16 +" L_16")
    for i in range(0,8):
        if xor(L16[i*6:i*6+6],L_16[i*6:i*6+6]) != s_box[0]:
        #    print(L_16)
    #        print(i)
        #    print(L_16[i*6:i*6+6] +" ajout bL")
    #        print(R_16[i*4:i*4+4]+ "ajout BR")
            #L.append(L16[i*6:i*6+6])
            #L_.append(L_16[i*6:i*6+6])
            #listOfSelectedBlock.append(i)
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

key = ""

key +=findSubKey(blocL0,blocR0,L16[0:6],0)
key +=findSubKey(blocL1,blocR1,L16[6:12],1)
key +=findSubKey(blocL2,blocR2,L16[12:18],2)
key +=findSubKey(blocL3,blocR3,L16[18:24],3)
key +=findSubKey(blocL4,blocR4,L16[24:30],4)
key +=findSubKey(blocL5,blocR5,L16[30:36],5)
key +=findSubKey(blocL6,blocR6,L16[36:42],6)
key +=findSubKey(blocL7,blocR7,L16[42:48],7)


print(key)

# for m in range(0,len(listOfSelectedBlock)):
    #     index = listOfSelectedBlock[m]
    #     #Quand y a 2 bloc faux il en prend 1
    #     R_16new = R_16[index*4:index*4+4]
    #     dfa = L_[m]
    #     correct = L[m]
    #     for j in range (0,63):
    #         #dfa à le bloc fauté
    #         # correct à le même bloc mais non fauté
    #
    #         dfa = xor(dfa,s_box[j])
    #         correct = xor(correct,s_box[j])
    #
    #         lignedfa = bin2dec(int(dfa[0]+dfa[5]))
    #         coldfa = bin2dec(int(dfa[1]+dfa[2]+dfa[3]+dfa[4]))
    #         lignecorret = bin2dec(int(correct[0]+correct[5]))
    #         colcorrect = bin2dec(int(correct[1]+correct[2]+correct[3]+correct[4]))
    #
    #         s_dfa = sbox[m][lignedfa][coldfa]
    #         s_dfa = bin(s_dfa)
    #         s_dfa = s_dfa[2:]
    #         s_dfa = addZero(s_dfa)
    #
    #         s_correct = sbox[i][lignecorret][colcorrect]
    #         s_correct = bin(s_correct)
    #         s_correct = s_correct[2:]
    #         s_correct = addZero(s_correct)
    #
    #         droit = xor(s_correct,s_dfa)
    #         if xor(R_16new,droit) == "0000":
    #             if index == 0:
    #                 bloc0.append(s_box[j])
    #             if index == 1:
    #                 bloc1.append(s_box[j])
    #
    #             if index == 2:
    #                 bloc2.append(s_box[j])
    #
    #             if index == 3:
    #                 bloc3.append(s_box[j])
    #
    #             if index == 4:
    #                 bloc4.append(s_box[j])
    #
    #             if index == 5:
    #                 bloc5.append(s_box[j])
    #
    #             if index == 6:
    #                 bloc6.append(s_box[j])
    #
    #             if index == 7:
    #                 bloc7.append(s_box[j])
    #
    #             a =a+1

# print(bloc0)
# print(bloc1)
# print(bloc2)
# print(bloc3)
# print(bloc4)
# print(bloc5)
# print(bloc6)
# print(bloc7)
                #for i in range(0,8):

                # R16 xor R'16 == (P(Si(L16))  xor K16 ) xor (P(Si(L'16))  xor K16 )  afficher K16
                #    if xor(R16[i*6:i*6+6],R_16[i*6:i*6+6]) == xor(xor(L16[i*6:i*6+6],s_box[j]),xor(L_16[i*6:i*6+6],s_box[j])):

#key = mediumBloc(bloc0)+ mediumBloc(bloc1)+mediumBloc(bloc2)+"011010"+mediumBloc(bloc4)+mediumBloc(bloc5)+"001100"+"101100"

#Test de la clé 010110

DFAoutHex = listOutput[4]
DFAoutBin = bin(int(DFAoutHex,16))
DFAoutBin = DFAoutBin[2:]
DFAoutBin = permutation(DFAoutBin,initial_perm,64)
R_16,L_16 = slipt(DFAoutBin)
L_16 = permutation(L_16,expension,48)
resu = xor(L_16,key)
#print(resu)
passageSbox = ""
passageSboxCorrect = ""
for i in range(0,8):
    tmp = resu[i*6:i*6+6]
#    print("----")
#    print(tmp)
    ligne = bin2dec(int(tmp[0]+tmp[5]))
    col = bin2dec(int(tmp[1]+tmp[2]+tmp[3]+tmp[4]))
    s_tmp = sbox[i][ligne][col]
    s_tmp = bin(s_tmp)
    s_tmp = s_tmp[2:]
    s_tmp = addZero(s_tmp)
#    print(s_tmp)
    passageSbox += s_tmp
passageSbox = permutation(passageSbox,per,32)
resu = xor(L16,key)
for i in range(0,8):
    tmp = resu[i*6:i*6+6]
    ligne = bin2dec(int(tmp[0]+tmp[5]))
    col = bin2dec(int(tmp[1]+tmp[2]+tmp[3]+tmp[4]))

    s_tmp = sbox[i][ligne][col]
    s_tmp = bin(s_tmp)
    s_tmp = s_tmp[2:]
    s_tmp = addZero(s_tmp)
    passageSboxCorrect += s_tmp

passageSboxCorrect = permutation(passageSboxCorrect,per,32)

droite = xor(passageSbox,passageSboxCorrect)

resu = xor(R16,R_16)
#print(resu)
#print(passageSbox)
print(xor(resu,droite))

#
# print(bloc1)
# print(bloc2)
# print(bloc3)
# print(bloc4)
# print(bloc5)
# print(bloc6)
# print(bloc7)
# # print(a)
# K16 : 48bit
#On sait ou sont les 8bit manquant et faire brut force sur les 8 bit
