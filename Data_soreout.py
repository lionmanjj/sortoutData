import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import os

# #=====================圖表指令===============================
# df = pd.read_csv('(P1)_1000rpm.txt',engine='python', sep='\s')
# #TYPE = df.dtypes #確認資料型態
# #print(TYPE)

# #current = df[['Ierms','Irms_3']]
# df["U123"]=(df["Urms_12"].astype(float) + df["Urms_23"].astype(float) + df["Urms_31"].astype(float))/3 #將series內的資料型態轉換成float
# #print(df["U123"])
# #print(df["嚜穋ecorder_time"])
# plt.plot(df["嚜穋ecorder_time"].astype(int)/1000,df["U123"], label="Urms123")
# #U123lines = plt.plot(df["嚜穋ecorder_time"].astype(int)/1000,df["U123"])
# #plt.setp(U123lines,marker = "o")
# plt.plot(df["嚜穋ecorder_time"].astype(int)/1000,df["Ierms"], label="Irms123")
# lines = plt.plot(df["嚜穋ecorder_time"].astype(int)/1000,abs(df["TORQUE_20HZ"]))
# plt.setp(lines,linestyle='--', label= "Torque")
# #plt.title("Population Growth") # title
# plt.ylabel("Voltage [Vrms]/ Current [Arms]") # y label
# plt.xlabel("Time [sec]") # x label
# plt.grid(True) #顯示網格
# plt.legend #顯示資料的標籤
# plt.show()
# #=====================圖表指令-end============================


# UISETCURRENT = df.nlargest(5,"UI_VALUE_SET_CURRENT")
# print("UISETCURRENT")

# pd.util.testing.makeMixedDataFrame()

# #=================================================================================
# dfcc = pd.DataFrame(pd.read_csv('(P1)_1000rpm.txt',engine='python', sep='\s'))

# #切片功能
# # UICURRENT = dfcc["UI_VALUE_SET_CURRENT"].between(100,650)
# # df1 = dfcc.loc[240:245,]#切片用法
# # print(df1["TORQUE_20HZ"])#此方式只能印出一欄

# #搜尋功能
# #找尋電流等於625A
# df2 = dfcc[dfcc.UI_VALUE_SET_CURRENT == 625]
# #列印出
# #print(df2.tail(5).mean())

# sort_resluts= df2.tail(5).mean()
# CC= sort_resluts.transpose()
# print(CC)
# #trans_data = list(zip(*sort_resluts))
# #CC.to_excel("export.xlsx")
# #print("Done!!")
# #=================================================================================

# # #=====================圖表指令===============================
# df = pd.read_csv('5000rpm_800DC_16kHz_261A_4m_L1 tst python.csv')
# TYPE = df.dtypes #確認資料型態
# # print(TYPE)
# MaxVol = df.max()
# print(MaxVol)
# plt.plot(df["TIME"],df["CH1"], label="Spike Voltage")
# #U123lines = plt.plot(df["嚜穋ecorder_time"].astype(int)/1000,df["U123"])
# #plt.setp(U123lines,marker = "o")
# #plt.plot(df["TIME"],df[""], label="Irms123")
# # lines = plt.plot(df["TIME"].astype(int)/1000,abs(df["TORQUE_20HZ"]))
# # plt.setp(lines,linestyle='--', label= "Torque")
# #plt.title("Population Growth") # title
# plt.ylabel("Voltage [Vrms]") # y label
# plt.xlabel("Time [sec]") # x label
# plt.grid(True) #顯示網格
# plt.legend #顯示資料的標籤
# plt.show()
# # #=====================圖表指令-end============================

# #=====================圖表指令===============================
df = pd.read_csv('Dmagnization_test_500 rpm.txt',engine='python', sep='\s')
x= np.linspace(1, df.shape[0]/100, df.shape[0] )
# #note=========
# 可以理解為共享y軸
# 1.ax1=ax.twiny()
# 2.ax1=plt.twiny()
# 可以理解為共享x軸
# 1.ax1=ax.twinx()
# 2.ax1=plt.twinx()
# #=============
fig, ax1 = plt.subplots()
plt.title('AVL Raw Data')
plt.xlabel('SCC')
ax2 = ax1.twinx()
ax3 = ax1.twiny()

ax1.set_ylabel('HVB_SCT_ACTIVE/HVB_IDLE_ACTIVE', color='tab:blue')
ax1.plot(x, df["HVB_SCT_ACTIVE"], color='tab:blue', alpha=0.75)
ax1.tick_params(axis='y', labelcolor='tab:blue')

ax2.set_ylabel('Ierms(Arms)', color='black')
ax2.plot(x, df["Ierms"], color='black', alpha=1)
ax2.tick_params(axis='y', labelcolor='black')

# ax3.set_ylabel('HVB_IDLE_ACTIVE', color='red')
ax3.plot(x, df["HVB_IDLE_ACTIVE"], color='red', alpha=0.75)
ax3.tick_params(axis='y', labelcolor='red')

fig.tight_layout()
plt.show()
# #=====================圖表指令-end============================