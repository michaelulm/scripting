#!/usr/bin/env python3
import pymysql      # pip3 install PyMySQL
import sys, csv, os # multiple imports in one line are possible
import datetime


## ----- Database Connection ----- ##
TABLE        = 'Arbeitszeit'
DROP_TABLE   = f'DROP TABLE IF EXISTS {TABLE}'
CREATE_TABLE = f'''CREATE TABLE {TABLE} (
    id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    mitarbeiter VARCHAR(255) NOT NULL, 
    datum DATE NOT NULL,
    von DATETIME NOT NULL DEFAULT 0,
    bis DATETIME NOT NULL DEFAULT 0,
    typ CHAR(1) NULL
);
'''
# added default value for 'von' and 'bis' (0 means, that MariaDB will insert a datetime with value 0000-00-00 00:00:00)

# extract DB-Config (Host, User, Password, Database) into separate variables -> easiar to change!
DB_HOST = 'localhost'
DB_USER = 'timekeeping'
DB_PASS = ''
DB_DABS = 'timekeeping'

try:
    DB = pymysql.connect(DB_HOST, DB_USER, DB_PASS, DB_DABS)
except Exception as e:
    print('Error connecting to DB:', e)
    sys.exit(1) # exit script at this point!



## ----- Database operations ----- ##
def init_table():
    try:
        with DB.cursor() as cursor:
            cursor.execute(DROP_TABLE)
            cursor.execute(CREATE_TABLE)
    except Exception as e:
        print('Error on init:', e)


def insert(sql, data):
    try:
        with DB.cursor() as cursor:
            cursor.execute(sql, data)
            DB.commit()
    except Exception as e:
        print('error while db operation (insert):', e)


def select(sql, data = None):
    try:
        with DB.cursor() as cursor:
            cursor.execute(sql, data)
            rows = cursor.fetchall()
            return rows
    except Exception as e:
        print('error while db operation (select):', e)


def insert_working_hours(employee, date, start, end):
    sql = f"INSERT INTO {TABLE} VALUES(DEFAULT, %s, %s, %s, %s, NULL)"
    insert(sql, (employee, date, start, end))


def insert_working_type(employee, date, working_type):
    sql = f"INSERT INTO {TABLE} (mitarbeiter, datum, typ) VALUES(%s, %s, %s)"
    insert(sql, (employee, date, working_type))


def select_employees():
    sql = f"SELECT DISTINCT mitarbeiter FROM {TABLE}"
    return select(sql)


def select_times4employee(employee):
    sql = f"SELECT datum, von, bis, typ FROM {TABLE} WHERE mitarbeiter = %s ORDER BY von"
    return select(sql, employee)


## ----- CSV operations ----- ##
def read_csv(filename):
    try:
        with open(filename) as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=';', quotechar='"')  ## better naming. at this point, we got a READER-Object and no data-object!
            csv_data = []    ## put read data into list, to return it at the end. you can't return the reader-object, because it needs an open file (and file will be automatically closed at the end of the `with` block!)
            for row in csv_reader:
                csv_data.append(row)
                '''
                for column in row:                  ## debug output!
                    print(f'{column:^10s}', end='') ## debug output!
                print()                             ## debug output!
                '''
            return csv_data  ## return csv_data (list of 'rows') to handle data on another place
    except Exception as e:
        print('Error on csv operation:', e)


def get_csv_files():
    files = os.listdir() # get all items in current working directory
    csv_files = []
    for f in files:
        # return just files that end on '.csv'
        if f.lower().endswith('.csv'):
            csv_files.append(f)
    return csv_files



## ----- helper functions ----- ##
## helper function to check if a value is an int/castable to int; returns boolean ##
def is_int(value):
    try:
        int(value)
        return True
    except ValueError:
        return False


## helper function to split a time formatted string (hh:mm); returns a tuple -> (int, int) ##
def split_timestr(timestr):
    l = timestr.split(':')
    if len(l) == 2:
        if is_int(l[0]) and is_int(l[1]):
            hour   = int(l[0])
            minute = int(l[1])
            # check value is 'between' borders
            if (0 <= hour <= 23) and (0 <= minute <= 59): return hour, minute
    return None, None


## helper function to build a datetime-object from separate date and time objects; returns datetime.datetime() ##
def get_datetime(date, time):
    if isinstance(date, datetime.date) and isinstance(time, datetime.time):
        return datetime.datetime(date.year, date.month, date.day, 
                                time.hour, time.minute, time.second, 
                                time.microsecond, time.tzinfo)


## helper function to build a date-object; returns datetime.date() or raises an Exception ##
def get_date(day, month, year):
    MONTHS = ['january', 'february', 'march', 'april', 'may', 'june', 'july', 'august', 'september', 'october', 'november', 'december']
    # list.index() will throw an error, when value not exists!
    try: month = MONTHS.index(month.lower()) + 1  
    except ValueError: month = 0
    if is_int(day) and is_int(year) and month > 0:
        return datetime.date(int(year), month, int(day))
    else:
        raise Exception(f'not a valid date ({day},{month},{year})')


