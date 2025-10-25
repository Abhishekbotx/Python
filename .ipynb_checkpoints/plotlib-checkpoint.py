import matplotlib.pyplot as plt

# plt.plot([1, 2, 3, 4])
# # plt.ylabel('some numbers')
# plt.show()


# plt.plot([1, 2, 3, 4],[5,6,7,8])
# # plt.ylabel('some numbers')
# plt.show()


x=[1,2,3,4,5]
y1=[10000,20000,30000,40000,50000]
y2=[20000,40000,60000,80000,120000]
plt.plot(x,y1,label="Bikes",color="r" ,linewidth=2,linestyle=":", l)
plt.plot(x,y2,'o',label="Cars") # put 'o' for having graph with dots only
# plt.xticks([2,4])
# plt.yticks([20000,40000,60000])

plt.title("Price of vehicles w.r.t to generations in USD")
plt.xlabel("Generation")
plt.ylabel("Minimum Price")
plt.legend(loc="lower right")

plt.show()


# y=[3, 8, 1, 10]
# x=[1, 2, 6, 8]

# plt.plot(x, y)
# plt.show()