# Calculate statistical characteristics of a data set

# From two_column_text_read_00.py
import numpy as np


data = list(un_data)
while True:
    try:
        u = data[0]
        v = data[1]
        break
    except IndexError:
        print('Data Array has inappropriate dimensions, please use an array with two dimensions')

# Mean
mean2 = sum(v)/len(v)


print('The mean of the second sample is: ', mean2)
#Standard deviation
variance2 = sum([((float(i) - mean2)**2) for i in v])/len(v)
res2 = variance2**0.5  # Taking the square root
print("Standard deviation of the second sample is: " + str(res2))

#Maximums and minimums
maxu = max(u)
maxv = max(v)
print(maxu)
print(maxv)

minu= min(u)
minv = min(v)
print(minu)
print(minv)

values = np.array([mean2, res2, maxu, minu, maxv, minv])  # Need mean and standard deviation
print(values)

