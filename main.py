import bs4 as beausoup
import urllib.request
import time

def fetchStats():
    # Open a stripped down (htmlembed) version of the spreadsheet
    source = urllib.request.urlopen('https://docs.google.com/spreadsheets/d/1di9JvURVglp10jakbaZoVBfy9xFWnJtiIVbU5QH94Q4/htmlembed/sheet?gid=1419716716').read()

    soup = beausoup.BeautifulSoup(source,'lxml')
    numbersArr = []

    # Fetch the cells from the url
    for numbers in soup.find_all('td'):
        numbersArr.append(numbers.text)
        
    # Concatenate and format string
    finalStr = " | Games vs Order: " + numbersArr[0] + " | Win% vs Order: " + numbersArr[1] + " | Games vs Chaos: " + numbersArr[2] + " | Win% vs Chaos: " + numbersArr[3]
    # Write to file
    file = open("OBSOutput.txt","w")
    file.write(finalStr)
    file.close()    
    
def main():
    # Run fetchStats() until forcefully terminated
    while True:
        fetchStats()
        time.sleep(10)

if __name__ == '__main__':
    main()
