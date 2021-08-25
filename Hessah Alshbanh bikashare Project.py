import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

def get_filters(city, month, day):
    """def  Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')

    # user input for city (chicago, new york city, washington).
    while True:
        city = input('Which of the following cities you want to ckeck? chicago, new york city, or washington? ' ).lower()
        if city not in CITY_DATA:
            print('Ops, no data for this city')
            continue
        else:
            break

    # user input for month (all, january, february, ... , june)
    months = ['january', 'february', 'march', 'april', 'may', 'june', 'all']
    while True:
        month = input('which month do you choose? january, february, march, april, may, june or all: ').lower()
        if month not in months:
            print('Ops, Wrong Input')
            continue
        else:
            break
    # user input for day of week (all, monday, tuesday, ... sunday)
    days = ['Sunday','Monday','Tuesday','Wednesday','Thursday','Friday','All']
    while True:
        day = input('which day of the week do you choose? sunday, monday, tuesday, wednesday, thursday, friday, saterday or all: ').title()
        if day not in days:
            print('Ops, Wrong Input')
            continue
        else:
            break

    print('Your Choice for city is: ' , city)
    print('Your Choice for month is: ' , month)
    print('Your choice for day is: ' , day)
    print('_'*40)
    return city, month, day

def load_data(city, month, day):

    """Loads data for the specified city and filters by month and day if applicable.

    Args:
    (str) city - name of the city to analyze
    (str) month - name of the month to filter by, or "all" to apply no month filter
    (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
    df - Pandas DataFrame containing city data filtered by month and day"""

    # load data file into a dataframe
    df = pd.read_csv(CITY_DATA[city])
    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    # extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day'] = df['Start Time'].dt.weekday_name
    # filter by month if applicable
    if month != 'all':
        # use the index of the months list to get the corresponding int
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1
        # filter by month to create the new dataframe
        df = df[df['month'] == month]

    # filter by day of week if applicable
    if day != 'All':
        # filter by day of week to create the new dataframe
        df = df[df['day'] == day]

    return df

def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # Display the most common month
    popular_month = df['month'].mode()[0]
    # Display the most common day of week
    popular_day = df['day'].mode()[0]
    # Extract hour from Start Time column
    df['hour'] = df['Start Time'].dt.hour
    # Display the most common start hour
    popular_hour = df['hour'].mode()[0]

    print('Most Popular Month:', popular_month)
    print('Most Popular Day:', popular_day)
    print('Most Popular Hour:', popular_hour)
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def station_stats(df):
    """Displays statistics on the most popular stations and trip."""
    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()
    # Display most commonly used start station
    popular_start_station = df['Start Station'].mode()[0]
    # Display most commonly used end station
    popular_End_station = df['End Station'].mode()[0]
    # Display most frequent combination of start station and end station trip
    df['popular_combination_trip'] = df['Start Station'] + '&' + df['End Station']
    popular_combination_trip = df['popular_combination_trip'].mode()[0]

    print('Most Popular Start Station:', popular_start_station)
    print('Most Popular End Station:', popular_End_station)
    print('Most Frequent Combination of Start Station and End Station Trip:', popular_combination_trip)
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()
    # Display total travel time
    total_travels = df['Trip Duration'].sum()
    # Display mean travel time
    average_trips_time = df['Trip Duration'].mean()

    print('Total Travels/trips Time is:', total_travels)
    print('Average Travels/trips Time is:', average_trips_time)
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def user_stats(df):
    """Displays statistics on bikeshare users."""
    print('\nCalculating User Stats...\n')
    start_time = time.time()
    # Display counts of user types
    user_types = df['User Type'].value_counts()
    # Display counts of gender
    if 'Gender' in df:
        gender_types = df['Gender'].value_counts()
        print('counts of Users Genders is:' , gender_types)
    else:
        print('there is no gender data for this city')
    # Display earliest, most recent, and most common year of birth
    if 'Birth Year' in df:
        earliest_birth = int(df['Birth Year'].min())
        recent_birth = int(df['Birth Year'].max())
        popular_birth = int(df['Birth Year'].mode()[0])
        print('Youngest Users are born in {}, and the eldest Users Birth is {}, while Most Users born in {}.'.format(recent_birth , earliest_birth , popular_birth))
    else:
        print('there is no Birth Year data for this city')

    print('Count of Users Types is: ', user_types)
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def data(df):
    raw_input = 0
    # Asking for raw input data by using while loop.
    while True:
        # Confirming if the user wants to see the data or not by using input.
        raw = input('Do you want to view 5 rows of the data? type: yes or no? ').lower()
        if raw == 'no':
            break
        elif raw == 'yes':
            raw_input += 5
            # printing 5 rows of the data
            print(df.iloc[raw_input : raw_input + 5])
            break
        else:
            print('Wrong input')
    while True:
        # starting a new loop to add 5 more rows everytime the user asks to.
        more = input('Do you want to view 5 more rows? type: yes or no? ').lower()
        if more == 'no':
            break
        elif more == 'yes':
            raw_input += 5
            print(df.iloc[raw_input : raw_input + 5])
            continue
        else:
            print('Wrong Input')

    return raw_input

def main():
    city = []
    month = []
    day = []
    while True:
        city, month, day = get_filters(city, month, day)
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        data(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break

if __name__ == "__main__":
	main()
