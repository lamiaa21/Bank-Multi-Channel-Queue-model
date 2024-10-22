# -*- coding: utf-8 -*-
"""simP1 (6).ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1svS0yJxQh6X_aCjUvalRI3-zLw8ncDnL
"""

# Import necessary modules

import random as rd
import numpy as np
from prettytable import PrettyTable
import matplotlib.pyplot as plt


# Determine the type of customer (0 for ordinary, 1 for distinguished) based on a random number
def det_type(r):
    if r >= 0 and r <= 60:
        i = 0
    elif r > 60 and r <= 100:
        i = 1
    return i


# Calculate the inter-arrival time for ordinary customers based on a random numberdef generate_o_iat(r):
def generate_o_iat(r):
    if r >= 0 and r <= 9:
        i = 0
    elif r > 9 and r <= 26:
        i = 1
    elif r > 26 and r <= 53:
        i = 2
    elif r > 53 and r <= 73:
        i = 3
    elif r > 73 and r <= 88:
        i = 4
    elif r > 88 and r <= 100:
        i = 5
    return i


# Calculate the inter-arrival time for distinguished customers based on a random number


def generate_d_iat(r):
    if r >= 0 and r <= 10:
        i = 1
    elif r > 10 and r <= 30:
        i = 2
    elif r > 30 and r <= 60:
        i = 3
    elif r > 60 and r <= 100:
        i = 4
    return i


# Calculate the service time for ordinary customers based on a random number
def generate_o_st(r):
    if r >= 0 and r <= 20:
        i = 1
    elif r > 20 and r <= 60:
        i = 2
    elif r > 60 and r <= 88:
        i = 3
    elif r > 88 and r <= 100:
        i = 4
    return i


# Calculate the service time for distinguished customers based on a random number


def generate_d_st(r):
    if r >= 0 and r <= 10:
        i = 1
    elif r > 10 and r <= 40:
        i = 2
    elif r > 40 and r <= 78:
        i = 3
    elif r > 78 and r <= 100:
        i = 4
    return i


# Initialize lists for storing customer data


o_IAT = []
d_IAT = []
IAT = []
ST = []
o_ST = []
d_ST = []
o_WT = []
D_WT = []
WT = []
AT = []
SST = []
ES = []
TIS = []
idle = []
typ = []
randTyp = []
randIAT = []
randST = []
max_queue_o = []
max_queue_d = []
queue_o = 1
queue_d = 1
counter_o = 0
counter_d = 0
counter_o_wt = 0
counter_d_wt = 0


# Set the number of Customers to simulate

n = int(input("Enter number of customers : "))

# Initialize Default Values
for i in range(n):
    SST.append(0)
    ES.append(0)
    WT.append(0)
    o_WT.append(0)
    D_WT.append(0)
    TIS.append(0)
    idle.append(0)


# To Loop on customers

for i in range(n):
    r1 = int(rd.uniform(0, 100))  # Generate Randoms
    randTyp.append(r1)
    genarated_type = det_type(r1)
    r3 = int(rd.uniform(0, 100))
    randST.append(r3)

    if i == 0:  # First Row
        if genarated_type == 0:
            typ.append("O")  # IF Ordinary
            counter_o += 1
            o_IAT.append(0)
            so = generate_o_st(r3)
            o_ST.append(so)
            ST.append(so)
        else:
            typ.append("d")  # IF Distinguished
            counter_d += 1
            d_IAT.append(0)
            sd = generate_d_st(r3)
            d_ST.append(sd)
            ST.append(sd)
        randIAT.append(0)
        IAT.append(0)
        AT.append(IAT[i])
        SST[i] = IAT[i]
        WT[i] = 0
        o_WT[i] = 0
        D_WT[i] = 0
        ES[i] = ST[i]
        TIS[i] = ES[i] - AT[i]
        idle[i] = AT[i]

    else:
        r2 = int(rd.uniform(0, 100))  # Rest Of Rows
        randIAT.append(r2)
        if genarated_type == 0:
            typ.append("O")
            counter_o += 1
            ao = generate_o_iat(r2)
            so = generate_o_st(r3)
            o_IAT.append(ao)
            o_ST.append(so)
            IAT.append(ao)
            ST.append(so)
            queue_o += 1
        else:
            typ.append("d")
            counter_d += 1
            ad = generate_d_iat(r2)
            sd = generate_d_st(r3)
            d_IAT.append(ad)
            d_ST.append(sd)
            IAT.append(ad)
            ST.append(sd)
            queue_d += 1
        AT.append(AT[i - 1] + IAT[i])
        if i < 1:
            continue
        # to Fulfillment of the priority condition of distinguished customer
        if ES[i - 2] > AT[i - 1] and ES[i - 2] > AT[i] and typ[i - 1] != typ[i]:
            # if distinguished customer arrive he start service regardless if there ordinary customer waiting
            if typ[i] == "d":
                SST[i] = ES[i - 2]
                D_WT[i] = SST[i] - AT[i]
                D_WT[i - 1] = 0
                WT[i] = SST[i] - AT[i]
                ES[i] = SST[i] + ST[i]
                TIS[i] = ES[i] - AT[i]
                idle[i] = 0
                SST[i - 1] = ES[i]
                o_WT[i - 1] = SST[i - 1] - AT[i - 1]
                o_WT[i] = 0
                WT[i - 1] = SST[i - 1] - AT[i - 1]
                ES[i - 1] = SST[i - 1] + ST[i - 1]
                TIS[i - 1] = ES[i - 1] - AT[i - 1]
                idle[i - 1] = 0
                counter_d_wt += 1
                counter_o_wt += 1
                if D_WT[i] > 0:
                    queue_d += 1
                else:
                    queue_d -= 1
                if o_WT[i - 1] > 0:
                    queue_o += 1
                else:
                    queue_o -= 1
            # the system work normally
            else:
                SST[i] = max(AT[i], ES[i - 2])
                if SST[i] > AT[i]:
                    WT[i] = SST[i] - AT[i]
                    if genarated_type == 0:
                        o_WT[i] = SST[i] - AT[i]
                        D_WT[i] = 0
                        if o_WT[i] > 0:
                            queue_o += 1
                        else:
                            queue_o -= 1
                        counter_o_wt += 1
                    else:
                        D_WT[i] = SST[i] - AT[i]
                        o_WT[i] = 0
                        if D_WT[i - 1] > 0:
                            queue_d += 1
                        else:
                            queue_d -= 1
                        counter_d_wt += 1
                else:
                    WT[i] = 0
                    o_WT[i] = 0
                    D_WT[i] = 0
                ES[i] = SST[i] + ST[i]
                if genarated_type == 1:
                    queue_d -= 1
                    if queue_d > 0:
                        max_queue_d.append(queue_d)
                    else:
                        max_queue_d.append(0)
                else:
                    queue_o -= 1
                    if queue_o > 0:
                        max_queue_o.append(queue_o)
                    else:
                        max_queue_o.append(0)
                TIS[i] = ES[i] - AT[i]
                idlee = AT[i] - ES[i - 1]
                if idlee <= 0:
                    idle[i] = 0
                else:
                    idle[i] = idlee

        else:
            SST[i] = max(AT[i], ES[i - 1])
            if SST[i] > AT[i]:
                WT[i] = SST[i] - AT[i]
                if genarated_type == 0:
                    o_WT[i] = SST[i] - AT[i]
                    D_WT[i] = 0
                    counter_o_wt += 1
                else:
                    D_WT[i] = SST[i] - AT[i]
                    o_WT[i] = 0
                    counter_d_wt += 1
            else:
                WT[i] = 0
                o_WT[i] = 0
                D_WT[i] = 0
            ES[i] = SST[i] + ST[i]
            if genarated_type == 1:
                queue_d -= 1
                if queue_d > 0:
                    max_queue_d.append(queue_d)
                else:
                    max_queue_d.append(0)
            else:
                queue_o -= 1
                if queue_o > 0:
                    max_queue_o.append(queue_o)
                else:
                    max_queue_o.append(0)
            TIS[i] = ES[i] - AT[i]
            idlee = AT[i] - ES[i - 1]
            if idlee <= 0:
                idle[i] = 0
            else:
                idle[i] = idlee

