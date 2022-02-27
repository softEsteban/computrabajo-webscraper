from bs4 import BeautifulSoup
from datetime import date, datetime
import requests

#User input
role_user = str(input("Which job you are you looking for? > "))

#Getting to the site. Filter included
html_text = requests.get('https://www.computrabajo.com.co/trabajo-de-'+role_user).text
soup = BeautifulSoup(html_text, 'lxml')
posts = soup.find_all('article', class_='box_border hover dFlex vm_fx mbB cp bClick mB_neg_m mb0_m')

#Initial vars and repository
counter = 0
jobs= []
now = str(datetime.now()).replace(' ', '-')
now2 = now.replace('-', '')
now3 = now.replace('.', '')
now4 = now.replace(':', '')
today = date.today()
today_format= today.strftime("%B %d, %Y")

#Looping through posts  
for p in posts:
    job_pub_time= p.find("p", class_="fs13 fc_aux").text
    job_title = p.find("h1", class_="fs18 fwB").text
    job_company = p.find("p", class_="fs16 fc_base mt5 mb10").text.replace(' ', '')
    job_description= p.find("p", class_="fc_aux t_word_wrap mb10 hide_m").text
    counter = counter + 1 
    line = f'Title: {job_title} \n Date published: {job_pub_time} \n Company: {job_company} \n Description: {job_description} '

    jobs.append(line)

    print("WHEN WAS IT PUBLISHED?   " + str(job_pub_time))
    print("WHAT IS THE ROLE?   " + str(job_title))
    print("WHICH COMPANY?   " + str(job_company))
    print("ARE THERE DETAILS?   " + str(job_description))
    print("________________________________________________")

#Generating a report in .txt file
f = open(f"jobs-report-{now4}", "x")
f.write(f"""
MY COMPUTRABAJO REPORT! \n
Date generated: {today_format} \n 
Info: {counter} jobs found for {role_user} \n
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


