# 📝 Python CLI To-Do List Manager

A simple and functional Command-Line Interface (CLI) tool built using Python. This tool helps you manage your daily tasks directly from the terminal. You can add, view, update, and delete tasks using simple commands.

---

## 🚀 Features

- ✅ Add new tasks
- 📋 View all tasks
- ✏️ Update existing tasks
- ❌ Delete tasks
- 💾 Tasks are stored in a local JSON file (`tasks.json`)

---

## 📦 Requirements

- Python 3.x
- `argparse` (built-in with Python)
- Git (for version control if contributing)

---

## ⚙️ Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/YourUsername/python-cli-todo.git
   cd python-cli-todo

2. Run the script with Python:

   ```bash
   python todo.py
   ```

> ⚠️ If you're using macOS/Linux or Python 3 explicitly, use `python3` instead.

---

## 💻 How to Use

### ➕ Add a Task

```bash
python todo.py add "Finish Python CLI project"
```

### 📋 View All Tasks

```bash
python todo.py view
```

### ✏️ Update a Task

```bash
python todo.py update 1 "Submit final report"
```

### ❌ Delete a Task

```bash
python todo.py delete 1
```

---

## 📁 File Structure

```
python-cli-todo/
│
├── todo.py         # Main Python script
├── tasks.json      # (Auto-created) Stores tasks in JSON format
└── README.md       # Project documentation
```

---

## 🛠️ Built With

* Python 3
* argparse
* JSON (for task storage)

---

## 📌 License

This project is open-source and free to use under the [MIT License](LICENSE).

---

## 🤝 Contributing

Contributions, issues, and feature requests are welcome! Feel free to open an issue or submit a pull request.
