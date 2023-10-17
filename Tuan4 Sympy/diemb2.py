import pandas as pd
from numpy import array
import matplotlib.pyplot as plt
import numpy as np

df = pd.read_csv('diemPython.csv', index_col=0, header=0)


in_data = array(df.iloc[:, :])


# Extract the total number of students
tongsv = in_data[:, 1]
tongsvabc= in_data[:, [3,5, 7]]
tongsvlonhonD= in_data[:,[3,4,5,6,7,8,9]]
# row_values = in_data[2, 3:9]
# Extract the data from columns 3 to 9 for all rows
sinhvienlonhondmoilop= in_data[:,11]
# Calculate the sum of total students
total_students = np.sum(tongsv)
total_ABC = np.sum(tongsvabc)
total_londonD=np.sum(tongsvlonhonD)
total_sinhvienlonhonD=(sinhvienlonhondmoilop)
# max_total = np.max(total_per_row)
#thong ke sinh vien co diem D



# Create a bar chart
plt.bar("Total Students", total_students)

# Add labels
plt.xlabel("Category")
plt.ylabel("Total Students")
plt.title("Du lieu diem cua sinh vien")
# Create a bar chart
plt.bar("Total ABC", total_ABC)

plt.bar("Total >=D", total_londonD)



# Show the plot
plt.show()
# Create a bar chart
plt.bar("Total Students", total_sinhvienlonhonD)

# Add labels
plt.xlabel("Category")
plt.ylabel("Total Students")
plt.title("Du lieu diem cua sinh vien")
plt.show()
