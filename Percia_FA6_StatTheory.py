#!/usr/bin/env python
# coding: utf-8

# ### APM111 - Statistical Theory
# #### Formative Assessment 6

# #### Number 1 
# 
# (5 points). Table 1 shows a frequency distribution of grades on a final examination in college algebra. Find the quartiles of the distribution,
# 
# 

# In[1]:


import pandas as pd
from IPython.display import display
import numpy as np

data = {'Grade': ['90-100', '80-89', '70-79', '60-69', '50-59', '40-49', '30-39'],
'Number of Students': [9, 32, 43, 21, 11, 3, 1]}

df = pd.DataFrame(data)
display(df)

total = 120

print(f"Total : {total}")

print()
print("Answer :")

midp_grades = [95,85,75,65,55,45,35]
frequency = [9,32,43,21,11,3,1]

distrib = np.repeat(midp_grades,frequency)

Q1 = np.percentile(distrib,25)
Q2 = np.percentile(distrib,50)
Q3 = np.percentile(distrib,75)

quartiles = {' ': ['Q1', 'Q2 (Median)', 'Q3'],
            'Quartiles of the Distribution': [Q1, Q2, Q3]}

answer1 = pd.DataFrame(quartiles)
display(answer1)


# #### Number 2
# 
# (5 points). On a final examination in statistics, the mean grade of a group of 150 students was 78 and the standard deviation was 8.0. In algebra, however, the mean final grade of the group was 73 and the standard deviation was 7.6. In which subject was there the greater (a) absolute dispersion and (b) relative dispersion?

# In[2]:


mean_stats = 78
std_stats = 8

mean_algebra = 73
std_algebra = 7.6

#The absolute dispersion is the standard deviation itself

absolute_dispersion = {
    'Statistics': [std_stats],
    'Algebra': [std_algebra],
}

#The relative distribution is the coefficient of variation

cv_stats = (std_stats/mean_stats) * 100
cv_algebra = (std_algebra/mean_algebra) * 100

relative_dispersion = {
    'Statistics (CV%)': [cv_stats],
    'Algebra (CV%)': [cv_algebra]
}

whole_data = {'Subject' : ['Statistics', 'Algebra'],
             'Mean' : [78, 73],
             'Absolute Dispersion' : [std_stats, std_algebra],
             'Relative Dispersion': [cv_stats, cv_algebra]}

df1 = pd.DataFrame(whole_data)
display(df1)


# #### Number 3
# 
# (10 points). Prove that the mean and standard deviation of a set of standard scores are equal to 0 and 1, respectively. Use the following problem to illustrate this: Convert the set 6, 2, 8, 7, 5 into standard scores

# In[3]:


from scipy.stats import zscore

data = [6, 2, 8, 7 ,5]

z_scores = zscore(data)

z_mean = np.round(np.mean(z_scores), decimals = 10)
z_std = np.round(np.std(z_scores), decimals = 10)

table = {'Set of Scores' : data,
        'Standard Scores' : z_scores}

df2 = pd.DataFrame(table)
display(df2)

print(f"The mean of a set of standard scores is : {z_mean:.2f}")
print(f"The standard deviation of a set of standard scores is : {z_std:.2f}")


# ##### Explanation
# 
# - 'zscore()' converts raw scroes in to a standard scores.
# - By the given example above, this proves that z-scores will always have a mean of 0 and a standard deviation of 1. (Look below that using a random generator numbers will have the same result)

# In[4]:


np.random.seed(42)

rand = np.random.randint(1, 101, size=20)

rz_scores = zscore(rand)

rz_mean =  np.round(np.mean(rz_scores), decimals = 10)
rz_std = np.round(np.std(rz_scores), decimals = 10)

print("Is mean of the standard scores equal to zero?")
print(rz_mean == 0)

print("Is standard deviation of the standard scores equal to one?")
print(rz_std == 1)


# #### Number 4
# 
# (5 points). Three masses are measured as 20.48, 35.97, and 62.34 g, with standard deviations of 0.21, 0.46, and 0.54 g, respectively. Find the (a) mean and (b) standard deviation of the sum of the masses.

# In[5]:


masses = [20.48, 35.97, 62.34]
std_devs = [0.21 , 0.46, 0.54]

mean_sum = np.sum(masses)/3

std_sum = np.sqrt(np.sum(np.square(std_devs)))

print(f"The mean of the sum of the masses : {mean_sum:.2f}")
print(f"The standard deviation of the sum of the masses : {std_sum:.2f}")


# #### Number 5
# 
# (10 points). The credit hour distribution at Metropolitan Technological College is as follows:

# In[6]:


last = {'x' : [6, 9, 12, 15, 18],
       'p(x)' : [0.1, 0.2, 0.4, 0.2, 0.1]}

df3 = pd.DataFrame(last)
display(df3.transpose())


# Find 𝜇 and variance. Give the 25 (with replacement) possible samples of size 2, their means, and their probabilities.

# In[7]:


from itertools import combinations

values = [6, 9, 9, 12, 12, 12, 12, 15, 15, 18]


mean = np.mean(values)
variance = np.var(values, ddof=0)  # Population variance

print(f"Mean: {mean:.2f}")
print(f"Variance: {variance:.2f}")

comb = combinations([6, 9, 9, 12, 12, 12, 12, 15, 15, 18],2)
x=1

totalvalues = []
total_six = 0
total_nine = 0
total_twelve = 0
total_fifteen = 0
total_eighteen = 0

for i in list(comb):
    
    p_six = i.count(6)
    p_nine = i.count(9)
    p_twelve = i.count(12)
    p_fifteen = i.count(15)
    p_eighteen = i.count(18)
    
    realprop_six= p_six/2
    tupe_six = (p_six/2,)
    i += tupe_six
    
    realprop_nine= p_nine/2
    tupe_nine = (p_nine/2,)
    i += tupe_nine
    
    realprop_twelve= p_twelve/2
    tupe_twelve = (p_twelve/2,)
    i += tupe_twelve
    
    realprop_fifteen= p_fifteen/2
    tupe_fifteen = (p_fifteen/2,)
    i += tupe_fifteen
    
    realprop_eighteen= p_eighteen/2
    tupe_eighteen = (p_eighteen/2,)
    i += tupe_eighteen
    
    total_six += realprop_six
    total_nine += realprop_nine
    total_twelve += realprop_twelve
    total_fifteen += realprop_fifteen
    total_eighteen += realprop_eighteen
    
    totalvalues.append(i)
    x+=1

samp_distrib = x-1

df4 = pd.DataFrame(totalvalues, columns=['1st Pick', '2nd Pick', 'p_6', 'p_9','p_12','p_15','p_18'])
display(df4.head(25))

ave_six = total_six/samp_distrib
ave_nine = total_nine/samp_distrib
ave_twelve = total_twelve/samp_distrib
ave_fifteen = total_fifteen/samp_distrib
ave_eighteen = total_eighteen/samp_distrib

print(f"Average Proportion of 6: {ave_six:.2f}")
print(f"Average Proportion of 9: {ave_nine:.2f}")
print(f"Average Proportion of 12: {ave_twelve:.2f}")
print(f"Average Proportion of 15: {ave_fifteen:.2f}")
print(f"Average Proportion of 18: {ave_eighteen:.2f}")

