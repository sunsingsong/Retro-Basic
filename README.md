# Retro-Basic
This project is a part of 2110316 Programming Languages Principles at Chulalongkorn University.

**Task :**
write a compiler to translate the source of Retro Basic to the "intermediate code".

**Grammar :**
```
pgm := line pgm | EOF
line := line_num stmt
stmt := asgmnt | if | print | goto | stop
asgmnt := id = exp
exp := term + term | term - term | term
term := id | const
if := IF cond line_num
cond := term < term | term = term
print := PRINT id
goto := GOTO line_num
stop := STOP
```

 *Full project description [here](https://www.cp.eng.chula.ac.th/~piak/teaching/prolang/2018/retro-basic.htm)* 
