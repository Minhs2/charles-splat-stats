import bs4 as beausoup
import urllib.request
import time

def fetchStats():
    source = urllib.request.urlopen('https://docs.google.com/spreadsheets/d/1di9JvURVglp10jakbaZoVBfy9xFWnJtiIVbU5QH94Q4/htmlembed/sheet?gid=1419716716').read()

    soup = beausoup.BeautifulSoup(source,'lxml')
    numbersArr = []

    for numbers in soup.find_all('td'):
        numbersArr.append(numbers.text)
        
    finalStr = " | Games vs Order: " + numbersArr[0] + " | Win% vs Order: " + numbersArr[1] + " | Games vs Chaos: " + numbersArr[2] + " | Win% vs Chaos: " + numbersArr[3]
    file = open("OBSOutput.txt","w")
    file.write(finalStr)
    
def main():
    while True:
        fetchStats()
        time.sleep(10)

if __name__ == '__main__':
    main()