# 🧮 UtilityHub

> **An all-in-one collection of calculators and unit converters built with Python, Streamlit, and FastAPI.**

UtilityHub is a modular utility application designed to bring commonly used calculators and unit converters into one clean and easy-to-use platform.

The project follows a **Frontend → API → Service** architecture, keeping the user interface, API endpoints, validation, and business logic separated and maintainable.

---

## ✨ Features

### 🧮 Calculators

UtilityHub currently provides several useful calculators:

- Basic Calculator
- Scientific Calculator
- CGPA Calculator
- GPA Calculator
- BMI Calculator
- Age Calculator
- Percentage Calculator

### 🔄 Converters

The application also provides multiple unit converters:

- Length Converter
- Weight Converter
- Temperature Converter
- Volume Converter
- Area Converter

---

## 🎯 Project Goals

The main goals of UtilityHub are:

- Build a practical Python application
- Practice FastAPI backend development
- Practice Streamlit frontend development
- Implement REST API communication
- Apply Pydantic data validation
- Separate business logic using service classes
- Build a modular and scalable project structure
- Create a professional and user-friendly interface

---

# 🏗️ Architecture

UtilityHub follows a layered architecture.

```text
                 ┌──────────────────────┐
                 │      Streamlit       │
                 │      Frontend        │
                 └──────────┬───────────┘
                            │
                            │ HTTP Request
                            ▼
                 ┌──────────────────────┐
                 │       FastAPI        │
                 │       Routers        │
                 └──────────┬───────────┘
                            │
                            ▼
                 ┌──────────────────────┐
                 │      Pydantic        │
                 │       Schemas        │
                 └──────────┬───────────┘
                            │
                            ▼
                 ┌──────────────────────┐
                 │      Services        │
                 │   Business Logic     │
                 └──────────┬───────────┘
                            │
                            ▼
                         Result
                            │
                            ▼
                 ┌──────────────────────┐
                 │      Streamlit       │
                 │      UI Result       │
                 └──────────────────────┘
