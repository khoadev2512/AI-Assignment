## WORDS SEARCH GAME (BOGGLE)
Using python 3 to solve boggle problem <br /> <br />




### Table of contents :
```
Name            | Content
----------------|----------------------------------
Log             | Contain log step by step txt files
dfs.py          | Implement deep first search way
heuristics.py   | Implement heuristics (Hill climping) way 
dictionary.txt  | Dictionary use for check words
---------------------------------------------------
```

## SET UP

### Tạo mysql database:

Open terminal and run commands below

```bash
pip install psutil
```

This package will be used to calculator memory used when running code

### OS:

If you use Unix OS like macOS or Ubuntu, please change this code in heuristics.py line 151<br>

```bash
with open(fileName, 'w+') as textFile:
```

If you use window OS

```bash
with open(fileName, 'w+', encoding='utf-8') as textFile:
```

### Calculate time and resource memory for Unix OS

If you use Unix OS like macOS or Ubuntu, please change this part of code bellow import library :

```bash
import resource 

time_start = time.clock()
```

And in last line of code:
```bash
time_elapsed = (time.clock() - time_start)
memMb=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss/1024.0
print ("%5.1f secs %5.1f KByte" % (time_elapsed,memMb))
```


## Run project

<br>

python | File name | Size | Log
| :--- | ---: | :---: | :---:
python  | dfs.py | Interger | 1 or 0
python  | heuristics.py | Interger | 1 or 0

To run project, run bellow command:

dfs.py
```bash
python dfs.py 3 0 
```

heuristics.py
```bash
python heuristics.py 3 0
```

#### You can change size and log to run the program on your request

