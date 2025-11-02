import matplotlib.pyplot as plt
import numpy as np
# plt.plot([1, 2, 3, 4])
# # plt.ylabel('some numbers')
# plt.show()


# plt.plot([1, 2, 3, 4],[5,6,7,8])
# # plt.ylabel('some numbers')
# plt.show()

# 🎫 Simple line plots for Bikes & Cars Price vs Generation
x=[1,2,3,4,5]
y1=[10000,20000,30000,40000,50000]
y2=[20000,40000,60000,80000,120000]
# plt.plot(x,y1,label="Bikes",color="r" ,linewidth=2,linestyle=":",)
plt.plot(x,y1,"r*--",label="Bikes",markersize=10) # short hand notation color ,marker and and style
plt.plot(x,y2,'o',label="Cars") # put 'o' for having graph with dots only
# plt.xticks([2,4])
# plt.yticks([20000,40000,60000])

plt.title("Price of vehicles w.r.t to generations in USD",fontdict={'fontname':"comic sans ms"})
plt.xlabel("Generation",fontdict={'fontname':"comic sans ms",'color':'orange'})
plt.ylabel("Minimum Price")
plt.legend(loc="lower right")


# 🎫Save figure :try to save file before show coz at time of show it clears the data
plt.savefig("price.png",dpi=1000)

# plt.show()


# y=[3, 8, 1, 10]
# x=[1, 2, 6, 8]

# plt.plot(x, y)
# plt.show()


# evenly sampled time at 200ms intervals
t = np.arange(0., 5., 0.2) # start from 0. to 5 and difference should be 0.2 --> [.2,.4 ....,5.0]

# red dashes, blue squares and green triangles
# plt.plot(t, t, 'r--', t, t**2, 'bs', t, t**3, 'g^') here 1 fig and 3 graphs in it 
# plt.show()


t = np.arange(1, 10)

plt.figure()

plt.subplot(3, 1, 1)
plt.plot(t, t,'r--')
plt.xlabel('t values')
plt.ylabel('output values')
plt.title('Linear Subplot')

plt.subplot(3, 1, 2)
plt.plot(t, t**2, 'bs')
plt.xlabel('t values')
plt.ylabel('output values')
plt.title('Quadratic Subplot')

plt.subplot(3, 1, 3)
plt.plot(t, t**3, 'g^')
plt.title('Cubic Subplot')

plt.suptitle('Different functions of t') # Common title for all 3
plt.tight_layout()
plt.xlabel('t values')
plt.ylabel('output values')

# plt.show()



# now here there is 1 fig and in that there is 3 subplot

plt.savefig('subplot.png')
# plt.show()




# 🎫 Subplots Example 2 → 6 different functions in grid layout (2 rows x 3 columns) axes
x = np.linspace(1, 10, 100) # from 1,10 there will be 100 points evenly distributed

fig, axes = plt.subplots(2, 3)

axes[0,0].plot(x, np.sin(x))
axes[0,0].set_title('Sin func')
axes[0,0].set_xlabel('x')
axes[0,0].set_ylabel('y')

axes[0,1].plot(x, np.cos(x))
axes[0,1].set_title('Cos func')
axes[0,1].set_xlabel('x')
axes[0,1].set_ylabel('y')

axes[0,2].plot(x, np.tan(x))
axes[0,2].set_title('Tan func')
axes[0,2].set_xlabel('x')
axes[0,2].set_ylabel('y')

axes[1,0].plot(x, np.exp(x))
axes[1,0].set_title('Exp func')
axes[1,0].set_xlabel('x')
axes[1,0].set_ylabel('y')

axes[1,1].plot(x, np.sqrt(x))
axes[1,1].set_title('Sqrt func')
axes[1,1].set_xlabel('x')
axes[1,1].set_ylabel('y')

axes[1,2].plot(x, np.log(x))
axes[1,2].set_title('Log func')
axes[1,2].set_xlabel('x')
axes[1,2].set_ylabel('y')

plt.tight_layout() # This makes evenly seperated and space
# plt.show()



#Scatter 

xs1=np.random.rand(100)*10
ys1=np.random.rand(100)*10

plt.scatter(xs1,ys1,c=ys1, cmap='plasma',marker='h',label='random',alpha=0.8)
plt.legend(loc="lower right")
plt.grid(True)
plt.show()



# Bar chart
courses = ["HLD", "GENAI", "LLD", "DSA", "PYTHON", "GO"]
students = [1877, 695, 203, 980, 1203, 1505]
hatches = ["/", "*", "o", "|", "-", "\\"]
bar_colors = ['violet', "indigo", "blue", "green", "yellow", "orange"]

bars = plt.bar(courses, students, width=0.5, align="center", edgecolor="black")

for bar, hatch, color in zip(bars, hatches, bar_colors):
    bar.set_hatch(hatch)
    bar.set_color(color)
    bar.set_edgecolor('black')

plt.xlabel("Courses")
plt.ylabel("Students")
plt.title("No. of Students Enrolled in Courses")
plt.show()




#Pie Chart

courses = ['GenAI' , 'HLD', 'HHLD', 'LLD', 'DSA', 'CPP']
students = [2500, 3000, 3200, 2800, 2700, 1000]
explode = [0.2, 0, 0, 0, 0, 0]
pie_colors = ['red', 'blue', 'magenta', 'yellow', 'orange', 'green']

# creating the pie chart by passing values and properties
plt.pie(students, labels=courses, shadow=True, explode=explode, colors=pie_colors)
plt.show()