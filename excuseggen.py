import random
leadIn = [
"I'm sorry but",
"Please forgive me",
"Beg you a thousand pardons",
"I apologize, however",
"I'm never usually like this but",
"You're never going to beleive this",
"Guess what happened?!?",
"Holy shit! Get this",
"Boy do I have a story for you,",
"So I was minding my own business and boom!",
"The most unbelievable thing just happened",
"I couldn't be more apologetic, but",
"Sorry I'm late,",
"I couldn't go becuase",
"I couldn't help it",
"This is a terrible excuse but",
"This going to sound crazy but",
"Holy Moses!",
"Blimey! Sorry I'm late guv'nha",
"I swear it wasn't my fault",
"I lost track of time because",
"I feel terrible, but",
"Don't blame me"
"Please,forgive me"
 "Sorry,but "
]

perpetrator = [
"your mom",
"Princess Peach",
"Godzilla",
"the offensive line of the '76 Dallas Cowboys",
"a handicapped gentleman",
"a triceratops named Penelope",
"the inventor of the slanket",
"the director of 101 Dalmatians",
"the little Asain kid from Indiana Jones",
"a man with 6 fingers on his right hand",
"my mom",
"Raiden from Mortal Kombat",
"Mayor McCheese",
"Scrooge McDuck",
"the ghost of Margaret Thatcher",
"the ghost of Hitler",
"Ghost Dad",
"the entire Roman Empire",
"Kevin Ware's leg bone",
"a British chap",
"a Hasidic Jew",
"Kevin Spacey",
"Kevin Costner's stunt double",
"Kevin McCallister's real life fake tarantuala",
"the Cthulhu"
]

delay = [
"gave me a hickey.",
"tried to kill me.",
"ran me over with a diesel backhoe.",
"died in front of me.",
"tried to seduce me.",
"beat me into submission.",
"hid my Trapper Keeper.",
"stole my bicycle",
"slept with my uncle.",
"called me \"too gay to fly a kite,\" whatever the means.",
"stole my identity.",
"broke into my house.",
"put me in a Chinese finger trap.",
"came after me.",
"came on me.",
"texted racial slurs from my phone.",
"spin-kicked me in the collar bone",
"tried to sell me vacuum cleaners.",
"crapped in my gas tank.",
"made me golf in shoes filled with macaroni and cheese.",
"pulled me over in a stolen cop car and demanded fellatio.",
"made me find Jesus.",
"kept telling me knock knock jokes."
]

data = [leadIn, perpetrator, delay]

#the excuse function, which combines an element of the 3 excuse
#lists randomly and returns it as a string.
def makeExcuse():
  excuse = ""
  for column in data:
    rand = random.randint(0,(len(column)-1))
    excuse = excuse + column[rand] + " "
  return excuse

