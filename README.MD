## 🇬🇧 EN

### 📝 Project Description

This project is used to analyze data from a CSV file containing Netflix titles. The program:

* checks whether the CSV file exists,
* loads data using pandas,
* saves data into a local SQLite database,
* displays the total number of records,
* generates a pie chart showing the share of movies and TV shows,
* generates a bar chart showing the top 10 countries with the highest number of titles.

---

### ⚙️ Requirements

To run the project, you need:

* Python 3.x
* pandas
* matplotlib
* sqlite3

Install the required libraries:

```bash
pip install pandas matplotlib
```

---

### 📁 Project Structure

```text
project/
│
├── netflix_titles.csv
├── main.py
├── netflix.db
└── README.md
```

---

### ▶️ How to Run the Program

1. Download the csv file from https://www.kaggle.com/datasets/shivamb/netflix-shows?resource=download
2. Place the `netflix_titles.csv` file in the correct directory.
3. Update the CSV file path in the following variable:

```python
csv_file = r"C:\Users\Dariusz\PyCharmMiscProject\netflix_titles\netflix_titles.csv"
```

3. Run the program:

```bash
python main.py
```

---

### 🚀 Features

#### 1. 📂 CSV File Check

The program checks whether the CSV file exists. If not, it stops execution.

#### 2. 💾 Save Data to SQLite

Data from the CSV file is saved into the `netflix_titles` table in the `netflix.db` database.

#### 3. 🔢 Record Count

The program displays the total number of records in the table.

#### 4. 🥧 Pie Chart

Shows the percentage share of movies and TV shows.

#### 5. 📊 Bar Chart

Shows the top 10 countries with the highest number of Netflix titles.

---

### 📈 Example Output

The program displays:

* the total number of records,
* a pie chart of movies vs TV shows,
* a bar chart for the top 10 production countries.
