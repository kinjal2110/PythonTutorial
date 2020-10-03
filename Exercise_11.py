# Email collector
import re
str1 = '''
i have lots of emails inside kinjal99@gail.com .
my account has lots of emails are included pritisha45@gmail.com. if you find for internship email then internshala545@gmail.com
i am new here.

if you guys finding for new email then it is barbiedoll6775@gmail.com.

it is garbage data, we need to find email for it. krutikarana645@gmail.com.
'''

list1 = re.findall(r"\w+@\S+\w",str1)
op = open("email_storage.txt","a")
j = 1
for i in list1:
    op.write(f"Email{j}: {i}\n")
    j = j + 1
op.close()

print(f"Email's are: {list1}")
print(f"Total Email's are: {j-1}")