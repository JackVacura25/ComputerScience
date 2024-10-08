#kind of like a math formula 15 + 10 = 25 
print(15+10)      #algebra
print(5 > 10)     #boolean algebra

x = 5
print(5==5)

#the perfect test question what is the diff between = and ==

print(4 >+2)    #true
print(1993 == 1993)  #true
print(-90 < -99)  #false
print(10!=10)   #true

#boolean expressions quiz
answer_one = input("give me an interger that is negative\n>")
answer_one = int(answer_one)
print(answer_one < 0)

answer_two = input("write the number 5\n>")
print(answer_two == 5)

print("Walrus" + "Walrus")  #WalrusWalrus
print("Walrus" == "Walrus")  #true
#if statements evaluate bbolean expressions they make decisions about which code to run next 
#take a temp
#print "<temperature> is hot" if its >= 80
# otherwise print "<temp is not hot"
temp = input("Whats the temperature in F?\n>")
temp = int(temp)

# if <boolean expression> :
#this should remind of writing a function
#def <name>():
if temp >= 80:
    print(str(temp) + " is hot!")

if temp < 80:
    print(str(temp) + "is not hot!")

else:  #otherwise
    print(str(temp) + "is not hot!")

    #not all if statements need an else, infact no else statements need an else
    #else statements are an option 
    #but all else statements must have a corresponding if statement 
    #else statements cannot exist alone
    #an if statement can only have one elsepass = int(pass) 


real_pass = "skibidi68"
input_pass = input("Whats the password?\n>")

if input_pass == real_pass:
    print("ACCESS GRANTED")
else:
    print("ACCESS DENIED")

    