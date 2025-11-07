# 🚗 Miles to Kilometers Converter (Python + Tkinter)

Ένα απλό αλλά χρήσιμο πρόγραμμα μετατροπής **μιλίων σε χιλιόμετρα**, φτιαγμένο με **Python** και **Tkinter GUI**.  
Ιδανικό για εξάσκηση σε βασικό GUI προγραμματισμό με Python.

---

## 📸 Screenshot
> <img width="500" height="329" alt="miles_km" src="https://github.com/user-attachments/assets/48c3446a-07b5-4c4b-ade2-936056953532" />


---

## 🧠 Features

✅ Μετατρέπει Miles → Kilometers με ένα κλικ  
✅ Εύκολο, καθαρό και responsive GUI  
✅ Έλεγχος εγκυρότητας για λανθασμένες τιμές εισόδου  
✅ Αυτόματη ενημέρωση του πεδίου αποτελέσματος  

---

## 🧰 Requirements

Για να τρέξει το πρόγραμμα χρειάζεσαι:

- **Python 3.x**  
- Δεν απαιτούνται εξωτερικά modules (μόνο η ενσωματωμένη βιβλιοθήκη `tkinter`)

---

## 🚀 How to Run

1. Κάνε **clone** το repository:
   ```bash
   git clone https://github.com/<your-username>/<repo-name>.git
   cd <repo-name>
   ```
2. Τρέξε το πρόγραμμα:
   ```bash
   python main.py
   ```

---

## How it works

Η συνάρτηση miles_to_km():
  1) Παίρνει την τιμή από το πεδίο Miles
  2) Τη μετατρέπει σε float
  3) Πολλαπλασιάζει με 1.60934 (το conversion rate)
  4) Εμφανίζει το αποτέλεσμα στο πεδίο Kilometers
  5) Αν η είσοδος δεν είναι αριθμός, εμφανίζει “Wrong”

---

## Functions

| Συνάρτηση       | Περιγραφή                                                                 |
| --------------- | ------------------------------------------------------------------------- |
| `miles_to_km()` | Κάνει τη μετατροπή Miles → Kilometers και ενημερώνει το GUI               |
| `UI setup`      | Δημιουργεί και τοποθετεί τα widgets του Tkinter (labels, entries, button) |

---

## Διάταξη GUI
```
+--------------------------------------------+
|  [ Miles Input ] Miles                     |
|  is equal to  [ KM Output ] KM             |
|            [   Calculate Button   ]        |
+--------------------------------------------+
```
