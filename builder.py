import uuid
postContent=[]
postTemplate=[]
postID=''
postTitle=''
postDate=''
imageSize=500
def getPostTitle():
        t=input("Post Title: ")
        return t
def getPostDate():
        t=input("Post Date (FORMAT DD/MM/YY): ")
        return t
def getImageSize():
        t=int(input("Image Size (press enter for default 500): "))
        return t
def generatePostID():
	ID=uuid.uuid1()
	return ID
def getPostTemplate():
	template=open("postTemplate.txt")
	tmp = template.read();
	return (tmp.split('['))
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
                                print(s)
                        if s=='DATE':
                                print(s)
                        if s=='IMAGESIZE':
                                print(s)
                        if s=='CONTENT':
                                print(s)


def readNewPost(fileName):
	f=open(fileName)
	line = f.readline()
	while line:
		postContent.append(line)
		line = f.readline()
readNewPost('newPost.txt')

postID= generatePostID()
postTemplate = getPostTemplate()
print(postID)
postTitle=getPostTitle()
postDate= getPostDate()
imageSize=getImageSize()
processPost(postTemplate)
