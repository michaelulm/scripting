# Code Snippets for Bash-Scripting

### get current year (full)
`date +%Y`

### loop through range
```bash
for i in 1 2 3 
do
  echo $i
done
```
***find other ways to loop through RANGE!***

### create directory-tree with one command
`mkdir -p root/child/sub`

### list filesystem-structure as tree
`tree /var/log`

> When `tree` is missing on your system:
> * CentOS/Fedora/RHL: `sudo yum install tree` 
> * Debian/Ubuntu: `sudo apt install tree`

### get first and third column with `cut`
`cut -d"," -f1,3 country.txt`

### `sort` numeric by second column
`sort -t"," -k2 country.txt`


