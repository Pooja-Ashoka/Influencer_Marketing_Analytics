import pandas as pd
import matplotlib.pyplot as plt

def readCsvData():
    data = pd.read_csv("C:\\Users\\shrey\\OneDrive\\Desktop\\Wife_Projects\\Influencer_Marketing_Analytics\\Data\\influencer_marketing_roi_dataset.csv")
    return data

df = readCsvData()
#print(df.groupby("platform").count())

df['platform'].value_counts().plot(kind='pie', autopct='%1.1f%%', startangle=90)
plt.title('Platform Usage')
plt.axis('equal')
plt.show()
#plot










