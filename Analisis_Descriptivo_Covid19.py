######################### IMPORTING THE LIBRARIES #########################

import pandas as pd 
import pandas_profiling
from pandas_profiling import ProfileReport 
import seaborn as sns
import matplotlib.pyplot as plt

######################### IMPORTING THE DATASET #########################

covid19us = pd.read_excel("Covid19Data-US.xlsx")

######################### EXPLORING THE DATAFRAME #########################

covid19us.head()

covid19us.shape
covid19us.info

#Unique Values 
covid19us.nunique()

#Duplicate Values 

covid19us.duplicated().sum()

#Descriptive Statistics 

desc_statistics = covid19us.describe()
desc_statistics

#########################  MISSING VALUES ######################### 

na = covid19us.isna().sum(axis = 0)
na 

""" Since some columns have certain quantity of missing values, we are going to 
    detail what percentage of missing values do the columns have. If these percentages 
    are high, then we are going to perfom some operations to deal with them. """

pct_na = (na/len(covid19us))*100
pct_na

"""As we saw, the last 4 columns, wich are the ones related to vaccinations, 
   have 27% of missing values and the 'hosp_patients'and 'icu_patients' columns have
   6% of missing values.
   
   Let's remember that in the case of the columns related to vaccinations, these ones
   arrived, in December 2020, at the United States, so it is logic to see missing
   values in this fields. The same happens with the ICU and Hospital patients, 
   people started to being hospitalized in July 2020, which was when the wave of 
   infections happened.
   
   So, for the sake of the analysis, let's leave these missing values as they are."""

######################### DESCRIPTIVE ANALYSIS #########################

sns.set_style("whitegrid")

#Percentage of Infected people per day 

covid19us["pct_totalcases"] = (covid19us["total_cases"]/covid19us["population"])*100

pct_totalcases = covid19us.loc[:, ["date", "pct_totalcases"]]
sns.lineplot(x = "date", y = "pct_totalcases", data = pct_totalcases)

#Percentage of Deaths per day 

covid19us["pct_totaldeaths"] = (covid19us["total_deaths"]/covid19us["population"])*100

pct_totaldeaths = covid19us.loc[:, ["date", "pct_totaldeaths"]]
sns.lineplot(x = "date", y = "pct_totaldeaths", data = pct_totaldeaths)

#Percentage of New Cases and Deaths per day

covid19us["pct_newcases"] = (covid19us["new_cases"]/covid19us["population"])*100
covid19us["pct_newdeaths"] = (covid19us["new_deaths"]/covid19us["population"])*100

pct_newcases_newdeaths = covid19us.loc[:, ["date", "pct_newcases", "pct_newdeaths"]]

figure, axis = plt.subplots(2,1,
                      figsize=(8,6),
                      sharex=True)


sns.lineplot(x = "date", y = "pct_newcases", data = pct_newcases_newdeaths, 
             ax = axis[0])                           
sns.lineplot(x = "date", y = "pct_newdeaths", data = pct_newcases_newdeaths,
             ax = axis[1])

#ICU Patients per day 

sns.lineplot(x = "date", y = "icu_patients", data = covid19us)

# Hospitalized Patients per day 

sns.lineplot(x = "date", y = "hosp_patients", data = covid19us)

#Percentage of People Vaccinated 

covid19us["pct_peoplevacc"] = (covid19us["people_vaccinated"]/covid19us["population"])*100

pct_peoplevacc = covid19us.loc[:, ["date", "pct_peoplevacc"]]
sns.lineplot(x = "date", y = "pct_peoplevacc", data = pct_peoplevacc)

#Percnetage of People Fully Vaccinated 

covid19us["pct_peoplefullvacc"] = (covid19us["people_fully_vaccinated"]/covid19us["population"])*100

pct_peoplefullvacc = covid19us.loc[:, ["date", "pct_peoplefullvacc"]]
sns.lineplot(x = "date", y = "pct_peoplefullvacc", data = pct_peoplefullvacc)

#People Vaccinated in relacion with Total Deaths

pct_peoplevacc_totaldeaths = covid19us.loc[:, ["date", "pct_peoplevacc", 
                                               "pct_totaldeaths"]]


figure, axis = plt.subplots(2,1,
                      figsize=(8,6),
                      sharex=True)


sns.lineplot(x = "date", y = "pct_peoplevacc", data = pct_peoplevacc_totaldeaths, 
             ax = axis[0])                           
sns.lineplot(x = "date", y = "pct_totaldeaths", data = pct_peoplevacc_totaldeaths,
             ax = axis[1])

#People Vaccinated in relation with New Deaths

pct_peoplevacc_newdeaths = covid19us.loc[:, ["date", "pct_peoplevacc", 
                                               "pct_newdeaths"]]

figure, axis = plt.subplots(2,1,
                      figsize=(8,6),
                      sharex=True)


sns.lineplot(x = "date", y = "pct_peoplevacc", data = pct_peoplevacc_newdeaths, 
             ax = axis[0])                           
sns.lineplot(x = "date", y = "pct_newdeaths", data = pct_peoplevacc_newdeaths,
             ax = axis[1])

"""As we can see in the plot, when people started getting vaccinated, around December 2020-January 2021,
   the number of daily new deaths decreased significately and remained so, at least 
   for the next 6 months."""

#People Vaccinated in relation with ICU Patients 

covid19us["pct_icupatients"] = (covid19us["icu_patients"]/covid19us["population"])*100

pct_peoplevacc_icupatients = covid19us.loc[:, ["date", "pct_peoplevacc", 
                                               "pct_icupatients"]]

figure, axis = plt.subplots(2,1,
                      figsize=(8,6),
                      sharex=True)


sns.lineplot(x = "date", y = "pct_peoplevacc", data = pct_peoplevacc_icupatients, 
             ax = axis[0])                           
sns.lineplot(x = "date", y = "pct_icupatients", data = pct_peoplevacc_icupatients,
             ax = axis[1])

"""As well as the case of the new deaths and people vaccinated, when people started getting vaccinated, around December 2020-January 2021,
   the number of ICU hopsitalization decreased significately and remained so, at least 
   for the next 6 or 8 months."""

#People Vaccinated in relation with Hospitalized Patients

covid19us["pct_hosppatients"] = (covid19us["hosp_patients"]/covid19us["population"])*100

pct_peoplevacc_hosppatients = covid19us.loc[:, ["date", "pct_peoplevacc", 
                                               "pct_hosppatients"]]

figure, axis = plt.subplots(2,1,
                      figsize=(8,6),
                      sharex=True)


sns.lineplot(x = "date", y = "pct_peoplevacc", data = pct_peoplevacc_hosppatients, 
             ax = axis[0])                           
sns.lineplot(x = "date", y = "pct_hosppatients", data = pct_peoplevacc_hosppatients,
             ax = axis[1])

"""Happens the same as in the case of ICU hospitlizations."""

#In case of wanting to remove all the created columns in this file, run the following code:

"""covid19us.drop(["pct_totalcases", "pct_totaldeaths", "pct_newcases", "pct_newdeaths"], 
               axis = 1, inplace = True)"""


############################ PANDAS PROFILING ############################## 

prof = ProfileReport(covid19us)
prof.to_file(output_file= "covid19us.html")




