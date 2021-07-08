import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import os

df = pd.read_csv('(P1)_1000rpm.txt',engine='python', sep='\s')
#TYPE = df.dtypes #確認資料型態
#print(TYPE)

#current = df[['Ierms','Irms_3']]
df["U123"]=(df["Urms_12"].astype(float) + df["Urms_23"].astype(float) + df["Urms_31"].astype(float))/3 #將series內的資料型態轉換成float
#print(df["U123"])
#print(df["嚜穋ecorder_time"])

#=====================圖表指令===============================
plt.plot(df["嚜穋ecorder_time"].astype(int)/1000,df["U123"], label="Urms123")
#U123lines = plt.plot(df["嚜穋ecorder_time"].astype(int)/1000,df["U123"])
#plt.setp(U123lines,marker = "o")
plt.plot(df["嚜穋ecorder_time"].astype(int)/1000,df["Ierms"], label="Irms123")
lines = plt.plot(df["嚜穋ecorder_time"].astype(int)/1000,abs(df["TORQUE_20HZ"]))
plt.setp(lines,linestyle='--', label= "Torque")
#plt.title("Population Growth") # title
plt.ylabel("Voltage [Vrms]/ Current [Arms]") # y label
plt.xlabel("Time [sec]") # x label
plt.grid(True) #顯示網格
plt.legend #顯示資料的標籤
plt.show()
#=====================圖表指令-end============================


UISETCURRENT = df.nlargest(5,"UI_VALUE_SET_CURRENT")
print("UISETCURRENT")

pd.util.testing.makeMixedDataFrame()

