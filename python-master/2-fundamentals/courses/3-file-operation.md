# Module 3: Directory & File Operation

## Session 1: Python Directory
- Python has the `os` module that provides us with many useful methods to work with directories (and files as well).
```python
import os
# Get current working directory with getcwd()
print(os.getcwd())
# List directories and files
print(os.listdir())
# Make new directory
os.mkdir('test')
# Rename directory or files
os.rename('test', 'files')
# Change directory
os.chdir('files')
print(os.getcwd())
# Remove empty directory only
os.rmdir('files')
```
- In order to remove a non-empty directory, we can use the `rmtree()` method inside the `shutil` module.

## Session 2: File Operation 
### 2.1 Opening & Closing Files in Python
- Python has a built-in `open()` function to open a file.This function returns a file object,
also called a `handle`, as it is used to read or modify the file accordingly.
- When we are done with performing operations on the file, we need to properly close the file.
`Closing a file` will `free up the resources` that were `tied with the file`.
It is done using the `close()` method available in Python.
- If an exception occurs when we are performing some operation with the file, the code exits without closing the file.
A safer way is to use a `try...finally...` block.
```python
try:
    # It is important to define the mode when opening a file
    # It is also highly recommended to specify encoding when working with files in text mode
    f = open('files/test.txt', mode='r', encoding='utf-8')
    print('Opened file:', f)
    # File operations
finally:
    f.close()
```
- The best way to close a file is by using the `with` statement.
This ensures that the file is closed when the block inside the `with` statement is exited.
We don't need to explicitly call the `close()` method. It is done internally.
```python
with open('files/test.txt', mode='r', encoding='utf-8') as file:
    print('Opened file:', file)
    # perform file operations
```
- Supported mode when opening a file in Python:

| Mode | Description |
| :---:| --- |
| `r` | Opens a file for reading. (default) |
| `w` | Opens a file for writing. Creates a new file if it does not exist or truncates the file if it exists. |
| `x` | Opens a file for exclusive creation. If the file already exists, the operation fails. |
| `a` | Opens a file for appending at the end of the file without truncating it. Creates a new file if it does not exist. |
| `t` | Opens in text mode. (default) |
| `b` | Opens in binary mode. |
| `+` | Opens a file for updating (reading and writing) |

### 2.2 Writing & Reading Files in Python
- In order to write into a file in Python, we need to open it in write `w`, append `a` or exclusive creation `x` mode.
```python
with open('files/test.txt', mode='w', encoding='utf-8') as f:
    f.write('This is my first file\n')
    f.write('This file\n\n')
    f.write('contains three lines\n')
```
- To read a file in Python, we must open the file in reading `r` mode.
```python
with open('files/test.txt', mode='r', encoding='utf-8') as f:
    # Output -> 'This'
    print(f.read(4))
    # Output -> ' is '
    print(f.read(4))
    # read in the rest till end of file
    # Output -> 'y first file\nThis file\ncontains three lines\n'
    print(f.read())
    # Further reading returns empty sting
    # Output -> ''
    print(f.read())  
```
- These are some common methods available to handle file object:

| Method | Description |
| :---: | --- |
| `close()` | Closes an opened file. It has no effect if the file is already closed. |
| `detach()` | Separates the underlying binary buffer from the `TextIOBase` and returns it. |
| `fileno()` | Returns an integer number (file descriptor) of the file. |
| `flush()` | Flushes the write buffer of the file stream. |
| `isatty()` | Returns `True` if the file stream is interactive. |
| `read(n)` | Reads at most `n` characters from the file. Reads till end of file if it is negative or `None`. |
| `readable()` | Returns `True` if the file stream can be read from. |
| `readline(n=-1)` | Reads and returns one line from the file. Reads in at most `n` bytes if specified. |
| `readlines(n=-1)` | Reads and returns a list of lines from the file. Reads in at most n bytes/characters if specified. |
| `seek(offset,from=SEEK_SET)` | Changes the file position to `offset` bytes, in reference to `from`(start, current, end). |
| `seekable()` | Returns `True` if the file stream supports random access. |
| `tell()` | Returns the current file location. |
| `truncate(size=None)` | Resizes the file stream to `size` bytes. If `size` is not specified, resizes to current location. |
| `writable()` | Returns `True` if the file stream can be written to. |
| `write(s)` | Writes the string `s` to the file and returns the number of characters written. |
| `writelines(lines)` | Writes a list of `lines` to the file. |