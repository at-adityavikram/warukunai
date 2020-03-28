# warukunai
a virtual-tape based esoteric 'programming language', in hex base.<br>
run this interpreter directly in cmd.

## main commands
<p>
> move pointer right. will add a cell with value '0x0' if at end.<br>
< move pointer left<br>
$0xn$ or $n$ sets current cell to '0xn' where n is a hex number of *any length*<br>
$(0)$ copy the value of cell at position 0 and assign it to current cell.
+ adds 1 to currrent cell (if current cell is f, + makes current cell 0)<br>
- subtracts 1 from current cell (if current cell is 0, + makes current cell f)<br>
r print raw bits<br>
!_[_]_ if not condition (!0x0[>$0x0$=]>0x$1$= is equivalent to 'if current cell is not 0x0 then >$0x0$= else >$0x1$=)<br>
?_[_]_ if condition (?0x0[>$0x0$=]>$0x1$= is equivalent to 'if current cell is 0x0 then >$0x0$= else >$0x1$=)<br>
# randomly assign a value to this cell<br>
(x) goto cell at location x (starts from 0, (not in hex!) if '-' in front of x, then go back x positions. if '+' in front of x, go forward x positions. wraps around if reaches end or start.)<br>
(~) goto last cell<br>
{.} goto beginning *of code*<br>
{~} goto end of code (basically break)<br>
{n} goto position n in code (n is not a hex number!)<br>
* reverse all cells behind pointer (including current cell)<br>
@ try to print output as string<br>
i print output as integer<br>
; reset<br>
= prints output in the [_.,.,.,._] format<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;=
</p>

## examples
<br>
example 1 - conditions
<br>
#?0x0[>$0x1$=]?0x1[>$0x0$=]$0x0$=
if # gets value 1, will print ['0x1','0x0'] else if # gets value 0x0, will print 01 ['0x0','0x1']
else prints 0

<br>
example 2 - value assignment
<br>
$0xabc$ or $abc$ will assign 0xabc to current cell
$0xf0$>$0x0$ will assign 0xf0 to current cell, move ahead one cell and assign 0x0 to that cell
$a||0xc||0xff$ does the same thing as $0xa$>$0xc$>$0xff$

note that to actually view the assigned changes, an '=' is required. in case you forgot to put it, and pressed enter, no worries. the bits are retained forever unless reset by ';'

example 3 - strings
$68||65||6c||6c||6f||20||77||6f||72||6c||64||21$@
prints hello world!

while

$68||65||6c||6c||6f||20||77||6f||72||6c||64||21$i
prints 32309054545037006034346730529

example 4 - looping
!0xf[+r{.}]
will print digits 1-f sequentially
while 

!0x5[+>-<={.}]
will have a much more *exotic* output

<h2>limitations</h2>
    - dont count them there are lots<br>
    - 'where' *might* not work due to a recent code port
<h2>fixes</h2>
    - fixed the buggy tag nesting. now ? and ! constructs should nest just fine.<br>
    - fixed bug in variable assignment where multi digit hex were not assigned at all.<br>
    - fixed big in looping and code + tape navigation<br>
<br><h2>v0.2</h2>
