import selenium.webdriver as webdriver
from selenium.webdriver.chrome.service import Service
import time
from bs4 import BeautifulSoup
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager




def scrape_website(website):
    print("Launching chrome browser...")

    # chrome_driver_path = "./chromedriver.exe"
    # options = webdriver.ChromeOptions()
    # driver = webdriver.Chrome(service=Service(chrome_driver_path), options=options)
    driver = webdriver.Chrome(ChromeDriverManager().install())

    try:
        driver.get(website)
        print("Page loaded")
        html = driver.page_source
        time.sleep(10)
        return html
    
    finally:
        driver.quit()


def extract_body_content(html_content):
    soup = BeautifulSoup(html_content,"html.parser") #parsing the html content using built in html parser of python

    body_content = soup.body #only takes the body part of html

    #if body content exists return it as a string
    if body_content:
        return str(body_content)
    return ""

#we need to clean the body content further to avoid passing unnecessary tokens to the LLM
def clean_body_content(body_content):
    soup = BeautifulSoup(body_content,"html.parser")

    # It looks for all <script> and <style> tags in the HTML content represented by soup. These tags usually contain JavaScript and CSS, respectively.

    #The extract() method is called on each of these tags, which removes them from the HTML document for easier analysis
    for script_and_style in soup(["script","style"]):
        script_and_style.extract()

    cleaned_content = soup.get_text(separator="\n") #retrieves all the text ignoring the html tag and organizes it into a single string with new lines between different elements

    cleaned_content= "\n".join(
        line.strip() for line in cleaned_content.splitlines() if line.strip()
        #cleaned_content.splitlines() splits content into separate lines
        #for each line strips off whitespaces at the beginning and end
        #line.strip() only keeps lines which are not empty after stripping off whitespaces
    )

    #after everything "\n".join again joins each line
    

    return cleaned_content

 #we wont pass the the entire dom cause there are some limits on the token size, so we break the (dom) content into parts and then pass it to the LLM 
def split_dom(dom_content, max_length=6000):
    return [
        dom_content[i:i + max_length] for i in range(0,len(dom_content),max_length) 
        #range syntax : range(start,stop,[,step]) i.e start+step, again start+step+step ....
    ]
