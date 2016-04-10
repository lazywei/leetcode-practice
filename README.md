LeetCode with Python
====================

This is my playground for practicing leetcode problems in Python.

## Usage

The `./get` executable is a handy Python script for downloading the LeetCode initial code for a specified problem.

Requirements for the `./get` script are
- Python 3
- [requests](https://github.com/kennethreitz/requests)
- [BeautifulSoup (bs4)](https://www.crummy.com/software/BeautifulSoup/)

Usage:

```shell
./get [problem_url]

# For example:
./get https://leetcode.com/problems/sum-root-to-leaf-numbers/
```

The downloaded script will be saved in the `./code/` directory, and the file will be properly named --- in the format [ProbNo-ProbName]. For example, `173-BinarySearchTreeIterator.py`.

