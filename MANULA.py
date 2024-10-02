import numpy as np
from scipy.stats import entropy
from math import log, e
import pandas as pd
import sys
import timeit
from random import randint
dickey = ["Pearl millet", "Maize","Millet","Legume","Tobacco","Cotton"]
def entropy1(labels, base=None):
  value,counts = np.unique(labels, return_counts=True)
  return entropy(counts, base=base)

def entropy2(labels, base=None):
  """ Computes entropy of label distribution. """

  n_labels = len(labels)

  if n_labels <= 1:
    return 0

  value,counts = np.unique(labels, return_counts=True)
  probs = counts / n_labels
  n_classes = np.count_nonzero(probs)

  if n_classes <= 1:
    return 0

  ent = 0.

  # Compute entropy
  base = e if base is None else base
  for i in probs:
    ent -= i * log(i, base)

  return ent

def entropy3(labels, base=None):
  vc = pd.Series(labels).value_counts(normalize=True, sort=False)
  base = e if base is None else base
  return -(vc * np.log(vc)/np.log(base)).sum()

def entropy4(labels, base=None):
  value,counts = np.unique(labels, return_counts=True)
  norm_counts = counts / counts.sum()
  base = e if base is None else base
  return -(norm_counts * np.log(norm_counts)/np.log(base)).sum()

#Decision-making tool for crop selection for agriculture development

usr_dst = input("Enter your Distric name::: ")
if(usr_dst=='krishna'):
  landscape_hect=int(randint(0, 10))
  season= int(randint(0, 4))
  temparature= int(randint(30, 40))
  rainfall= int(randint(0, 5))
  EC = int(randint(0, 10))
  PH = int(randint(0, 10))
  Available_N= int(randint(0, 10))
  Available_P= int(randint(0, 10))
  Available_K= int(randint(0, 10))
  Available_Zn= int(randint(0, 10))
  Available_Cu= int(randint(0, 10))
  Available_Fe= int(randint(0, 10))
  Available_Mn= int(randint(0, 10))
  Nitrogen= int(randint(0, 10))
  Urea = int(randint(0, 10))
  P205 = int(randint(0, 10))
  SSP = int(randint(0, 10))
  K2O = int(randint(0, 10))
  MOP= int(randint(0, 10))
elif(usr_dst=='west'):
  landscape_hect=int(randint(0, 10))
  season= int(randint(0, 4))
  temparature= int(randint(25, 38))
  rainfall= int(randint(0, 7))
  EC = int(randint(0, 10))
  PH = int(randint(0, 10))
  Available_N= int(randint(0, 10))
  Available_P= int(randint(0, 10))
  Available_K= int(randint(0, 10))
  Available_Zn= int(randint(0, 10))
  Available_Cu= int(randint(0, 10))
  Available_Fe= int(randint(0, 10))
  Available_Mn= int(randint(0, 10))
  Nitrogen= int(randint(0, 10))
  Urea = int(randint(0, 10))
  P205 = int(randint(0, 10))
  SSP = int(randint(0, 10))
  K2O = int(randint(0, 10))
  MOP= int(randint(0, 10))
elif (usr_dst=='guntur'):
  landscape_hect=int(randint(0, 10))
  season= int(randint(0, 4))
  temparature= int(randint(38, 50))
  rainfall= int(randint(0, 5))
  EC = int(randint(0, 10))
  PH = int(randint(0, 10))
  Available_N= int(randint(0, 10))
  Available_P= int(randint(0, 10))
  Available_K= int(randint(0, 10))
  Available_Zn= int(randint(0, 10))
  Available_Cu= int(randint(0, 10))
  Available_Fe= int(randint(0, 10))
  Available_Mn= int(randint(0, 10))
  Nitrogen= int(randint(0, 10))
  Urea = int(randint(0, 10))
  P205 = int(randint(0, 10))
  SSP = int(randint(0, 10))
  K2O = int(randint(0, 10))
  MOP= int(randint(0, 10))
elif (usr_dst=='east'):
  landscape_hect=int(randint(0, 10))
  season= int(randint(0, 4))
  temparature= int(randint(25, 38))
  rainfall= int(randint(0, 7))
  EC = int(randint(0, 10))
  PH = int(randint(0, 10))
  Available_N= int(randint(0, 10))
  Available_P= int(randint(0, 10))
  Available_K= int(randint(0, 10))
  Available_Zn= int(randint(0, 10))
  Available_Cu= int(randint(0, 10))
  Available_Fe= int(randint(0, 10))
  Available_Mn= int(randint(0, 10))
  Nitrogen= int(randint(0, 10))
  Urea = int(randint(0, 10))
  P205 = int(randint(0, 10))
  SSP = int(randint(0, 10))
  K2O = int(randint(0, 10))
  MOP= int(randint(0, 10))
  
###########################################


labels = [landscape_hect,season,temparature,rainfall,EC,PH,Available_N,Available_P,Available_K,Available_Zn,Available_Cu,5]
k=(entropy1(labels))
res=int(k)+randint(0,3)
#print(k)
if k>=0.4 and k<=1.0 and season==1:
    print(dickey[res],"Is possible to yield ::",(k*10))
elif k>=0.4 and k<=1.0 or season==2:
    print(dickey[res],"Is possible to yield ::",(k*10))
elif k>=0.4 and k<=1.0 or season==3:
    print(dickey[res],"Is possible to yield  ::",(k*10))
elif k>=0.4 and k<=1.0 or season==4:
    print(dickey[res],"Is possible to yield  ::",(k*10))

else:
    print("Is Not possible to yield ::0.0")
    
