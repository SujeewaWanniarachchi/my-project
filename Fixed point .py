
def fixedp(g,x0, tol, max_itr):
    e =1
    itr = 0
    xp = []
    while (e > tol and itr <max_itr):
        x = g(x0) #fixed point equation
        e = abs(x0-x) # error of current iteration
        x0 = x
        xp.append(x0) 
        itr =+ 1
    print("Root of g(x) = ", x)
    print("No of Iterations = ",len(xp) )

def g(x):
    g = (3*x + 2)**(1/2)
    return g

x0 =2
tol = 0.001
max_itr = 50
fixedp(g,x0, tol, max_itr)







