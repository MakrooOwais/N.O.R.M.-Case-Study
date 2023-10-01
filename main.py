from bs4 import BeautifulSoup
import requests
import numpy as np
import os

years = [
    "-historical-data?end_date=830457000&st_date=798921000",
    "-historical-data?end_date=887481000&st_date=856031400",
    "-historical-data?end_date=936383400&st_date=904933800",
    "-historical-data?end_date=1082313000&st_date=1050777000",
    "-historical-data?end_date=1239733800&st_date=1208284200",
    "-historical-data?end_date=1396722600&st_date=1365273000",
    "-historical-data?end_date=1554834600&st_date=1523385000",
]

companies = {
    "Adani Enterprises Ltd": "https://in.investing.com/equities/adani-enterprises",
    "Adani Ports and Special Economic Zone Ltd": "https://in.investing.com/equities/mundra-port-special-eco.-zone",
    "Apollo Hospitals Enterprises Ltd.": "https://in.investing.com/equities/apollo-hospitals",
    "Asian Paints Ltd.": "https://in.investing.com/equities/asian-paints",
    "Axis Bank Ltd": "https://in.investing.com/equities/axis-bank",
    "Bajaj Auto Ltd": "https://in.investing.com/equities/bajaj-auto",
    "Bajaj Finance Ltd": "https://in.investing.com/equities/bajaj-finance",
    "Bajaj Finserv Ltd": "https://in.investing.com/equities/bajaj-finserv-limited",
    "Bharti Airtel Ltd.": "https://in.investing.com/equities/bharti-airtel",
    "Bharat Petroleum Corp. Ltd.": "https://in.investing.com/equities/bharat-petroleum",
    "Cipla Ltd.": "https://in.investing.com/equities/cipla",
    "Coal India Ltd": "https://in.investing.com/equities/coal-india",
    "Divi's Laboratories Ltd.": "https://in.investing.com/equities/divis-laboratories",
    "Dr. Reddy’s Laboratories Ltd": "https://in.investing.com/equities/dr-reddys-laboratories",
    "Eicher Motors Ltd.": "https://in.investing.com/equities/eicher-motors",
    "Grasim Industries Ltd": "https://in.investing.com/equities/grasim-industries",
    "HCL Technologies Ltd": "https://in.investing.com/equities/hcl-technologies",
    "HDFC Bank Ltd": "https://in.investing.com/equities/hdfc-bank-ltd",
    "HDFC Life Insurance Company Ltd": "https://in.investing.com/equities/hdfc-standard-life",
    "Hero MotoCorp Ltd": "https://in.investing.com/equities/hero-motocorp",
    "Hindalco Industries Ltd.": "https://in.investing.com/equities/hindalco-industries",
    "Hindustan Unilever Ltd.": "https://in.investing.com/equities/hindustan-unilever",
    "ICICI Bank Ltd": "https://in.investing.com/equities/icici-bank-ltd",
    "IndusInd Bank Ltd.": "https://in.investing.com/equities/indusind-bank",
    "Infosys Ltd": "https://in.investing.com/equities/infosys",
    "Indian Oil Corporation Ltd": "https://in.investing.com/equities/indian-oil-corporation",
    "ITC Ltd": "https://in.investing.com/equities/itc",
    "JSW Steel Ltd": "https://in.investing.com/equities/jsw-steel",
    "Kotak Mahindra Bank Ltd.": "https://in.investing.com/equities/kotak-mahindra-bank",
    "Larsen & Toubro Ltd": "https://in.investing.com/equities/larsen---toubro",
    "LTIMindtree Ltd": "https://in.investing.com/equities/larsen-toubro-infotech-ltd",
    "Mahindra & Mahindra Ltd.": "https://in.investing.com/equities/mahindra---mahindra",
    "Maruti Suzuki India Ltd.": "https://in.investing.com/equities/maruti-suzuki-india",
    "Nestle India Ltd": "https://in.investing.com/equities/nestle",
    "NTPC Ltd": "https://in.investing.com/equities/ntpc",
    "Oil And Natural Gas Corporation Ltd": "https://in.investing.com/equities/oil---natural-gas-corporation",
    "Power Grid Corporation of India Ltd": "https://in.investing.com/equities/power-grid-corp.-of-india",
    "Reliance Industries Ltd": "https://in.investing.com/equities/reliance-industries",
    "State Bank Of India": "https://in.investing.com/equities/state-bank-of-india",
    "SBI Life Insurance Company Ltd": "https://in.investing.com/equities/sbi-life-insurance",
    "Sun Pharmaceutical Industries Ltd.": "https://in.investing.com/equities/sun-pharma-advanced-research",
    "Tata Consumer Products Ltd": "https://in.investing.com/equities/tata-global-beverages",
    "Tata Motors Ltd": "https://in.investing.com/equities/tata-motors-ltd",
    "Tata Steel Ltd": "https://in.investing.com/equities/tata-steel",
    "Tata Consultancy Services Ltd.": "https://in.investing.com/equities/tata-consultancy-services",
    "Tech Mahindra Ltd": "https://in.investing.com/equities/tech-mahindra",
    "Titan Company Ltd": "https://in.investing.com/equities/titan-industries",
    "UltraTech Cement Ltd": "https://in.investing.com/equities/ultratech-cement",
    "UPL Ltd": "https://in.investing.com/equities/united-phosphorus",
    "Wipro Ltd": "https://in.investing.com/equities/wipro-ltd",
}

for company in companies.keys():
    for year in years:
        url = companies[company] + year
        r = requests.get(url)

        soup = BeautifulSoup(r.content, "html5lib")

        head = ["date", "close", "open", "high", "low", "volume"]

        # Loading Dates Column
        date = []
        for a in soup.findAll("td", attrs={"class": "col-rowDate"}):
            date_txt = a.find("span", attrs={"class": "text"})
            date.append(date_txt.text)

        close = []
        for a in soup.findAll("td", attrs={"class": "col-last_close"}):
            close_txt = a.find("span", attrs={"class": "text"})
            close.append(close_txt.text)
        # Loading Open Prices
        open = []
        for a in soup.findAll("td", attrs={"class": "col-last_open"}):
            open_txt = a.find("span", attrs={"class": "text"})
            open.append(open_txt.text)
        # Loading High Prices
        high = []
        for a in soup.findAll("td", attrs={"class": "col-last_max"}):
            high_txt = a.find("span", attrs={"class": "text"})
            high.append(high_txt.text)
        # Loading Low Prices
        low = []
        for a in soup.findAll("td", attrs={"class": "col-last_min"}):
            low_txt = a.find("span", attrs={"class": "text"})
            low.append(low_txt.text)

        volume = []
        for a in soup.findAll("td", attrs={"class": "col-volume"}):
            volume_txt = a.find("span", attrs={"class": "text"})
            volume.append(volume_txt.text)

        final = [head]
        for i in range(len(date)):
            final.append([date[i], close[i], open[i], high[i], low[i], volume[i]])

        path = company + "/"
        if len(final) > 1:
            if not os.path.exists(path):
                os.mkdir(path)
            np.savetxt(
                f"{path}/{date[0]} - {date[-1]} .csv", final, delimiter=", ", fmt="% s"
            )

            print(company + " " + date[0] + "-" + date[-1] + " Done")
