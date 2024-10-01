def frequency_Analysis(ciphertext:str) -> dict:
	frequencyDict = {}
	for x in ciphertext:
		#if in dictionary then add one to the value
		#if not then add to dictionary
		if x.isalpha():
			if str(x) in frequencyDict.keys():
				frequencyDict[str(x)] += 1
			else:
				frequencyDict.update({str(x): 1})
	frequencyDict = dict(sorted(frequencyDict.items(), key=lambda item: item[1], reverse=True))
	return frequencyDict
ciphterText = input("Please enter your ciphertext: ")
print(frequency_Analysis(ciphterText))
