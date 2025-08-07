import requests
from bs4 import BeautifulSoup
import pandas as pd # output in table
def scrap():
      
      responce = requests.get('https://wuzzuf.net/search/jobs/?q=machine+learning&a=navbl')
      
      soup = BeautifulSoup(responce.content , 'html')
      

      titels =  soup.find_all("h2",{'class':'css-m604qf'})

      titels_list = [ titel.text for titel in titels]
  

      occupattions = soup.find_all('div',{'class':'css-1lh32fc'})
 
      occupattions_list = [occupattion.text for occupattion in occupattions]
   

      companies = soup.find_all('a',{'class':'css-17s97q8'})
      
      companies_list = [company.text for company in companies]
     
      companies_list = [company.replace(' -','') for company in companies_list]


      spics = soup.find_all('div',{'class':'css-y4udm8'})
    
      spics_list =[spic.text for spic in spics]
     

      scraped_data = {} # dectionary key and values   collectt data
      scraped_data['titels']=titels_list
      scraped_data['occupation']=occupattions_list
      scraped_data['company']=companies_list
      scraped_data['spics']=spics_list
     


      df = pd.DataFrame(scraped_data)
     
      df.to_csv("wazzf.csv",index=False)
      print("jops scraped successfully")
      return df
if __name__ =='__main__':
      scrap()
