### -*- coding: utf-8 -*-
###
#
#
# coding: utf-8
#
# In[1]:
#
#get_ipython().magic(u'pylab inline')
#
#
## In[3]:
#
#import scipy as sp
#import time
# 
#
#class Heat_Equation(object):
#    """
#    Class which implements a numerical solution of the 2d heat equation
#    """
#    def __init__(self, dx, dy, a, kind, timesteps = 1):
#                 self.dx = dx # Interval size in x-direction.
#                 self.dy = dy # Interval size in y-direction.
#                 self.a = a # Diffusion constant.
#                 self.timesteps = timesteps  #Number of time-steps to evolve system.
#                 self.dx2 = dx**2
#                 self.dy2 = dy**2
#                 self.nx = int(1/dx)
#                 self.ny = int(1/dy)
#                # For stability, this is the largest interval possible
#                # for the size of the time-step:
#                 self.dt = self.dx2*self.dy2/( 2*a*(self.dx2+self.dy2) )
#                 self.u,self.ui = self.get_initial_conditions(kind)
#                    
#    def get_initial_conditions(self, kind):
#        # Start u and ui off as zero matrices:
#        ui = sp.zeros([self.nx,self.ny])
#        u = sp.zeros([self.nx,self.ny])
#        # Now, set the initial conditions (ui).
#        for i in range(self.nx):
#            for j in range(self.ny):
#                if kind == "two_circles":
#                    p = (i*self.dx - 0.5)**2 + (j*self.dy - 0.5)**2
#                    if ( p  <= .03 and p >= 0.020 ):
#                        ui[i,j] = 1
#                    elif ( p  <= .108 and p >= 0.09 ):
#                        ui[i,j] = 1
#                elif kind == "part_circle":
#                    p = (i*self.dx - 0.5)**2 + (j*self.dy - 0.5)**2
#                    if ( p  <= .01 and p >= 0.009):
#                        ui[i,j] = 1
#                elif kind == "four_blobs":
#                    p = (i*self.dx - .4)**2 + (j*self.dy - .4)**2
#                    if ( p  <= 0.02 and p >= 0.02):
#                        ui[i,j] = 1
#                elif kind == "two_blobs":
#                    p = (i*self.dx - .4)**2 + (j*self.dy - .4)**2
#                    if ( p  <= 0.05 and p >= .05):
#                        ui[i,j] = 1
#                elif kind == "half_moon":
#                    p = (i*self.dx-.2)**2+(j*self.dy-.2)**2
#                    if ( p <= 0.1 and p >=.05 ):
#                        ui[i,j] = 1
#                elif kind == "2_lines":
#                    p = (i*self.dx-.5)**2+(j*self.dy-j*.4)**2
#                    if ( p <= 0.1 and p >=.05 ):
#                        ui[i,j] = 1
#                elif kind == "circle":
#                    p = (i*self.dx-0.5)**2+(j*self.dy-0.5)**2
#                    if ( p <= 0.1 and p >=.05 ):
#                        ui[i,j] = 1
#                elif kind == "lower_blob":
#                    p = (i*self.dx-0.)**2+(j*self.dy-0.)**2 
#                    if ( p <= 0.1 and p >=.05 ):
#                        ui[i,j] = 1
#                elif kind  == "two_half_moons":
#                    p = (i*self.dx - 0.5)**3 + (j*self.dy - 0.5)**3
#                    if ( p  <= .03 and p >= 0.020 ):
#                        ui[i,j] = 1
#                    elif ( p  <= .108 and p >= 0.09 ):
#                        ui[i,j] = 1
#        return u,ui
#    
#    def evolve_ts(self):
#        self.u[1:-1, 1:-1] = self.ui[1:-1, 1:-1] + self.a*self.dt*( (self.ui[2:, 1:-1] - 2*self.ui[1:-1, 1:-1] + self.ui[:-2, 1:-1])/self.dx2 + (self.ui[1:-1, 2:] - 2*self.ui[1:-1, 1:-1] + self.ui[1:-1, :-2])/self.dy2 )
#        self.ui = self.u.copy()
#        
#def evolve_ts(u, ui):
#    global nx, ny
#    """
#    This function uses two plain Python loops to
#    evaluate the derivatives in the Laplacian, and
#    calculates u[i,j] based on ui[i,j].
#    """
#    for i in range(1,nx-1):
#        for j in range(1,ny-1):
#            uxx = ( ui[i+1,j] - 2*ui[i,j] + ui[i-1, j] )/ dx2
#            uyy = ( ui[i,j+1] - 2*ui[i,j] + ui[i, j-1] )/ dy2
#            u[i,j] = ui[i,j]+dt*a*(uxx+uyy)
#
#
## In[4]:
#
#from tempfile import NamedTemporaryFile
#
#def anim_to_mp4(anim,k):
#    if not hasattr(anim, '_encoded_video'):
#        with NamedTemporaryFile(suffix='.mp4') as f:
#            newname = "/tmp/" + k + f.name.split("/")[-1]
#            print newname
#
#            anim.save(newname, fps=20, extra_args=['-vcodec', 'libx264', '-pix_fmt', 'yuv420p'])    
#    return None
#
#def save_animation(anim,k):
#    plt.close(anim._fig)
#    return anim_to_mp4(anim,k)
#
#
## In[5]:
#
#from matplotlib import animation
##initial_shapes = ["two_circles", "part_circle", "four_blobs", "two_blobs", "half_moon", "two_half_moons", "2_lines", "circle", "lower_blob"]
#initial_shapes = ["two_circles"]
#
#for k in initial_shapes:
#    test_heat = Heat_Equation(0.001,0.001,.5,k,1)    
#    
#    # First set up the figure, the axis, and the plot element we want to animate
#    
#    
#    fig = plt.figure()
#    img = plt.subplot(111)
#    
#    im = img.imshow(test_heat.ui, cmap=get_cmap("hot"), interpolation='nearest', origin='lower')
#    im.figure = fig
#    fig.colorbar(im)
#                
#    def animate(i,im):
#        if i % 50 == 0:
#            print i
#        test_heat.evolve_ts()
#        im.set_array(test_heat.ui)
#
#        return [im]
#        
#        
#    anim = animation.FuncAnimation(fig, animate, frames=2000, fargs=(im,),  interval=30, blit=True)
#save_animation(anim,k)
#x=print(get_values())
#        
#
#def list(*food):
#    print(food)
#    
#    
#list('apples')
#list('apples','peaches','beef')
#
##
#def profile(name,last,*ages,**items):
#    print(name)
#    print(ages)
#    print(ages)
#    print(items)
#profile('becky','kamal', 20, 25, 30, 15, bacon=3,sweet=4,suya=3)
#
#def cart(**items):
#    print (items)
#    
#cart(apples=2,peaches=6,beefs=5)
#
#
#def example(a,b,c):
#    return a+b*c
#tuna = (2,5,4)
#
#print (example(*tuna))
#
#def example2(**this):
#    print (this)
#
#fruits= {'apples': 2, 'peaches': 6, 'beefs': 5}
#
#example2(**fruits)
#
#
##class exampleclass:
##    eyes='blue'
##    age = 22
##    def thismethod(self):
##        return('hey this method works')
##    
##    
#exampleobject=exampleclass()
#print(exampleobject.eyes)
#
#print(exampleobject.thismethod())
#
#
#class classname:
#    def createname(self,name):
#        self.name= name
#    def displayname(self):
#        return self.name
#    def saying(self):
#        print(self.name)
#        
#
#first=classname()
#second=classname()
#first.createname('kamal')
#second.createname('adekola')
#print(first.displayname())
#first.saying()
#second.saying()
#
#
#constructors
#class new:
#    def __init__(self):
#        print('this is a new class')
#        print('i love printing')
#        
#newclass= new()
#
#((course_offered),(credit))=input('ENTER (course code,credit unit): ')
#print((course_offered,credit))
#
#
#
#
#
#def most_common_words(freqs):
#    values = freqs.values()
#    print(values)
#    best = max(freqs.values())
#    words = []
#    for k in freqs:
#        if freqs[k] == best:
#            words.append(k)
#    return (words, best)
#
#lst=[]
#freqs = {'mee111': 2,'mee112': 82}
#for k,v in freqs.items():
#    lst.append(v)
#print(lst)
#
#
#print(most_common_words(freqs))
#
#
#class Coordinate(object):
#    """ A coordinate made up of an x and y value """
#    def __init__(self, x, y):
#        """ Sets the x and y values """
#        self.x = x
#        self.y = y
#    def __str__(self):
#        """ Returns a string representation of self """
#        return "(" + str(self.x) + "," + str(self.y) + ")"
#    def distance(self, other):
#        """ Returns the euclidean distance between two points """
#        x_diff_sq = (self.x-other.x)**2
#        y_diff_sq = (self.y-other.y)**2
#        return (x_diff_sq + y_diff_sq)**0.5
#
#
#
#c= Coordinate(3,4)
#origin=Coordinate(0,0)
#print(c.distance(origin))
#print(c)
#print(type(Coordinate))
#print(isinstance(c,Coordinate))
#
#
#origin = Coordinate(0,0)
#print(c.x, origin.x)
#print(c.distance(origin))
#print(Coordinate.distance(c, origin))
#print(origin.distance(c))
#print(c)
#        
#
#class Fraction(object):
#    """
#    A number represented as a fraction
#    """
#    def __init__(self, num, denom):
#        """ num and denom are integers """
#        assert type(num) == int and type(denom) == int, "ints not used"
#        self.num = num
#        self.denom = denom
#    def __str__(self):
#        """ Retunrs a string representation of self """
#        return str(self.num) + "/" + str(self.denom)
#    def __add__(self, other):
#        """ Returns a new fraction representing the addition """
#        top = self.num*other.denom + self.denom*other.num
#        bott = self.denom*other.denom
#        return Fraction(top, bott)
#    def __sub__(self, other):
#        """ Returns a new fraction representing the subtraction """
#        top = self.num*other.denom - self.denom*other.num
#        bott = self.denom*other.denom
#        return Fraction(top, bott)
#    def __float__(self):
##        """ Returns a float value of the fraction """
#        return self.num/self.denom
#    def inverse(self):
#        """ Returns a new fraction representing 1/self """
#        return Fraction(self.denom, self.num)
#
#a = Fraction(1,4)
#b = Fraction(3,4)
#c = a + b # c is a Fraction object
#print(c)
#print(float(c))
#print(Fraction.__float__(c))
#print(float(b.inverse()))
#
#############
## EXAMPLE: a set of integers as class
##############
#
#
#s = intSet()
##print(s)
#s.insert(3)
#s.insert(4)
#s.insert(3)
#print(s)
#s.member(3)
#print(s.member(5))
#s.insert(6)
#print(s)
##s.remove(3)  # leads to an error
#print(s)
#s.remove(3)
#
#
#
#from operator import itemgetter
#
#def format_as_table(data,keys,header=None,sort_by_key=False,sort_order_reverse=False):
#    if sort_by_key:
#        data=sorted(data,key=itemgetter(sort_by_key),reverse=sort_order_reverse)
#    if header:
#        for name in header:
#            header_divider.append('-'*len(name))
#
#
#summation=0
#for i in range(0,16):
#    summation+=i
#print(summation)
#
#N=15
#for i in range(N+1):
#    if i != N:
#        print(i,end='+')
#    else:
#        print(i)
#
##n=0
#
#
#"""
#Write a program that asks the number of courses she has registered in a semester. The code should ask
#for the course codes the respective credit units. After entering the courses the code should ask for 
#the scores in each course. The code will then output the transcript with the GPA using the following
#A       70-100      5
#B       60-69       4
#C       50-59       3
#D       46-49       2
#E       40-45       1
#F       00-39       0
#"""
#
#number_of_courses_registered = input("Enter number of courses registered for the semester: ")
#container = []
#for i in range(int(number_of_courses_registered)):
#    course_code = input("Enter course code for course %d: "%(i+1))
#    credit_unit = int(input("Enter credit unit for %s: "%course_code))
#    score = int(input("Enter score for %s: "%course_code))
#    value = None
#    grade = None
#    if score >=70:
#        value = 5
#        grade= "A"
#    elif score >=60 and score < 70:
#        value = 4
#        grade = "B"
#    elif score >=50 and score < 60:
#        value = 3
#        grade = "C"
#    elif score >= 46 and score < 50:
#        value = 2
#        grade="D"
#    elif score >= 40 and score < 46:
#        value = 1
#        grade="E"
#    else:
#        value = 0
#        grade="F"
#    container.append(dict(course_code=course_code,credit_unit=credit_unit,score=score,value_point=value,grade=grade))
#numerator = 0
#denominator = 0
#for item in container:
#    item_product = item['value_point'] * item['credit_unit']
#    numerator += item_product
#    denominator += item['credit_unit']
#
#gpa = numerator/denominator
#print("\n%-20s%-20s%-20s%-20s"%("Course Code","Credit Unit","Score","Grade"))
#for item in container:
#    print("%-20s%-20s%-20s%-20s"%(item['course_code'],item['credit_unit'],item['score'],item["grade"]))
#print("\n")
#print("And the gpa is  %s"%str(gpa))
#
#import numpy as np
#zero_vector=np.zeros(5)
#zero_matrix=np.zeros((5,3))
#
#print(zero_vector)
#print(zero_matrix)
#
#import random
#
##################################
### Animal abstract data type 
##################################
#class Animal(object):
#    __age = 0
#    def __init__(self, age):
#        self.age = age
#        self.name = None
#    def get_age(self):
#        return self.age
#    def get_name(self):
#        return self.name
#    def set_age(self, newage):
#        self.age = newage
#    def set_name(self, newname=""):
#        self.name = newname
#    def __str__(self):
#        return "animal:"+str(self.name)+":"+str(self.age)
#        
##print("\n---- animal tests ----")
#a = Animal(4)
##print(a)
#print(a.get_age())
#a.set_name("fluffy")
#print(a)
#a.set_name()
#print(a)
#
#for i in range(7,35,7):
#    print(i, end=" __ ")
#
#
#
#import math
#from math import factorial as fact
#print('start')
#lambda_value= float(input("enter initial lambda value: "))
#k=float(input('enter initial value of relative roughness: '))
#Re=float(input('enter initial value of reynolds no: '))
#new_lambda=0
#iteration_count=0
#lambda_diff =lambda_value
#
#while (lambda_diff> 0.000001):
#    formula= -2*(math.log10((k/3.7)+ (2.51/Re)*(1/math.sqrt(lambda_value))))
#    new_lambda=1/formula**2
#    lambda_value=new_lambda
#    lambda_diff=abs(new_lambda - lambda_value)
#    iteration_count += 1
#    print('iteration number %d' %(iteration_count))
#    print('the value of friction factor is : %f' %(new_lambda))
#for i in range(1000):
#    n=i
#    n=str(n).zfill(3)
#    a=int(n[0])
#    b=int(n[1])
#    c=int(n[2])
#    if (a**3+b**3+c**3)==i:
#        print(i)
#x=6
#while True:
#    y=(x)**2+math.e**x-1
#    if y==0:
#        break    
#    if y < 0:
#        x=x+1
#    else:
#        x=x-1
#    print(x)
#print(x)
#
#def fact(n):
#    if n<=1:
#        return(1)
#    else:
#        return(n*fact(n-1))    
##print(fact(5))
#def combination(n,r):
#    ans=(fact(n)/(fact(r)*fact(n-r)))
#    return(int(ans))
##print(combination(5,2))
#n=int(input("Enter no of rows: "))
#r=0
#while r<n+1:
#    for i in  range(n+1):
#        print(combination(n,r),end='  ')
#        r+=1
#
#i=0.05
#while i>=0.05:
#    x=(i**2)+(math.log(i))
#    print(x)
#    i+=0.001
#    if i>0.5:
#        break
#
#"""       
#n=int(input("Enter no of rows: "))
#for i in range(0,n+1):
#    if i==0 or i ==n:
#        a=1
#    else:
#        a=(fact(n))/((fact(i))*(fact(n-i)))
#    print("{0: .0f}".format(a), "", end="")
#print("\n")
#"""
#def maxofanarray():
#    max_area=-1
#    x=0
#    while True:
#        x+=0.0001
#        y=(1-x**3)**0.5
#        area=x*y*0.5
#        if area>max_area:
#            max_area=area
#        else:
#            print(x,y)
#            return (max_area)
#        
#        
#print(maxofanarray())
#
#x=0
#y=50
#z=10
#for i in range (6):
#    print("\t",i,end="      ")
#for n in range(x,y,z):
#    print("\n")
#    print(n,"\t",(n+0)**2,"\t",(n+1)**2,"\t\t",(n+2)**2,"\t\t",(n+3)**2,"\t\t",(n+4)**2,"\t\t",(n+5)**2)
#
#n=20
#col=5
#for c in range(col+1):
#    print("     ",c,end="\t")
#print("\n")
#for i in range (0,n*10,10):
#    print(i,end="\t")
#    for c in range(col+1):
#        print((c+i)**2,"\t",end="")
#    print("")
#
#import numpy as np
#from math import factorial
##num=21
#print("x\t\tJ(X)")
#for x in np.arange(0,1.05,0.05):
#    sumx=0
#    for n in range(num):
#        sumx+=((3*(2**n)-1)*(x**n))/factorial(n)
#    sumy=(1-(x**2))-sumx
#    print ("{0:.2f}\t\t{1:.4f}".format(x,sumy))
#
#a=float(input('enter a: '))
#b=float(input('enter b: '))
#c=float(input('enter c: '))
#d=float(input('enter d: '))
#x=float(input('x:'))
#eqn=a*x**5 + b*x**2 + c*x + d
#min_epsilon=0.00001
#epsilon=10
#maxiter=10000000
#def F(x):
#    return(eqn)
#def df(x):
#    return(5*a*x**4 + 2*b*x + c)
#i=0
#while (epsilon>min_epsilon):
#    xn=x-F(x)/df(x)
#    epsilon=abs(xn-x)
#    x=xn
#    i+=1
#print(xn)
#
#
#for i in range(\)
#
#i=2
#j=10
#k=j-1
#for i in range(i,j):
#    print("{0}x{1}^{2}".format(k,i,i+1),end="+")
#    k=k-1
#    
#def fact(n):
#    f=1
#    for i in range(1,n):
#            f=f*i
#    return(n)
#print(fact(4))
#def fact(n):
#    if n<=1:
#        return(1)
#    else:
#        return(n*fact(n-1))
#summ=0
#for count in range(1,100,2):
#    f=factorial(count)
##    print(f)
#    g=1/f
#    summ+=g
#print(summ)
#
#i=2
#lb=0
#for k in range(i):
#    lb+=((-1)**k)/((2*k)+1)
#    
#print(lb)
#
#a=((-1)**k)/((2*k)+1)
##print(a)
#x=float(input('enter x :'))
#x=x-1
#def ln(x):
#    n=100
#    s=0
#    for k in range(1,n):
#        s=s+((-1)**k+1)*((x**k)/k)
#    return(s)
#print(ln(x))
#        
#    
#x = 4
#if not x:
#    print("First attempt")
#elif x % 2 == 0:
#    print("Second attempt")
#else:
#    print("Final attempt")

        

