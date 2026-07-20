# 🧰 Multi-Utility Toolkit (Moduler & Packager)

A Python-based **Multi-Utility Toolkit** that combines standard (built-in) modules, custom modules, and a custom package into one simple, menu-driven console application.

![Python](https://img.shields.io/badge/Python-3.8%2B-blue)
![Status](https://img.shields.io/badge/Status-Complete-brightgreen)
![License](https://img.shields.io/badge/License-MIT-lightgrey)

---

## 📖 Overview

This project demonstrates Python's **modular structure** — built-in modules, custom modules, and custom packages — by building practical utility tools for:

- 📅 Date & time operations
- 🧮 Mathematical calculations
- 🎲 Random data generation
- 🆔 Unique ID (UUID) generation
- 📂 File handling
- 🔍 Dynamic module exploration with `dir()`
- 📏 Unit conversions

---

## 📁 Project Structure

```
MultiUtilityToolkit/
├── main.py                 # Entry point — menu-driven UI
├── datetime_ops.py         # Built-in: datetime, time
├── math_ops.py              # Built-in: math
├── random_ops.py            # Built-in: random
├── uuid_ops.py               # Built-in: uuid
├── explorer.py                # Dynamic module exploration using dir()
├── utility_pkg/                # Custom PACKAGE
│   ├── __init__.py             # Initializes the package
│   ├── file_ops.py             # Custom module: create/write/read/append files
│   └── math_custom.py          # Custom module: unit conversions
├── data_files/                  # Auto-created folder for file operations output
└── README.md
```

---

## ✨ Features

| # | Module | What it does |
|---|--------|---------------|
| 1 | **Datetime & Time Operations** | Current date/time, date difference, custom `strftime` formatting, stopwatch, countdown timer |
| 2 | **Mathematical Operations** | Factorial, compound interest, trigonometry (sin/cos/tan), area of circle/rectangle/triangle |
| 3 | **Random Data Generation** | Random number, random list, random password, 6-digit OTP |
| 4 | **UUID Generation** | Unique identifiers (UUID4) for files, records, or sessions |
| 5 | **File Operations** *(custom module)* | Create, write, read, append text files |
| 6 | **Module Explorer** | Explore attributes of any built-in/custom module using `dir()` |
| 7 | **Unit Conversion** *(custom module)* | km↔miles, kg↔lbs, °C↔°F |

---

## 🚀 Getting Started

### Prerequisites
- Python 3.8 or higher installed ([download here](https://www.python.org/downloads/))

### Installation
```bash
git clone https://github.com/<your-username>/MultiUtilityToolkit.git
cd MultiUtilityToolkit
```

### Run the Toolkit
```bash
python main.py
```

### Run Individual Modules (standalone testing)
Thanks to the `__name__ == "__main__"` paradigm, every module can be tested independently:
```bash
python math_ops.py
python utility_pkg/file_ops.py
```

---

## 🖥️ Example Console Interaction

```
===========================
Welcome to Multi-Utility Toolkit
===========================
Choose an option:
1. Datetime and Time Operations
2. Mathematical Operations
3. Random Data Generation
4. Generate Unique Identifiers (UUID)
5. File Operations (Custom Module)
6. Explore Module Attributes (dir())
7. Unit Conversion (Custom Module)
8. Exit
===========================
Enter your choice: 2

Mathematical Operations:
1. Calculate Factorial
2. Solve Compound Interest
3. Trigonometric Calculations
4. Area of Geometric Shapes
5. Back to Main Menu
Enter your choice: 1

Enter a number: 5
Factorial: 120
```

---

## 🧠 Assumptions

- File operations store files inside a local `data_files/` folder (auto-created on first run).
- Numeric/date inputs are validated with `try/except`; invalid input returns to the menu instead of crashing.
- Trigonometric angles are entered in **degrees** and converted internally with `math.radians()`.
- `explorer.py` can explore **any** importable module (built-in or custom) using `importlib` + `dir()`.
- Stopwatch/countdown timer are console-blocking (expected for a CLI tool).

---

## 💼 Example Use Case

A small business owner uses the toolkit to:
- Calculate working hours using the time module.
- Generate random passwords for their team.
- Assign unique invoice IDs using the UUID module.
- Save logs/outputs into text files via the custom `file_ops` module.
- Convert units (e.g., km to miles) via the custom `math_custom` module.
- Explore any module's capabilities dynamically using `dir()`.

---

## 🏗️ Built With

- **Python 3** — core language
- **Built-in modules**: `datetime`, `time`, `math`, `random`, `uuid`, `string`, `importlib`, `os`
- **Custom package**: `utility_pkg` (`file_ops`, `math_custom`)

---

## 📌 Evaluation Highlights

- ✅ **Functionality** — all required built-in modules implemented with real-world use cases
- ✅ **Code Structure** — modular design, custom package with `__init__.py`, `__name__`/`__main__` paradigm
- ✅ **Documentation** — docstrings in every module + this README
- ✅ **Innovation** — added unit conversion module + generic `dir()`-based module explorer

---

## 📄 License

This project is open-sourced for educational purposes. Feel free to fork and build on it.

---

## 🙋 Author

Made as part of a Python "Moduler & Packager" assignment — *"Quality is our Motto."*
