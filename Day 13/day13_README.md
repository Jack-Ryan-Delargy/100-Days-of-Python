# Day 13: Python Debugging Techniques

## Overview
Day 13 focuses on essential debugging techniques that every Python developer needs to master. This lesson covers systematic approaches to identifying, reproducing, and fixing bugs in your code. Debugging is not just about fixing errors—it's about developing problem-solving skills that improve with practice.

## Learning Objectives
By the end of this lesson, you will be able to:
- Fix syntax and runtime errors efficiently
- Reproduce bugs consistently for easier debugging
- Use print statements strategically to track program flow
- Implement try-except blocks for error handling
- Use IDE debuggers (like PyCharm) for advanced debugging
- Apply systematic debugging strategies to any code problem

---

## 10 Debugging Tips Covered

### 1. Fix Errors and Watch for Red Underlines
Always address errors highlighted by your editor before continuing. Modern IDEs provide immediate feedback through:
- Red underlines for syntax errors
- Hover tooltips explaining the issue
- Console error messages for runtime errors

**Example: Indentation Error**
```python
# ❌ Wrong - Missing indentation
def greet():
print("Hello")  # Error: expected an indented block

# ✅ Correct
def greet():
    print("Hello")
```

**Tip**: When encountering errors, copy the generic part of the error message (not your specific code) and search it on Google with "Python" added.

### 2. Use Try-Except Blocks
Handle errors gracefully to prevent program crashes and provide better user feedback.

**Example: Handling ValueError**
```python
# Without error handling - program crashes
age = int(input("How old are you? "))

# With try-except - program continues running
try:
    age = int(input("How old are you? "))
except ValueError:
    print("You have typed in an invalid number.")
    print("Please try again with a numerical response such as 15.")
    age = int(input("How old are you? "))
```

**Common Exception Types**:
- `ValueError`: Invalid value conversion (e.g., `int("twelve")`)
- `ZeroDivisionError`: Division by zero
- `IndexError`: List index out of range
- `KeyError`: Dictionary key doesn't exist
- `TypeError`: Operation on incompatible types

### 3. Reproduce the Bug
Intermittent bugs are the hardest to fix. The key is making the bug happen consistently so you can study it.

**Example: Random Bug with List Indexing**
```python
import random

dice_images = ["⚀", "⚁", "⚂", "⚃", "⚄", "⚅"]
dice_num = random.randint(1, 6)  # Bug: Sometimes causes IndexError
print(dice_images[dice_num])

# Problem: randint(1, 6) returns 1-6, but list indices are 0-5
# To reproduce: Set dice_num = 6 to trigger error every time

# ✅ Fixed version
dice_num = random.randint(0, 5)  # Now matches list indices 0-5
print(dice_images[dice_num])
```

**Key Insight**: Understanding how functions like `randint()` work helps identify the root cause. Unlike `range()`, `randint(a, b)` includes both endpoints.

### 4. Play Computer - Evaluate Each Line
Manually trace through your code like a computer would, checking what each variable equals at each step.

**Example: Generation Classifier Bug**
```python
year = int(input("What's your year of birth? "))

if year > 1980 and year < 1994:
    print("You are a millennial.")
elif year > 1994:
    print("You are a Gen Z.")

# Input: 1994 → No output! 
# Playing computer:
# - Is 1994 > 1980? Yes (True)
# - Is 1994 < 1994? No (False)
# - True AND False = False → First block skipped
# - Is 1994 > 1994? No (False) → Second block skipped
# Result: No output

# ✅ Fixed version
if year > 1980 and year <= 1994:  # Include 1994
    print("You are a millennial.")
elif year > 1994:
    print("You are a Gen Z.")
```

**Tip**: This technique is especially useful for logical errors where there are no error messages to guide you.

### 5. Squash Bugs with print() Statements
Print statements are your best friend for tracking variable values and program flow.

