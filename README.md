# Simple notebook to organize life

This is a simple python3 notebook app that organizes small notes into text 
files and helps in retrieving them. It aims to be editor driven so all the 
sweet vim magic is possible when editing text.



## Notes
`note`
opens text body in editor

`note "text text"`
creates simple note with text string



## TODOS

`todo`
opens text body in editor

`todo "text text"`
creates simple todo with text string


And then seeing the current list:
`todos`
opens list of todos in editor



## Installation

define environment variable `$NOTEBOOKDIR` to point to directory where 
notes are to be save.


In addition, it is good idea to add aliases to your `.bash_profile` for 
`todo` and `todos` as:
```
export NOTEBOOKDIR=/Users/natj/projects/notebook
alias todo='/Users/natj/projects/notebook/todo.sh'
alias todos='/Users/natj/projects/notebook/todos.sh'

```
