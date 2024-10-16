import numpy as np 

#function for factorial used in macLaurin series
def factorial(k):                           
    facValue = 1                
    for k in range(1,k + 1):   
        facValue *= k
    return facValue             

 #function for macLaurin series of e^x
def macLaurin(x, n):                       
    macValue = 0                           
    for k in range(0, n+1):                 
        macValue += x**k / factorial(k)
    return macValue                         

#the absolute error function 
def abserr(x1, x2):                                                                            
    return np.linalg.norm(np.array(storArray) - np.array(compArray))                                

#the relative error function
def relerr(x1, x2):                                                                                 
    return (np.linalg.norm(np.array(storArray) - np.array(compArray)))/np.linalg.norm(storArray)    

x = [2, 4, 6, 9, 10, 12, 15, 18, 20, 25]
n = [10, 20, 50, 75, 100, 125] 

#for loop to execute the whole program
print("n \tAbsolute Error  \t Relative Error")
for k in n:         
    storArray = []
    compArray = []
    for i in x:
        storArray.append(np.exp(i))
        compArray.append(macLaurin(i,k))
    print(f"{k}\t{abserr(storArray,compArray):.15e} \t {relerr(storArray, compArray):.15e}")

    
