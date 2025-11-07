# 🔐 Password Manager (with Tkinter)

Ένα απλό και λειτουργικό **Password Manager** σε Python, φτιαγμένο με τη βιβλιοθήκη **Tkinter** για το γραφικό περιβάλλον.  
Το πρόγραμμα σου επιτρέπει να:
- Δημιουργείς ισχυρούς τυχαίους κωδικούς
- Αποθηκεύεις και αναζητάς κωδικούς σε αρχείο `.json`
- Αντιγράφεις αυτόματα τους κωδικούς στο clipboard
- Διαχειρίζεσαι τα credentials σου με εύκολο GUI

---

## 📸 Screenshot
> <img width="514" height="431" alt="pass_manager" src="https://github.com/user-attachments/assets/360c103b-dbbe-46a8-997f-1a12fa256233" />


---

## 🧠 Features
✅ Δημιουργία ασφαλών τυχαίων κωδικών  
✅ Αυτόματη αντιγραφή στο clipboard  
✅ Αποθήκευση credentials σε `data.json`  
✅ Αναζήτηση αποθηκευμένων κωδικών ανά ιστοσελίδα  
✅ Απλό και καθαρό γραφικό περιβάλλον (Tkinter GUI)

---

## 🧩 Requirements

Για να τρέξει το πρόγραμμα, χρειάζεσαι:
- Python 3.x  
- Εγκατεστημένα τα παρακάτω modules:
  ```bash
  pip install pyperclip
  
Οι βιβλιοθήκες tkinter, json, και random είναι ενσωματωμένες στην Python.

---

## 💾 Data Storage

Οι κωδικοί αποθηκεύονται τοπικά στο αρχείο data.json με την εξής δομή:
{
  "example.com": {
    "email": "user@example.com",
    "password": "S3cuR3P@ss!",
  }
}

Τα δεδομένα δεν είναι κρυπτογραφημένα. Για προσωπική χρήση ή δοκιμή.

---

## How to Run

1) Κάνε clone το repository:
```bash
git clone https://github.com/<your-username>/<repo-name>.git
cd <repo-name>
2) Βεβαιώσου ότι έχεις την εικόνα logo.png στον ίδιο φάκελο με το script.
3) Τρέξε το Πρόγραμμα:
```bash
python main.py


---

## Functions Overview

| Συνάρτηση             | Περιγραφή                                                   |
| --------------------- | ----------------------------------------------------------- |
| `generate_password()` | Δημιουργεί και αντιγράφει έναν τυχαίο, ασφαλή κωδικό        |
| `save()`              | Αποθηκεύει το website, email και password σε αρχείο JSON    |
| `find_password()`     | Εμφανίζει αποθηκευμένα credentials για συγκεκριμένο website |
| `UI setup`            | Δημιουργεί και τοποθετεί όλα τα widgets του Tkinter GUI     |

---

## Disclaimer

Αυτό το project προορίζεται για εκπαιδευτική χρήση.
Μην χρησιμοποιείς αυτή τη μορφή αποθήκευσης για ευαίσθητα πραγματικά δεδομένα χωρίς κρυπτογράφηση.
