# 📊 Netflix Statistics Analyzer

## 🇵🇱 PL

### 📝 Opis projektu

Projekt służy do analizy danych z pliku CSV zawierającego produkcje dostępne na Netflixie. Program:

* sprawdza, czy plik CSV istnieje,
* wczytuje dane do biblioteki pandas,
* zapisuje dane do lokalnej bazy SQLite,
* wyświetla liczbę wszystkich rekordów,
* generuje wykres kołowy pokazujący udział filmów i seriali,
* generuje wykres słupkowy przedstawiający 10 krajów z największą liczbą produkcji.

---

### ⚙️ Wymagania

Aby uruchomić projekt, należy zainstalować:

* Python 3.x
* pandas
* matplotlib
* sqlite3

Instalacja wymaganych bibliotek:

```bash
pip install pandas matplotlib
```

---

### 📁 Struktura projektu

```text
projekt/
│
├── netflix_titles.csv
├── main.py
├── netflix.db
└── README.md
```

---

### ▶️ Jak uruchomić program

1. Umieść plik `netflix_titles.csv` w odpowiednim katalogu.
2. Uzupełnij poprawną ścieżkę do pliku CSV w zmiennej:

```python
csv_file = r"C:\Users\Dariusz\PyCharmMiscProject\netflix_titles\netflix_titles.csv"
```

3. Uruchom program:

```bash
python main.py
```

---

### 🚀 Funkcjonalności

#### 1. 📂 Sprawdzenie istnienia pliku CSV

Program sprawdza, czy plik istnieje. Jeśli nie, kończy działanie.

#### 2. 💾 Zapis danych do SQLite

Dane z pliku CSV są zapisywane do tabeli `netflix_titles` w bazie `netflix.db`.

#### 3. 🔢 Liczba rekordów

Program wyświetla całkowitą liczbę rekordów w tabeli.

#### 4. 🥧 Wykres kołowy

Pokazuje procentowy udział filmów i seriali w danych.

#### 5. 📊 Wykres słupkowy

Pokazuje 10 krajów z największą liczbą produkcji na Netflixie.

---

### 📈 Przykładowe wyniki

Program wyświetli:

* liczbę rekordów,
* wykres kołowy filmów i seriali,
* wykres słupkowy dla top 10 krajów produkcji.

---