**Example: Word Counter Bug**
```python
words = 0
pages = int(input("Number of pages: "))
words_per_page == int(input("Number of words per page: "))  # Bug: == instead of =
total_words = pages * words_per_page
print(total_words)  # Always prints 0

# Adding debug print statements:
print(f"pages = {pages}")
print(f"words_per_page = {words_per_page}")  # Shows 0 instead of user input!

# The bug: == is comparison, not assignment
# ✅ Fixed version
words_per_page = int(input("Number of words per page: "))  # Single =
```

**Strategic Print Statement Placement**:
- At the start of functions (check inputs)
- Inside loops (track iterations)
- Before calculations (verify values)
- After assignments (confirm changes)

### 6. Use a Debugger (PyCharm, VS Code, etc.)
Modern IDE debuggers are like having print statements on steroids—you can inspect ALL variables at ANY point.

**Debugger Features**:

**Breakpoints**: Click in the gutter next to line numbers to pause execution
```python
def mutate(a_list):
    b_list = []
    new_item = 0
    for item in a_list:
        new_item = item * 2  # ← Set breakpoint here
        new_item += random.randint(1, 3)
        new_item = add(item, new_item)
        b_list.append(new_item)  # Bug: Wrong indentation
    return b_list
```

**Debugger Controls**:
- **Step Over**: Execute current line, move to next
- **Step Into**: Enter into function calls
- **Step Out**: Exit current function
- **Step Into My Code**: Skip library functions, only step into your code
- **Resume**: Continue until next breakpoint

**Variables Panel**: Watch all variables update in real-time as you step through code

**Example Debug Session**:
1. Set breakpoint inside loop
2. Run in debug mode (bug icon)
3. Observe that `b_list` stays empty until outside loop
4. Realize `append()` is incorrectly indented outside the loop
5. Fix indentation, confirm with another debug run

### 7. Take a Break
When stuck, step away. Your brain needs downtime to process problems.

**Why Breaks Work**:
- Fresh perspective when you return
- Subconscious problem-solving during rest
- Reduced frustration and tunnel vision

**Break Activities**:
- Get a cup of tea or coffee
- Take a short walk
- Sleep on it (seriously—overnight debugging is real!)
- Switch to a different task

### 8. Ask a Friend (or Rubber Duck)
Explaining your code to someone else often reveals the solution—even if they don't say anything!

**Rubber Duck Debugging**: Explain your code line-by-line to an inanimate object (like a rubber duck). The act of verbalizing forces you to think differently.

**Benefits of Peer Debugging**:
- Fresh eyes spot assumptions you've made
- Different approaches to the same problem
- Learning opportunity for both people
- Building community and support

**Where to Find Help**:
- Course Discord channel
- Study groups
- Stack Overflow (for unique problems)
- Programming communities

### 9. Run Your Code Often
Don't write 100 lines of code before testing—run it frequently!

**Best Practice**:
- Write a small function → Test it
- Add a feature → Test it
- Fix one bug → Test it
- Make any change → Test it

