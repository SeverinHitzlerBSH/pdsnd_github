import time
import pandas as pd
import numpy as np
import calendar

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    city = ''
    while city =='':
        city = input("Do you like to analyse bike share data for Chicago, New York City or Washington? ").lower()
        if city not in CITY_DATA:
            print('Invalid input, please try again.')
            city = ''

    # get user input for month (all, january, february, ... , june)
    
    month =''
    while month =='':
        month = input("Please enter the month that you like to analyse or 'all': ").lower()
        if month.capitalize() not in list(calendar.month_name[1:]) and month !="all":
            print('Invalid input, please try again.')
            month = ''

    # get user input for day of week (all, monday, tuesday, ... sunday)
    day = ""
    while day =='':
        day = input("Please enter the day that you like to analyse or 'all': ").lower()
        if day.capitalize() not in list(calendar.day_name) and day !="all":
            print('Invalid input, please try again.')
            day = ''

    print('-'*40)
    return city, month, day


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



    df = pd.read_csv(CITY_DATA[city])
    
    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month_name()
    df['day_of_week'] = df['Start Time'].dt.day_name()
    df['hour'] = df['Start Time'].dt.hour
    df['Start End'] = df['Start Station'] +' to '+ df['End Station']
    # filter by month if applicable
    if month != 'all':

        # filter by month to create the new dataframe
        df = df[df['month'] == month.title()]

    # filter by day of week if applicable
    if day != 'all':
        # filter by day of week to create the new dataframe
        df = df[df['day_of_week'] == day.title()]

    i = 0
    show_data = input('\nWould you like to see some raw data? Enter yes or no.\n').lower()
    while show_data == 'yes':
        print(df[1+i:6+i])
        i += 5
        more_data = input('\nWould you like to see more data? Enter yes or no.\n')
        if more_data.lower() != 'yes':
            break
    
    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # display the most common month
    print('The most common month is ' + df['month'].mode()[0] + '.')

    # display the most common day of week
    print('The most common weekday is ' + df['day_of_week'].mode()[0] + '.')

    # display the most common start hour
    print('The most common start hour is ' + str(df['hour'].mode()[0]) + '.')

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # display most commonly used start station
    print('The most common start station is ' + df['Start Station'].mode()[0] + '.')

    # display most commonly used end station
    print('The most common end station is ' + df['End Station'].mode()[0] + '.')

    # display most frequent combination of start station and end station trip
    print('The frequent combination of start station and end station is ' + df['Start End'].mode()[0] + '.')

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # display total travel time
    print('The total travel time is: {}'.format(df['Trip Duration'].sum()))

    # display mean travel time
    print('The total travel time  is: {}'.format(df['Trip Duration'].mean()))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types
    print('Counts of user types:')
    user_types = df['User Type'].value_counts()
    print(user_types)
    try:
        # Display counts of gender
        print('\nCounts of user genders:')
        user_gender = df['Gender'].value_counts()
        print(user_gender)

        # Display earliest, most recent, and most common year of birth
        earliest_yob = str(df['Birth Year'].min())
        most_recent_yob = str(df['Birth Year'].max())
        most_common_yob = str(df['Birth Year'].mode()[0])

        print('\nEarliest year of birth: ' + earliest_yob)
        print('Most recent year of birth: ' + most_recent_yob)
        print('Most common year of birth: ' + most_common_yob)
    except KeyError:
        print('There is no data on user gender or year of birth available.')

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()