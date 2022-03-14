from ast import JoinedStr
from re import I
from bs4 import BeautifulSoup
from datetime import date, datetime
import requests

today = date.today()
today_format = today.strftime("%B %d, %Y")
now = str(datetime.now()).replace(' ', '-')
now2 = now.replace('-', '')
now3 = now.replace('.', '')
now4 = now.replace(':', '')

## Function
#  Sends a request the website based on a 
#  job opening and and the indexed page

def websiteRequest(role, page):
    #Initial vars
    jobs = []
    
    counter = 0
    #Request
    html_textUse = requests.get('https://www.computrabajo.com.co/trabajo-de-'+role+'?p='+str(page)).text
    soup = BeautifulSoup(html_textUse, 'lxml')
    posts = soup.find_all('article', class_='box_border hover dFlex vm_fx mbB cp bClick mB_neg_m mb0_m')
    #Extracting data
    for p in posts:
        job_pub_time= p.find("p", class_="fs13 fc_aux").text
        job_title = p.find("h1", class_="fs18 fwB").text
        job_company = p.find("p", class_="fs16 fc_base mt5 mb10").text.replace(' ', '')
        job_description= p.find("p", class_="fc_aux t_word_wrap mb10 hide_m").text
        job = job_title + " " +  job_pub_time + " " + job_company
        jobs.append(str(job))  
        counter += 1
    return jobs if len(jobs) > 0 else "No posts found"

# User input
user_role= input("What job opening are you looking for?")
index = 0
# Request instance
result = websiteRequest(user_role, index)

if(isinstance(result, list)):
    jobs_repository = []
    index= index + 2
    flag= True

    while flag:
        # Request instance
        result = websiteRequest(user_role, index)
        print("INDEX " + str(index))

        if(isinstance(result, list)):
            for p in result:
                print("ITEM: " + p)
                jobs_repository.append(p)
                
            print('im a list') 
            # print(result[1])
            index = index + 1

        elif(isinstance(result, str)):
            print('im a str')
            print('finished')
            flag=False


## Function
#  Sends a request the website based on a 
#  job opening and and the indexed page

def generateReport(jobs):
    f = open(f"jobs-report{now4}.txt" , "x")
    f.write(f"""
    MY COMPUTRABAJO REPORT! \n
    Date generated: {today_format} \n 
    Info: {(str(len(jobs)))} jobs found for {user_role} \n
    This report is a product of a Python programm to scrap
    Computrabajo website. At first it asks users to input
    the job role they want and concatenates it to the route
    filter. 
    """)
    f.write('__________________________________________________________ \n \n')
    for job in jobs:
        f.write(job + "\n") 
        f.write("________________________________________________ \n")
    f.close()

if(len(jobs_repository)>0):
    generateReport(jobs_repository)

    