# Print Table Of Customers

t = PrettyTable(
    [
        "customer",
        "RT",
        "Type",
        "RIAT",
        "inter_arrival",
        "arrival_time",
        "waiting_time_o",
        "waiting_time_d",
        "start_Service_time",
        "RST",
        "servicetime",
        "endService",
        "totaltinsystem",
        "idle",
    ]
)
for i in range(n):
    t.add_row(
        [
            i + 1,
            randTyp[i],
            typ[i],
            randIAT[i],
            IAT[i],
            AT[i],
            o_WT[i],
            D_WT[i],
            SST[i],
            randST[i],
            ST[i],
            ES[i],
            TIS[i],
            idle[i],
        ]
    )
print(t)

# Calculations
avgIAT = sum(IAT) / n
avgO_IAT = sum(o_IAT) / counter_o
avgD_IAT = sum(d_IAT) / counter_d
avgST = sum(ST) / n
avgO_wt = sum(o_WT) / counter_o
if counter_d > 0:
    avgD_wt = sum(D_WT) / counter_d

# max of queue in both
prob_o_wt = counter_o_wt / counter_o
if counter_d > 0:
    prob_d_wt = counter_d_wt / counter_d

idl = sum(idle) / (max(ES))

print("Average Inter-Arrival Time for ordinary customer: ", "%.2f" % avgO_IAT, "\n")
print(
    "Average Inter-Arrival Time for distinguished customer: ", "%.2f" % avgD_IAT, "\n"
)
print("Average Inter-Arrival Time: ", "%.2f" % avgIAT, "\n")
print("Average Service Time: ", "%.2f" % avgST, "\n")
print("Average waiting time for Ordinary: ", "%.2f" % avgO_wt, "\n")
print("Average waiting time for Distinguished: ", "%.2f" % avgD_wt, "\n")
print("probability of waiting time for Ordinary: ", "%.2f" % prob_o_wt, "\n")
print("probability of waiting time for Distinguished: ", "%.2f" % prob_d_wt, "\n")
print("Portion of Idle Time: ", "%.2f" % idl, "\n")
print("the maximum lenght of ordinary queue: ", max(max_queue_o))
print("the maximum lenght of distinguished queue: ", max(max_queue_d))


# Graphs
plt.title("Type of Customers")
plt.hist(typ)
plt.show()
plt.title("Inter-Arrival Time")
plt.hist(IAT, color="c")
plt.show()
plt.title("Ordinary Waiting Time")
plt.hist(o_WT, color="grey")
plt.show()
plt.title("Distinguished Waiting Time")
plt.hist(D_WT, color="black")
plt.show()
plt.title("Waiting Time")
plt.hist(WT, color="m")
plt.show()
plt.title("Time in System")
plt.hist(ST, color="pink")
plt.show()
plt.title("Service Time")
plt.hist(ST, color="green")
plt.show()