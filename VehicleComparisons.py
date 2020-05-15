#!c:/python/python.exe
print('Content-type: text/html\n\n')

### imports ###
from selenium import webdriver
from selenium.webdriver.chrome.options import Options 
import time
from bs4 import BeautifulSoup

###########################################################
options = webdriver.ChromeOptions()
prefs = {"download.default_directory":  "C:/New_Download"}
options.add_experimental_option("prefs", prefs)

# using webdriver to control browser UI
browser = webdriver.Chrome('c:/chromedriver.exe',chrome_options=options)
#################################################
browser.set_window_position(-150,-150)
browser.set_window_size(10,10)


#open a csv file to record information
file = open('vehicles.csv', 'w', encoding="utf-8")
#################################################

#
###*** Retrieving data for Toyota vehicles ***###
#

browser.get('https://www.toyota.ca/toyota/en/build-price')
time.sleep(3)

html = browser.page_source
soup = BeautifulSoup(html,'html.parser')
soup.prettify()

try:
    
    name = soup.find_all('h4',{'class':'vehicle-grid-header'})
    price = (soup.find_all('span',{'class':'from-price'}))
    pic = soup.find_all('div',{"class":"responsive-image spinner-medium-blue ng-isolate-scope"})

    vehicles = []
    for n in name:
        vehicles.append(n.text)

    index1 = vehicles.index('Cars')
    index2 = vehicles.index('Hybrids')
    index3 = vehicles.index('SUVs & Minivans')
    index4 = vehicles.index('Trucks')
    index5 = vehicles.index('Future Vehicles')

    toyota_cars = list(vehicles[(index1+1):index2])
    toyota_hybrids = list(vehicles[(index2+1):index3])
    toyota_suvs = list(vehicles[(index3+1):index4])
    toyota_trucks = list(vehicles[(index4+1):index5])
    
    prices = []
    for prc in price:
        toyota_price = (prc.text).strip()
        toyota_price = toyota_price.strip('From ')
        toyota_price = toyota_price.strip('*')
        prices.append(toyota_price.replace(',',''))
    
    toyota_car_prices = list(prices[(index1+1):index2])
    toyota_hybrid_prices = list(prices[(index2+1):index3])
    toyota_suv_prices = list(prices[(index3+1):index4])
    toyota_truck_prices = list(prices[(index4+1):index5])

    img_list = []

    for pics in pic:
        img_list.append(pics.img.get('src'))
    
    toyota_car_pic = img_list[(index1+1):index2]
    toyota_hybrid_pic = img_list[(index2+1):index3]
    toyota_suv_pic = img_list[(index3+1):index4]
    toyota_truck_pic = img_list[(index4+1):index5]
    
except TimeoutError:
    print ("Timed out paage load.")


#
###*** Retrieving data for Honda vehicles ***###
#

browser.get('https://www.honda.ca/buildyourhonda?returnUrl=true#/models')

#make the parser wait until the webpage is loaded
time.sleep(3)

html_honda = browser.page_source
soup_honda = BeautifulSoup(html_honda,'html.parser')
soup_honda.prettify()

