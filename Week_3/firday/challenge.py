import requests

class Partners:
    def __init__(self,first,last,email, country, avail_dates):
        self.first = first
        self.last = last
        self.email = email
        self.country = country
        self.dates = avail_dates
class Attendees:
    _list = []
    
    @classmethod
    def get_info(self,idx):
        l = []
        res = requests.get(f'https://ct-api-challenge.herokuapp.com/').json()['partners']
        f_name = res[idx]['firstName']
        l_name = res[idx]['lastName']
        email = res[idx]['email']
        country = res[idx]['country']
        for i in res[idx]['availableDates']:
            l.append(i)
        p = Partners(f_name,l_name,email,country,l)
        return p
    
    @classmethod
    def bestDate_byCountry(self,l_of_partners,country):
        mostOcc = {}
        count = 0
        for p in l_of_partners:
            if p.country == country:
                for i in p.dates:
                    if i not in mostOcc:
                        mostOcc.append(i)
        for i in mostOcc:
            for p in l_of_partners:
                if p.country == country:
                    for k in p.dates:
                        if i in k:
                            count += 1
            mostOcc[i] = count
            count = 0
        
        sorted_mO = sorted(mostOcc.items(), key=lambda kv:kv[1])
        best_date = sorted_mO[-1][0]
        return best_date
    
    @classmethod
    def run(self):
        l_partner = []
        l_country = {}
        res = requests.get(f'https://ct-api-challenge.herokuapp.com/').json()['partners']
        for i in range(len(res)):
            l_partner.append(self.get_info(i))
        
        for i in l_partner:
            for c in i.country:
                if c not in l_country:
                    l_country[c] = {}
        for i in l_partner:
            for c in i.country:
                date = bestDate_byCountry(l_partner,c)
                for d in i.dates:
                    if date == d:
                        if i.email not in l_country[c]:
                            p_data = {
                                i.email: {
                                    'First Name': i.first,
                                    'Last Name': i.last,
                                }
                            }
                            l_country[c].update(p_data)
        print(l_country)
        
Attendees.run()
            
            