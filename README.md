# Biblioteca Popular "El Aljibe" — Management System

> Python CLI management system for a community library: books, members, loans, reservations, and donations. No external dependencies.

![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)

## About

Final Integrative Project for **Programming 1** — Tecnicatura Universitaria en Desarrollo Web (UNER, 2026). A console-based application built from a real requirements document written by the library board's president of Biblioteca Popular "El Aljibe", a community library founded in 1962 in Entre Ríos, Argentina (3,200 books, 480 active members). Replaces a manual card-catalog system with a digital CLI app running locally on the library's computer.

## Features

- **Book catalog** — add, list, search (title/author/inventory number), change status, and remove books.
- **Members** — register, search, update, remove; detects inactive members (no activity in 2+ years).
- **Loans** — register loans, view active/history, return books; auto-updates book status on loan and return.
- **Reservations** — reserve unavailable books; fulfilling a reservation auto-creates a loan.
- **Donations** — register donations, track processing status (received → cataloged → integrated).
- **JSON persistence** — all data saved to files on exit; no database or external dependencies.
- **Input validation** — numeric fields, email format, confirmation prompts for destructive actions.

## Project Structure

```
biblioteca-el-aljibe/
├── biblioteca.py       Main source code (all modules)
├── catalogo.json       Book catalog data
├── socios.json         Registered members data
├── prestamos.json      Loans data
├── reservas.json       Reservations data
└── donaciones.json     Donations data
```

## Setup

**Requirements:** Python 3.10+ (uses `match/case`).

```bash
git clone https://github.com/aleoviedo071298/biblioteca-el-aljibe.git
cd biblioteca-el-aljibe
python biblioteca.py
```

---

**Alejandro Oviedo** · [LinkedIn](https://www.linkedin.com/in/aleoviedo071298/) · [GitHub](https://github.com/aleoviedo071298)
