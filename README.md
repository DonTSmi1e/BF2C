# Brainfuck to C
**well, uh, yes.**

## Usage as main script
```bash
# -------------------------------------------------------------------------- #
#   You need Tiny C Compiler to use this script (https://bellard.org/tcc/)   #
# -------------------------------------------------------------------------- #
# Works in Windows, Linux, <add something else after testing>.

# Usage: (program.b - brainfuck source file)
python bfc.py program.b

# Usage: (program.b - brainfuck source file) [with memory dump]
python bfc.py program.b -d
```

## Usage as module
```python
import bfc

bf_code = "+>+>->-><<<<"
c_code = bfc(bf_code)

print(c_code)
```
