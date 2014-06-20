from azure_translate import trans
import sys

count=0
container=[]
chinese=[]
with open (sys.argv[1], "r") as myfile:	
	string_eng=""
	for keyword in myfile:
		container.append(keyword.rstrip('\n'))
	for i in range(len(container)):
		string_eng += (container[i]+'* ')
		count += 1
		if(count==50):
			string_cht = trans(string_eng)
			chinese.extend(string_cht.split('*'))
			string_eng=""
			count=0
			break
	#for i in range(len(chinese)):
		#string=chinese[i]
		#print(string.decode("utf-8"))

with open ("translated", "w") as myfile:
	for i in range(len(chinese)):
		myfile.write(container[i] + ' ')
		myfile.write(chinese[i] + '\n')