try:    
    name_honda = soup_honda.find_all('h3',{'class':"Model__ModelName-sc-1p5xzwi-5 dsUnZa"})
    price_honda = (soup_honda.find_all('div',{'class':"PriceWithTooltip__Amount-sc-1fpsh67-2 fhLVq"}))
    pic_honda = soup_honda.find_all('img',{"class":"Image-aggy6x-0 cgdXKF"})
    
    edit_names=[]
    for edit in name_honda:
        edit_names.append(edit.text)
    
    indx1 = edit_names.index('2020 HR-V')
    indx2 = edit_names.index('2020 Accord Hybrid')
    indx3 = edit_names.index('2020 Ridgeline')

    #listing Honda Vehicles by category
    honda_cars = edit_names[:indx1]
    honda_hybrids = edit_names[indx2:indx1]
    honda_suvs = edit_names[indx1:indx3]
    honda_trucks = edit_names[indx3:]

    edit_price = []
    for prc in price_honda:
        prc = prc.text
        prc = prc.replace(',','')
        edit_price.append(prc.replace('.00',''))
    
    honda_cars_price = edit_price[:indx1]
    honda_hybrids_price = edit_price[indx2:indx1]
    honda_suvs_price = edit_price[indx1:indx3]
    honda_trucks_price = edit_price[indx3:]

    
    edit_pics = []
    for images in pic_honda:
        edit_pics.append(images.get('src'))
    
    honda_cars_img = edit_pics[:indx1]
    honda_hybrids_img = edit_pics[indx2:indx1]
    honda_suvs_img = edit_pics[indx1:indx3]
    honda_trucks_img = edit_pics[indx3:]
    
except TimeoutError:
    print ("Timed out paage load.")

#
###*** Retrieving data for Nissan vehicles ***###
#

browser.get('https://www.nissan.ca/shopping-tools/build-price.html')
time.sleep(3)

html_nissan = browser.page_source
soup_nissan = BeautifulSoup(html_nissan,'html.parser')


try:
    
    name_nissan = soup_nissan.find_all('h3',{'class':'car-title'})
    price_nissan = (soup_nissan.find_all('div',{'class':'price-item primary-price'}))
    pic_nissan = soup_nissan.find_all('picture', {"class":"picture-element analytics-target"})

    name_list = []
    for v in name_nissan:
        name_list.append((v.a.text).strip())

    nissan_cars = name_list[:7]
    nissan_hybrid = name_list[4]
    nissan_suv = name_list[7:13]
    nissan_trucks = name_list[13:18]

    price_list = []
    for prc in price_nissan:
        final_price = ((prc.text).strip()).strip("Starting at")
        final_price = (final_price).strip()
        price_list.append((final_price).replace(',',''))
    
    nissan_cars_price = price_list[:7]
    nissan_hybrid_price = price_list[4]
    nissan_suv_price = price_list[7:13]
    nissan_trucks_price = price_list[13:18]
    
    img_list = []
    for img in pic_nissan:
        img_list.append("https://www.nissan.ca/"+img.img['src'])
    
    nissan_cars_img = img_list[:7]
    nissan_hybrid_img = img_list[4]
    nissan_suv_img = img_list[7:13]
    nissan_trucks_img = img_list[13:18]
    
    
except TimeoutError:
    print ("Timed out page load.")
finally:
    browser.quit()
    

### writing to CSV file ###

