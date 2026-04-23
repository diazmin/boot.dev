whoami: prints out the current user.
pwd: "print working directory".
cd ~ is the alias of /Users/diazmin (the home directory)
cd: "change directory".
ls: displays a list of the content inside a folder.

cat: 'concatenate'. To show content of a file (or multiple files).
head: to show the first lines of a file: head -n 10 file1.txt
tail: to show the last lines of a file: tail -n 10 file1.txt
less: opens an interactive mode: less -N 2023.csv to show line numbers.
    Press "enter" to scroll down line by line.  
    Press "q" to exit the program.
    Press spacebar to scroll down a page at a time. Go back up pressing "b".
touch: The touch command updates the access and modification timestamps of a file. By default, if the specified file does not exist, touch will create an empty file with the given filename.
grep: search for a string in a file: grep "hello" words.txt
    search for a strinf in multiple files: grep "hello" hello.txt hello2.txt
    search an entire directory: grep -r "hello" .
find: for finding files and directories by name, not by their contents: find some_directory -name hello.txt
    for searching for files that match a pattern. For example, if you wanted to find all files that end in .txt, you could run: find some_directory -name "*.txt"
    find all filenames that contain the word "chad": find some_directory -name "*chad*"

mkdir: "make directory" command. Creates a new folder.
mv: moves a file or directory from one location to another. You can use it to rename a file or to move it to a different directory altogether. Your working directory can't be the directory you're moving.
    renaming a file: mv some_file.txt some_other_name.txt
    moving a file from the current directory to another nested directory: mv some_file.txt some_directory/some_file.txt
    moving a file from the current directory, to the parent directory: mv some_file.txt ../some_file.txt

    if you don't want to rename the file and you're just moving it to a different directory, you can omit the filename:
    mv some_file.txt some_directory/
rm: "remove command" deletes a file or empty directory: rm some_file.txt
    to delete a directory and all of its contents recursively: rm -r some_directory
cp: it copies a file from one location to another: cp source_file.txt destination/
    copying a directory and all of its contents recursively: cp -R my_dir new_dir

### Running multiple commands
You can run multiple commands on a single line by separating them with a semicolon (;).

command1 ; command2

The second command runs immediately after the first command finishes. If you only want to run the second command if the first succeeds, then you can use &&:

command1 && command2