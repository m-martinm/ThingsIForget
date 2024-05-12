# NVIM Commands

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
