## Installing NVIM
simply place the init.lua at the right directory
if it complains about the markdown plugin go to nvim-data folder find the modules /app folder and node install

## NVIM Commands

Replace the first foo with bar
```bash
:s/foo/bar
```
Replace all occuriences
```bash
:%s/foo/bar/g
```
Select in VISUAL mode to the next mathcing character
```bash
%[(/)/{/}/[/]]
```
```
vi[char] // inside select
va[char] // outside select
```
Opening new split window
```
<C-w>+s // to down
<C-w>+v // to right
<C-w>+q // quit window
:vsp [filename]
```
Fuzzy find in file
```
<leader>/
```
Search files
```
<leader>sf
```

## C dev

Adding a compile_commands.json with cmake
```bash
cmake -DCMAKE_EXPORT_COMPILE_COMMANDS=1
```
