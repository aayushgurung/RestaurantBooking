import numpy as np
from scipy.sparse import csr_matrix
import json

with open('C:/Users/Nirajan/Desktop/python 30 days/final data for restaurant/user_item_matrix_test.json', 'r',encoding='utf-8') as f:
    reviews = json.load(f)

# reviews={
#     "15290": {
#         "Lemon Tree": 5
#     },
#     "28850": {
#         "Sukra-bar and restaurant": 4
#     },
#     "31815": {
#         "Roadhouse Cafe Pulchowk": 5,
#         "Fish Tail Lodge": 5,
#         "The Old House": 5
#     },
#     "73689": {
#         "Lumbini Invitation 365 Restaurant": 1
#     },
#     "76926": {
#         "Jatra cafe & Bar": 5
#     },
#     "92075": {
#         "Secret Garden Cafe": 4,
#         "Big Belly Restaurant": 3
#     },
#     "170260": {
#         "Rox Restaurant": 5
#     },
#     "170759": {
#         "Tukche Thakali Kitchen": 5
#     },
#     "294449": {
#         "Once Upon A Time Restaurant": 5
#     },
#     "391123": {
#         "Melrose Restaurant & Bar": 5
#     },
#     "537844": {
#         "Spize": 5
#     },
#     "887016": {
#         "Garden Kitchen Kathmandu": 4
#     },
#     "6865146": {
#         "Namanta Kitchen": 5
#     },
#     "24101976": {
#         "Roadhouse Cafe Pokhara": 4,
#         "Byanjan Restaurant": 5
#     },
#     "61913868": {
#         "Fresh Elements Restaurant": 5
#     },
#     "65611069": {
#         "Kava": 5
#     },
#     "298484535": {
#         "Rainbow Restaurant & Bar": 4
#     },
#     "913320198": {
#         "Fresh Elements Restaurant": 5
#     },
#     "parilya": {
#         "Byanjan Restaurant": 5
#     },
#     "Explorer64015381498": {
#         "Frituur No.1": 5
#     },
#     "buddhit": {
#         "Rainbow Restaurant & Bar": 3
#     },
#     "Chester_Chazzy": {
#         "Chilly Bar & Restaurant": 5
#     },
#     "P5266JMrebeccab": {
#         "Tiki Bar Pokhara": 5
#     },
#     "JohnE858": {
#         "Coffee Escape": 5
#     },
#     "SeorasWesternIsles": {
#         "Byanjan Restaurant": 5
#     },
#     "sanja_copo_96": {
#         "Chilly Bar & Restaurant": 5
#     },
#     "2054bibekg": {
#         "Fire Pizza": 5
#     },
#     "Jonas V": {
#         "Rosemary Kitchen Pokhara": 4
#     },
#     "Fanny F": {
#         "Asian Tea House": 5
#     },
#     "Balram M": {
#         "Everest view cafe": 5
#     },
#     "Shir A": {
#         "Anaki": 5
#     },
#     "Shmick15": {
#         "Black Water Restro & Bar": 5
#     },
#     "Sybille V": {
#         "Spice Garden Restaurant": 5
#     },
#     "bradyandkarlie": {
#         "Nepal Organic Cafe & Bakery": 5,
#         "Busy Bee Cafe": 4,
#         "Black & White Cafe & Restaurant": 3
#     },
#     "SwapnaC3": {
#         "Umbrella Cafe": 4
#     },
#     "colefr": {
#         "Kc's Restaurant and Bar": 5
#     },
#     "edanoren": {
#         "OR2K Pokhara": 5
#     },
#     "yveslendlpar": {
#         "Pho 99": 1
#     },
#     "disposablemitch": {
#         "Lakeside Pizzeria": 5
#     },
#     "Cas C": {
#         "Frituur No.1": 5
#     },
#     "Sharisett": {
#         "Rama's Thakali Kitchen": 4,
#         "Mitho Restaurant": 4
#     },
#     "Pioneer442812": {
#         "The Tribal Bar": 4
#     },
#     "Rina L": {
#         "Lemon Grass Restaurant": 4,
#         "Cafe Soma": 5,
#         "Lemon Tree": 2
#     },
#     "bishnurimal": {
#         "Rocksalt Grill and Bar": 5,
#         "Fresh Elements Restaurant": 5
#     },
#     "kanxu": {
#         "Silk Road Restaurant and Bar": 4,
#         "Fresh Elements Restaurant": 5,
#         "Aankhi Jhyal Restaurant and Bar": 4,
#         "Byanjan Restaurant": 5
#     },
#     "DantheMemeMan": {
#         "Artmandu": 5
#     },
#     "Deekshakap": {
#         "Roadhouse Cafe Pulchowk": 3,
#         "Kaiser Cafe": 4,
#         "Sing-Ma Food Court": 5
#     },
#     "Zeetus C": {
#         "Rainbow Restaurant & Bar": 5
#     },
#     "Amanda998": {
#         "Mezze by Roadhouse": 5
#     },
#     "Vampirebite2": {
#         "The Cafe With No Name": 5
#     },
#     "Killian C": {
#         "Deja Vu Restaurant": 5
#     },
#     "MainulAhmed": {
#         "Barista Lavazza": 5
#     },
#     "f0rces": {
#         "The Harbor Restaurant": 5
#     },
#     "Dippal123": {
#         "Hotel Dailo": 5
#     },
#     "akshattyagi": {
#         "The Maya Pub & Restaurant": 4,
#         "Once Upon A Time Restaurant": 4,
#         "The Old Lan Hua Chinese Restaurant": 5
#     },
#     "kathyaU1180QE": {
#         "Pumpernickel Bakery": 5
#     },
#     "Ting2H": {
#         "Western Tandoori & Naan House": 5
#     },
#     "flowergrg": {
#         "MarcoPolo Restaurant": 5
#     },
#     "MsKral": {
#         "Lumbini Invitation 365 Restaurant": 5
#     },
#     "Kingkrk": {
#         "Anatolia Halal Food Restaurant": 4,
#         "Bawarchi": 4
#     },
#     "kaloyank2020": {
#         "The Balcony Restaurant & Bar": 5
#     },
#     "shhadow": {
#         "De Lamar Cafe": 5
#     },
#     "DelroyAguiar": {
#         "Namaste Pub": 4,
#         "Shisha Terrace Cafe & Bar": 4
#     },
#     "wanderlustbirdy": {
#         "1905 Suites & Restaurant": 5
#     },
#     "Ioannis K": {
#         "Fewa Paradise Restaurant and Bar": 4,
#         "Once Upon A Time Restaurant": 4
#     },
#     "Marciugali": {
#         "Himalayan Arabica Beans Coffee": 4,
#         "The Old House": 4
#     },
#     "Hartrey1995": {
#         "Joy's Restaurant & Bar": 5
#     },
#     "632timn": {
#         "Greasy Spoon Restaurant": 5
#     },
#     "sop624": {
#         "Mint Cafe and Restaurant": 5
#     },
#     "Yonatan Y": {
#         "OR2K Pokhara": 5
#     },
#     "MarikenJ2": {
#         "Bamboo Bar": 5,
#         "Perky Beans": 5
#     },
#     "tomv881": {
#         "Kaiser Cafe": 3
#     },
#     "mytaufik": {
#         "Garden of Dreams - Cafe": 5
#     },
#     "KanwarTavy": {
#         "Bao Xuan - Flavours of China": 4
#     },
#     "josselink227": {
#         "Site Restaurant & Bar": 5
#     },
#     "TekTeh": {
#         "Sherpa Barista Bakery,Food & Coffee Shop": 4
#     },
#     "Mahendra M": {
#         "Top Ladder View Multi cuisine Restaurant & Bar": 5
#     },
#     "gladyslmc": {
#         "Utse Restaurant": 3
#     },
#     "cebbu2019": {
#         "Atithi Satkar Restaurant": 5
#     },
#     "kerenc2022": {
#         "Hard Rock Cafe": 5
#     },
#     "lkpoli": {
#         "Zaika": 5
#     },
#     "MeiKufman": {
#         "Byanjan Restaurant": 5
#     },
#     "Rashmi R": {
#         "Sunset view restaurant and bar": 1
#     },
#     "HydroTraveler": {
#         "Fresh Elements Restaurant": 5
#     },
#     "Eve S": {
#         "Bluebell Resto & Bar": 5
#     },
#     "wildhanias": {
#         "Japanese Kitchen Kizuna": 5,
#         "The Old Lan Hua Chinese Restaurant": 5
#     },
#     "JGCross": {
#         "The Harbor Restaurant": 5
#     },
#     "433elisabethe": {
#         "Trail's End": 5
#     },
#     "nepalidelicacies": {
#         "Trisara Pokhara": 2
#     },
#     "Ritamalpa": {
#         "Mechung Restaurant": 5
#     },
#     "robert j": {
#         "Black Olives Cafe and Bar": 4,
#         "Med5 Restaurant": 5,
#         "Northfield Cafe": 3,
#         "Byanjan Restaurant": 5,
#         "Bhojan Bhumi": 1
#     },
#     "rotemp785": {
#         "Artmandu": 5
#     },
#     "Nathaliev34": {
#         "Pokhara Thakali Kitchen": 1,
#         "Black & White Cafe & Restaurant": 4
#     },
#     "TerenceMMM": {
#         "Roadhouse Cafe Pokhara": 5
#     },
#     "Lauraendajo": {
#         "Rama's Thakali Kitchen": 4
#     },
#     "himalaia2019": {
#         "Med5 Restaurant": 5
#     },
#     "chrysalic": {
#         "Busy Bee Cafe": 5,
#         "The Harbor Restaurant": 5,
#         "Byanjan Restaurant": 5
#     },
#     "Bishal K": {
#         "Your Koseli Bakery": 5,
#         "The Classic Bamboo": 5,
#         "SUPPER Club (Dim Sum & Disco House)": 5
#     },
#     "Tanka C": {
#         "Upstairs Cafe": 5
#     },
#     "Bfaben": {
#         "Melrose Restaurant & Bar": 5
#     },
#     "MarilliM": {
#         "Western Tandoori & Naan House": 5
#     },
#     "florianed326": {
#         "Spize": 5,
#         "Upstairs Cafe": 5,
#         "Mitho Restaurant": 4,
#         "Yala Cafe": 5
#     },
#     "Chalk S": {
#         "Bricks Cafe": 5
#     },
#     "tonswinkels": {
#         "Step Up Restro and Sports Bar": 5
#     },
#     "Taylor F": {
#         "Once Upon A Time Restaurant": 4
#     },
#     "Benny B": {
#         "Kathmandu Grill Restaurant And Wine Bar": 1
#     },
#     "NareshN": {
#         "Everest Steak House Restaurant": 4
#     },
#     "Manish A": {
#         "Kava": 5
#     },
#     "647asthat": {
#         "Lavie Garden": 5
#     },
#     "ivor919": {
#         "Royal Garden Restaurant & Coffee House": 5
#     },
#     "Brynners": {
#         "Helena's": 4,
#         "Paradise Cafe and Bar": 1,
#         "Tea Time Bamboostan Cafe": 4
#     },
#     "Olly H": {
#         "Thakali Kitchen": 5
#     },
#     "Vienna2Nizza": {
#         "Tara's  Restaurant Vegetarien": 5
#     },
#     "Mayank A": {
#         "Byanjan Restaurant": 5
#     },
#     "Sevenstartravelling": {
#         "Atithi Satkar Restaurant": 5
#     },
#     "EBC2011": {
#         "Fire Pizza": 5
#     },
#     "MarjoleinP84": {
#         "Metro": 5,
#         "Hot Sandwich Corner & Cheese Shop": 5,
#         "Rosemary Kitchen Pokhara": 5,
#         "Asian Tea House": 5
#     },
#     "Goldenmax14": {
#         "Kc's Restaurant and Bar": 5
#     },
#     "Fariha F": {
#         "Monsoon Restaurant & Bar": 5
#     },
#     "Babagahnoosh": {
#         "The Harbor Restaurant": 5
#     },
#     "marcetannie187147": {
#         "Green Organic Cafe and Farmers Bar": 5
#     },
#     "Matbarbour": {
#         "Roadhouse Cafe Pokhara": 5,
#         "Boomerang Restaurant & German Bakery": 2
#     },
#     "Kael_0000": {
#         "Cafe Beyond": 5
#     },
#     "Twoxtw": {
#         "Once Upon A Time Restaurant": 4
#     },
#     "408hasane": {
#         "Shafqat Halal Food Restaurant": 5
#     },
#     "Aby_89": {
#         "Hungry Eye Restaurant & Bar": 5
#     },
#     "peteropreis2": {
#         "Cafe Mitra Restaurant & Bar": 5
#     },
#     "Neeme S": {
#         "Aniyor Veg & Vegan Restaurant": 5
#     },
#     "katejumps": {
#         "Dalo Restaurant": 5
#     },
#     "Metin_MM": {
#         "Loving Heart Vegan Restaurant": 5
#     },
#     "wasedajapanese s": {
#         "Ace Cafe": 5
#     },
#     "87sandim": {
#         "Hotel eagle eye": 5
#     },
#     "477deepikas": {
#         "Jimbu Thakali by Capital Grill - Jhamsikhel": 5
#     },
#     "Lynne M": {
#         "Hity Cafe": 5
#     },
#     "ZoeAG99": {
#         "Yala Cafe": 5
#     },
#     "Shivam M": {
#         "Bota - simply mo:mo": 1
#     },
#     "poojarijal": {
#         "Salud Cafe & Bar": 5
#     },
#     "Roger E": {
#         "La Dolce Vita": 1,
#         "Cafe De Stupa": 2
#     },
#     "theronbarc10": {
#         "The Crust Pizza & Bread": 3
#     },
#     "Prashanthexplorer": {
#         "Kausi Dreamers Terrace Cafe": 3,
#         "Reef Restaurant and Lounge Bar": 5,
#         "Avataar Cafe": 5,
#         "Momotarou Restaurant": 5
#     },
#     "gabyk573": {
#         "Vajra Restaurant & Bar": 5,
#         "Coffee In Style": 5
#     },
#     "ericfU9832HT": {
#         "Laxman Restaurant & Bar": 1
#     },
#     "Anna F": {
#         "Helena's": 5
#     },
#     "weixi z": {
#         "The Maya Pub & Restaurant": 4
#     },
#     "Roheet R": {
#         "Wok Up Thai Inspired Kitchen": 5
#     },
#     "nepal b": {
#         "Roadhouse Cafe Boudha": 5
#     },
#     "SchmidtShow": {
#         "Maya Cocktail Bar": 4
#     },
#     "Binay A": {
#         "Dechenling Garden Restaurant": 5,
#         "Alice Restaurant Group": 5
#     },
#     "Kunsanglopchan7": {
#         "Monkey Temple Restro And Bar": 5
#     },
#     "Nabin D": {
#         "TipTop": 4,
#         "Hot Breads": 4,
#         "Daawat Indian Cuisine Restaurant": 5,
#         "Jacob's Cafe": 4,
#         "El Bocaíto Español": 4,
#         "Cafe dorje lakpa": 5,
#         "Northfield Cafe": 4
#     },
#     "AnonyJenny": {
#         "La Dolce Vita": 5,
#         "Bro Bakery": 4,
#         "Lavie Garden": 5
#     },
#     "roddy m": {
#         "Funky Buddha Kathmandu": 5
#     },
#     "SN_1211": {
#         "Metro": 4,
#         "Thamel Momo Hut": 4,
#         "Electric Pagoda Bar/Cafe": 4
#     },
#     "nativetea": {
#         "Moksh": 4,
#         "Hankook Sarang Korean Restaurant": 5
#     },
#     "SPA01": {
#         "Green Organic Cafe and Farmers Bar": 5,
#         "Punjabi Restaurant": 1,
#         "Black Olives Cafe and Bar": 4
#     },
#     "Jason K": {
#         "Momo Mazza": 5
#     },
#     "Jonas-Sera": {
#         "Roadhouse Cafe Pokhara": 5
#     },
#     "aayush_mainali": {
#         "Level 3 Terraces": 1
#     },
#     "mallika123": {
#         "Revolution Cafe & Restaurant": 5
#     },
#     "sallythode": {
#         "Coffee Pasal": 5,
#         "am:pm cafe": 5,
#         "Rosemary Kitchen Pokhara": 5,
#         "Tara's  Restaurant Vegetarien": 5
#     },
#     "asimk208": {
#         "Mezze by Roadhouse": 4,
#         "Anatolia Halal Food Restaurant": 2
#     },
#     "481catherynl": {
#         "Fresh Elements Restaurant": 5
#     },
#     "Jim P": {
#         "Mint Cafe and Restaurant": 5
#     },
#     "Shailesh530": {
#         "Dunatapari Restaurant": 4
#     },
#     "jennlow43": {
#         "Mul Chowk Restaurant": 4,
#         "The Lazy Gringo": 4,
#         "Chez Caroline": 5
#     },
#     "Vikas S": {
#         "Byanjan Restaurant": 5
#     },
#     "Nitin J": {
#         "Mezze by Roadhouse": 4
#     },
#     "redbeef2019": {
#         "Phat Kath": 5
#     },
#     "Marv1981": {
#         "Hovoli": 5
#     },
#     "amrit t": {
#         "Spice Garden Restaurant": 5,
#         "Olive Cafe": 5,
#         "Dorje's Bar & Grill": 5,
#         "Western Tandoori & Naan House": 4,
#         "Teafresho": 5
#     },
#     "Yehuda R": {
#         "Olive Cafe": 2
#     },
#     "Silver8938": {
#         "Loving Heart Vegan Restaurant": 2
#     },
#     "kshatriyaL": {
#         "Dr Espresso": 5
#     },
#     "YNNYN": {
#         "French Bakery kathmandu": 3,
#         "Phat Kath": 5
#     },
#     "ayalw2017": {
#         "Raithaane": 5
#     },
#     "SluggerOToole": {
#         "The Maya Pub & Restaurant": 4
#     },
#     "Alpine N": {
#         "Bhojan Bhumi": 5
#     },
#     "FamilienOlesen4": {
#         "Metro": 5,
#         "Samay Baji": 5,
#         "Perky Beans": 4,
#         "Thamel Momo Hut": 3,
#         "OR2K Pokhara": 4,
#         "The Harbor Restaurant": 4,
#         "Kc's Restaurant and Bar": 5
#     },
#     "rupak2019": {
#         "Nepalaya Rooftop Restaurant": 5
#     },
#     "dawatembas2020": {
#         "Cafe De Imja Tse & Bakery": 5
#     },
#     "Raumbegrenzer": {
#         "D & D Cafe": 2
#     },
#     "Arun F": {
#         "Roots bar": 5
#     },
#     "DBruce24": {
#         "The Vesper House": 5
#     },
#     "Aasiya R": {
#         "The Garuda Bar": 5,
#         "Downtown Pub & Grill": 5
#     },
#     "Skyoverlord": {
#         "Byanjan Restaurant": 5
#     },
#     "nehalbkt": {
#         "Downtown Pub & Grill": 5,
#         "Koyla Lounge & Cafe - Pokhara": 2,
#         "Genesis Cafe": 5,
#         "Sky High": 1,
#         "Mul Chowk Restaurant": 2,
#         "The Maya Pub & Restaurant": 5,
#         "The Old House": 5
#     },
#     "Anne D": {
#         "Saigon Pho": 5
#     },
#     "SUJATA S": {
#         "KGH Dream Garden Restaurant": 5
#     },
#     "rajubhatta": {
#         "Atithi Satkar Restaurant": 5
#     },
#     "Rozen R": {
#         "Thamel Restaurant": 5
#     },
#     "KirstyW1241": {
#         "am:pm cafe": 5,
#         "The Maya Pub & Restaurant": 4
#     },
#     "869avishekm": {
#         "Tibetan Pema Restaurant": 2,
#         "Bubble Tea & More": 5,
#         "Kc's Restaurant and Bar": 3
#     },
#     "kalsangt2023": {
#         "Raksi Music Bar": 5
#     },
#     "Enthousiast": {
#         "Newa Chhen Restaurant": 5
#     },
#     "Journey43742393957": {
#         "Spize": 5
#     },
#     "Rooney_blue": {
#         "Tea Time Bamboostan Cafe": 5
#     },
#     "Peter_Clare_50": {
#         "Veg MO MO Restaurant": 4,
#         "Utse Restaurant": 4,
#         "K-Too Beer & Steakhouse": 3
#     },
#     "jnfblumm": {
#         "The Garuda Bar": 5
#     },
#     "Bruce98765": {
#         "Manjusha cafe": 5
#     },
#     "Puskal L": {
#         "Mountain Steak House Restaurant": 5
#     },
#     "ric_ant0": {
#         "Upstairs Cafe": 5,
#         "Boudha Stupa Restaurant & cafe": 5
#     },
#     "Jan L": {
#         "Hotel Florid Nepal": 4,
#         "am:pm cafe": 5,
#         "Perky Beans": 5,
#         "Gaia Holiday Home Restaurant": 4
#     },
#     "PhilandDi-Matira": {
#         "Boomerang Restaurant & German Bakery": 4
#     },
#     "kjayhay": {
#         "Casa Mexicana Kathmandu (MEXICAN FOOD)": 5,
#         "Melrose Restaurant & Bar": 5
#     },
#     "Wayne A": {
#         "Thamel Momo Hut": 4
#     },
#     "Shiiriin": {
#         "Evoke Cafe & Bistro": 4
#     },
#     "True_Blue_Iowan": {
#         "Hotel Mandap": 1,
#         "Metro": 5,
#         "French Bakery kathmandu": 5,
#         "Olive Cafe": 5,
#         "La Dolce Vita": 4,
#         "Doubleview restaurant & Bar": 5,
#         "Aankhi Jhyal Restaurant and Bar": 5,
#         "Northfield Cafe": 5
#     },
#     "Lush018": {
#         "Olive Cafe": 4
#     },
#     "JordanKelly91": {
#         "Cafe B.K.'s Place": 5
#     },
#     "436elizabetho": {
#         "The Juicery Cafe": 5
#     },
#     "soumayyal": {
#         "Lazeez": 5
#     },
#     "yumpyk": {
#         "Saffron Restaurant & Bar": 5
#     },
#     "829rizwana": {
#         "Nepalaya Rooftop Restaurant": 5
#     },
#     "Kami1973": {
#         "The Harbor Restaurant": 4,
#         "Kc's Restaurant and Bar": 5
#     },
#     "keithtpassmore": {
#         "The Harbor Restaurant": 5
#     },
#     "Fee_and_Floyd": {
#         "Top of the World Coffee": 4
#     },
#     "perth08Perth": {
#         "Pokhara Thakali Kitchen": 4,
#         "Olive Cafe": 3,
#         "Byanjan Restaurant": 5,
#         "Boomerang Restaurant & German Bakery": 3
#     },
#     "95dilshan": {
#         "El Bocaíto Español": 5
#     },
#     "mahesht398": {
#         "Kulung Kitchen": 5
#     },
#     "Katrina D": {
#         "Hot Breads - Curry Kitchen": 1
#     },
#     "M7789OFnicolasc": {
#         "Rest Point Cafe & Bar": 5
#     },
#     "D L": {
#         "Rosemary Kitchen Pokhara": 5
#     },
#     "threeninefour": {
#         "Al Bait Thakali Kitchen": 5
#     },
#     "Elena1Prekrasna9": {
#         "Green Organic Cafe and Farmers Bar": 5,
#         "OR2K Pokhara": 5
#     },
#     "Sarah_and_Oli": {
#         "Om Dhuri Gallery Live Cafe": 5
#     },
#     "458saskiab": {
#         "The Factory": 1
#     },
#     "rrl_ukgal": {
#         "La Dolce Vita": 4
#     },
#     "mickfingers": {
#         "Jatra cafe & Bar": 5
#     },
#     "Nahiyan N": {
#         "Fresh Elements Restaurant": 5
#     },
#     "brandbuildernepal": {
#         "Frituur No.1": 5
#     },
#     "SarahAgnesE": {
#         "Sukra-bar and restaurant": 5
#     },
#     "Beth G": {
#         "H2O Cafe N Pub": 5,
#         "Eco Garden Restaurant": 5,
#         "The Hub": 5,
#         "Black & White Cafe & Restaurant": 5
#     },
#     "InaMariaBarbara": {
#         "Nepali Chulo": 5,
#         "Casa Pagoda": 5,
#         "Hotel Manaslu Pvt. Ltd.": 4,
#         "Kaiser Cafe": 5
#     },
#     "CaritoT23": {
#         "Revolution Cafe & Restaurant": 5
#     },
#     "d1anaspell": {
#         "Alpine Lodge": 5
#     },
#     "Matthew J": {
#         "Asian Tea House": 5
#     },
#     "amitshtc": {
#         "Barista Lavazza": 1
#     },
#     "jsheehan130": {
#         "Med5 Restaurant": 5,
#         "Bon Appetit Cafe and Restaurant": 4
#     },
#     "Vassil_Spasov": {
#         "The Hub": 5
#     },
#     "Abhijeet_gehlot": {
#         "Sukra-bar and restaurant": 5
#     },
#     "Withlilygrace": {
#         "French Bakery kathmandu": 5
#     },
#     "stupifiedsnitch": {
#         "Edamame": 5,
#         "Roadhouse Cafe Pokhara": 5
#     },
#     "VincentP279": {
#         "Electric Pagoda Bar/Cafe": 4
#     },
#     "Hilde T": {
#         "Cafe Swotha": 5
#     },
#     "Slersh": {
#         "Hotel Mandap": 4
#     },
#     "mmeroyale79": {
#         "Northfield Cafe": 4
#     },
#     "J99AKmariac": {
#         "Kathmandu Grill Restaurant And Wine Bar": 5
#     },
#     "sp l": {
#         "Garden Kitchen Kathmandu": 5
#     },
#     "moodysujip": {
#         "Lama Kudap Restaurant": 5
#     },
#     "Sadrul_Tusher": {
#         "Northfield Cafe": 5,
#         "La Thamel Brasserie Pvt. Ltd": 5
#     },
#     "Blondefool": {
#         "K-Too Beer & Steakhouse": 4
#     },
#     "NicolaJT23": {
#         "Black Olives Cafe and Bar": 5
#     },
#     "Jueanne T": {
#         "Himali farmers kitchen": 4
#     },
#     "Bec M": {
#         "Funky Buddha Kathmandu": 5
#     },
#     "kdan2019": {
#         "Spize": 5
#     },
#     "Explore44904930997": {
#         "Melrose Restaurant & Bar": 5
#     },
#     "Myanmartraveler": {
#         "Utopia Garden & Snacks Bar,": 5
#     },
#     "Jasmine T": {
#         "Deja Vu Restaurant": 5
#     },
#     "Fuadango": {
#         "Pokhara Halal Food Land": 2
#     },
#     "LCLB24": {
#         "Hot Sandwich Corner & Cheese Shop": 5,
#         "Mo2's Delights Pokhara": 5,
#         "Med5 Restaurant": 5
#     },
#     "Martin R": {
#         "Thakali Kitchen": 5,
#         "Dhokaima Cafe": 4
#     },
#     "Manray4619": {
#         "Yala Cafe": 5
#     },
#     "susielyly": {
#         "Norling Restaurant & Guest House": 4
#     },
#     "shresthadurga": {
#         "Big Belly Restaurant": 5,
#         "Kaya's Kitchen": 5
#     },
#     "676amarm": {
#         "Mint Cafe And Tandoori House": 5
#     },
#     "208daisyj": {
#         "OR2K Pokhara": 5
#     },
#     "ghostr713": {
#         "Roadhouse Cafe Boudha": 5
#     },
#     "amarb612": {
#         "Spize": 5
#     },
#     "leonief300": {
#         "The Cafe With No Name": 5
#     },
#     "Max B": {
#         "Chilly Bar & Restaurant": 5
#     },
#     "ismailsuboh": {
#         "Kava": 5
#     },
#     "Johnneek": {
#         "Du Chhuk Ken": 5
#     },
#     "Chili909": {
#         "Hungry Bite Burguer Corner": 5,
#         "Thamel Cave Kitchen": 5,
#         "The Cafe With No Name": 5,
#         "New Marwari Restaurant": 5,
#         "Chikusa Cafe": 5,
#         "Utse Restaurant": 5
#     },
#     "GajalAT123": {
#         "City Square Banquet & Restaurant": 1
#     },
#     "saffronpixi": {
#         "Garden of Dreams - Cafe": 5
#     },
#     "mikkelrobin": {
#         "Freak Street Kaffe": 5
#     },
#     "banmayank": {
#         "Paleti Bhanchha Ghar Restaurant & Bar": 5
#     },
#     "HETTNepal": {
#         "Peaceful Restaurant": 5
#     },
#     "gudmen": {
#         "La Dolce Vita": 5
#     },
#     "dill564": {
#         "Natssul": 5
#     },
#     "Gwarcha": {
#         "Oliva Cafe": 4
#     },
#     "Sanokanchi": {
#         "Revolution Cafe & Restaurant": 5,
#         "Little Buddha Restaurant & Bar": 4
#     },
#     "tibo e": {
#         "Hot Sandwich Corner & Cheese Shop": 5
#     },
#     "Gil Z": {
#         "Curilo": 5
#     },
#     "Efrat W": {
#         "Mo2's Delights Pokhara": 5
#     },
#     "in_sl373": {
#         "Melrose Restaurant & Bar": 5
#     },
#     "Avalon W": {
#         "French Bakery kathmandu": 5
#     },
#     "wanakaramea": {
#         "Nanglo West": 1,
#         "Nepal Organic Coffee Shop": 5
#     },
#     "J D": {
#         "Sam's One Tree Cafe": 5,
#         "Tukche Thakali Kitchen": 5,
#         "Yala Cafe": 5
#     },
#     "atit g": {
#         "Atithi Satkar Restaurant": 5
#     },
#     "brunod250": {
#         "La Dolce Vita": 4
#     },
#     "406cbd": {
#         "Everest Burger & Steak House": 5
#     },
#     "hopemak": {
#         "Get Together": 5
#     },
#     "Rachel M": {
#         "Bamboo Bar": 5,
#         "Lemon Tree": 5
#     },
#     "suchhaiyebath": {
#         "Al Madina Halal Foods": 4
#     },
#     "Anusha2076": {
#         "MarcoPolo Restaurant": 5
#     },
#     "Jny t": {
#         "Hot Sandwich Corner & Cheese Shop": 5,
#         "Perky Beans": 3
#     },
#     "Bikram B": {
#         "Embassy Restaurant and Bar": 5,
#         "Roadhouse Pizzeria": 5
#     },
#     "ghochuofn": {
#         "Royal Mithila Food Palace": 5
#     },
#     "jcdcitadel": {
#         "Freshpresso Coffee Bar": 5
#     },
#     "GSexton": {
#         "Busy Bee Cafe": 4,
#         "Third Eye Restaurant": 5,
#         "K-Too Beer & Steakhouse": 1
#     },
#     "gigichou": {
#         "Once Upon A Time Restaurant": 4
#     },
#     "Gieg": {
#         "Peaceful Restaurant": 4,
#         "Frituur No.1": 5
#     },
#     "Ashwingupta": {
#         "Punjabi Restaurant": 4,
#         "Revolving Restaurant": 1
#     },
#     "N794EKdaveb": {
#         "The Cafe With No Name": 5
#     },
#     "888kedark": {
#         "Kaya's Kitchen": 5
#     },
#     "Arcche": {
#         "Genesis Cafe": 5
#     },
#     "Mattwhitepaint": {
#         "Electric Pagoda Bar/Cafe": 5
#     },
#     "lafermata2018": {
#         "Olive Cafe": 5,
#         "Rolling Stones Rock Bar": 5
#     },
#     "BladeApprentice": {
#         "am:pm cafe": 5
#     },
#     "GHUMANTE_KB": {
#         "Lime and Lemon Lounge cafe Bharatpur": 5
#     },
#     "jonsY5494LO": {
#         "Revolution Cafe & Restaurant": 5
#     },
#     "김 민": {
#         "Sarang": 5
#     },
#     "amsterdam05": {
#         "Nepali Kitchen": 4,
#         "Hill Top Restaurat": 4,
#         "Lotus Restaurant": 3,
#         "Rameshwaram Sweets and Snacks": 3,
#         "Mo2's Delights Pokhara": 3,
#         "Naulo Restaurant": 3,
#         "Hamlet Restaurant": 3,
#         "Utopia Garden & Snacks Bar,": 4,
#         "Canova Cafe": 4,
#         "Falcha Cafe": 3
#     },
#     "NinaHen3217": {
#         "Garden Kitchen Kathmandu": 4
#     },
#     "Lisa P": {
#         "Hungry Eye Restaurant & Bar": 5
#     },
#     "Kashish C": {
#         "Momotarou Japanese Restaurant": 5
#     },
#     "ankurg21": {
#         "The Juicery Cafe": 2
#     },
#     "Chiara A": {
#         "Roadhouse Cafe Pokhara": 5,
#         "Third Eye Restaurant": 5
#     },
#     "945samikshyat": {
#         "Yala Cafe": 5
#     },
#     "Robin M": {
#         "Gilingche": 5
#     },
#     "43buffyg": {
#         "Pumpernickel Bakery": 4,
#         "Royal Garden Restaurant & Coffee House": 4
#     },
#     "abishekb2020": {
#         "Byanjan Restaurant": 5
#     },
#     "maratz_smb": {
#         "Roadhouse Cafe Pokhara": 5,
#         "Roadhouse Cafe Boudha": 5,
#         "Shantiko Kitchen": 5
#     },
#     "metalaarif": {
#         "Koyla Lounge & Cafe - Pokhara": 4,
#         "Le Mirch Kathmandu": 5
#     },
#     "korinat2016": {
#         "Hello Kitty Restaurant": 5
#     },
#     "Andalib H": {
#         "Busy Bee Cafe": 5
#     },
#     "234prismm": {
#         "Won Korean Restaurant": 5
#     },
#     "Eleesia": {
#         "Rise & Grind Coffee": 5
#     },
#     "Umesh S": {
#         "Mount Everest Arirang Korean Cafe & Restaurant": 5
#     },
#     "Zahyan S": {
#         "French Bakery kathmandu": 5,
#         "Taza": 5,
#         "The Lazy Gringo": 5,
#         "Ghangri Cafe": 5
#     },
#     "447zulkarnaina": {
#         "Taza": 5
#     },
#     "laxman2018": {
#         "Sukra-bar and restaurant": 5,
#         "Black & White Cafe & Restaurant": 2
#     },
#     "Sabindh": {
#         "Horizon Garden Restaurant": 5
#     },
#     "prince j": {
#         "El Dorado Avenue, Butwal": 5
#     },
#     "Stéfan B": {
#         "Mint Cafe And Tandoori House": 5,
#         "Mint Cafe and Restaurant": 5
#     },
#     "SarinaNapit0369": {
#         "MarcoPolo Restaurant": 5
#     },
#     "2015ashah": {
#         "OR2K Pokhara": 5
#     },
#     "welsh_matt79": {
#         "Green Organic Cafe and Farmers Bar": 5
#     },
#     "samcL3298PB": {
#         "Coffee With Menz": 4,
#         "Little Buddha Restaurant & Bar": 2
#     },
#     "OhriTours": {
#         "Spize": 5,
#         "Daily Caffeine House": 5
#     },
#     "DreandKaren": {
#         "The Kabab King": 5
#     },
#     "deejaypeebee": {
#         "am:pm cafe": 4
#     },
#     "raylim78": {
#         "La Dolce Vita": 4
#     },
#     "AsisBandyopadhyay": {
#         "Kakori": 5,
#         "Byanjan Restaurant": 5,
#         "The Old Lan Hua Chinese Restaurant": 5
#     },
#     "Willy P": {
#         "The Maya Pub & Restaurant": 5
#     },
#     "IntoTheWorldUK": {
#         "Gokarna House Restaurant": 3,
#         "Third Eye Restaurant": 4,
#         "The Harbor Restaurant": 4,
#         "Hungry Eye Restaurant & Bar": 3
#     },
#     "alextX4302LE": {
#         "Art Cafe": 5
#     },
#     "willh446": {
#         "Monsoon Restaurant & Bar": 4,
#         "Chilly Bar & Restaurant": 5,
#         "Rosemary Kitchen Pokhara": 5,
#         "Byanjan Restaurant": 5
#     },
#     "OblongLW": {
#         "The Blind Tiger": 5
#     },
#     "bigyans2019": {
#         "Upstairs Cafe": 5
#     },
#     "Jasmine_0007": {
#         "The Juicery Cafe": 5
#     },
#     "dhondupg2022": {
#         "Ananda Tree House Cafe": 5
#     },
#     "Adva R": {
#         "El Bocaíto Español": 5,
#         "Tea Time Bamboostan Cafe": 5
#     },
#     "Christopher d": {
#         "Queen Forest Restro - Bar": 5
#     },
#     "Ashley H": {
#         "Nir's Toast Bakery & Restaurant": 5,
#         "G Cafe": 2
#     }}

