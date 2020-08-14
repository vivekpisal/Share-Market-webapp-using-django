import cv2
import easyocr
from pylab import rcParams
from IPython.display import Image
import pytesseract

rcParams['figure.figsize']=8,16

def card_recognize(name):
	op1=pytesseract.image_to_string(name,lang='hin')
	op2=pytesseract.image_to_string(name)
	if 'आम आदमी का अधिकार' in op1 or 'आधार' in op1:
		card=1
		name=""
		for i in range(len(op2)):
			if op2[i:i+4]=="Name" or op2[i:i+3]=="Nae":
				j=0
				k=i
				while j!=3:
					if (op2[k]==' ' and (op2[k-1]!="e" or op2[k-2]!="m" or op2[k-2]!="a")):
						name+=op2[i:k]
						i=k
						j+=1
					k+=1
				for i in range(len(name)):
					if "Name" in name:
						name=name[i+5:]
						break
					elif "Nae" in name:
						name=name[i+4:]
						break
				cardno=""
				for i in range(len(op2)):
					try:
						if int(op2[i])>=0 and int(op2[i])<=9:
							cardno+=op2[i]
					except:
						pass
				for j in range(len(cardno)):
					if "Card" in cardno:
						loc=cardno.index("Card")
						cardno=cardno[loc+3:]
				
	elif 'INCOMETAX DEPARTMENT' in op2 or 'NCOMETAX DEPARTMENT' in op2 or 'आयकर विभाग' in op1 or 'ज्ञायकर विभाज' in op1 or 'ज्ञायकर विभाग' in op1 or 'स्आवायकर विभाण' in op1 or 'स्थायी लेखा संख्या कार्ड' in op1:
		card=2
		name=""
		for i in range(len(op2)):
			if op2[i:i+4]=="Name" or op2[i:i+3]=="Nae":
				j=0
				k=i
				while j!=4:
					try:
						if op2[k]==' ':
							name+=op2[i:k]
							i=k
							j+=1
						k+=1
					except:
						j+=1
				break
		for i in range(len(name)):
			if "Name" in name:
				name=name[i+4:]
				break
			elif "Nae" in name:
				name=name[i+3:]
				break
		if len(name)==0:
			name=" "
		if 'Permanent Account Number Card' in op2:
			loc=op2.index('Card')
			j=0
			cardno=""
			k=loc
			while j!=1:
				if op2[loc]==' ':
					cardno+=op2[k:loc]
					k=loc
					j+=1
				loc+=1
			for j in range(len(cardno)):
				if "Card" in cardno:
					loc=cardno.index("Card")
					cardno=cardno[loc+4:]
					break
			new=cardno
			cardno=""
			for i in range(len(new)):
				try: 
					if int(new[i])>=0 and int(new[i])<=9:
						cardno+=new[i]
				except:
					if new[i]>='A' and new[i]<='Z':
						cardno+=new[i]

		else:
			cardno=" "


	else:
		card=0
		name=""
		cardno=""
	return card,name,cardno