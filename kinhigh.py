# This script extracts the highlights from the Kindle to properly formatted .txt files (one for each book).
import os

# Default name
filename = "My Clippings.txt"

# Minimum Highlights - To only consider pulling from a book that has atleast this many highlights
minHighlights = 2

try:  
    fhand = open(filename, encoding="utf8")
    print("'My clippings.txt' file has been loaded...")
    print("\n")
except: 
    print("Either file not found or not in a readable format")
    quit()

# Extracting the names of the books
count = 1
BookList = list()
isitabook = False

for line in fhand:
    line = line.strip()
    if count == 1 or isitabook:
        # This is always a book name
        book = line.replace('\ufeff','')             # getting rid of a the BOM character which appears in front of the book names SOMETIMES
        if book not in BookList:
             BookList.append(book)
        isitabook = False

    if line.startswith('=========='):
        # This means that the next line will be a book name
        isitabook = True

    count = count + 1

# The book format I have is: Book Name (Author Name)
print("The Following", len(BookList), "books were found on your Kindle:")
for Title in BookList:
    print(Title)
print("\n")


# Now let me start extracting the highlights
fhand = open(filename, encoding="utf8")
lineNum,nextline,highlightline = 0,0,0
Highlights = dict()
quotes = list()

for line in fhand:
    lineNum +=1
    line = line.strip()
    if line in BookList or line.replace('\ufeff','') in BookList:
        # it means that it is a book
        Book = line.replace('\ufeff','')            # getting rid of a the BOM character which appears in front of the book names SOMETIMES
        nextline = lineNum + 1
    
    if lineNum == nextline :
        if line.startswith('- Your Highlight'):     # Since we don't want to capture any bookmarks
            highlightline = lineNum + 2
    
    if lineNum == highlightline :
        quote = line
        if Book not in Highlights:
            Highlights[Book] = [quote]
        else:
            if Highlights[Book][-1][:50] == quote[:50]:
                Highlights[Book][-1] = quote        # Since this is a duplicate highlight
            else:
                Highlights[Book].append(quote)



# Writing the highlights to the .txt files
isExist = os.path.exists('./KindleBooks')
if not isExist:
    os.makedirs('./KindleBooks')
os.chdir('./KindleBooks')
print("Highlights from the following books have been extracted (check 'KindleBooks' folder)")
for (bk,highs) in Highlights.items():
    if len(highs) >= minHighlights:
        print(bk)
        #Remove any invalid characters from the file name
        invalid = '<>:"/\|?-*'
        for char in invalid:
            bk = bk.replace(char,'')
        if len(bk) > 80:
            bk = bk[0:80]      

        filename = bk + ".txt"
        f = open(filename, "w+")
        if len(highs) >= minHighlights:
            f.write("The following parts are what I highlighted while reading the book:\n\n")
            for high in highs:
                try:
                    f.write("- " + high)
                    f.write('\n')
                except:
                    f.write("- THIS HIGHLIGHT IS MISSING FOR SOME REASON")
                    f.write('\n')

        f.close()

print("\n\n------ If you are seeing this message, everything has been done SUCCESSFULLY------ \n")