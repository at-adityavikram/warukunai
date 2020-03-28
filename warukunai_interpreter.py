import random
legalchars="1234567890abcdefx"
shcoms=["help","where","info","examples"]#everything other than 'where' is not yet implemented...
bits=["0x0"]
#hex(int(bits[0],0)+value)
cur_pos=0
def findBrackets(ipstr):
   if '[' in ipstr:
      match = ipstr.split('[',1)[1]
      open = 1
      for index in range(len(match)):
         if match[index] in '[]':
            open = (open + 1) if match[index] == '[' else (open - 1)
         if not open:
            return match[:index]
def pntRaw(prstr):
    hst=""
    for i in range(0,len(prstr)):
        hst+= prstr[i].replace("0x","")
    return hst
while True:
    num_br=0
    oprog=""
    prog_tape=""
    #prog_tape = str(__import__('sys').argv[1]).strip()
    if prog_tape == "":
        prog_tape = input("$ ")
        if "||" in prog_tape:
            num_br=prog_tape.count("||")
            prog_tape = prog_tape.replace("||","$>$")            
        oprog=prog_tape
    i=0
    if prog_tape.split(" ")[0] not in shcoms:
        while i < len(prog_tape):
            if prog_tape[i] == "?":
               for k in range(i,len(prog_tape)):
                   if prog_tape[k] == "[":
                       break
               chbit = prog_tape[i+1:k]
               if chbit[0] == "(":
                   chbit = bits[int(chbit[1:len(chbit)-1])]                   
                   inner=findBrackets(prog_tape[i:])
                   outer=prog_tape[i+5+len(chbit)+len(inner):]
               else:
                   inner=findBrackets(prog_tape[i:])
                   outer=prog_tape[i+3+len(chbit)+len(inner):]
               #print(chbit,inner,outer)
               if chbit == bits[cur_pos]:
                   prog_tape,i = inner,-1
                   #print(inner)
               else:
                   #print(outer)
                   prog_tape,i = outer,-1
            elif prog_tape[i] == "!":
               for k in range(i,len(prog_tape)):
                   if prog_tape[k] == "[":
                       break
               chbit = prog_tape[i+1:k]
               if chbit[0] == "(":
                   chbit = bits[int(chbit[1:len(chbit)-1])]                   
                   inner=findBrackets(prog_tape[i:])
                   outer=prog_tape[i+5+len(chbit)+len(inner):]
               else:
                   inner=findBrackets(prog_tape[i:])
                   outer=prog_tape[i+3+len(chbit)+len(inner):]
               inner=findBrackets(prog_tape[i:])
               outer=prog_tape[i+3+len(chbit)+len(inner):]
               #print(chbit,inner,outer)
               if chbit != bits[cur_pos]:
                   prog_tape,i = inner,-1
                   #print(inner)
               else:
                   #print(outer)
                   prog_tape,i = outer,-1
            elif prog_tape[i] == ">":
               cur_pos+=1
               if cur_pos == len(bits):
                   bits.append("0x0")
               if prog_tape.strip() == ">":
                   print(bits)
                   tlen=2
                   for i in range(0,cur_pos):
                       tlen+= len(bits[i])+4
                   print(tlen * " " ,len(bits[cur_pos])*"˭",sep="")
            elif prog_tape[i] == "<":
               if cur_pos != 0:
                   cur_pos -=1
               if prog_tape.strip() == "<":
                   print(bits)
                   tlen=2
                   for i in range(0,cur_pos):
                       tlen+= len(bits[i])+4
                   print(tlen * " " ,len(bits[cur_pos])*"˭",sep="")
            elif prog_tape[i] == "#":
               bits[cur_pos] = "0x" + str(random.choice("0 1 2 3 4 5 6 7 8 9 a b c d e f".split(" ")))
            elif prog_tape[i] == "=":
                print(bits)
                tlen=2
                for i in range(0,cur_pos):
                    tlen+= len(bits[i])+4
                print(tlen * " " ,len(bits[cur_pos])*"˭",sep="")
            elif prog_tape[i] == "+":
                bits[cur_pos] = str(hex(int(bits[cur_pos],0)+1))
            elif prog_tape[i] == "-":
                bits[cur_pos] = str(hex(int(bits[cur_pos],0)-1))
            elif prog_tape[i] == "$":
                for h in range(i+1,len(prog_tape)):
                    if prog_tape[h] == "$":
                        break
                k = 0
                chbit = prog_tape[i+1:h]
                if "0x" not in chbit:
                    chbit = "0x" + chbit
                for m in chbit:
                    if m not in legalchars:
                        k=1
                        break
                if k == 0:
                    bits[cur_pos] = chbit               
                i+= h-i
            elif prog_tape[i] == "(":
               for l in range(i,len(prog_tape)):
                   if prog_tape[l] == ")":
                       break
               if str(prog_tape[i+1:l]) == "~":
                   cur_pos = len(bits)-1              
               else:
                   if "-" not in str(prog_tape[i+1:l]) and "+" not in str(prog_tape[i+1:l]):
                       psn = int(str(prog_tape[i+1:l]),0)
                       if psn + 1 <= len(bits):                       
                           cur_pos=psn
                           #print(bits[cur_pos])
                       else:
                           print("err - out of range")
                           break
                   elif "-" in str(prog_tape[i+1:l]):
                       psn = int(str(prog_tape[i+2:l]))
                       if cur_pos != 0:
                           cur_pos-=psn
                       else:
                           cur_pos=len(bits)-1
                   elif "+" in str(prog_tape[i+1:l]):
                       psn = int(str(prog_tape[i+2:l]))
                       if cur_pos < len(bits)-1:
                           cur_pos+=psn
                       else:
                           cur_pos=0
            elif prog_tape[i] == "{":
                l=0
                for l in range(i,len(prog_tape)):
                   if prog_tape[l] == "}":
                       break
                if l != 0:
                    gto=str(prog_tape[i+1:l])
                    if gto == ".":
                        prog_tape=oprog
                        i = -1
                    elif gto == "~":
                        break
                    elif val(gto) < len(prog_tape):
                        i = int(gto) + 2*num_br -1
            elif prog_tape[i] == "*":
                crbts = bits[0:cur_pos+1]
                bits = crbts[::-1] + bits[cur_pos+1:]
                cur_pos=0
            elif prog_tape[i] == ".":
                if cur_pos < len(bits) - 1:
                    bits[cur_pos],bits[cur_pos+1] = bits[cur_pos+1],bits[cur_pos]
                    cur_pos+=1
                else:
                    bits.append("0x0")
                    bits[cur_pos],bits[cur_pos+1] = bits[cur_pos+1],bits[cur_pos]
                    cur_pos+=1
            elif prog_tape[i] == "@":
               try:
                   print(bytes.fromhex(pntRaw(bits)).decode('utf-8'))
               except:
                   print("err - hex code did not produce a string")
            elif prog_tape[i] == "r":
               if i < len(prog_tape)-1:
                   print(pntRaw(bits))
            elif prog_tape[i] == ";":
                bits=["0x0"]
                cur_pos=0
                lstlen=[3]
                if prog_tape == ";":
                    print("reset all")
                prog_tape=""
    else:
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
            
            i+=1
