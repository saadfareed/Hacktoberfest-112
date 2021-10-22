#Add Yor Name And sename on the top of your program

#Name: Saad fareed
#Username:saadfareed

#program to find the position of senetence in the corpra 
def position(inde):
    flag=False
    sentence= "my name is Saad fareed. I am student of Computer Science.Need help bro. I am from Session 18 and Section A."
    sentence=sentence.split(".") #As english sentence end up with "." 
    #print(sentence)
    for i in sentence: #sentence is basically corpra and i is the sentence don't confuse 
        #print(i)
        if(inde==i):
            flag=True
            print(sentence.index(inde))
    return flag
print(position(" I am from Session 18 and Section A"))
