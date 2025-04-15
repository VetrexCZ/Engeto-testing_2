# Engeto: Automatizované Testy pro StartupJobs.cz

## Popis Projektu
Tento projekt obsahuje automatizované testy pro určenou webovou stránku s využitím nástrojů Playwright a Python. Testy ověřují základní funkčnost, vyhledávání a výkon webových stránek.

## Požadavky
- Python 3.x
- Playwright
- pytest

## Instalace
```bash
pip install playwright pytest
playwright install chromium
```

## Testovací Případy

### 1. Test Ověření Stránky (test_vysledku_stranky)
Ověřuje základní prvky stránky:
- Kontroluje správnost titulku stránky
- Ověřuje text autorských práv v patičce

### 2. Test Funkce Vyhledávání (test_funkce_vyhledavani)
Testuje funkci vyhledávání:
- Potvrzuje souhlas s cookies
- Zadává "Tester" do vyhledávacího pole
- Ověřuje výsledky vyhledávání
- Kontroluje přítomnost hledaného výrazu v URL a výsledcích

### 3. Test Výkonu (test_vykonu)
Měří a ověřuje výkon stránky:
- Měří dobu načítání stránky
- Ověřuje, že načítání trvá méně než 3 sekundy
- Kontroluje viditelnost klíčových prvků stránky
