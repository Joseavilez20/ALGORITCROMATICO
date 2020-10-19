#parameters 
#pobinicial2 :array 10x40 uniform distribution
#matrizdatos :array data excel
#matrizai : array 72x2 with zeros
#m : iteration
#rr : 3 columns
#t : 72 rows
import numpy as np
import math
def evaluacionalvr2(pobinicial2, matrizdatos, m, rr, matrizai, t):
    #se redeclara matrizai para que vuelva a contener zeros
    matrizai = np.zeros((t, rr-1), dtype=float, order='C') #newline
    for k in range(1,t+1):
        
        for j in range(1,(rr-1)+1):
            
            g1= (pobinicial2[m-1][1+(20*(j-1))-1]) +( pobinicial2[m-1][2+(20*(j-1))-1])*((matrizdatos[k-1][j-1])**(pobinicial2[m-1][10+(20*(j-1))-1]))+( pobinicial2[m-1][3+(20*(j-1))-1])*((matrizdatos[k-1][j-1])**(pobinicial2[m-1][11+(20*(j-1))-1]))+(pobinicial2[m-1][4+(20*(j-1))-1])*((matrizdatos[k-1][j-1])**(pobinicial2[m-1][12+(20*(j-1))-1]))+ (pobinicial2[m-1][5+(20*(j-1))-1])*((matrizdatos[k-1][j-1])**(pobinicial2[m-1][13+(20*(j-1))-1]))+(pobinicial2[m-1][6+(20*(j-1))-1])*((matrizdatos[k-1][j-1])**(pobinicial2[m-1][14+(20*(j-1))-1]))
            
            g2=(abs(pobinicial2[m-1][7+(20*(j-1))-1])+1)**((pobinicial2[m-1][15+(20*(j-1))-1])*(abs(matrizdatos[k-1][j-1]))) +(pobinicial2[m-1][(8+(20*(j-1)))-1])*(math.sin(pobinicial2[m-1][16+(20*(j-1))-1]*(matrizdatos[k-1][j-1])))+(pobinicial2[m-1][(9+(20*(j-1)))-1])*(math.cos((pobinicial2[m-1][(17+(20*(j-1)))-1])*(matrizdatos[k-1][j-1])));

            if g1 > 0: 
               g4 = g1
            else:
               g4 = 1
               
            g = g1 + g2

            g3 = (pobinicial2[m-1][(18+(20*(j-1)))-1])+(pobinicial2[m-1][(19+(20*(j-1)))-1])*(g +(pobinicial2[m-1][(20+(20*(j-1)))-1])*(math.log(g4)))

            z = g/g3

            matrizai[k-1][j-1] = z
            
            
        #endfor
    #endfor
    return matrizai
    
