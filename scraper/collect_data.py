from bs4 import BeautifulSoup
import os
import pandas as pd

d = {'job': [], 'company': [], 'location': [], 'stipend': [], 'duration': [], 'link': []}

# Iterate over all HTML files in the "data" folder
for file in os.listdir("data"):
    try:
        with open(f"data/{file}", "r", encoding="utf-8") as f:
            html_docs = f.read()
        
        soup = BeautifulSoup(html_docs, 'html.parser')

        # Extract the job title
        job = soup.find("a", class_="job-title-href").get_text(strip=True)

        # Extract the company name
        company = soup.find("p", class_="company-name").get_text(strip=True)

        # Extract the location
        location = soup.find("div", class_="row-1-item locations").find("a").get_text(strip=True)

        # Extract the stipend
        stipend = soup.find("span", class_="stipend").get_text(strip=True)

        # Extract the duration
        duration = soup.find("div", class_="row-1-item").find("span").get_text(strip=True)

        # Extract the job link (base URL + relative path)
        link = "https://internshala.com" + soup.find("a", class_="job-title-href")["href"]

        # Append data to the dictionary
        d['job'].append(job)
        d['company'].append(company)
        d['location'].append(location)
        d['stipend'].append(stipend)
        d['duration'].append(duration)
        d['link'].append(link)

    except Exception as e:
        print(f"Error processing file {file}: {e}")

# Create a DataFrame and save it to CSV
df = pd.DataFrame(data=d)
df.to_csv('data.csv', index=False)
print("Data extraction complete and saved to data.csv")
