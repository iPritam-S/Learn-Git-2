# Learn Git

Git-Cheat-Sheet: https://drive.google.com/file/d/1Gn-cRyhKE9WyrUL0DN0fgc5EsaHHeNXm/view?usp=drive_link

- First commit by Pritam

- So till now we have used:
	- git init
	- git branch -M main
		- M does renaming/new branch name
	- git add remote origin <url>
	- git log 
		- gives you all the logs till now 
		- commit history, ids, etc
		- git log --oneline --graph (linear history only details in one line)
		- git log --oneline (counts commits)

---


# Git Practice Notes (Quick Revision)

---

## Core Mental Model

Git has **3 layers**:

1. **HEAD (commits)**
2. **Staging Area (index)**
3. **Working Directory (files)**

---

## Basic Flow

```bash
git init
git add .
git commit -m "message"
git remote add origin <url>
git push -u origin main
```

---

## Branching

```bash
git checkout -b feature-1   # create + switch
git branch                  # list branches
git branch -d branch_name   # delete (safe)
git branch -D branch_name   # force delete
```

One branch = one feature / one PR

---

## Tracking & Push

```bash
git push -u origin main
```

* `-u` → sets upstream (tracking)
* After this: `git push` works directly

---

## Reset (Very Important)

| Command   | Effect           |
| --------- | ---------------- |
| `--soft`  | move HEAD only   |
| `--mixed` | reset staging    |
| `--hard`  | reset everything |

```bash
git reset --soft HEAD~1
git reset HEAD~1
git reset --hard HEAD~1
```

---

## Restore

```bash
git restore file.txt              # restore working dir
git restore --staged file.txt     # unstage
```

---

## Stash

```bash
git stash          # stash tracked
git stash -u       # include untracked
git stash list
git stash apply
git stash pop
git stash clear
```

stash = temporary storage (not commit)

---

## Remotes

```bash
git remote -v
```

* `origin` → your fork
* `upstream` → original repo

---

## Fork Workflow

### Setup

```bash
git clone <fork-url>
git remote add upstream <original-url>
```

---

### Contribution Flow

```bash
git checkout -b feature-1
# make changes
git add .
git commit -m "msg"
git push origin feature-1
```

Then create PR on GitHub

---

### PR Updates

```bash
# same branch
git add .
git commit -m "update"
git push origin feature-1
```

PR updates automatically

---

## After PR Merge

### Sync Fork

```bash
git pull upstream main
git push origin main
```

---

### Sync Original Local Repo

```bash
git pull origin main
```

---

## Delete Branch

```bash
git push origin --delete branch_name   # remote
git branch -d branch_name              # local
```

---

## Key Concepts

* `origin` = your fork
* `upstream` = main repo
* PR = request to merge your branch
* `git pull` = fetch + merge
* `git push` = sync local → remote

---

## Important Rules

* Never work directly on `main`
* Always create new branch for new feature
* Same PR → same branch
* Sync fork regularly
* Prefer `restore` over `reset --hard`

---

## Common Mistakes

Using `git pull` instead of `git pull upstream main`
Creating new PR for same changes
Using `reset --hard` without understanding
Not syncing fork before new work

---

## Final Mental Model

```text
upstream (original repo)
        ↑
     pull
        ↑
local repo
        ↓
     push
        ↓
origin (your fork)
```

---

## One Line Summary

Git = managing history + syncing between local and remote safely

