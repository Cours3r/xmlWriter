# @author Benjamin Stewart
# rc.xml builder, specifically for openbox configs


def versionTag(f,version,encoding):
	f.write("<?xml version=\"{0}\" encoding=\"{1}\"?>\n".format(version,encoding))

def tabStr(level):
	outStr = ""
	for i in range(0,level):
		outStr += "\t"
	return outStr

class longTag:
	def __init__(self,f,tabLevel,section):
		self.section = section
		self.file = f
		self.tabs = tabStr(tabLevel)
		self.file.write(self.tabs + "<{0}>\n".format(self.section))

	def close(self):
		self.file.write(self.tabs + "</{0}>\n".format(self.section))

def tag(f,tabLevel,style,title,arg1,arg2=[]):
	if style == "s" or style == "solo" or style == 1:
		f.write(tabStr(tabLevel) + "<{0} {1}=\"{2}\"/>\n".format(title,arg1[0],arg1[1]))
	elif (style == "g" or style == "gen" or style == 2):
		if arg2:
			f.write(tabStr(tabLevel) + "<{0} {1}=\"{2}\">{3}</{0}>\n".format(title,arg1[0],arg1[1],arg2))
		else:
			f.write(tabStr(tabLevel) + "<{0}>{1}</{0}>\n".format(title,arg1))
	elif (style == "b" or style == "big" or style == 3):
		if arg1:
			f.write(tabStr(tabLevel) + "<{0} {1}=\"{2}\">\n".format(title,arg1[0],arg1[1]))
		else:
			f.write(tabStr(tabLevel) + "<{0}>\n".format(title))
		for inner in arg2:
			if len(inner) == 3:
				tag(f,tabLevel+1,inner[0],inner[1],inner[2])
			else:
				tag(f,tabLevel+1,inner[0],inner[1],inner[2],inner[3])
		f.write(tabStr(tabLevel) + "</{0}>\n".format(title))
	else:
		print("!! Error: Style Not Valid !!")
		print("tag {0} \nstyle {1}".format(title,style))
