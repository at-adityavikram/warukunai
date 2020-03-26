import random
legal_commands="><10=?[]!@/#*"
shcoms=["help","where","info","examples"]
bits="0"
cur_pos=0
all_help='''
HELP
==============================================
> move pointer right
< move pointer left
n set this cell to n (where n is any hex digit 0 to f)
+ adds 1 to currrent cell (if current cell is f, + makes current cell 0)
- subtracts 1 from current cell (if current cell is 0, + makes current cell f)
r print raw bits
!_[_]_ if not condition (?0[>0=]>1= is equivalent to 'if current cell is not 0 then >0= else >1=)
?_[_]_ if condition (?0[>0=]>1= is equivalent to 'if current cell is 0 then >0= else >1=)
# randomly assign a value to this cell
(x) goto cell at location x (starts from 0, in hex. if '-' in front of x, then go back x positions. 
    if '+' in front of x, go forward x positions. wraps around if reaches end or start.)
(~) goto last cell e.g. f(0)a>b>0(2)c(~)d= prints abcd
(.n) goto beginning *of code*
* reverse all cells
@ try to print output as string
i print output as integer
. swaps current cell with next cell (wraps around if current cell is last cell)
; resets tape to [0] and empties redundant program
= prints output in the [_..._] format
                         ^
base commands
==============================================
help prints help
about prints about
where x finds all occurences of x in tape
==============================================
'''
all_info='''
warutape - a tape *based* hexadecimal *base* language
[_____________......_______________]
 ^
"^" is the 'pointer', [_____________] is the 'tape'
'''
all_examples='''
==============================================
example 1 

#?0[>1=]?1[>0=]0=
if # gets value 1, will print 10 else if # gets value 0, will print 01
else prints 0
================================================

example 2
f?0[>1=]?1[>0=]!f[1>1>1=]>0>0*= 
should print 00f

while

o>o>f=
should print oof
=================================================

example 3
6>8>6>5>6>c>6>c>6>f>2>0>7>7>6>f>7>2>6>c>6>4>2>1@
prints hello world!

while

6>8>6>5>6>c>6>c>6>f>2>0>7>7>6>f>7>2>6>c>6>4>2>1i
prints 32309054545037006034346730529
=================================================
example 4: looping
!f[+^(.)]
will print digits 1-f sequentially
while 

!5[+>-<=(.)]
will print
[1f]
 ^
[2e]
 ^
[3d]
 ^
[4c]
 ^
[5b]
 ^
=================================================
'''
def findBrackets(ipstr):
   if '[' in ipstr:
      match = ipstr.split('[',1)[1]
      open = 1
      for index in range(len(match)):
         if match[index] in '[]':
            open = (open + 1) if match[index] == '[' else (open - 1)
         if not open:
            return match[:index]
