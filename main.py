# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import pandas as pd
import sqlite3
import os
import matplotlib.pyplot as plt

def netflix_statistics(name):
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
    print(count)

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

    cursor.close()
    connection.close()

    print("Dane zostały zapisane do SQLite")


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    netflix_statistics('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
