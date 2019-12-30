# THIS PROGRAM CHECKS VALIDITY OF PASSWARD (VALIDITY : MIN LENGTH = 6 MAX LENGTH = 16. AT LEAST ONE CAPITAL LETTER, SMALL LETTER, SPECIAL CHARACTER AND ONE DIGIT)
Caps = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
Smalls = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
Digits = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
SpecialChars = ["@", "$", "%"]
passward = input('Enter Your Passward ')
isCap = False
isSmall = False
isDigits = False
isSpecialChar = False

if len(passward) > 5 and len(passward) < 17:
	for i in passward:
		if i in Caps:
			isCap = True

		elif i in Smalls:
			isSmall = True

		elif i in Digits:
			isDigit = True

		elif i in SpecialChars:
			isSpecialChar = True

		if isCap and isSmall and isDigit and isSpecialChar:
			break

	if isCap and isSmall and isDigit and isSpecialChar:
		print('Passward is Valid')
	else:
		print('Passward is Invalid')

else:
	print('Passward should have at least 6 letters and maximum 16')
