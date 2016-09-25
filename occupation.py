import csv
import random

occFile = open("occupations.csv","r")
#use to deal with anything weird the user may have done (spaces, commas, etc.)
occReader = csv.DictReader(occFile)
occDict = {}

def googlify(q):
    if not q:
        return "nope"
    orig = q.split(" ")
    ret = orig.pop(0)
    while orig:
        ret += "+" + orig.pop(0)
    return "get+started+in+" + ret


for row in occReader:
    #save job title as string
    job = row["Job Class"]
    #google search url (to get you started on your search)
    end = googlify(job).lower()
    url = "https://google.com/#q=" + end
    #assign dictionary values
    occDict[job] = [(float)(row["Percentage"]), url]

occFile.close()

def printDict():
    for row in occDict:
        print row + ":", #want to print on same line
        #diagnostics
        print occDict[row][0] + 0, #still same line
        print "%"

def stringDict():
    #table
    ret = "<table bordercolor:\"black\" border=\"5\">"
    #headings
    ret += "<th>Occupation</th><th>Percent</th>"
    #add in info
    for row in occDict:
        ret += "<tr><td>"+ row + "</td><td>" + str(occDict[row][0]) + "%</td></tr>"
    return ret + "</table>"

#modified for occu-table.py
def randomPick():
    message = "<p>Want to get started in this field? Start with this "
    rand = random.randrange(100)
    for row in occDict:
        rand -= occDict[row][0]
        if rand <= 0:
            #this is all the important, descriptive stuff about your occupation in the header
            #also, opens link in new tab, b/c same tab annoys me
            return "<h1>" + row + "</h1>" + message + "<a href=" + occDict[row][1] + " target=\"_blank\"> this </a> google search! </p>"
    return "Something went wrong"


#diagnostics
#printDict()
print randomPick()
