import numpy as np

X = [1,2,3,4,5]
Y = [3,4,2,4,5]

n = len(X)
sumx = sum(X)
sumy = sum(Y)

xmean = sumx / n

ymean = sumy/n

print("Length : ",n)
print("Sum of X:",sumx)
print("Sum of Y:",sumy)

# x = Summation of X divide by lenth
print("Summation of X divide by lenth:",xmean)
print("Summation of Y divide by lenth:",ymean)

#---------------------------------------------
# caluclate slope
summation = sum((X[i] - xmean)* (Y[i] - ymean) for i in range(n))
print("Summation of (X - x̄)(Y - ȳ):", summation)

summationx = sum((X[i] - xmean)**2 for i in range(n))

print(summationx)

m = summation / summationx

print("Slope :",m)
#------------------------------------------------
#Calculate intercept
b  = ymean - (m * xmean)
print("intercept:",b)
#--------------------------------------

#Final regression equation
yp = [m * X[i] + b for i in range(n)]
print("Predicted values",yp)

#-----------------------------------------
#Residual error 
re = [Y[i] - yp[i] for i in range(n)]

for r in re:
 print(f"Residual error:{r:.2f}")

#--------------------------------------

Mse = sum((Y[i] - yp[i])**2 for i in range(n))/n
print("MSE:",Mse)


