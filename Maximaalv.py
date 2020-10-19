import numpy as np

from evaluacionalvr2dummi import evaluacionalvr2
def maximaalv(pobinicial,e,v,u,z1,matrizdatos,matrizai,t,rr,ll):

    a = None
    b = None
    c = None
    if e>=z1 and  e<=(z1 + 0.25): 
        a = z1
        b = e
        c = z1 + 0.25
    #endif
    if e>=(z1+0.25) and  e<=(z1 + 0.5): 
        a = z1 + 0.25
        b = e
        c = z1 + 0.5
    #endif    
    primero = np.zeros((2, v+1), dtype=float, order='C')
    primero[0,:] = pobinicial[ll-1,:]
    primero[1,:] = pobinicial[ll-1,:]
    primero[0,u-1] = np.random.uniform(a, b, size=(1,1))
    primero[1,u-1] = np.random.uniform(b, c, size=(1,1))

    
    busqueda = np.zeros((2, v), dtype=float, order='C')
    #$$$$$$$$$$$ ANALIZAR DONE $$$$$$$$$$$$$$$
    busqueda[0,:] = primero[0,0:v]
    busqueda[1,:] = primero[1,0:v]
    
    
    R = np.zeros((2,1), dtype=float, order='C')


    for m in range(1,3):
      

        matrizai = evaluacionalvr2(busqueda,matrizdatos,m,rr,matrizai,t)
        
        for s in range(1,t+1):
            if matrizai.shape[1] < rr:
                    matrizai = np.hstack((matrizai,[[0]]*t))
                    
            matrizai[s-1,rr-1] = sum(matrizai[s-1,:])
                
        #endfor
        
        
        promedioai = np.mean(matrizai[:,rr-1])
        ybarra = np.mean(matrizdatos[:,rr-1])
        K = ybarra/promedioai

        for w in range(1,t+1):
            matrizdatos[w-1,rr] = K*matrizai[w-1,rr-1]
        #endfor


        for zx in range(1,t+1):
            matrizdatos[zx-1,rr+1] =  matrizdatos[zx-1,rr-1] - matrizdatos[zx-1,rr]
        #endfor


        for sa in range(1,t+1):
            matrizdatos[sa-1,rr+2]= matrizdatos[sa-1,rr] - ybarra
            
        #endfor
        

        sse = sum(matrizdatos[:,rr+1]**2)
        ssr = sum(matrizdatos[:,rr+2]**2)
        sst = sse + ssr

        R[m-1,0] = ssr /sst
         
    #endfor
    

    if busqueda.shape[1] < v+1:  #new line
        busqueda = np.hstack((busqueda,[[0]]*2))

    busqueda[:,v] = R.T 

    orden111 = busqueda[np.argsort(busqueda[:,v])]
    
    
    mejorTem111 = np.zeros((1,v+1), dtype=float, order='C')
    #$$$$$$$$$$$
    mejorTem111[0,0:v] = orden111[orden111.shape[0]-1,0:v]
    pobinicial = mejorTem111
             
    mas = pobinicial
   
    return mas
