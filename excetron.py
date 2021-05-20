import pandas as pd
#import numpy as np

def entrenar(theta,fac_ap,w1,w2,epochs,x1,x2,d,n_muestras):
    errores = True
    while errores:
        errores = False
        for i in range(n_muestras):
            z = ((x1[i] * w1)+(x2[i] * w2)) - theta
            
            if z>= 0:
                z = 1
            else:
                z = 0
            
            if z != d[i]:
                errores = True
                
                error = (d[i] - z)
                
                theta = theta + (-(fac_ap * error))
                
                w1 = w1 + (x1[i] * error * fac_ap)
                w2 = w2 + (x2[i] * error * fac_ap)
                epochs +=1
    return w1, w2, epochs, theta
            
if __name__ == "__main__":

    archivo_excel = pd.read_excel("/home/tomer/Documentos/apendiceA.xlsx")
    theta = 0.4
    fac_ap = 0.2
    w1 = 0.3
    w2 = 0.5
    epochs = 0
    x1 = archivo_excel["x1"]
    x2 = archivo_excel["x2"]
    d = archivo_excel["d"]
    n_muestras = len(d)
    w1, w2, epochs, theta = entrenar(theta,fac_ap,w1,w2,epochs, x1,x2,d,n_muestras)
    print ("w1 = ", w1)
    print ("w2 = ", w2)
    print ("theta = ", theta)
    print ("epochs = ", epochs)  
