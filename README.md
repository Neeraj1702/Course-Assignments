Here’s the full **README.md** content in proper Markdown format. You can copy–paste it directly into your `README.md` file:

```markdown
# Python Basics – Two Small Programs

A beginner-friendly repository with two simple Python scripts:

1) **Basic Mathematical Operations** – takes two numbers and prints their sum, difference, product, and quotient.  
2) **Personalized Greeting** – asks for your first and last name and prints a friendly welcome message.

---

## 📁 Repository Structure

```

.
├── task1\_basic\_math.py
├── task2\_greeting.py
└── README.md

````

> Rename your files to the above (or adjust names here) so everything matches.

---

## 🧰 Requirements

- Python 3.8+ (any recent Python 3 version is fine)
- No external libraries needed

Check your Python version:
```bash
python --version
# or
python3 --version
````

---

## ▶️ How to Run

From the project folder, run each script in a terminal:

### 1) Basic Mathematical Operations

```bash
python task1_basic_math.py
# or
python3 task1_basic_math.py
```

**What it does:**

* Prompts for two integers
* Calculates: addition, subtraction, multiplication, division
* Prints all results

**Example run:**

```
Enter First Number : 12
Enter Second Number : 3

Addition :  15
Subtraction:  9
Multiplication:  36
Division : 4.0
```

> Note: Division outputs a decimal (float). If you enter `0` as the second number, Python will raise a `ZeroDivisionError`.

---

### 2) Personalized Greeting

```bash
python task2_greeting.py
# or
python3 task2_greeting.py
```

**What it does:**

* Prompts for first and last name
* Prints a greeting using both an f-string and the `.format()` method

**Example run:**

```
Enter your First Name: Ada
Enter your Last Name: Lovelace

Hello, Ada Lovelace!,Welcome to Python Program.

Hello, Ada Lovelace!,Welcome to Python Program.
```

---

## 📝 Program Details

### Task 1: Basic Math

* Inputs: two integers (`x`, `y`)
* Operations:

  * `add = x + y`
  * `sub = x - y`
  * `mul = x * y`
  * `div = x / y`  (floating-point division)
* Output: prints each result on a new line

### Task 2: Greeting

* Inputs: first name (`a`), last name (`b`)
* Output:

  * Greeting with an **f-string**
  * Greeting with **`.format()`**

---

## 💡 Notes & Possible Improvements

* Add input validation (e.g., handle non-number inputs for Task 1).
* Handle division by zero gracefully (e.g., warn the user instead of crashing).
* Trim extra spaces and capitalize names in Task 2 for cleaner output.

---

## 🤝 How to Use This Repo (GitHub Basics)

1. Click **“Fork”** or **“Use this template”** (optional) to copy it to your account.
2. Click **“Code” → “Download ZIP”** or clone:

   ```bash
   git clone https://github.com/<your-username>/<your-repo-name>.git
   ```
3. Add/commit your files:

   ```bash
   git add .
   git commit -m "Add basic math and greeting scripts"
   git push
   ```

---

## 📜 License

This project is for learning purposes. You can use and modify it freely.

```

Do you want me to also **add screenshots of sample runs** (terminal outputs) in the README so it looks even better on GitHub?
```
