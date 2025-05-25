# 24154022_CDOC_INFOSEC



### 🟢 Task 1: **Bandit (OverTheWire)**

**🔹 Objective:**  
Solve beginner-level Linux wargame challenges from OverTheWire's [Bandit].

**🔹 Progress:**  
Completed **Levels 0 to X** (update this).

**🔹 Skills Demonstrated:**
- Navigating Linux filesystem and permissions.
- Reading hidden files, environment variables, and unusual input/output redirections.
- Using tools like `ssh`, `cat`, `find`, `base64`, `xxd`, and `grep`.

**🔹 Commands Practiced:**
```bash
cat <filename>
ls -la
find / -user bandit7 -group bandit6 -size 33c
strings <filename> | grep "password"
```

**🔹 What I Learned:**
- Practical use of the Linux command line for CTFs.
- Working with file permissions and shell redirections.
- Importance of attention to detail in security challenges.

---

### 🟣 Task 2: **Russian Roulette Game**  
**[`PIKArussian_roulette.py`]**

**🔹 Objective:**  
Simulate a terminal-based Russian Roulette game for multiple players.

**🔹 Key Features:**
- Each player sets their bullet chamber.
- Chamber spins randomly each round.
- A player dies if the bullet is in position.
- Game continues until one player survives.

**🔹 Technologies Used:**
- Python
- `numpy` for position tracking
- `random` for spin logic
- `time.sleep()` for suspenseful animations

**🔹 Sample Output:**
```bash
=== Round 1 ===
Spinning the chamber...
CLICK.. player 0 survives
BANG!!.. player 1 got killed
```

**🔹 What I Learned:**
- Building interactive CLI games in Python.
- Simulating randomness and round-based logic.
- Fun use of ASCII art and animation in terminals.

---

### 🔵 Task 3: **Multi-User To-Do List**  
**[`PIKA-TODO.py`]**

**🔹 Objective:**  
Create a command-line multi-user to-do list manager with login protection.

**🔹 Key Features:**
- Register/Login with password protection.
- Passwords hashed using SHA256.
- Each user has their own `username_todo.txt` file.
- Tasks: Add, View, Mark as Done, Delete.

**🔹 Bonus:**
- Encryption functions with `cryptography.Fernet` are prepared (currently commented out for simplicity).

**🔹 Technologies Used:**
- Python
- `hashlib` for password hashing
- `getpass` for hidden input
- `os` for file handling

**🔹 What I Learned:**
- Managing secure user data without storing plain-text passwords.
- File handling and persistence per user.
- Building a clean, interactive CLI menu for multiple roles.

---

### 🔴 Task 4: **PIKALang – A Simple Programming Language**  
**[`Pikalang.py`]**

**🔹 Objective:**  
Build a basic interpreter for a custom toy programming language.

**🔹 Language Features:**
- Variable declaration: `let x = 5`
- Print: `print x` or `print "Hello"`
- Conditionals: `if x > 2 then { print "ok" } else { print "not ok" }`
- Loops: `while x > 0 then { print x; let x = x - 1 }`

**🔹 Operators Supported:**
`==`, `!=`, `<`, `>`, `<=`, `>=`

**🔹 How it Works:**
- Input is read via prompt (`>>>`)
- Code is parsed and executed line by line.
- Condition checking and expression evaluation via `eval()`.
- Blocks handled using `{}` and `;`.

**🔹 What I Learned:**
- Basics of interpreter design and language parsing.
- Safe expression evaluation using scoped `eval()`.
- Handling control flow and variable environments.
- At first it might seem hard but once you figure out how the commands are gonna be for your language, all you have to do is to split the condition(if any) and the statement and then it's really easy.
- This same rule applies to all the commands i implemented and i wish i could have made it more which i will now for my own learning.
---

## ✅ Final Thoughts

This set of CSOC tasks helped me dive deep into:
- Security basics (OverTheWire)
- Python logic for games
- Building secure, user-friendly CLI apps
- Language design and interpreters

Feel free to check out the code for each task in the respective `.py` files in this repo. 🎉

---