users = list(reviews.keys())
restaurants = sorted(set.union(*[set(r.keys()) for r in reviews.values()]))

user_ratings = []
for user in users:
    row = []
    for restaurant in restaurants:
        if restaurant in reviews[user]:
            row.append(reviews[user][restaurant])
        else:
            row.append(0)
    user_ratings.append(row)

user_ratings_sparse = csr_matrix(user_ratings)
print(user_ratings_sparse)

# Compute cosine similarity
def cosine_similarity(a, b):
    dot_product = a.dot(b.T).toarray()[0][0]
    norm_a = np.linalg.norm(a.toarray())
    norm_b = np.linalg.norm(b.toarray())
    return dot_product / (norm_a * norm_b)

cosine_similarities = np.zeros((len(users), len(users)))
for i in range(len(users)):
    for j in range(i+1, len(users)):
        similarity = cosine_similarity(user_ratings_sparse.getrow(i), user_ratings_sparse.getrow(j))
        cosine_similarities[i][j] = similarity
        cosine_similarities[j][i] = similarity

print(cosine_similarities)
cosine_similarities_list = cosine_similarities.tolist()
with open('C:/TEST FINAL YEAR/cosine.json', 'w', encoding='utf-8') as f:
    json.dump(cosine_similarities_list, f)
