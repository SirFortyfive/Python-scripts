# -*- coding: utf-8 -*-
"""
Created on Mon Sep 12 00:54:28 2022

@author: user
"""

import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': "C:/Users/user/Downloads/chicago.csv",
              'new york city': "C:/Users/user/Downloads/new_york_city.csv",
              'washington': "C:/Users/user/Downloads/washington.csv" }


fil_city = ['chicago','new york city','washington']
fil_month = ['january', 'february','march','april','may','june','all']
fil_day = ['sunday','monday','tuesday','wednesday','thursday','friday','saturday','all']



def get_filters():   #user_city, user_month, user_day
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! \nThis is Ayomide Aladesanmi \nLet\'s explore some US bikeshare data!')
    user_city= ''
    user_month = ''
    user_day = ''
    # get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    while True:
        try:  #handle exceptions from user prompted errors
            user_city = input('Please select from the following list; {}:: '.format(fil_city)).lower()
            if  user_city.casefold() in (i.casefold() for i in fil_city):
             global city
             city = user_city
             break
        except:
                print('Please select a city from the list')
                     
                
    # get user input for month (all, january, february, ... , june)
    while True: 
         try:  #handle exceptions from user prompted errors
             user_month = input('To filter by month; {}:: '.format(fil_month)).lower()
             if user_month.casefold() in (j.casefold() for j in fil_month):
              global month
              month = user_month
              break
         except:
           print('Please select a month or all from the list')
        

    # get user input for day of week (all, monday, tuesday, ... sunday)
    while True:
        try: #handle exceptions from user prompted errors
            user_day = input('To filter by day; {}:: '.format(fil_day)).lower()
            if user_day.casefold() in (k.casefold() for k in fil_day):
             global day
             day = user_day
             print('Thank you ')
             break
        except:
         print('Please select a day or all from the list')

    print('-'*40 + ('\n \n You have selected the following; {} city, {} month(s) and {}day(s)'.format(user_city.title(),user_month.title(),user_day[:-3].title()) + '\n \n' + '-'*40))
    return city, month, day





#global df

def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """
    
    df = pd.read_csv(CITY_DATA[city])      #read selected csv file
    
    df['Start Time'] = pd.to_datetime(df['Start Time']) #convert Start time to datetime format for analysis
    
    df['month'] = df['Start Time'].dt.month #assign selected month filter
     
    
    if month != 'all':
           # use the index of the months list to get the corresponding int
           
           month = fil_month.index(month) + 1
           df = df[df['month'] == month] 
    
            
    df['days'] = df['Start Time'].dt.day_name()
            
    if day != 'all':
            # filter by day of week to create the new dataframe
            df = df[df['days'] == day.title()] #object weekday_name carries capitalized first letters
        
        
    
    return df



def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()
    

    # display the most common month
    
    df['pop_month'] = df['Start Time'].dt.month #strip month from datetime
    popular_month = df['pop_month'].mode()[0] #get most frequent month
    pop_month_name = fil_month[popular_month - 1] #get most frequent month name
        
    print('Most Popular Month:', pop_month_name.title())
    
    
    # display the most common day of week
    df['pop_day'] = df['Start Time'].dt.day_name()  #strip day from datetime
    popular_day = df['pop_day'].mode()[0] #get most popular day

    print('Most Popular Day:', popular_day)


    # display the most common start hour
    df['hour'] = df['Start Time'].dt.hour #strip hour from datetime
    
    # find the most popular hour
    popular_hour = df['hour'].mode()[0] #get most popular hour
    
    print('Most Popular Start Hour:', str(popular_hour)+":00 hrs")

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)



def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # display most commonly used start station
    user_starts = df['Start Station'].value_counts().head(1) #use highest count to get most frequent start station
    print('Most frequently start station: ', user_starts)
        
    # display most commonly used end station
    user_ends = df['End Station'].value_counts().head(1) #use highest count to get most frequent end station
    print('Most frequent end station: ', user_ends)
    
        # display most frequent combination of start station and end station trip
    user_combo = ('from ' + df['Start Station'] + ' to ' + df['End Station']).mode()[0] #get most frequent combination of start and end stations
    print('Most frequent travel path: ', user_combo)
    

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
    
    


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # display total travel time
    total_travel = df['Trip Duration'].sum() #use sum to get total time
    print('total travel time is: ' , ' ' , total_travel , "secs" + " i.e  " , round((total_travel/360), 3),"hrs" )

    # display mean travel time
    mean_travel = df['Trip Duration'].mean() #use mean funtion to get mean/average trip duration
    print('mean travel time is: ' , ' ' , mean_travel , "secs", " i.e  ",round((mean_travel/360), 3),"hrs" )

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)



def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types
    user_types = df['User Type'].value_counts() #use value_counts to count each occurrence of a value type
    print('User counts are: ' , user_types) 
   
    
   # Display counts of gender
    while True:  #catch error due to lack of data in washington.csv
        try:
            Gender = df['Gender'].value_counts()
            print('Gender counts are: ' , Gender,'\n')
        except:
            print('Unfortunately Washington does not have any data on gender...')
        break
   
   
   # Display earliest, most recent, and most common year of birth
    while True:   #catch error due to lack of data in washington.csv
        try:
            youngest = df['Birth Year'].sort_values(ascending=False).head(1) #sort by birth year
            print('\n','Earliest birth year is: ', round(youngest),0)
        except:
           print('Unfortunately Washington does not have any data on birth year...')
        break
   
    while True:    #catch error due to lack of data in washington.csv
        try:
            print('Most recent birth year is: ','\n' ,( ((df[['month' , 'Birth Year']]).sort_values(by = 'Birth Year',ascending = False).head(1) )) )   #group columns by month and sort by birth year for most recent birth year
        except:
            print('Unfortunately Washington does not have any data on birth year...')
        break
    while True:    #catch error due to lack of data in washington.csv
        try:
            common_year = df['Birth Year'].mode()[0]
            print('Most common birth year is: ', common_year)
        except:
            print('Unfortunately Washington does not have any data on birth year...')
        break
    
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def displays(df):
  while True:
      try:                                          #catch errors
        dt_reqt = input('Would you like to view the raw data? Yes or No \n').lower()  #receive user prompt
        if dt_reqt == 'yes':
            for i in range(len(df)):               # define iterator
               if i < i+5:                         #set iterator range
                   dfo = pd.DataFrame(df.iloc[i:])
               print(dfo)                          #print first 5 rows
               break
        elif dt_reqt == 'no':                      #exit function
            break
        while True:
                dt_cont = input('Would you like to view more? Yes or No \n').lower()   #receive user prompt to continue
                if dt_cont == 'yes':
                    j = i+5                             #define iterator
                    j_range = range(len(df))
                    for j in j_range[i+5:]:                  #adjust startpoint for new iterator
                       if j < j+5:                          #set iterator range
                           dfo = pd.DataFrame(df.iloc[j:])
                       print(dfo)                       #print following 5 rows
                       i += 5                           #adjust loop index/startpoint
                       break
                if dt_cont == 'no':                     #exit function
                    break
        
        break
      except:
             print('Please enter Yes or No \n')


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        displays(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