try:
    #Cars#
    file.write("Cars\n")

    file.write("\nToyota\n")
    for tc,tp,ti in zip(toyota_cars,toyota_car_prices,toyota_car_pic):
        file.write(str(tc)+','+str(tp)+','+str(ti)+'\n')
    
    file.write("\nHonda\n")
    for hc,hp,hi in zip(honda_cars,honda_cars_price,honda_cars_img):
        file.write(str(hc)+','+str(hp)+','+str(hi)+'\n')

    file.write("\nNissan\n") 
    for nc,np,ni in zip(nissan_cars,nissan_cars_price,nissan_cars_img):
        file.write(str(nc)+','+str(np)+','+str(ni)+'\n')
    
    
    #Hybrids&Electrics
    file.write("\n\nHybrids and ELectrics\n")

    file.write("\nToyota\n")
    for thc,thp,thi in zip(toyota_hybrids,toyota_hybrid_prices,toyota_hybrid_pic):
        file.write(str(thc)+','+str(thp)+','+str(thi)+'\n')
    
    file.write("\nHonda\n")
    for hhc,hhp,hhi in zip(honda_hybrids,honda_hybrids_price,honda_hybrids_img):
        file.write(str(hhc)+','+str(hhp)+','+str(hhi)+'\n')

    file.write("\nNissan\n") 
    file.write(str(nissan_hybrid)+','+str(nissan_hybrid_price)+','+str(nissan_hybrid_img)+'\n')
    
    #SUV & Vans#
    file.write("\n\nSUV and Vans\n")

    file.write("\nToyota\n")
    for tsc,tsp,tsi in zip(toyota_suvs,toyota_suv_prices,toyota_suv_pic):
        file.write(str(tsc)+','+str(tsp)+','+str(tsi)+'\n')
    
    file.write("\nHonda\n")
    for hsc,hsp,hsi in zip(honda_suvs,honda_suvs_price ,honda_suvs_img):
        file.write(str(hsc)+','+str(hsp)+','+str(hsi)+'\n')

    file.write("\nNissan\n") 
    for nsc,nsp,nsi in zip(nissan_suv,nissan_suv_price,nissan_suv_img):
        file.write(str(nsc)+','+str(nsp)+','+str(nsi)+'\n')

    #Trucks#
    file.write("\n\nTrucks\n")

    file.write("\nToyota\n")
    for ttc,ttp,tti in zip(toyota_trucks,toyota_truck_prices,toyota_truck_pic):
        file.write(str(ttc)+','+str(ttp)+','+str(tti)+'\n')
    
    file.write("\nHonda\n")
    for htc,htp,hti in zip(honda_trucks,honda_trucks_price,honda_trucks_img):
        file.write(str(htc)+','+str(htp)+','+str(hti)+'\n')

    file.write("\nNissan\n") 
    for ntc,ntp,nti in zip(nissan_trucks,nissan_trucks_price,nissan_trucks_img):
        file.write(str(ntc)+','+str(ntp)+','+str(nti)+'\n')
    
    
except Exception:
    print(Exception.with_traceback)

finally: 
    file.close()


############################################################
#                    Web Display                           #
############################################################



width = '100px'
height = '70px'

