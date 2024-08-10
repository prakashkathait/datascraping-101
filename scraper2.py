import requests
from bs4 import BeautifulSoup
import openpyxl, csv

# Define the CSV file and write the header
csv_file_path = 'D:/Python Projects/web scrapping/Books.csv'
with open(csv_file_path, 'w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    field = ['Book_Name', 'Author', 'Ratings', 'Type', 'Price']
    writer.writerow(field)

# Define a function to write data into the CSV file
def write_into_csv(Book_Name, Author, Ratings, Type, Price):
    with open(csv_file_path, 'a', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow([Book_Name, Author, Ratings, Type, Price])

# Create an Excel workbook and add the header
wb = openpyxl.Workbook()
sheet = wb.active
sheet.append(['Book_Name', 'Author', 'Ratings', 'Type', 'Price'])

# Define a function to write data into the Excel file
def write_into_excel(Book_Name, Author, Ratings, Type, Price):
    sheet.append([Book_Name, Author, Ratings, Type, Price])

# Fetch the webpage content
data = requests.get('https://www.amazon.in/gp/bestsellers/books/ref=zg_bs_nav_books_0')
soup = BeautifulSoup(data.content, "html.parser")

# Find the relevant section containing the book details
job_elements = soup.find_all("div", class_="a-column a-span12 a-text-center _cDEzb_grid-column_2hIsc")

# Iterate through each book entry
for job_element in job_elements:
    try:
        title_element = job_element.find("div", class_="_cDEzb_p13n-sc-css-line-clamp-1_1Fn1y").text
        author = job_element.find("div", class_="a-row a-size-small").text
        ratings = job_element.find("span", class_="a-icon-alt").text.split(' ')[0]
        book_type = job_element.find("span", class_="a-size-small a-color-secondary a-text-normal").text
        price_element = job_element.find("span", class_="_cDEzb_p13n-sc-price_3mJ9Z")

        # Fallback to check if price is in a different tag or format
        if not price_element:
            price_element = job_element.find("span", class_="p13n-sc-price")

        if price_element:
            price = price_element.text
        else:
            price = "N/A"

        #Printing all the details
        print(title_element, "---", author, "---", ratings, "---", book_type, "---", price)
        write_into_excel(title_element, author, ratings, book_type, price)
        write_into_csv(title_element, author, ratings, book_type, price)

    except Exception as e:
        print(f"Error: {e}")

# Save the Excel workbook
wb.save("D:/Python Projects/web scrapping/Top_50_Selling_Books.xlsx")
