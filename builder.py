import uuid
postContent=[]
postTemplate=[]
indexTemplate=[]
postID=''
postTitle=''
postDate=''
imageFileName=''
imageSize=500
toWrite=[]
def getPostTitle():
        t=input("Post Title: ")
        return t
def getImage():
        t=input("Image File Name: ")
        return t
def getPostDate():
        t=input("Post Date (FORMAT DD/MM/YY): ")
        if t.count('/')!=2:
                return getPostDate()
        return t
def getImageSize():
        t=input("Image Size (press enter for default 500): ")
        if t=='':
                t=500
        return int(t)
def generatePostID():
	ID=uuid.uuid1()
	return ID
def getPostTemplate(file):
	template=open(file)
	tmp = template.read();
	return (tmp.split('['))
def splitIndex(file):
        template=open(file)
        tmp = template.read();
        sp= tmp.split('leftcolumn">')
        sp[0] = sp[0] +'leftcolumn">'
        return sp
def processPost(postTempList):
	if len(postTempList)>1:
		for i in range(1,len(postTempList)):
			s=''
			for c in postTempList[i]:
				if c==']':
					break
				else:
					s=s+c
			if s=='TITLE':
                                #print(s)
                                
                                newTmp=postTitle+(postTempList[i][6:])
                                postTempList[i]=newTmp
                                #print(postTempList)
			if s=='DATE':
                                newTmp = postDate + (postTempList[i][5:])
                                postTempList[i]=newTmp
                                #print(postTempList)
			if s=='IMAGENAME':
                                newTmp = imageFileName + (postTempList[i][10:])
                                postTempList[i]=newTmp

			if s=='IMAGESIZE':
                                newTmp = str(imageSize) + (postTempList[i][10:])
                                postTempList[i]=newTmp
                                #print(postTempList)
			if s=='CONTENT':
                                
                                cont=''.join(postContent)
                                newTmp = cont + (postTempList[i][8:])
                                postTempList[i]=newTmp
                                #print(postTempList)
			if s=='POSTFILE':
                                newTmp = "post_"+str(postID)+".html"+ (postTempList[i][9:])
                                postTempList[i]=newTmp
	return postTempList



def readNewPost(fileName):
	f=open(fileName)
	line = f.readline()
	while line:
                print(line)
                postContent.append("<p>"+line+"</p>")
                line = f.readline()
def writePostFile():
        fname= "post_"+str(postID)+".html"
        with open('../blog/posts/'+fname, 'w') as f:
                f.writelines(toWrite)
def writeIndexFile():
        with open('../blog/index.html','w') as f:
                f.writelines(indexTemplate[0])
                f.writelines(indexWrite)
                f.writelines(indexTemplate[1])

readNewPost('newPost.txt')

postID= generatePostID()
postTemplate = getPostTemplate("postTemplate.txt")
print(postID)
postTitle=getPostTitle()
postDate= getPostDate()
imageFileName = getImage()
imageSize=getImageSize()
toWrite=processPost(postTemplate)
#print(toWrite)
writePostFile()
cardTemplate = getPostTemplate("cardTemplate.txt")
indexWrite = processPost(cardTemplate)

indexTemplate = splitIndex("../blog/index.html")
writeIndexFile()