**Why This Matters**:
- Easier to locate new bugs (they're in recent changes)
- Prevents bug pile-up
- Faster development in the long run
- More confidence in your code

### 10. Use Stack Overflow Wisely
Stack Overflow is invaluable, but use it strategically.

**When to Search Stack Overflow**:
- You have a specific error message
- The problem seems common
- You've tried basic debugging first

**When to Ask a Question**:
- You've searched thoroughly with no results
- The issue is unique or unusual
- You've exhausted all other debugging methods
- You can provide a clear, minimal example

**Stack Overflow Etiquette**:
- Search before asking
- Provide a minimal reproducible example
- Show what you've tried
- Be respectful of others' time

---

## Key Debugging Principles

### Bugs Are Normal
Every programmer creates bugs—even experienced developers. The difference is they know how to debug efficiently.

> "I'm not a programmer of code, I'm a programmer of bugs." - Common developer feeling

Creating bugs means you're learning and pushing your boundaries. Embrace them as part of the journey!

### Debugging Makes You Stronger
Each bug you fix is like a rep at the gym—you're building your programming muscles.

**Leveling Up Your Skills**:
- Help others debug their code
- Practice on coding challenges
- Join programming communities
- Debug daily for consistent improvement

### Systematic Approach Wins
Don't debug randomly—follow a methodical process:

1. **Identify**: What is the bug? What should happen vs. what does happen?
2. **Reproduce**: Can you make it happen consistently?
3. **Isolate**: Where in the code is the problem?
4. **Fix**: Apply the appropriate solution
5. **Test**: Verify the bug is gone and nothing else broke
6. **Reflect**: What did you learn?

---

## Common Python Debugging Scenarios

### Scenario 1: The Silent Bug (Logical Error)
**Problem**: Code runs without errors but gives wrong results
**Solution**: Use print statements or debugger to trace variable values

### Scenario 2: The Intermittent Bug
**Problem**: Bug only happens sometimes
**Solution**: Reproduce consistently by identifying the conditions

### Scenario 3: The Indentation Bug
**Problem**: Python-specific issues with code blocks
**Solution**: Watch for editor warnings, use consistent spacing

### Scenario 4: The Off-by-One Error
**Problem**: List indices, ranges, or counters are off by one
**Solution**: Remember Python uses 0-based indexing

### Scenario 5: The Type Error
**Problem**: Wrong data type for an operation
**Solution**: Use type() function to check, convert as needed

---

## Practice Exercises

This lesson includes hands-on debugging challenges covering:
- Fixing indentation errors
- Handling user input validation
- Correcting list index errors
- Debugging logical conditions
- Using try-except blocks effectively
- Working with the IDE debugger

---

## Resources

### Documentation
- [Python Official Docs - Errors and Exceptions](https://docs.python.org/3/tutorial/errors.html)
- [Python Debugger (pdb) Documentation](https://docs.python.org/3/library/pdb.html)

### Learning Resources
- [Real Python - Python Debugging](https://realpython.com/python-debugging-pdb/)
- [Stack Overflow](https://stackoverflow.com/) - For searching common errors
- Course Discord - For peer support

### Tools Mentioned
- PyCharm Debugger
- Thonny Editor
- Python Tutor (pythontutor.com)

---

## Files in This Repository

- `bug_exercises.py` - Practice debugging challenges
- `solutions.py` - Fixed versions with explanations
- `debugging_examples.py` - Code examples from the lesson

---

## How to Run the Code

```bash
# Run the example files
python debugging_examples.py

# Run with PyCharm debugger
# 1. Open file in PyCharm
# 2. Click gutter to set breakpoints (red dots)
# 3. Click the debug icon (bug symbol)
# 4. Use Step Over/Into buttons to navigate

# Run with Python's built-in debugger (pdb)
python -m pdb your_script.py
```

---

## Summary: The 10 Debugging Tips

1. **Fix errors and watch for red underlines** - Address IDE warnings immediately
2. **Use try-except blocks** - Handle errors gracefully
3. **Reproduce the bug** - Make it happen consistently
4. **Play computer** - Trace through code manually
5. **Use print() statements** - Track variables and flow
6. **Use a debugger** - Leverage IDE debugging tools
7. **Take a break** - Step away when stuck
8. **Ask a friend** - Get fresh eyes on your code
9. **Run code often** - Test frequently, not at the end
10. **Use Stack Overflow wisely** - Search first, ask when unique

---

## Final Thoughts

Debugging is a skill that improves with practice. Every bug you encounter and fix makes you a better programmer. Don't get discouraged—even professional developers spend significant time debugging. The key is having a systematic approach and the right tools.

Remember: **Bugs are not a sign of failure, they're a sign of learning!**

Happy debugging! 🐛 → ✅

---

**Course**: Python Programming  
**Day**: 13  
**Topic**: Debugging Techniques  
**Level**: Intermediate
