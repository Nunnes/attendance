import sqlite3
from sqlite3 import Error
import datetime
 
def create_connection(db_file):
    """ create a database connection to a SQLite database """
    try:
        return sqlite3.connect(db_file)
    except Error as e:
        print(e)

    return None

def create_table(conn):
    """ create a table from the create_table_sql statement
    :param conn: Connection object
    :param create_table_sql: a CREATE TABLE statement
    :return:
    """
    sql_create_attendance_table = """ CREATE TABLE IF NOT EXISTS attendance (
                                        id integer PRIMARY KEY,
                                        rfid text NOT NULL,
                                        date text NOT NULL,
                                        time text NOT NULL
                                    ); """
    try:
        c = conn.cursor()
        c.execute(sql_create_attendance_table)
    except Error as e:
        print(e)

def insert_attendance(conn,attendance):
    if conn is None:
        print("conn is none")
        return

    today = datetime.date.today()
    date = today.strftime('%d - %A')
    now_time = datetime.datetime.now().strftime('%H:%M:%S')
    attendance = ("0016581666", date, now_time)

    print("insert into attendace")
    sql = ''' INSERT INTO attendance(rfid,date,time)
              VALUES(?,?,?) '''
    cur = conn.cursor()
    cur.execute(sql, attendance)
    return cur.lastrowid
    
def init(db_path):
    conn = create_connection(db_path + "/attendance.db")
    create_table(conn)
    return conn

def main():
    database = "./data/attendance.db"
 
  # create a database connection
    conn = create_connection(database)

    while True: 
        print("Menu")
        print("1 - Create table")
        print("2 - Insert into table")

        option = input("Choose action:")        

        if option == 1:
            if conn is not None:
                # create projects table
                create_table(conn)         
            else:
                print("Error! cannot create the database connection.")

        if option == 2:
            with conn:
                print("inseting data")
                today = datetime.date.today()
                date = today.strftime('%d - %A')
                now_time = datetime.datetime.now().strftime('%H:%M:%S')
                attendance = ("0016581666", date, now_time)
                insert_attendance(conn, attendance)


if __name__ == '__main__':
    main()