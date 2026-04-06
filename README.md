# Understanding `__main__` in Python

## The Files We Used

**`greet.py`** — a module with a single function:
```python
def say_hello(name):
    print(f"Hello, {name}!")
```

**`main.py`** — the entry point:
```python
import greet

def main():
    print("main.py: Now I'm running under main()...")
    name = input("Enter your name (press Enter for default): ")
    greet.say_hello(name)

if __name__ == "__main__":
    print("main.py: This block runs only when main.py is executed directly.")
    main()
```

**`external.py`** — simulates another file importing `main.py`:
```python
import main
print("external.py: I'm running external.py, which imports main.py.")
main.main()
```

---

## How `__name__` Works

When Python runs a file, it sets a special variable `__name__`:

| How the file is used | `__name__` value |
|---|---|
| Run directly (`python main.py`) | `"__main__"` |
| Imported (`import main`) | `"main"` |

So `if __name__ == "__main__":` asks: *"Was this file run directly?"*

---

## What Happens Without the Guard

If `main.py` has a **loose** `main()` call instead of the guard:

```python
# ❌ No guard
main()  # runs immediately on import!
```

Running `external.py` produces:

```
main.py: Now I'm running under main()...   ← uninvited, triggered by import
Enter your name (press Enter for default):
Hello, World!
external.py: I'm running external.py, which imports main.py.
main.py: Now I'm running under main()...   ← called explicitly by external.py
Enter your name (press Enter for default):
Hello, World!
```

`main()` runs **twice** — once from `import main`, once from `main.main()`.

---

## What Happens With the Guard

```python
# ✅ With guard
if __name__ == "__main__":
    main()
```

Running `external.py` produces:

```
external.py: I'm running external.py, which imports main.py.
main.py: Now I'm running under main()...   ← called once, explicitly
Enter your name (press Enter for default):
Hello, World!
```

`main()` runs **once** — only when explicitly called by `external.py`.

---

## The Simple Rule

| File contains | Need guard? |
|---|---|
| Only functions/classes | ❌ No — nothing runs on import anyway |
| Loose code at the top level | ✅ Yes — protect it |
| Entry point (`main.py`) | ✅ Yes — always |

> **Best practice:** Put all logic inside functions. The `__main__` guard is then just the entry point — it decides when `main()` runs.

---

## Summary

```
python main.py      → __name__ == "__main__" → guard runs → main() called ✅
import main         → __name__ == "main"     → guard skipped → nothing runs ✅
```

The guard gives you a file that can be **both run directly and safely imported** — without any unwanted side effects.
