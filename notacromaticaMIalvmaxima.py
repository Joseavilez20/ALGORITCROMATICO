import math
import numpy as np
import random
from Maximaalv import maximaalv
#NOTA: El cambio de la estructura case podría afectar el resultado si
#no se estructura correctamente las condicionales if ,elif etc
def notacromaticaMIalvmaxima(pobinicial2,v,mejor1,opp,ll,matrizdatos,matrizai,t,rr):

    h = np.zeros((1,v), dtype=float, order='C') #new line
    
    #$$$$$$$$$$$$$ ANALIZAR POR QUE 0:V] Y NO 0:V-1] $$ CHANGED
    h[0,:] = pobinicial2[ll-1,:v]     
    for u in range(1,v+1):
        matrizdatos2 = np.copy(matrizdatos) #$$$$
        e = h[0,u-1]
       
        z1 =None
        dar = random.uniform(0,1)

        #%opp=0.483767
        if dar < opp:
            
            pobinicial2[ll-1,u-1] = mejor1[0,u-1]
            
        else:
            
            temp1 =  math.ceil(e/0.5);
            nota2 = temp1 - 12 * math.floor(temp1/12)
            #if 0<= nota2<=11
            r1 = math.floor(temp1/12)
            
            
            if nota2 == 0:
                
                z1= ((r1)*6) -0.5
                
            elif nota2 == 1:
                
                z1= ((r1)*6)
                
            elif nota2 == 2:
                
                z1= ((r1)*6) + 0.5
                
            elif nota2 == 3:
                
                z1= ((r1)*6) + 1
                
            elif nota2 == 4:
                
                z1= ((r1)*6) + 1.5
                
            elif nota2 == 5:
                
                z1= ((r1)*6) + 2
                
            elif nota2 == 6:
                
                z1= ((r1)*6)+ 2.5
                
            elif nota2 == 7:
                
                z1= ((r1)*6) + 3
                
            elif nota2 == 8:
                
                z1= ((r1)*6) + 3.5
                
            elif nota2 == 9:
                
                z1= ((r1)*6) + 4
                
            elif nota2 == 10:
                
                z1= ((r1)*6) + 4.5
                
            elif nota2 == 11:
                
                z1= ((r1)*6) + 5
                
            else:
                print('Default')
        if z1 is not None:        
            pobinicial2[ll-1,:] = maximaalv(pobinicial2,e,v,u,z1,matrizdatos2,matrizai,t,rr,ll)
        #endif
        
        
    #endfor
##    mejorTemsab1= np.zeros((1,v+1), dtype=float, order='C') #new line
##    mejorTemsab1[0,0:v-1]=pobinicial2[ll-1,0:v-1]
    
    #$$$$ ANALIZAR POR QUE 0:V] Y NO 0:V-1]$$$$$
    return pobinicial2[ll-1,0:v] #changed

