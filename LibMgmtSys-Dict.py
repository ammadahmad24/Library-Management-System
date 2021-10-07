lines = []
with open('E:/OneDrive/VSCode/Python/Library Management System/books.data') as f:
    lines = f.read()

lines = lines.split('\n\n')
nisbn = []
booklib = []

for bookinfo in lines:
    start = bookinfo.find('isbn')+7
    end = bookinfo.find('"\n',start)
    nisbn.append(bookinfo[start:end])
    
    start = bookinfo.find('"title')
    booklib.append(bookinfo[start:])  

booklibdict = dict(zip(nisbn,booklib))

# '''Sample Book Data'''
# booklibdict = {'9781593279509': '"title":"Eloquent JavaScript Third Edition"\n"subtitle":"A\
#  Modern Introduction to Programming"\n"author":"Marijn Haverbeke"\n"published":"2018-12-04T00:\
# 00:00.000Z"\n"publisher":"No Starch Press"\n"pages":472\n"description":"JavaScript lies at the \
# heart of almost every modern web application from social apps like Twitter to browser-based \
# game frameworks like Phaser and Babylon. Though simple for beginners to pick up and play with \
# JavaScript is a flexible complex language that you can use to build full-scale applications.\
# "\n"website":"http://eloquentjavascript.net/"', '9781491943533': '"title":"Practical Modern \
# JavaScript"\n"subtitle":"Dive into ES6 and the Future of JavaScript"\n"author":"NicolÃ¡s \
# Bevacqua"\n"published":"2017-07-16T00:00:00.000Z"\n"publisher":"O\'Reilly Media"\n"pages":334\n"\
# description":"To get the most out of modern JavaScript you need learn the latest features of its \
# parent specification ECMAScript 6 (ES6). This book provides a highly practical look at ES6 \
# without getting lost in the specification or its implementation details."\n"website":\
# "https://github.com/mjavascript/practical-modern-javascript"'}
# booklibdict = dict((k.title(),v.title()) for k, v in booklibdict.items())asd

#View Current Library
def viewLibrary(booklibdict):
    return booklibdict

#Searching a book
def searchBook(bookisbn,booklibdict):
    if bookisbn in booklibdict:
        print('The book with ISBN ',bookisbn,' has been found in the Library')
        return booklibdict[bookisbn]
    else:
        return "The book could not be found in the Library Management System"        

#Add a book
def addbook(bookinfo,booklibdict):
    try:
        booklibdict.update(bookinfo)
        print('The book information ',bookinfo,' has been added to the Library')
        return booklibdict
    except:
        return "The book could not be added to the Library Management System"

#Removing a book
def removeBook(bookisbn,booklibdict):
    try:
        del(booklibdict[str(bookisbn)])
        print('The book with ISBN ',str(bookisbn),' has been removed from the Library')
        return booklibdict
    except:
        return'The book to remove, could not be found in the Library Management System'


'''Lib Mgmt Switch'''
librarySwitch = True

while librarySwitch == True:
    txtprompt = 'Please select a feature to use in Library Management System \nEnter "V" to view, "S" for search, "A" for adding a new book, "R" for remove: '
    selectFeature = input(txtprompt)

    if selectFeature.lower() == 'v':
        liboutp = viewLibrary(booklibdict)
    elif selectFeature.lower() == 's':
        txtprompt = "Please Enter a book ISBN to search: "
        bookisbn = input(txtprompt)
        #Feature 1: Search a book
        liboutp = searchBook(bookisbn,booklibdict)
    elif selectFeature.lower() == 'a':
        txtprompt = "Please Enter a book ISBN to add: "
        bookinfo1 = input(txtprompt)

        txtprompt = '-- Please enter following information of book (hit enter after entering one info) -- \
            Title, Subtitle, Author, Publish date, Publisher name, Pages, Description, \
                Website address:\n'
        print(txtprompt)
        bookinfo2 = [input('"Title":"').title()+'"',input('"Subtitle":"').title()+'"',\
            input('"Author":"').title()+'"',input('"Published":"').title()+'"',\
                input('"Publisher":"').title()+'"',input('"Pages":').title(),\
                    input('"Description":"').title()+'"',input('"Website":"').title()+'"']
        # bookinfo2 = ['"Title":"'+input().title()+'"','"Subtitle":"'+input().title()+'"',\
        #     '"Author":"'+input().title()+'"','"Published":"'+input().title()+'"',\
        #         '"Publisher":"'+input().title()+'"','"Pages":'+input().title(),\
        #             '"Description":"'+input().title()+'"','"Website":"'+input().title()+'"']

        bookinfo = {bookinfo1:bookinfo2}
        #Feature 3: Add a book
        liboutp = addbook(bookinfo,booklibdict)        
    elif selectFeature.lower() == 'r':
        txtprompt = "Please Enter a book ISBN to remove: "
        bookisbn = input(txtprompt)
        #Feature 3: Remove a book
        liboutp = removeBook(bookisbn,booklibdict)
    print("Result:\n")
    if type(liboutp) is dict:
        for k, v in liboutp.items():
            print(k,'\n',v,'\n\n\n')
    else:
        print(liboutp)

    #Exiting the Library Management System?
    usrCmd = input("Do you wish to exit? Enter 'Yes' or 'No': ")
    if usrCmd.lower() == 'yes':
        librarySwitch = False
        print("Library Management System has now been closed. Cya!")
    else:
        librarySwitch = True