inputText= "6/nbarco/ncasa/nbarco/nperro/nlote/nlote"

arrayInput = inputText.split(sep='/n') #split the wrods according to the parameter /n
arrayInput.pop(0) #delete the first element which  has the amount of words

repeatedWords=dict() # Create a dicttionary to save the words 
#{key => (words) , value=> (according to the amount of words found)} 

for word in arrayInput: #define the variable "word" to select each word in Array Input
    repeatedWords[word] = repeatedWords.get(word, 0) +1   #get the current value of the key, if this doesn't have value, set 0
print(len(repeatedWords))  #print Quantity of words
showList= " ".join(str(e) for e in repeatedWords.values()) #function lamba to get the values in text plain
print(showList) #Quantity found of each word