def lyrics_to_frequencies(lyrics):
    myDict = {}
    for word in lyrics:
        if word in myDict:
            myDict[word] += 1
        else:
            myDict[word] = 1
    return myDict
    
    
she_loves_you = ['she', 'loves', 'you', 'yeah', 'yeah', 
'yeah','she', 'loves', 'you', 'yeah', 'yeah', 'yeah',
'she', 'loves', 'you', 'yeah', 'yeah', 'yeah',

'you', 'think', "you've", 'lost', 'your', 'love',
'well', 'i', 'saw', 'her', 'yesterday-yi-yay',
"it's", 'you', "she's", 'thinking', 'of',
'and', 'she', 'told', 'me', 'what', 'to', 'say-yi-yay',

'she', 'says', 'she', 'loves', 'you',
'and', 'you', 'know', 'that', "can't", 'be', 'bad',
'yes', 'she', 'loves', 'you',
'and', 'you', 'know', 'you', 'should', 'be', 'glad',

'she', 'said', 'you', 'hurt', 'her', 'so',
'she', 'almost', 'lost', 'her', 'mind',
'and', 'now', 'she', 'says', 'she', 'knows',
"you're", 'not', 'the', 'hurting', 'kind',

'she', 'says', 'she', 'loves', 'you',
'and', 'you', 'know', 'that', "can't", 'be', 'bad',
'yes', 'she', 'loves', 'you',
'and', 'you', 'know', 'you', 'should', 'be', 'glad',

'oo', 'she', 'loves', 'you', 'yeah', 'yeah', 'yeah',
'she', 'loves', 'you', 'yeah', 'yeah', 'yeah',
'with', 'a', 'love', 'like', 'that',
'you', 'know', 'you', 'should', 'be', 'glad',

'you', 'know', "it's", 'up', 'to', 'you',
'i', 'think', "it's", 'only', 'fair',
'pride', 'can', 'hurt', 'you', 'too',
'pologize', 'to', 'her',

'Because', 'she', 'loves', 'you',
'and', 'you', 'know', 'that', "can't", 'be', 'bad',
'Yes', 'she', 'loves', 'you',
'and', 'you', 'know', 'you', 'should', 'be', 'glad',

'oo', 'she', 'loves', 'you', 'yeah', 'yeah', 'yeah',
'she', 'loves', 'you', 'yeah', 'yeah', 'yeah',
'with', 'a', 'love', 'like', 'that',
'you', 'know', 'you', 'should', 'be', 'glad',
'with', 'a', 'love', 'like', 'that',
'you', 'know', 'you', 'should', 'be', 'glad',
'with', 'a', 'love', 'like', 'that',
'you', 'know', 'you', 'should', 'be', 'glad',
'yeah', 'yeah', 'yeah',
'yeah', 'yeah', 'yeah', 'yeah'
]

