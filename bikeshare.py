import time
import pandas as pd
import numpy as np

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
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    while True:
        city = (str(input('\nPlease enter the name of one of the following cities that you want to analyze: chicago, new york city, washington.\n'))).lower()
        if city in ['chicago', 'new york city', 'washington']:
            break  
        else:
            print('\nPlease try again!\n')
            print('{} is not a valid city name.'.format(city))
                        
    # TO DO: get user input for month (all, january, february, ... , june)
    while True:
        month = (str(input('\nPlease enter one of the following months that you want to analyze: all, january, february, march, april, may, june.\n'))).lower()
        if month in ['all','january', 'february', 'march', 'april', 'may', 'june']:
            break   
        else:
            print('\nPlease try again!\n')
            print('{} is not a valid month.'.format(month))
            
    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    while True:
        day = (str(input('\nPlease enter one of the following weekdays that you want to analyze: all, monday, tuesday, wednesday, thursday, friday, saturday, sunday.\n'))).lower()
        if day in ['all', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']:
            break
        else:
            print('\nPlease try again!\n')
            print('{} is not a valid weekday.'.format(day))
           
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
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name
    df['hour'] = df['Start Time'].dt.hour
    
    if month != 'all':
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1
        df = df[df['month'] == month]

    if day != 'all':
        df = df[df['day_of_week'] == day.title()]

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    month = df['month'].mode()[0]
    months = ['January', 'February', 'March', 'April', 'May', 'June']
    top_month = months[month - 1]
    print('The most common month:', top_month)

    # TO DO: display the most common day of week
    top_day = df['day_of_week'].mode()[0]
    print('The most common day of week:', top_day)

    # TO DO: display the most common start hour
    top_hour = df['hour'].mode()[0]
    print('The most common start hour:', top_hour)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

    
def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    top_start_station = df['Start Station'].mode()[0]
    print('The most commonly used start station is:', top_start_station)

    # TO DO: display most commonly used end station
    top_end_station = df['End Station'].mode()[0]
    print('The most commonly used end station is:', top_end_station)

    # TO DO: display most frequent combination of start station and end station trip
    top_start_end_station = df.groupby(['Start Station', 'End Station']).size().sort_values(ascending=False).head(1)
    print('\nThe most frequent combination of start and end station with number of occurence is:\n',top_start_end_station)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

    
def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_travel_time = df['Trip Duration'].sum()
    total_travel_time /= 360
    print('The total travel time is: {} hours.'.format(total_travel_time))

    # TO DO: display mean travel time
    mean_travel_time = df['Trip Duration'].mean()
    mean_travel_time /= 60
    print('The mean travel time is: {} minutes.'.format(mean_travel_time))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

    
def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    count_user_types = df.groupby('User Type').size()
    print('This is the user type distribution:\n',count_user_types)

    # TO DO: Display counts of gender
    if 'Gender' in df.columns:
        count_gender = df.groupby('Gender').size()
        print('\nThis is the gender distribution:\n',count_gender)
    else:
        print('\nThis dataset has no gender data available.\n')
        pass
      
    # TO DO: Display earliest, most recent, and most common year of birth
    if 'Birth Year' in df.columns:
        earliest_year = df['Birth Year'].min()
        print('\nThe earliest year of birth is {}.'.format(int(earliest_year)))
        
        most_recent_year = df['Birth Year'].max()
        print('The most recent year of birth is {}.'.format(int(most_recent_year)))

        favorite_year = df['Birth Year'].mode()[0]
        print('The most common year of birth is {}.'.format(int(favorite_year)))
    else:
        print('This dataset has no birth year data available.')
        pass
            
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
  
                           
    # TO DO: Prompt the user if they want to see 5 lines of raw data and display that data if the answer is 'yes'
    df = df.drop(['month', 'day_of_week', 'hour'], axis = 1)
    starting_row = 0
    raw_data = input('\nWould you like to see 5 rows of the raw data of the bikeshare dataset? Enter yes or no.\n').lower()
    input_options = ['yes', 'no']
    while raw_data not in input_options:
        print('\nInvalid input, please try again!')
        raw_data = input('\nWould you like to see 5 rows of the raw data of the bikeshare dataset? Enter yes or no.\n').lower()    
    # TO DO: Continue user prompts and display 5 additional lines of raw data until the user says 'no'
    while True:
        if raw_data == 'no':
            return
        if raw_data == 'yes':
            print(df[starting_row: starting_row + 5])
            input_options = ['yes', 'no']
            starting_row += 5
            raw_data = input('\nWould you like to see 5 more rows of the raw data? Enter yes or no.\n').lower()
            while raw_data not in input_options:
                print('\nInvalid input, please try again!')
                raw_data = input('\nWould you like to see 5 rows of the raw data of the bikeshare dataset? Enter yes or no.\n').lower()    
       
        
def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        
        restart = input('\nWould you like to restart? Enter yes or no.\n').lower()
        input_options = ['yes', 'no']
        while restart not in input_options:
            print('\nInvalid input, please try again!')
            restart = input('\nWould you like to restart? Enter yes or no.\n').lower() 
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
