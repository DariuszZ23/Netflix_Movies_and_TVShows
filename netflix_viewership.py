# This project is used to analyze data from a CSV file containing Netflix titles.
from sqlite3 import Connection, Cursor
import pandas as pd
import sqlite3
import os
import matplotlib.pyplot as plt

def netflix_statistics(name):
    connection, cursor = get_db_connection()
    netflix_productions_by_type(cursor)
    productions_by_country(cursor)
    cursor.close()
    connection.close()

def productions_by_country(cursor: Cursor):
    # top 10 krajów produkcji
    cursor.execute("""
                   SELECT country, COUNT(*) AS total_titles
                   FROM netflix_titles
                   WHERE country IS NOT NULL
                     AND country != ''
                   GROUP BY country
                   ORDER BY total_titles DESC
                       LIMIT 10;
                   """)

    results = cursor.fetchall()

    countries = []
    totals = []

    for country, total in results:
        countries.append(country)
        totals.append(total)

    plt.figure(figsize=(12, 6))
    plt.bar(countries, totals)

    plt.xlabel("Kraj")
    plt.ylabel("Liczba produkcji")
    plt.title("10 najpopularniejszych krajów produkcji na Netflix")

    plt.xticks(rotation=45, ha='right')
    plt.tight_layout()

    plt.show()


def netflix_productions_by_type(cursor: Cursor):
    # ilość filmów (movies) i seriali
    cursor.execute("""
                   SELECT type, COUNT(*)
                   FROM netflix_titles
                   GROUP BY type;
                   """)

    results = cursor.fetchall()

    labels = []
    sizes = []

    for row in results:
        labels.append(row[0])
        sizes.append(row[1])

    plt.figure(figsize=(8, 8))
    plt.pie(sizes, labels=labels, autopct='%1.1f%%')

    plt.title("Udział filmów i seriali na Netflix")
    plt.show()


def get_db_connection() -> tuple[Connection, Cursor]:
    csv_file = r"./netflix_titles.csv"
    if os.path.exists(csv_file):
        print("Plik istnieje")
    else:
        print("Plik nie istnieje")
        quit()
    print(os.getcwd())
    db_file = "netflix.db"
    df = pd.read_csv(csv_file)
    connection = sqlite3.connect(db_file)
    cursor = connection.cursor()
    df.to_sql(
        name="netflix_titles",
        con=connection,
        if_exists="replace",
        index=False
    )

    # ilość wierszy w tabeli
    cursor.execute("SELECT COUNT(*) FROM netflix_titles;")
    count = cursor.fetchone()[0]
    print("Records: " + str(count))
    return connection, cursor


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    netflix_statistics('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