beatles = lyrics_to_frequencies(she_loves_you)


def most_common_words(freqs):
    values = freqs.values()
    best = max(values)
    words = []
    for k in freqs:
        if freqs[k] == best:
            words.append(k)
    return (words, best)
    
def words_often(freqs, minTimes):
    result = []
    done = False
    while not done:
        temp = most_common_words(freqs)
        if temp[1] >= minTimes:
            result.append(temp)
            for w in temp[0]:
                del(freqs[w])  #remove word from dict
        else:
            done = True
    return result
#    
#print(words_often(beatles, 5))

def fib(n):
    if n == 1:
        return 1
    elif n == 2:
        return 2
    else:
        return fib(n-1) + fib(n-2)
#print (fib(34))

def fib_efficient(n, d):
    if n in d:
        return d[n]
    else:
        ans = fib_efficient(n-1, d)+fib_efficient(n-2, d)
        d[n] = ans
#        print(d)
        return ans
        
d = {1:1, 2:2}
argToUse = 34

#print(fib_efficient(argToUse, d))
#print(d[20])

#
def perms(s):        
    if(len(s)==1):
        return [s]
    result=[]
    for i,v in enumerate(s):
        result += [v+p for p in perms(s[:i]+s[i+1:])]
    return result
k='abc'
#print(perms(k))

def permute(seq):
    if not seq:
        yield seq
    else:
        for i in range(len(seq)):
            rest = seq[:i]+seq[i+1:]
            for x in permute(rest):
                yield seq[i:i+1]+x

#print(list(permute('abc')))
#
#def get_permutations(word):
#    if len(word) == 1:
#        yield word
#
#    for i, letter in enumerate(word):
#        for perm in get_permutations(word[:i] + word[i+1:]):
#            yield letter + perm
            
#print(list(get_permutations('abc')))
#
#def get_permutations(sequence):
#    if len(sequence)<= 1:
#        return sequence
#    else:
#        perms = []
#        for i in get_permutations (sequence[1:]):
#            for j in range(len(i)+1):
#                perms.append(i[:j]+sequence[0]+i[j:])
#        return perms
#print(get_permutations('abc'))


#k='kamal likes ada'
#l=list(k)
#l[3]='i'
#print(l)
#l=''.join(l)
#print(l)

from ps4a import get_permutations
VOWELS_LOWER = 'aeiou'
vowels_permutation=get_permutations(VOWELS_LOWER)
print(vowels_permutation)
