# Proiect BDD – OrangeHRM Automation Testing

## Descriere proiect
Acest proiect reprezintă o suită de teste automate de tip **BDD (Behavior Driven Development)** pentru aplicația web **OrangeHRM**, folosind **Python, Behave și Selenium WebDriver**.

Scopul proiectului este validarea funcționalităților principale ale aplicației OrangeHRM, precum:
- autentificarea utilizatorilor
- gestionarea angajaților (adăugare, căutare, editare)
- verificarea funcționalităților din Dashboard

Aplicația testată este versiunea demo OrangeHRM:  
https://opensource-demo.orangehrmlive.com

---

## Tipuri de teste
- ✅ Teste funcționale automate
- ✅ Teste BDD (Gherkin – Given / When / Then)
- ❌ Teste negative (login cu date invalide)

---

## Tehnologii folosite
- **Python**
- **Behave**
- **Selenium WebDriver**
- **Page Object Model (POM)**
- **Gherkin**
- **ChromeDriver**

---

## Structura proiectului
```
Proiect-BDD-OrangeHRM/
├── features/
│   ├── login.feature
│   ├── dashboard.feature
│
│── steps/
│       ├── login_steps.py
│       └── dashboard_steps.py
├── pages/
│   ├── base_page.py
│   ├── login_page.py
│   └── dashboard_page.py
├── browser.py
├── environment.py
├── requirements.txt
└── README.md
```

---

## Rulare teste
```bash
behave
```

---

## Autor
Proiect creat în scop educațional pentru testare automată BDD.