print('''
    <script>
        function showImg() {
            if (document.getElementById("vehicles").value == "car") {
                document.getElementById("category").innerHTML = "Cars";
                document.getElementById("t_cars").style.display = "block";
                document.getElementById("h_cars").style.display = "block";
                document.getElementById("n_cars").style.display = "block";
                document.getElementById("t_suvs").style.display = "none";
                document.getElementById("h_suvs").style.display = "none";
                document.getElementById("n_suvs").style.display = "none";
                document.getElementById("t_hybrids").style.display = "none";
                document.getElementById("h_hybrids").style.display = "none";
                document.getElementById("n_hybrids").style.display = "none";
                document.getElementById("t_trucks").style.display = "none";
                document.getElementById("h_trucks").style.display = "none";
                document.getElementById("n_trucks").style.display = "none";
            }
            else if (document.getElementById("vehicles").value == "suv") {
                document.getElementById("category").innerHTML = "SUV & VANs";
                document.getElementById("t_suvs").style.display = "block";
                document.getElementById("h_suvs").style.display = "block";
                document.getElementById("n_suvs").style.display = "block"
                document.getElementById("t_cars").style.display = "none";
                document.getElementById("h_cars").style.display = "none";
                document.getElementById("n_cars").style.display = "none";
                document.getElementById("t_hybrids").style.display = "none";
                document.getElementById("h_hybrids").style.display = "none";
                document.getElementById("n_hybrids").style.display = "none";
                document.getElementById("t_trucks").style.display = "none";
                document.getElementById("h_trucks").style.display = "none";
                document.getElementById("n_trucks").style.display = "none";
            }
            else if (document.getElementById("vehicles").value == "hybrid") {
                document.getElementById("category").innerHTML = "Hybrids";
                document.getElementById("t_hybrids").style.display = "block";
                document.getElementById("h_hybrids").style.display = "block";
                document.getElementById("n_hybrids").style.display = "block";
                document.getElementById("t_suvs").style.display = "none";
                document.getElementById("h_suvs").style.display = "none";
                document.getElementById("n_suvs").style.display = "none";
                document.getElementById("t_cars").style.display = "none";
                document.getElementById("h_cars").style.display = "none";
                document.getElementById("n_cars").style.display = "none";
                document.getElementById("t_trucks").style.display = "none";
                document.getElementById("h_trucks").style.display = "none";
                document.getElementById("n_trucks").style.display = "none";
            }
            else if (document.getElementById("vehicles").value == "trucks") {
                document.getElementById("category").innerHTML = "Trucks";
                document.getElementById("t_trucks").style.display = "block";
                document.getElementById("h_trucks").style.display = "block";
                document.getElementById("n_trucks").style.display = "block";
                document.getElementById("t_suvs").style.display = "none";
                document.getElementById("h_suvs").style.display = "none";
                document.getElementById("n_suvs").style.display = "none";
                document.getElementById("t_hybrids").style.display = "none";
                document.getElementById("h_hybrids").style.display = "none";
                document.getElementById("n_hybrids").style.display = "none";
                document.getElementById("t_cars").style.display = "none";
                document.getElementById("h_cars").style.display = "none";
                document.getElementById("n_cars").style.display = "none";
            }
        }
    </script>
        
    <div id='results' style="width:98%; margin:auto; text-align:center;">
        <div width=100%>
            <h1>Vehicle Comparisons for Toyota, Honda and Nissan</h1>
        <div width=100%>
        
        <div width=100%>
            <form>
                <label for="vehicles"><h3>Select the category of Vehicle to compare prices:</h3></label>
                <select name="vehicles" id="vehicles" onchange="showImg()" style="font-size:20px;">
                    <option value="car">Cars</option>
                    <option value="suv">SUV & Vans</option>
                    <option value="hybrid">Hybrids</option>
                    <option value="trucks">Trucks</option>
                </select>
                
            </form>
        </div>
        <div width=100%>
            <h2 id="category"></h2>
        </div>
        <div style=" width:100%;text-align: center;">
            <div id='toyota' style='width:30%;float:left'>
                <h3>Toyota</h3>
                <div id='t_cars' style='display:block; width:95%;'>
                    <table border=1 width="100%">
                    ''')
for tc,tp,ti in zip(toyota_cars,toyota_car_prices,toyota_car_pic):
    print("<tr>")
    print("<td>",tc,"</td>","<td>",tp,"</td>","<td><img src='",ti,"' width='",width,"' height='",height,"'/></td>")
    print("</tr>")
print('''           </table>
                </div>
                <div id='t_suvs' style='display:none;width:95%;'>
                    <table border=1 width='100%'>
                    ''')

for tsc,tsp,tsi in zip(toyota_suvs,toyota_suv_prices,toyota_suv_pic):
    print("<tr>")
    print("<td>",tsc,"</td>","<td>",tsp,"</td>","<td><img src='",tsi,"' width='",width,"' height='",height,"'/></td>")
    print("</tr>")
print('''
                    </table>
                </div>
                <div id='t_hybrids' style='display:none;width:95%;'>
                    <table border=1 width='100%'>
''')

for thc,thp,thi in zip(toyota_hybrids,toyota_hybrid_prices,toyota_hybrid_pic):
    print("<tr>")
    print("<td>",thc,"</td>","<td>",thp,"</td>","<td><img src='",thi,"' width='",width,"' height='",height,"'/></td>")
    print("</tr>")
print('''
                    </table>
                </div>
                <div id='t_trucks' style='display:none;width:95%;'>
                    <table border=1 width='100%'>
     ''')

for ttc,ttp,tti in zip(toyota_trucks,toyota_truck_prices,toyota_truck_pic):
    print("<tr>")
    print("<td>",ttc,"</td>","<td>",ttp,"</td>","<td><img src='",tti,"' width='",width,"' height='",height,"'/></td>")
    print("</tr>")
