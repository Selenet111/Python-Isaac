# a = "Hello, WorLd!"
# print(len(a)) #number of characters

# count = 0

# for char in a.lower(): #make lowercase or .upper for uppercase
#     if char=="l":
#         count+=1


# print(f"There are {count} l\"s in this string. \nyay") #use f string to insert variables with curly brackets

# #\ for escape characters
# #  can insert quotes into the string
# # \n can split into 2 lines

# print("Hello" in a) #check if characters are in string: true or false - can also be "not in"

# y=a.index("d") #index() will tell you where the character is found
# print(y)

#___________________________________TASK 1________________________________

# listOfBadlyMixedNames = ["JohnSmith", "JaneDoe", "AliceJohnson", "BobBrown", "CharlieDavis"]
# listOfFixedNames = []
# upletters = 0

# for n in listOfBadlyMixedNames:
#     upletters = 0
#     for pos, m in enumerate(n):
#         if m.isupper() and pos!=0:
#             listOfFixedNames.append(n[0:pos] + " " + n[pos:])

# print(listOfFixedNames)

#______________________________________TASK 2_______________________________

highlighted_poems = "Afterimages:Audre Lorde:1997,  The Shadow:William Carlos Williams:1915, Ecstasy:Gabriela Mistral:1925,   Georgia Dusk:Jean Toomer:1923,   Parting Before Daybreak:An Qi:2014, The Untold Want:Walt Whitman:1871, Mr. Grumpledump's Song:Shel Silverstein:2004, Angel Sound Mexico City:Carmen Boullosa:2013, In Love:Kamala Suraiyya:1965, Dream Variations:Langston Hughes:1994, Dreamwood:Adrienne Rich:1987"
finalpoems = []

splitpoems = highlighted_poems.split(", ")

for poem in splitpoems:
    moresplit = poem.split(":")
    finalpoems.append(moresplit)

print(finalpoems)