while True:
    oprog=""
    prog_tape=""
    #prog_tape = str(__import__('sys').argv[1]).strip()
    if prog_tape == "":
        prog_tape = input(">> ")
    oprog=prog_tape
    i=0
    looptimes = []
    mcode = []
    if prog_tape.split(" ")[0] not in shcoms:
       while i < len(prog_tape):
           if prog_tape[i] == "!":
               chbit = prog_tape[i + 1]
               inner=findBrackets(prog_tape)
               outer=prog_tape[1+len(inner)+3:]
               if chbit != bits[cur_pos]:
                   prog_tape,i = inner,-1
               else:
                   prog_tape,i = outer,-1
           elif prog_tape[i] == "?":
               chbit = prog_tape[i + 1]
               inner=findBrackets(prog_tape)
               outer=prog_tape[1+len(inner)+3:]
               if chbit == bits[cur_pos]:
                   prog_tape,i = inner,-1
               else:
                   prog_tape,i = outer,-1
           elif prog_tape[i] == ">":
               cur_pos+=1
               if cur_pos == len(bits):
                   bits += "0"
               if prog_tape.strip() == ">":
                   print("[",bits,"]",sep="")
                   print((cur_pos) * " " ," ^",sep="")
           elif prog_tape[i] == "<":
               if cur_pos != 0:
                   cur_pos -=1
               if prog_tape.strip() == "<":
                   print("[",bits,"]",sep="")
                   print((cur_pos) * " " ," ^",sep="")
           elif prog_tape[i] == "#":
               bits = bits[0:cur_pos] + random.choice("0 1 2 3 4 5 6 7 8 9 a b c d e f".split(" ")) + bits[cur_pos+1:len(bits)]
           elif prog_tape[i] == "r":
               print(bits)
           elif prog_tape[i] == "*":
               bits = bits[::-1]
           elif prog_tape[i] == "@":
               try:
                   print(bytes.fromhex(bits).decode('utf-8'))
               except:
                   print("err - invalid hex number")
           elif prog_tape[i] == "i":
               print(int("0x"+bits,0))
           elif prog_tape[i] == "(":
               for l in range(i,len(prog_tape)):
                   if prog_tape[l] == ")":
                       break
               if str(prog_tape[i+1:l]) == "~":
                   cur_pos = len(prog_tape)
               elif str(prog_tape[i+1:l]) == ".":
                   prog_tape = oprog
                   i = -1              
               else:
                   if "-" not in str(prog_tape[i+1:l]) and "+" not in str(prog_tape[i+1:l]):
                       psn = int("0x"+ str(prog_tape[i+1:l]),0)
                       if psn + 1 <= len(bits):                       
                           cur_pos=psn
                           #print(bits[cur_pos])
                       else:
                           print("err - out of range")
                           break
                   elif "-" in str(prog_tape[i+1:l]):
                       psn = int("0x"+ str(prog_tape[i+2:l]),0)
                       if cur_pos != 0:
                           cur_pos-=psn
                       else:
                           cur_pos=len(bits)-1
                   elif "+" in str(prog_tape[i+1:l]):
                       psn = int("0x"+ str(prog_tape[i+2:l]),0)
                       if cur_pos < len(bits)-1:
                           cur_pos+=psn
                       else:
                           cur_pos=0
               i+=len(prog_tape[i:l])-1
           elif prog_tape[i] == "+":
               if bits[cur_pos] == "f":
                   bits = bits[0:cur_pos] + "0" + bits[cur_pos+1:len(bits)]
               else:
                   bits = bits[0:cur_pos] + str("0123456789abcdef"[int("0x"+bits[cur_pos],0) + 1]) + bits[cur_pos+1:len(bits)]
           elif prog_tape[i] == "-":
               bits = bits[0:cur_pos] + str("0123456789abcdef"[int("0x"+bits[cur_pos],0) - 1]) + bits[cur_pos+1:len(bits)]
           elif prog_tape[i] in "0123456789abcdef":
               for z in "0123456789abcdef":
                   if z == prog_tape[i]:
                       bits = bits[0:cur_pos] + z + bits[cur_pos+1:len(bits)]
           elif prog_tape[i] == ";":
               bits="0"
               cur_pos=0
               if prog_tape == ";":
                   print("cleared all")
           elif prog_tape[i] == ".":
               if cur_pos < len(bits) - 1:
                   bits = bits[0:cur_pos] + bits[cur_pos+1] + bits[cur_pos] +bits[cur_pos+2:]
                   cur_pos += 1
               else:
                   bits = bits[cur_pos] + bits[1:len(bits)-1] + bits[0]
                   cur_pos = 0
           elif prog_tape[i] == "=":
               print("[",bits,"]",sep="")
               print((cur_pos) * " " ," ^",sep="")
           elif prog_tape[i] == "*":
               bits = bits[::-1]
           i+=1
    else:
       if prog_tape.split(" ")[0] == shcoms[0]:
          print(all_help)
       elif prog_tape.split(" ")[0] == shcoms[1]:
          cout=[]
          if len(prog_tape.split(" ")) != 1:
             for b in range(0,len(bits)):
                if bits[b] == prog_tape.split(" ")[1]:
                   cout.append(b)
             if len(cout) > 0:
                print("found given value at location(s) ",cout)
             else:
                print("not found")
       elif prog_tape.split(" ")[0] == shcoms[2]:
          print(all_info)
       elif prog_tape.split(" ")[0] == shcoms[3]:
          print(all_examples)
       

