## homework2
import pandas as pd 
from datetime import datetime 
df = pd.read_csv('tackoverflow_qa.csv')
df.head()
1 Find all questions that were created before 2014

df['year'] = df.creationdate.dt.year
df[df.year < 2014]
df
2 Find all questions with a score more than 50
df[df['score']>50]
3 Find all questions with a score between 50 and 100

df[df['score'].between(50, 100)]
4 Find all questions answered by Scott Boston

df[df['ans_name'] == 'Scott Boston']
5 Find all questions answered by the following 5 users

names = ['Andy hayden', 'Jeff', 'unutbu', 'DSM', 'EdChum']
df[df['ans_name'].isin(names)]
6 Find all questions that were created between March, 2014 and October 2014 that were answered by Unutbu and have score less than 5.

created = df['creationdate'].between('2014-03-01', '2014-11-01')
answered = df['ans_name'] == 'Unutbu'
score_less_than = df['score'] < 5 
df[answered & score_less_than]

7 Find all questions that have score between 5 and 10 or have a view count of greater than 10,000

score_bet = df['score'].between(5, 10)
view_count = df['viewcount'] > 10000
df[score_bet|view_count]
8 Find all questions that are not answered by Scott Boston

df[df['ans_name'] != 'SCott Boston']
## Homework3
titanic_df = pd.read_csv("titanic.csv")
titanic_df.head()
1 Select Female Passengers in Class 1 with Ages between 20 and 30: Extract a DataFrame containing female passengers in Class 1 with ages between 20 and 30.


check_class = titanic_df['Pclass'] == 1
check_age = titanic_df['Age'].between(20,30) 
check_gender = titanic_df['Sex'] == 'female'
titanic_df[check_class & check_age & check_gender]

2 Filter Passengers Who Paid More than $100: Create a DataFrame with passengers who paid a fare greater than $100.


titanic_df[titanic_df['Fare']> 100]
3 Select Passengers Who Survived and Were Alone: Filter passengers who survived and were traveling alone (no siblings, spouses, parents, or children).


titanic_df[titanic_df['SibSp']==0]
4 Filter Passengers Embarked from 'C' and Paid More Than $50: Create a DataFrame with passengers who embarked from 'C' and paid more than $50.
embarked = titanic_df['Embarked'] == 'C'
paid_morethan_50 = titanic_df['Fare'] > 50
titanic_df[embarked & paid_morethan_50]
5 Select Passengers with Siblings or Spouses and Parents or Children: Extract passengers who had both siblings or spouses aboard and parents or children aboard.


titanic_df[titanic_df['SibSp'].between(2, 4)]
6 Filter Passengers Aged 15 or Younger Who Didn't Survive: Create a DataFrame with passengers aged 15 or younger who did not survive.





aged = titanic_df['Age'] >= 15
not_Survive = titanic_df['Survived'] ==0
titanic_df[aged & not_Survive]
7 Select Passengers with Cabins and Fare Greater Than $200: Extract passengers with known cabin numbers and a fare greater than $200.


fare_greater_200 = titanic_df['Fare'] > 200
Cabin_number = titanic_df['Cabin'].notnull()
titanic_df[fare_greater_200 & Cabin_number]
8 Filter Passengers with Odd-Numbered Passenger IDs: Create a DataFrame with passengers whose PassengerId is an odd number.


titanic_df[titanic_df['PassengerId'] % 2==1]
9 Select Passengers with Unique Ticket Numbers: Extract a DataFrame with passengers having unique ticket numbers.


unique_tickets = titanic_df['Ticket'].value_counts() == 1
unique_ticket_list = unique_tickets[unique_tickets].index
unique_passengers_df = titanic_df[titanic_df['Ticket'].isin(unique_ticket_list)]
unique_passengers_df

10 Filter Passengers with 'Miss' in Their Name and Were in Class 1: Create a DataFrame with female passengers having 'Miss' in their name and were in Class 1.


check_name = titanic_df['Name'].str.contains('Mis', case=False, na=False)
class_check = titanic_df['Pclass']==1
check_gender = titanic_df['Sex'] == 'female'
titanic_df[class_check & check_gender & check_name]
