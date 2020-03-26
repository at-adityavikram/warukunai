# warukunai
a virtual-tape based esoteric 'programming language'<br>
run this program directly in cmd.
to get help, type help and press enter.
## main commands
<p>
> move pointer right<br>
< move pointer left<br>
n set this cell to n (where n is any hex digit 0 to f)<br>
+ adds 1 to currrent cell (if current cell is f, + makes current cell 0)<br>
- subtracts 1 from current cell (if current cell is 0, + makes current cell f)<br>
r print raw bits<br>
!_[_]_ if not condition (?0[>0=]>1= is equivalent to 'if current cell is not 0 then >0= else >1=)<br>
?_[_]_ if condition (?0[>0=]>1= is equivalent to 'if current cell is 0 then >0= else >1=)<br>
# randomly assign a value to this cell<br>
(x) goto cell at location x (starts from 0, in hex. if '-' in front of x, then go back x positions. <br>
    if '+' in front of x, go forward x positions. wraps around if reaches end or start.)<br>
(~) goto last cell e.g. f(0)a>b>0(2)c(~)d= prints abcd<br>
(.n) goto beginning *of code*<br>
* reverse all cells<br>
@ try to print output as string<br>
i print output as integer<br>
. swaps current cell with next cell (wraps around if current cell is last cell)<br>
; resets tape to [0] and empties redundant program<br>
= prints output in the [_..._] format<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;^<br>
</p>

## examples
<br>
example 1 
<br>
#?0[>1=]?1[>0=]0=
if # gets value 1, will print 10 else if # gets value 0, will print 01
else prints 0

<br>
example 2
<br>
f?0[>1=]?1[>0=]!f[1>1>1=]>0>0*= 
should print 00f

while
<br>
0>0>f=
should also print 00f

<br>
example 3
6>8>6>5>6>c>6>c>6>f>2>0>7>7>6>f>7>2>6>c>6>4>2>1@
prints hello world!
<br>
while
<br>
6>8>6>5>6>c>6>c>6>f>2>0>7>7>6>f>7>2>6>c>6>4>2>1i
prints 32309054545037006034346730529
<br>
example 4: looping
<br>
!f[+^(.)]
will print digits 1-f sequentially
<br>
___________________________<br><br>
## limitations
- as of now nesting of constructs is buggy
v0.1