## helper function to build a time-object; returns datetime.time() or None ##
def get_time(timestr):
    hour, minute = split_timestr(timestr) 
    if (hour is not None) and (minute is not None):
        return datetime.time(hour, minute)


## helper function to get timedelta-object (delta of two datetime, date or time objects); returns datetime.timedelta()
def get_timediff(first, second):
    if first > second: return first - second
    else:              return second - first 


## helper function to create worked hours string in format HH:MM; returns str()
def get_worked_hours(worked_seconds):
    hours   = int(worked_seconds // 60 // 60)
    minutes = round(((worked_seconds / 60 / 60) - hours) * 60)
    return f'{hours:02}:{minutes:02}'


## ----- helper functions for formatted output (fixed width = 80) ----- ##
OUTPUT_WIDTH = 80
def print_header(value):
    vl = len(value)
    prefix = ((OUTPUT_WIDTH-vl-2) // 2) * '-'
    suffix = prefix if vl % 2 == 0 else prefix + '-'
    print(f'{prefix} {value} {suffix}')


def print_sub_header(value):
    value = f'[ {value} ]'
    print(f'{value:^{OUTPUT_WIDTH}}')


def print_content(key, value):
    space = OUTPUT_WIDTH-len(str(key))-1
    print(f'{key}:{value:>{space}}')



## ----- import function, to import available (valid) CSV-Data into database ----- ##
def import_data():
    TYPES = ('f', 'k', 'u', 'z')      # will only support types Feiertag, Krankenstand, Urlaub and Zeitausgleich
    for csv_file in get_csv_files():  ## Problem in lecture: use useful naming! at this point, we got just the file(names), not the content of the csv files!
        clean_filename = csv_file.replace('.csv', '')  # remove file extension from filename
        splits = clean_filename.split('_')             # split parts of filename into list => (lastname, firstname, month, year)
        employee = f'{splits[0]} {splits[1]}'
        print(csv_file, clean_filename, splits, employee) ## debug output
        csv_data = read_csv(csv_file) ## before we can access rows and columns of the csv_file, we have to read them with our `read_csv` function
        for row in csv_data:
            # schema of row should be: day_of_month, day_of_week_num, day_of_week_name, type, am_from, am_to, pm_from, pm_to, break_from, break_to, total
            if len(row) == 11:
                try:
                    date    = get_date(row[0], splits[2], splits[3])
                    w_type  = row[3].lower()
                    
                    am_from = get_time(row[4])
                    am_to   = get_time(row[5])
                    pm_from = get_time(row[6])
                    pm_to   = get_time(row[7])

                    ## debug output, e.g.: 2019-09-20 [ ] | am: 07:00:00 - 11:30:00        pm: 12:00:00 - 16:10:00
                    print(f'{date} [{w_type:^1}] | am: {str(am_from):^8} - {str(am_to):^8}\tpm: {str(pm_from):^8} - {str(pm_to):^8}')

                    if w_type in TYPES:
                        insert_working_type(employee, date, w_type)
                    if (am_from is not None) and (am_to is not None):
                        insert_working_hours(employee, date, get_datetime(date, am_from), get_datetime(date, am_to))
                    if (pm_from is not None) and (pm_to is not None):
                        insert_working_hours(employee, date, get_datetime(date, pm_from), get_datetime(date, pm_to))
                except Exception as e:
                    print('ERROR while importing data:', e)


## ----- statistic function, read database content and print it out ----- ##
def create_statistic():
    employees = select_employees()
    for employee in employees:
        # datum, von, bis, typ
        data = select_times4employee(employee)
        months = dict()   # dictionary to save different months (year-month), e.g.: {'2019-08': {data}, '2019-09': {data}}
        
        print_header(employee[0])
        for row in data:
            month = f'{row[0]:%Y-%m}'
            if month not in months:
                ## initialise sub-dictionary for 'new' month. 
                months[month] = {
                   'total_seconds'   : 0,
                   'bonus_time_days' : 0,
                   'vacation_days'   : 0,
                   'sick_leave_days' : 0,
                }

            ## increment 'special' days/types
            if   row[3] == 'z': months[month]['bonus_time_days'] += 1
            elif row[3] == 'u': months[month]['vacation_days']   += 1
            elif row[3] == 'k': months[month]['sick_leave_days'] += 1
            
            ## ignore dates, where no valid (e.g. 0000-00-00 00:00:00) datetimes in 'von' (row[1]) and 'bis' (row[2])
            if isinstance(row[2], datetime.datetime) and isinstance(row[1], datetime.datetime):
                months[month]['total_seconds'] += get_timediff(row[2], row[1]).total_seconds()

        ## print formatted output
        for key, val in months.items():
            print_sub_header(key)
            print_content('Worked Hours', get_worked_hours(val['total_seconds']))
            print_content('Consumed Bonustime Days', val['bonus_time_days'])
            print_content('Consumed Vacation Days', val['vacation_days'])
            print_content('Sick Leave Days', val['sick_leave_days'])



print('INIT DATABASE-TABLE')
init_table()

print('\nIMPORT DATA FROM CSV TO DATABASE')
import_data()

print()
create_statistic()


# finally, close the database!
DB.close()
