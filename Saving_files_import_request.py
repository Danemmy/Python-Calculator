import requests

Deep_work_url = "https://www.newslodge.com.ng/wp-content/uploads/2021/09/professional-cover-letter.zip"

getbookpdf = {"download_cover_letter": "PDF"}

response = requests.get(Deep_work_url, params=getbookpdf)
response.url
'https://www.newslodge.com.ng/wp-content/uploads/2021/09/professional-cover-letter.zip'
response.ok
True
response.status_code
200

if response.ok == True:
    with open("download_cover_letter.zip", mode="wb") as file:
     file.write(response.content)
     print("saved succesfuly")
else:
    print("Error while saving")
