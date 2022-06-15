import uuid
postContent=[]
postTemplate=[]
postID=''

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
processPost(postTemplate)