import re       #it is regular expression

mustr = '''Post Office: INFOSYS CAMPUS
Post Office Type: SUB OFFICE
District: MYSORE
State: KARNATAKA
Pin Code: 570027 (Click to see all Post Offices with same Pin Code)
Contact Address: Postmaster, Post Office INFOSYS CAMPUS (SUB OFFICE), MYSORE, KARNATAKA (KA), India (IN), Pin Code:- 570027
Delivery Status:- DELIVERY
Postal Taluk:- MYSORE
Postal Division:- MYSORE
Postal Region:- SOUTH KARNATAKA
Postal Circle:- KARNATAKA 
no:- 56789-5432
mno:- 8866622758
mno1:- +916789012345
mno2: - +913452277884
'''

#---------------------------------------findall--------------------------------------------------
# specific string match find and retirn

#---------------------------------------------search----------------------------------------------
# search is also searching  but it will return match object.

#---------------------------------------------split-----------------------------------------------
#it returns list

#--------------------------------------------finditer-----------------------------------------------
print(r"\n")        #it wil print \n
pat = re.compile(r"KARNATAKA")        #r means rowstring
# pat = re.compile(r".")          #it matches with all character
# # pat = re.compile(r".INFO")
# pat = re.compile(r"$Post")        #if string start with those character then retrun atherwise not.
# pat = re.compile(r"KARNATAKA $")         #IT RETURNS END WITH
# pat = re.compile(r"a*i*")         #IT REturns a and i of character.
# pat = re.compile(r"ai+")         #IT least 1 i requered.
# pat = re.compile(r"at{2}")         #if we required exact 2 k.
# pat = re.compile(r"at{2}|S")         #either 1st or second.

#special sequences
pat = re.compile(r"\APost")     #it will return string if start with or not.
pat = re.compile(r"KARNATAKA\b")        #it will retrun ending with karnataka.
pat = re.compile(r"MYSORE\b")        #it will retrun ending with mysore.
pat = re.compile(r"\d{5}-\d{4}")        #it will retrun digits.
pat = re.compile(r"\d{10}")        #it will retrun exactly 10 digits.
pat = re.compile(r"[+][9][1]\d{10}")        #it will retrun exactly 10 digits.
matches = pat.finditer(mustr)
for match in matches:
    print(match)
    # print(mustr[448:452])

# Task:- given a string with the lots of mno. staring from +91.