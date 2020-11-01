import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york': 'new_york_city.csv',
              'washington': 'washington.csv' }
Months = ['january','february', 'march', 'april', 'may', 'june', 'all']

Days = ['monday', 'tuesday', 'wednesday','thursday','friday','saturday', 'sunday', 'all']

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
    CityChosen = input("Would you like to see data for Chicago, New York, or Washington?")

    while CityChosen.lower() not in CITY_DATA.keys():
        print ("Sorry, There is not info for this city")
        CityChosen = input("Would you like to see data for Chicago, New York, or Washington?")

    # TO DO: get user input for month (all, january, february, ... , june)

    MonthChosen = input("Which month? {}?".format(Question_Text(Months)))

    while MonthChosen.lower() not in Months:
        print ("Sorry, There is not info for this month")
        MonthChosen = input("Which month? {}?".format(Question_Text(Months)))

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)


    DayChosen = input("Which day? {}?".format(Question_Text(Days)))

    while DayChosen.lower() not in Days:
        print ("Sorry, There is not info for this day. You could try again")
        DayChosen = input("Which day? {}?".format(Question_Text(Days)))


    print('-'*40)

    return CityChosen, MonthChosen, DayChosen

def Question_Text(lista):

    Question = ""
    i = 0
    for elemento in lista:
        i=i+1
        if i < len(lista)-1:
            Question = Question + elemento.title() + ", "
        elif i == len(lista) :
            Question = Question + " or " + elemento.title()
        else:
            Question = Question + elemento.title()

    return Question


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
    df = pd.read_csv(CITY_DATA[city.lower()])
    df['Start Time']= pd.to_datetime(df['Start Time'])
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name


     # filter by month if applicable
    if month.lower() != 'all':
        # use the index of the months list to get the corresponding int
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month.lower()) + 1


        # filter by month to create the new dataframe
        df = df[df['month'] == month]

    # filter by day of week if applicable
    if day.lower() != 'all':
        # filter by day of week to create the new dataframe
        df = df[df['day_of_week'] == day.title()]

    #print (df.head())

    return df


def time_stats(df, month, day):

    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month

    if month.lower() == "all":
        Most_Common_Month_index = df['month'].mode()[0]
        Most_Common_Month = Months[Most_Common_Month_index-1]

        print ('Most popular month: {}'.format(Most_Common_Month.title()))

    # TO DO: display the most common day of week

    if day.lower() == "all":
        Most_Common_Day = df['day_of_week'].mode()[0]


        print ('Most popular day: {}'.format(Most_Common_Day))

    # TO DO: display the most common start hour
    df['Hour_Start_Time'] = df['Start Time'].dt.hour

    Most_Common_Hour = df['Hour_Start_Time'].mode()[0]

    print ('Most popular hour: {}'.format(Most_Common_Hour))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    Most_Common_Start_Station = df['Start Station'].mode()[0]
    print ('Most commonly used start station: {}'.format(Most_Common_Start_Station))

    # TO DO: display most commonly used end station
    Most_Common_End_Station = df['End Station'].mode()[0]
    print ('Most commonly used end station: {}'.format(Most_Common_End_Station))

    # TO DO: display most frequent combination of start station and end station trip
    Start_Station = df['Start Station']
    End_Station = df['End Station']

    popular_stations_combination = df.groupby(['Start Station', 'End Station']).size().sort_values(ascending=False).nlargest(1)

    print ("Most popular trip: ")
    print (popular_stations_combination.to_string())

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time


    Duration = df['Trip Duration'].sum()

    print ("Total time traveled: {}".format(Duration))


    # TO DO: display mean travel time

    AverageDuration = df['Trip Duration'].mean()

    print ("Average travel time: {}".format(AverageDuration))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types

    User_Type_Count = df['User Type'].value_counts()

    print ('User types : ')
    print(User_Type_Count.to_string())
    print ("")

    # TO DO: Display counts of gender
    try:
        CountGender = df['Gender'].value_counts()

        print ('Gender Count :')
        print (CountGender.to_string())
        print ("")
    except:
        print ("There is no data on the gender of the users")


    # TO DO: Display earliest, most recent, and most common year of birth
    try:
        Earliest_Year = int(df['Birth Year'].min())
        Recent_Year = int(df['Birth Year'].max())
        Common_Year = int(df['Birth Year'].mode())

        print ('Earliest year of birth: {}'.format(Earliest_Year))
        print ('Recet year of birth: {}'.format(Recent_Year))
        print ('Common year of birth: {}'.format(Common_Year))

    except:
        print ('There is no data on user birthdays')


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


    ViewRawData = input('Would you like to see first 5 rows of data? Please enter yes or no:')

    if ViewRawData.lower() == 'yes':
        TimesRawData = 0
        while True:
            print(df.iloc[TimesRawData:TimesRawData+5])
            TimesRawData += 5
            More_data = input('Would you like to see next 5 rows of data? Please enter yes or no: ')
            if More_data.lower() != "yes":
                break

def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df, month, day)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