print(''' 
                    </table>
                </div>
            </div>
            <div id='honda' style='float:left;width:30%;'>
                <h3>Honda</h3>
                <div id=h_cars style='display:block;width:95%;'>
                    <table border=1 width="100%">
''')

for hc,hp,hi in zip(honda_cars,honda_cars_price,honda_cars_img):
    print("<tr>")
    print("<td>",hc,"</td>","<td>",hp,"</td>","<td><img src='",hi,"' width='",width,"' height='",height,"'/></td>")
    print("</tr>")
print('''
                    </table>
                </div>
                <div id='h_suvs' style='display:none;width:95%;'>
                    <table border=1 width='100%'>
     ''')

for hsc,hsp,hsi in zip(honda_suvs,honda_suvs_price,honda_suvs_img):
    print("<tr>")
    print("<td>",hsc,"</td>","<td>",hsp,"</td>","<td><img src='",hsi,"'width='",width,"' height='",height,"'/></td>")
    print("</tr>")
print('''
                    </table>
                </div>
                <div id='h_hybrids' style='display:none;width:95%;'>
                    <table border=1 width='100%'>
    ''')

for hhc,hhp,hhi in zip(honda_hybrids,honda_hybrids_price,honda_hybrids_img):
    print("<tr>")
    print("<td>",hhc,"</td>","<td>",hhp,"</td>","<td><img src='",hhi,"' width='",width,"' height='",height,"'/></td>")
    print("</tr>")
print('''
                    </table>
                </div>
                <div id='h_trucks' style='display:none;width:95%;'>
                    <table border=1 width='100%'>
     ''')

for htc,htp,hti in zip(honda_trucks,honda_trucks_price,honda_trucks_img):
    print("<tr>")
    print("<td>",htc,"</td>","<td>",htp,"</td>","<td><img src='",hti,"' width='",width,"' height='",height,"'/></td>")
    print("</tr>")
print(''' 
                    </table>
                </div>
            </div>
                <div id='nissan' style='float:left;width:30%;'>
                    <h3>Nissan</h3>
                    <div id='n_cars' style='display:block;width:95%;'>
                        <table border=1 width="100%">
    ''')
for nc,np,ni in zip(nissan_cars,nissan_cars_price,nissan_cars_img):
    print("<tr>")
    print("<td>",nc,"</td>","<td>",np,"</td>","<td><img src='",ni,"' width='",width,"' height='",height,"'/></td>")
    print("</tr>")
print('''
                        </table>
                    </div>
                    <div id='n_suvs' style='display:none;width:95%;'>
                        <table border=1 width='100%'>
     ''')
for nsc,nsp,nsi in zip(nissan_suv,nissan_suv_price,nissan_suv_img):
    print("<tr>")
    print("<td>",nsc,"</td>","<td>",nsp,"</td>","<td><img src='",nsi,"'width='",width,"' height='",height,"'/></td>")
    print("</tr>")
print('''
                        </table>
                    </div>
                    <div id='n_hybrids' style='display:none;width:95%;'>
                        <table border=1 width='100%'>
     ''')
print("<tr>")
print("<td>",str(nissan_hybrid),"</td>","<td>",str(nissan_hybrid_price),"</td>","<td><img src='",str(nissan_hybrid_img),"' width='",width,"' height='",height,"'/></td>")
print("</tr>")    
print('''
                        </table>
                    </div>
                    <div id='n_trucks' style='display:none;width:95%;'>
                        <table border=1 width='100%'>
     ''')
for ntc,ntp,nti in zip(nissan_trucks,nissan_trucks_price,nissan_trucks_img):
    print("<tr>")
    print("<td>",ntc,"</td>","<td>",ntp,"</td>","<td><img src='",nti,"' width='",width,"' height='",height,"'/></td>")
    print("</tr>")
print(''' 
                        </table>
                    </div>
                </div>
            </div>
        </div>
    
''')

