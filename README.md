# Biblioteca Popular "El Aljibe" — Management System

A management system for the Biblioteca Popular "El Aljibe", built as the Final
Integrative Project for the **Programming 1** course of the Tecnicatura
Universitaria en Desarrollo Web (UNER — Facultad de Ciencias de la Administración,
1st semester 2026).

## About the Course

Programming 1 is the introductory programming course of the degree. It covers the
fundamentals of software development in Python: variables, control structures,
functions, data structures (lists, dictionaries, tuples), JSON file handling, and
code modularization.

The final integrative project asks students to put everything learned into
practice, get close to building a real program against a client's requirements, and
make their own design decisions.

## Project Context

Biblioteca Popular "El Aljibe" is a community library founded in 1962 in a small
town in Entre Ríos, Argentina, 40 km from Concordia. With 3,200 books and 480 active
members, it needed to replace its manual card-catalog system with a digital
application running locally on the library's computer.

The system was built from a requirements document written by the library board's
president, simulating a real development scenario with a client.

## Features

The system manages five core modules through an interactive console menu interface:

### 1. Book Catalog
- Add, list (with status filters), search (by title, author, or inventory number), change status, and remove books.
- States: available, on loan, under repair, retired.

### 2. Members
- Register, list, search (by card number, ID, or name), update, and remove members.
- Categories: general, retired, student, child.
- Detection of inactive members (no activity in over 2 years).
- Viewing a member shows their loan history.

### 3. Loans
- Register a loan, which automatically sets the book's status to "on loan".
- View active loans and history.
- Search by book inventory number or member ID.
- Register a return, which automatically sets the book's status back to "available".
- On return, the system flags any pending reservations for that book.

### 4. Reservations
- Reserve books that are currently unavailable.
- List active reservations, search by book or member.
- Mark a reservation as fulfilled (automatically creates a new loan).
- Cancel reservations.

### 5. Donations
- Register, list, search (by donor or date), and update processing status.
- States: received, cataloged, integrated.

## Technical Overview

| Aspect | Detail |
|---|---|
| **Language** | Python 3 |
| **Persistence** | JSON files (catalog, members, loans, reservations, donations) |
| **Interface** | Console (CLI) with interactive menus |
| **External dependencies** | None — standard library only (`json`, `datetime`, `os`) |

### Project Structure

```
biblioteca-el-aljibe/
├── biblioteca.py        Main source code
├── catalogo.json         Book catalog data
├── socios.json            Registered members data
├── prestamos.json         Loans data
├── reservas.json          Reservations data
├── donaciones.json        Donations data
└── README.md
```

### Design Decisions

- **Reusable utility functions**: `buscar_por_id()`, `buscar_por_texto()`, `siguiente_id()`, `confirmar()`, `pedir_entero()`, `pedir_email()` avoid duplicated logic.
- **Input validation**: numeric fields only accept digits, emails require `@`, and destructive actions require confirmation.
- **Auto-incrementing IDs**: each entity generates its next ID from the current maximum.
- **Automatic referential integrity**: registering a loan sets the book to "on loan"; returning it sets it to "available"; fulfilling a reservation auto-creates a loan.
- **Persistence on exit**: data is saved back to the JSON files when the program closes.

## How to Run

```bash
python biblioteca.py
```

Requires **Python 3.10+** (uses `match/case`).

## Evaluation Criteria

Per the integrative project guidelines, the following are assessed:
- **Accuracy**: the program meets the requirements document.
- **Efficiency**: solutions are optimal and non-redundant.
- **Code quality**: consistent indentation and good practices.
- **Presentation**: oral defense of the project.

---

*Built for the Tecnicatura Universitaria en Desarrollo Web — UNER, Facultad de Ciencias de la Administración (2026).*
