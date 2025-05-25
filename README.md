# 24154022_CDOC_INFOSEC



### 🟢 Task 1: **Bandit (OverTheWire)**

**🔹 Objective:**  
Solve beginner-level Linux wargame challenges from OverTheWire's [Bandit].

**🔹 Progress:**  
Sure! Here's a **concise writeup for Bandit levels 0 to 27**, perfect for a GitHub README file. Each level has a brief note on how it was solved.

---

## 🐧 OverTheWire: Bandit Writeup (Level 0–27)

### 🔐 Level 0 ➡ 1

* `The password for the next level is stored in a file called - located in the home directory.`

### 🔐 Level 1 ➡ 2

* `cat ./-` or `cat ' '`

### 🔐 Level 2 ➡ 3

* `cat .hidden` in `inhere/`

### 🔐 Level 3 ➡ 4

* `cat inhere/ & file ./-file0*`

### 🔐 Level 4 ➡ 5

* find ./inhere/ -type f -readable ! -executable -size 1033c

### 🔐 Level 5 ➡ 6

* find / -type f -size 33c -group bandit6 -user bandit7 2>&1 | grep -v "Permission denied"

### 🔐 Level 6 ➡ 7

* `find / -user bandit7 -group bandit6 -size 33c 2>/dev/null`

### 🔐 Level 7 ➡ 8

* `grep millionth data.txt`

### 🔐 Level 8 ➡ 9

* `sort data.txt | uniq -u`

### 🔐 Level 9 ➡ 10

* strings data.txt | grep "^=="

### 🔐 Level 10 ➡ 11

* cat data.txt | base64 -d

### 🔐 Level 11 ➡ 12

* Use ROT 13 cypher

### 🔐 Level 12 ➡ 13

* Reversed hex to binary, then decompressed multiple layers (gzip, bzip2, tar) to get the password.

### 🔐 Level 13 ➡ 14

* ssh -i sshkey.private bandit14@bandit.labs.overthewire.org -p 2220

### 🔐 Level 14 ➡ 15

* cat /etc/bandit_pass/bandit14 | nc localhost 30000
  
### 🔐 Level 15 ➡ 16

* cat /etc/bandit_pass/bandit15 | openssl s_client -connect localhost:30001 -quiet

### 🔐 Level 16 ➡ 17

* Check which ports are listening in the given range and wich respond to ssl connection

### 🔐 Level 17 ➡ 18

* Checked `diff passwords.old passwords.new` for the new password.

### 🔐 Level 18 ➡ 19

* ssh bandit18@bandit.labs.overthewire.org -p 2220 "cat readme"

### 🔐 Level 19 ➡ 20

* Used `setuid` binary to run as `bandit20` - "./bandit20-do cat /etc/bandit_pass/bandit20 ".

### 🔐 Level 20 ➡ 21

* Create two terminals and listen from one while send the password from the other and wait to get the next level password.

### 🔐 Level 21 ➡ 22

* * * * * * bandit22 /usr/bin/cronjob_bandit22.sh &> /dev/null.
          * cat /usr/bin/cronjob_bandit22.sh
          * you can see where the password is being stored just use cat for it.

### 🔐 Level 22 ➡ 23

* echo "I am user bandit23" | md5sum.
* cat /tmp/8ca319486bfbbc3663ea0fbe81326349.

### 🔐 Level 23 ➡ 24

* The cron script execute and delete all scripts in /var/spool/bandit24.
* We just need to write our own script, copy it in /var/spool/ bandit24 and wait for the result.

### 🔐 Level 24 ➡ 25

* Wrote script to get response from a daemon running on port 30002 with correct header.
  
**I wasn't able to go further but i will complete all of them soon or already done by the time you are reading as they are really exciting and not that hard i think.


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
