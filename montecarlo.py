print("Nama : Revi Mochamad F")
print("NRP : 152017071")
print("Montecarlo")

import pandas as pd
import numpy as np
import random
data = np.array([[0, 20], [1, 40], [2, 20], [3, 10], [4, 10]])
pd.DataFrame(data, columns=["Minggu Ke", "Frekuensi"])

mingguke = data[:0]
frekuensi = data[:,1]

sigma_f = 0
for i in range(len(frekuensi)):
    sigma_f = sigma_f + frekuensi[i]

print("ΣFrekuensi:",sigma_f)

prob =[]
sum_f=0
for a in range(len(frekuensi)):
    sum_f = frekuensi[a]/sigma_f
    print("probabilitas minggu ke-",a,"=",sum_f)
    prob.append(sum_f)

prob_d=np.array([prob])
data = np.concatenate((data, prob_d.T),axis=1)
pd.DataFrame(data, columns=["Minggu Ke", "Frekuensi","Probabilitas"])

prob_k =[]
sum_p=0
for a in range(len(frekuensi)):
    sum_p = sum_p + prob[a]
    print("probabilitas kumulatif minggu ke-",a,"=",sum_p)
    prob_k.append(sum_p)
    
prob_kd=np.array([prob_k])
data = np.concatenate((data, prob_kd.T),axis=1)
pd.DataFrame(data, columns=["Minggu Ke", "Frekuensi","Probabilitas","Probabilitas Kumulatif"])

interval_min = []
min_v=0
for a in range(len(frekuensi)):
    if(a==0):
        interval_min.append(min_v)
        print("Interval Minggu ke-",a," = ",min_v,"-",prob_k[a])
    else:
        min_v = prob_k[a-1]+0.001
        interval_min.append(min_v)
        print("Interval Minggu ke-",a," = ",min_v,"-",prob_k[a])
        
interval_mind=np.array([interval_min])
data = np.concatenate((data, interval_mind.T),axis=1)
interval_maxd=np.array([prob_k])
data = np.concatenate((data, interval_maxd.T),axis=1)
pd.DataFrame(data, columns=["Minggu Ke", "Frekuensi","Probabilitas","Probabilitas Kumulatif","Interval Batas Bawah","Interval Batas Atas"])

minggu_baru=101
p_minggu = []
angka_acak = []
permintaan = []
for a in range(16):
    p_minggu.append(minggu_baru)
    acak = random.random()
    angka_acak.append(acak)
    if(acak<0.2):
        jenis = 0
        permintaan.append(jenis)
    elif(acak<0.6):
        jenis = 1
        permintaan.append(jenis)
    elif(acak<0.8):
        jenis = 2
        permintaan.append(jenis)
    elif(acak<0.9):
        jenis = 3
        permintaan.append(jenis)
    elif(acak<=1):
        jenis = 4
        permintaan.append(jenis)
    minggu_baru+=1

print("Minggu Ke-","|","Angka Acak","|","Permintaan")
for a in range(16):
    print(p_minggu[a],"|",angka_acak[a],"|",permintaan[a])