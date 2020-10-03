import requests
# it will give html contents.URL ocntent we want in our program then we can use it.here url saved in browser
r = requests.get("https://financialmodelingprep.com/developer/docs/?gclid=CjwKCAjw57b3BRBlEiwA1ImytjUUBXWTZouNldQQ1oFnRWT0LsluHAB-qBjqvGUxrCdq-Ftr8c9_YhoCWC4QAvD_BwE")
print(r.text)
print(r.status_code)        #200=ok, 100=continue, 202=accpted
'''
# here post request in url is not saved in browser.
url = "www.thoughtsofkinjal.com"
data = {
    "p1":4,
    "p2":3
}
r2 = requests.post(url= url, data= data)
'''