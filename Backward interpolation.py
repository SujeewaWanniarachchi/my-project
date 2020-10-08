 
def u_cal(u, n): 
    temp = u; 
    for i in range(1, n): 
        temp = temp * (u + i); 
    return temp; 

def fact(n): 
    f = 1; 
    for i in range(2, n+1): 
        f *= i; 
    return f; 

n = 5; 
x = [ 70, 80, 90, 100, 110]; 

y = [[0 for i in range(n)] 
        for j in range(n)]; 
y[0][0] = 30; 
y[1][0] = 35; 
y[2][0] = 47; 
y[3][0] = 58; 
y[4][0] = 70;

for i in range(1, n): 
    for j in range(n): 
        y[j][i] = y[j][i - 1] - y[j - 1][i - 1]; 

for i in range(n): 
    print(x[i], end = "\t"); 
    for j in range(i+1): 
        print(y[i][j], end = "\t"); 
    print(""); 

value = 95; 

sum = y[n - 1][0]; 
u = (value - x[n - 1]) / (x[1] - x[0]); 
for i in range(1,n): 
    sum = sum + (u_cal(u, i) * y[n - 1][i]) / fact(i); 
  
print("\nValue at", value,  "is", round(sum, 6));

      
      
      
      
      
      
      
