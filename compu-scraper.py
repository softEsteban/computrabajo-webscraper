from bs4 import BeautifulSoup
import requests

html_text = requests.get('https://www.computrabajo.com.co/trabajo-de-nodejs').text
soup = BeautifulSoup(html_text, 'lxml')
posts = soup.find_all('article', class_='box_border hover dFlex vm_fx mbB cp bClick mB_neg_m mb0_m')

for p in posts:
    # print(p.text)

    job_title = p.find("h1", class_="fs18 fwB").text
    job_company = p.find("p", class_="fs16 fc_base mt5 mb10").text
    job_description= p.find("p", class_="fc_aux t_word_wrap mb10 hide_m").text
    job_pub_time= p.find("p", class_="fs13 fc_aux").text

    print("WHEN WAS IT PUBLISHED?   " + job_pub_time)
    print("WHAT IS THE ROLE??   " + job_title)
    print("WHICH COMPANY?   " + job_company)
    print("ARE THERE DETAILS?   " + job_description)
    print("________________________________________________")