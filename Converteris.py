from tkinter import*
from tkinter import messagebox
from functools import partial
import sys
import re
import webbrowser
#Programa konvertuoja temperatūrų matus tarpusavyje bei pateikia temperatūrų atradėjų faktus
#Konvertuojama iš X mato į Y matą
def XIY(*_):
#Tikrinama ar nėra įvestas tekstas
    try:
        variable4.get()
    except:
#Jei tekstas įvestas nustatome įvedima 0
        if wg.get()!="-" and wgf.get()!="-" or re.search('[a-zA-Z]+',wg.get())!=None or re.search('[a-zA-Z]+',wgf.get())!=None:
            variable4.set("0.0")
            XIY()
            return
    variable4.set(float(variable4.get()))
    if variable.get()==variable1.get():
        variable3.set(round((variable4.get()),3))
#___________________________________________________________________________________________
#___________________________________________________________________________________________
    elif variable.get()=="K" and variable1.get()=="°C":
        variable3.set(round((variable4.get())-273.15,3))
    elif variable.get()=="°C" and variable1.get()=="K":
        variable3.set(round((variable4.get())+273.15,3))
#___________________________________________________________________________________________
#___________________________________________________________________________________________
    elif variable.get()=="°C" and variable1.get()=="°F":
        variable3.set(round((variable4.get())*9/5+32,3))
    elif variable.get()=="°F" and variable1.get()=="°C":
        variable3.set(round(((variable4.get())- 32)*5/9,3))
#___________________________________________________________________________________________
    elif variable.get()=="K" and variable1.get()=="°F":
        variable3.set(round((variable4.get())* 9/5 - 459.67,3))
    elif variable.get()=="°F" and variable1.get()=="K":
        variable3.set(round(((variable4.get()) + 459.67)*5/9,3))
#___________________________________________________________________________________________
#___________________________________________________________________________________________
    elif variable.get()=="°C" and variable1.get()=="°Ra":
        variable3.set(round(((variable4.get())+ 273.15)*9/5,3))
    elif variable.get()=="°Ra" and variable1.get()=="°C":
        variable3.set(round(((variable4.get()) - 491.67)*5/9,3))
#___________________________________________________________________________________________
    elif variable.get()=="K" and variable1.get()=="°Ra":
        variable3.set(round((variable4.get())*9/5,3))
    elif variable.get()=="°Ra" and variable1.get()=="K":
        variable3.set(round((variable4.get())*5/9,3))
#___________________________________________________________________________________________
    elif variable.get()=="°F" and variable1.get()=="°Ra":
        variable3.set(round((variable4.get())+ 459.67,3))
    elif variable.get()=="°Ra" and variable1.get()=="°F":
        variable3.set(round((variable4.get())- 459.67,3))
#___________________________________________________________________________________________
#___________________________________________________________________________________________
    elif variable.get()=="°C" and variable1.get()=="°De":
        variable3.set(round((100 - (variable4.get()))*3/2,3))
    elif variable.get()=="°De" and variable1.get()=="°C":
        variable3.set(round(100 - (variable4.get())*2/3,3))
#___________________________________________________________________________________________
    elif variable.get()=="K" and variable1.get()=="°De":
        variable3.set(round((373.15-(variable4.get()))*1.5,3))
    elif variable.get()=="°De" and variable1.get()=="K":
        variable3.set(round(373.15-((variable4.get()))*2/3,3))
#___________________________________________________________________________________________
    elif variable.get()=="°F" and variable1.get()=="°De":
        variable3.set(round((212-(variable4.get()))*5/6,3))
    elif variable.get()=="°De" and variable1.get()=="°F":
        variable3.set(round(212-((variable4.get()))*6/5,3))
#___________________________________________________________________________________________
    elif variable.get()=="°Ra" and variable1.get()=="°De":
        variable3.set(round((671.67 - (variable4.get()))*5/6,3))
    elif variable.get()=="°De" and variable1.get()=="°Ra":
        variable3.set(round(671.67 - (variable4.get())*6/5,3))
#___________________________________________________________________________________________
#___________________________________________________________________________________________
    elif variable.get()=="°C" and variable1.get()=="°N":
        variable3.set(round((variable4.get())*33/100,3))
    elif variable.get()=="°N" and variable1.get()=="°C":
        variable3.set(round((variable4.get())*100/33,3))
#___________________________________________________________________________________________
    elif variable.get()=="°F" and variable1.get()=="°N":
        variable3.set(round(((variable4.get())-32)*11/60,3))
    elif variable.get()=="°N" and variable1.get()=="°F":
        variable3.set(round((variable4.get())*60/11+32,3))
#___________________________________________________________________________________________
    elif variable.get()=="°N" and variable1.get()=="K":
        variable3.set(round((variable4.get())*100/33+273.15,3))
    elif variable.get()=="K" and variable1.get()=="°N":
        variable3.set(round(((variable4.get())-273.15)*33/100,3))
#___________________________________________________________________________________________
    elif variable.get()=="°N" and variable1.get()=="°Ra":
        variable3.set(round((variable4.get())*60/11+491.67,3))
    elif variable.get()=="°Ra" and variable1.get()=="°N":
        variable3.set(round(((variable4.get())- 491.67)*11/60,3))
#___________________________________________________________________________________________
    elif variable.get()=="°N" and variable1.get()=="°De":
        variable3.set(round((33-(variable4.get()))*50/11,3))
    elif variable.get()=="°De" and variable1.get()=="°N":
        variable3.set(round(33-(variable4.get())*11/50,3))
#___________________________________________________________________________________________
#___________________________________________________________________________________________
    elif variable.get()=="°C" and variable1.get()=="°Re":
        variable3.set(round((variable4.get())*4/5,3))
    elif variable.get()=="°Re" and variable1.get()=="°C":
        variable3.set(round((variable4.get())*5/4,3))
#___________________________________________________________________________________________
    elif variable.get()=="°F" and variable1.get()=="°Re":
        variable3.set(round(((variable4.get())-32)*4/9,3))
    elif variable.get()=="°Re" and variable1.get()=="°F":
        variable3.set(round((variable4.get())*9/4+32,3))
#___________________________________________________________________________________________
    elif variable.get()=="°Re" and variable1.get()=="K":
        variable3.set(round((variable4.get())*5/4+273.15,3))
    elif variable.get()=="K" and variable1.get()=="°Re":
        variable3.set(round(((variable4.get())-273.15)*4/5,3))
#___________________________________________________________________________________________
    elif variable.get()=="°Ra" and variable1.get()=="°Re":
        variable3.set(round(((variable4.get())- 491.67)*4/9,3))
    elif variable.get()=="°Re" and variable1.get()=="°Ra":
        variable3.set(round((variable4.get())*9/4+491.67,3))
#___________________________________________________________________________________________
    elif variable.get()=="°Re" and variable1.get()=="°De":
        variable3.set(round((80-(variable4.get()))*15/8,3))
    elif variable.get()=="°De" and variable1.get()=="°Re":
        variable3.set(round(80-(variable4.get())*8/15,3))
#___________________________________________________________________________________________
    elif variable.get()=="°N" and variable1.get()=="°Re":
        variable3.set(round((variable4.get())*80/33,3))
    elif variable.get()=="°Re" and variable1.get()=="°N":
        variable3.set(round((variable4.get())*33/80,3))
#___________________________________________________________________________________________
#___________________________________________________________________________________________

    elif variable.get()=="°C" and variable1.get()=="°Rø":
        variable3.set(round((variable4.get())*21/40+7.5,3))
    elif variable.get()=="°Rø" and variable1.get()=="°C":
        variable3.set(round(((variable4.get())-7.5)*40/21,3))
#___________________________________________________________________________________________
    elif variable.get()=="°F" and variable1.get()=="°Rø":
        variable3.set(round(((variable4.get())-32)*7/24+7.5,3))
    elif variable.get()=="°Rø" and variable1.get()=="°F":
        variable3.set(round(((variable4.get())-7.5)*24/7+32,3))
#___________________________________________________________________________________________
    elif variable.get()=="°Rø" and variable1.get()=="K":
        variable3.set(round(((variable4.get())-7.5)*40/21+273.15,3))
    elif variable.get()=="K" and variable1.get()=="°Rø":
        variable3.set(round(((variable4.get())-273.15)*21/40+7.5,3))
#___________________________________________________________________________________________
    elif variable.get()=="°Ra" and variable1.get()=="°Rø":
        variable3.set(round(((variable4.get())- 491.67)*7/24+7.5,3))
    elif variable.get()=="°Rø" and variable1.get()=="°Ra":
        variable3.set(round(((variable4.get())- 7.5)*24/7+491.67,3))
#___________________________________________________________________________________________
    elif variable.get()=="°Rø" and variable1.get()=="°De":
        variable3.set(round((60-(variable4.get()))*20/7,3))
    elif variable.get()=="°De" and variable1.get()=="°Rø":
        variable3.set(round(60-(variable4.get())*7/20,3))
#___________________________________________________________________________________________
    elif variable.get()=="°N" and variable1.get()=="°Rø":
        variable3.set(round((variable4.get())*35/22+7.5,3))
    elif variable.get()=="°Rø" and variable1.get()=="°N":
        variable3.set(round(((variable4.get())-7.5)*22/35,3))
#___________________________________________________________________________________________
    elif variable.get()=="°Rø" and variable1.get()=="°Re":
        variable3.set(round(((variable4.get())-7.5)*32/21,3))
    elif variable.get()=="°Re" and variable1.get()=="°Rø":
        variable3.set(round((variable4.get())*21/32+7.5,3))
#___________________________________________________________________________________________
#___________________________________________________________________________________________
#Keitimo funkcijos nurodo, iš kokios konvertuojama. Ar X>Y, ar Y>X. Jei yra į Y>X, tai kintamieji yra sukeičiami, kad veiktų funkcijai XIY()
faa=0
def keitimas1(*args):
    global faa,variable,variable1,variable3,variable4
    if faa>0:
        variable1,variable=variable,variable1
        variable3,variable4=variable4,variable3
    faa=0
    wg.config(textvariable=variable3)
    wgf.config(textvariable=variable4)
    w.config(textvariable=variable)
    g.config(textvariable=variable1)
    XIY()
def keitimas2(*args):
    global faa,variable,variable1,variable3,variable4
    if faa==0:
        variable1,variable=variable,variable1
        variable3,variable4=variable4,variable3
    wgf.config(textvariable=variable3)
    wg.config(textvariable=variable4)
    g.config(textvariable=variable)
    w.config(textvariable=variable1)
    faa=faa+1
    XIY()
#Funkcija, kuri pakeičia temperatūrų atradėjų paveikslėlius bei tekstą.
def keiciasi(a):
    global photo1
    af.config(text=B[a])
    photo1=PhotoImage(file=C[a])
    photo1=photo1.zoom(dydis1)
    photo1=photo1.subsample(dydis)
    nuotrauka1.config(image=photo1)
#___________________________________________________________________________________________
#Funkcija, kuri paklausia, ar nori išeiti iš programos. 
def isejimas():
    ats=messagebox.askyesno("Išėjimas","Ar norite išeiti iš šios programos?")
    if ats==True:
        pg.destroy()
#___________________________________________________________________________________________
#Funkcija, kuri atstoja du mygtukus. Pati funkcija sukuria dukterin5 langą su išjungimo mygtuku. Toliau funkcijoje išsiaiškinama, kuris mygtukas paspaustas. Jei paspaustas mygtukas 0, tai parašomas tekstas apie šios programos kūrėją. Jei paspaustas mygtukas 1, tai sukūriami mygtukai su informacijos šaltiniais.
def apiemane(a):
    global phito
    naujas=Toplevel(pg,relief=RAISED,bd=5)
    naujas.geometry("%dx%d%+d%+d" % (800,300,ilgis/4,plotis/4))
    naujas.resizable(False,False)
    naujas.overrideredirect(1)
    naujas.config(bg="linen")
    info11= PhotoImage(file="output_RuZCcv.gif")
    du=Button(naujas,image=info11,command=naujas.destroy)
    du.pack(side=RIGHT,padx=5)
    du.image=info11
    a1=Frame(naujas,bd=5,relief=RIDGE,bg="#F6F6F6");a1.pack(side=LEFT,fill=X, expand=True,padx=10)
    if a==0:
        phito=PhotoImage(file="output_qDSvmK.gif")
        Label(a1,bg="#F6F6F6",text="About creator",font=("Times","25", "bold underline")).pack()
        Label(a1,image=phito,bd=5, highlightthickness=0, relief=RIDGE).pack(side=LEFT,padx=7,pady=7)
        Label(a1,bg="#F6F6F6",font=("Times","11", "bold"),justify=LEFT,text="First Name - Kristupas\nLast Name - Jakubonis\nDate of Birth - 2002/04/02\nCity - Pasvalys\nEducation place - Pasvalys gymnasium named after Petras Vileisis\nPhone - +370 65608566\nEmail - kr.jakubonis@gmail.com\nHobbies - swimming, playing computer games, learning advanced Math,\n watching movies/TV series, programming, listening to music").pack(side=LEFT)
    elif a==1:
        Label(a1,text="\n\n").grid(row=0,column=0)
        Label(a1,bg="#F6F6F6",text="Information sources",font=("Times","25", "bold underline")).place(x=200,y=3)
        for x in range(2):
            for y in range(4):
                Button(a1,command=partial(link,4*x+y),text=A[4*x+y],width=40,font=("Times",10,"bold")).grid(column=x,row=y+1,padx=30,pady=7)
D=["https://lt.wikipedia.org/wiki/Anders_Celsius","http://www.studijos.lt/nepatvirtinti-rasto-darbai/referatas/3520/viljamas-tomsonas-kelvinas-andersas-celsijus-temperaturu-skales","https://lt.wikipedia.org/wiki/Gabriel_Fahrenheit","https://en.wikipedia.org/wiki/William_John_Macquorn_Rankine","https://en.wikipedia.org/wiki/Joseph-Nicolas_Delisle","https://en.wikipedia.org/wiki/Isaac_Newton","https://www.britannica.com/biography/Rene-Antoine-Ferchault-de-Reaumur","https://en.wikipedia.org/wiki/Ole_R%C3%B8mer"]
#___________________________________________________________________________________________
#Funkcija, kuri atidaro hyperlinką, kai paspaudi ant mygtuko.
def link(a):
        webbrowser.open(D[a])    
#___________________________________________________________________________________________
#Nustatomi lango parametrai
pg=Tk();ilgis=pg.winfo_screenwidth();plotis=pg.winfo_screenheight();pg.geometry("%dx%d" % (ilgis,plotis));pg.config(background="#F6F6F6");pg.resizable(False,False);pg.attributes("-fullscreen", True)
pg.config(bg='papayawhip')
#___________________________________________________________________________________________
#Įdedamas lango išjungimo mygtukas
info1= PhotoImage(file="output_RuZCcv.gif")
d=Button(pg,image=info1,command=isejimas)
d.place(x=ilgis-45,y=0)
d.image=info1
#___________________________________________________________________________________________
#Įdedamas mygtukas šaltiniams gauti
info= PhotoImage(file="output_YS75nq.gif")
d1=Button(pg,image=info,command=partial(apiemane,1))
d1.place(x=ilgis-90,y=0)
d1.image=info
#___________________________________________________________________________________________
#Įdedamas mygtukas apie programos autorių
info2= PhotoImage(file="output_5r88Ta.gif")
d2=Button(pg,image=info2,command=partial(apiemane,0))
d2.place(x=ilgis-135,y=0)
d2.image=info2
#___________________________________________________________________________________________
#Nustatomi dydžiai pagal ekrano rezoliuciją
if ilgis<=1300 or plotis <=700:
    sriftas="6"
    sriftas1=7
    atimam=-1
    dydis=2
    dydis1=1
elif ilgis>1300 and ilgis<1650 or plotis >700 and plotis <=900:
    sriftas="10"
    sriftas1=9
    atimam=-1
    dydis=3
    dydis1=2
elif ilgis>=1650 and plotis >900:#Panašiai su šia rezoliucija buvo daryta programa
    sriftas="12"
    atimam=0
    sriftas1=11
    dydis=1
    dydis1=1
f=("Times",sriftas,"bold")
#___________________________________________________________________________________________
#Antraštė
da=Frame(pg,bd=5,relief=RIDGE,bg="#F6F6F6");da.pack(pady=ilgis/40)
Label(da,text="Temperatūrų konvertavimas",bg="#F6F6F6",font=("Times","25", "bold underline")).pack(padx=5,pady=5)
#___________________________________________________________________________________________
#Temperatūrų konvertavimo aparato rėmai ir atradėjų informacijos rėmai
a=Frame(pg,bd=5,relief=RIDGE,bg="#F6F6F6");a.pack(pady=ilgis/150)
c=Frame(pg,bd=5,relief=RIDGE,bg="#F6F6F6");c.pack(pady=ilgis/150,anchor="n",padx=plotis/50,fill=X, expand=True)
b=LabelFrame(c,labelanchor="n",text="Temperatūrų atradėjai",font=("Times","25","bold"),bd=3,relief=RIDGE,bg="#F6F6F6");b.pack(pady=15,padx=3,fill=X, expand=True)
#___________________________________________________________________________________________
#Sukūriamas pirmas temperatūros pasirinkimo meniu
variable = StringVar()
variable.set("°C")
w = OptionMenu(a, variable, "°C", "K", "°F","°Ra","°De","°N","°Re","°Rø")
w.grid(row=0,column=1)
w.configure(width=3,justify=CENTER, highlightthickness=0)
#___________________________________________________________________________________________
#Sukūriamas antras temperatūros pasirinkimo meniu
variable1 = StringVar()
variable1.set("°C")
g = OptionMenu(a, variable1, "°C", "K", "°F","°Ra","°De","°N","°Re","°Rø")
g.grid(row=0,column=5,padx=15)
g.configure(width=3,justify=CENTER, highlightthickness=0)
#___________________________________________________________________________________________
#Sukūriama pirma temperatūros įrašymo vieta
variable3 = DoubleVar()
wg = Spinbox(a,justify=CENTER,command=keitimas2,from_=-9999999999999999999999999,to=9999999999999999999999999,textvariable=variable3,increment=0.1,width=20,font="10",bg="#F6F6F6")
wg.grid(row=0,column=4)
#___________________________________________________________________________________________
#Sukūriama antra temperatūros įrašymo vieta
variable4 = DoubleVar()
wgf = Spinbox(a,command=keitimas1,justify=CENTER,from_=-9999999999999999999999999,to=9999999999999999999999999,textvariable=variable4,increment=0.1,width=20,font="10",bg="#F6F6F6")
wgf.grid(row=0,column=0,padx=15)
#___________________________________________________________________________________________
#Patalpinamos kovertavimo rodyklės
photo=PhotoImage(file="ezgif.com-gif-maker.gif")
photo=photo.subsample(3)
nuotrauka=Label(a,image=photo,bd=0, highlightthickness=0)
nuotrauka.grid(row=0,column=2,padx=15,pady=15)
#___________________________________________________________________________________________
#Kai tarp įrašymo vietų kažkas atleidžia klavišą, yra išsiunčiama komanda į funkciją.
wg.bind("<KeyRelease>", keitimas2)
wgf.bind("<KeyRelease>", keitimas1)
#___________________________________________________________________________________________
#Duomenys sudėti masyve.
C=["Celsijus.gif","kelvinas.gif","farenheitas.gif","rankine.gif","delislis.gif","niutonas.gif","reumeris.gif","romeris.gif"]
B=["Andersas Celsijus (gimė - 1701 m. lapkričio 27 d. Upsaloje, mirė – 1744 m. balandžio 25 d.) – švedų astronomas.\n\n 1742 m. sukūrė 100 laipsnių termometrą, kuris dabar naudojamas daugelyje pasaulio šalių.\n\n Vandens virimo temperatūrą jis pažymėjo 100 laipsnių, o ledo tirpimo temperatūrą 0 laipsnių.\n\n Celsijus dirbo Upsalos universiteto profesoriumi, nuo 1740 m. Upsalos observatorijos direktoriumi.\n\n Jis dalyvavo topografiniuose Laplandijos bei Peru tyrimuose, kurių rezultatai patvirtino Niutono hipotezę, kad Žemė plokštėja.\n\n Jis stengėsi, kad būtų įvestas Grigaliaus kalendorius. Be to jis pirmą kartą įrodė šiaurės pašvaistės ir magnetinio lauko ryšį.","Viljamas Tomsonas-Kelvinas (gimė – 1824 m. birželio 26 d. Belfaste, mirė – 1907 m. gruodžio 17 d. Largse) - anglų fizikas.\n\nPadėjo suformuluoti Antrąjį termodinamikos dėsnį. 1848 m. sudarė absoliutinę temperatūros skalę.\n\n Plėtojo elektromagn. virpesių teoriją, sudarė kontūro virpesių periodo ir kontūro talpos bei induktyvumo sąryšio formulę.\n\n Apskaičiavo molekulių matmenis pagal skysčio plėvelės paviršinę energiją.\n\n 1870 m. nustatė sočiųjų garų tamprumo priklausomybę nuo skysčio paviršiaus formos.\n\n 1881 m. Tomsonas įėjo į komisiją, kuri sudarė pirmąją suderintą elektros vienetų sistemą.","Gabrielis Danielis Farenheitas (gimė - 1686 m. gegužės 24 d. Gdanske, mirė - 1736 m. rugsėjo 16 d. Hagoje) – vokiečių fizikas ir inžinierius.\n\nFarenheitas pagamino šiuolaikinės formos termometrą, naudojantį alkoholį, o vėliau termometrams panaudojo gyvsidabrį.\n\n Jis sudarė Farenheito skalę, kuri buvo plačiai naudojama Europoje iki Celsijaus skalės įvedimo.\n\n Farenheito skalėje 0 °F yra vandens užšalimo temperatūra, 32 °F - ledo tirpimo taškas, o 98 °F – sveiko žmogaus kūno temperatūra.\n\n Jo pavarde buvo pavadintas ir temperatūros matavimo vienetas – Farenheito laipsnis.\n\n Buvo įrengęs dirbtuves, kuriose gaminti termometrai, areometrai, barometrai. ","Wiliamas Johnas Macquornas Rankine (gimė - 1820 m. liepos 5 d. Edinburge, mirė - 1872 m. gruodžio 24 d. Glazge) - škotų inžinierius, fizikas.\n\nJis sukūrė Rankinės skalę, susiejusia su Kelvino temperatūros skale, tačiau Fahrenheito laipsniais, o ne Celsijaus laipsniais.\n\nRankine sukūrė išsamią garo variklio ir visų šilumos variklių teoriją.\n\nJis paskelbė kelis šimtus mokslo ir inžinerijos leidinių.\n\nJo inžinerijos mokslo ir praktikos vadovai buvo naudojami daugelį dešimtmečių po jų paskelbimo.\n\nJis buvo entuziastingas mėgėjiškas dainininkas, pianistas ir violončelininkas, kuris kūrė savo humoristines dainas.","\n\nJosephas-Nicolas Delislis (gimė - 1688 m. balandžio 4 d. Paryžiuje, mirė - 1768 m. rugsėjo 11 d. Paryžiuje) - prancūzų astronomas, kartografas.\n\n1712 m. Liuksemburgo rūmuose įsteigė observatoriją ir po trejų metų persikėlė į „Hotel de Taranne“.\n\n1725 m. jis buvo išrinktas karališkosios draugijos nariu ir 1749 m. - Švedijos karališkosios mokslų akademijos užsienio nariu.\n\n1732 m. Delislis sukūrė termometrą, kuriame gyvsidabris naudojamas kaip darbinis skystis.\n\n1740 m. Delislis vyko ekspedicija į Sibirą, siekiant stebėti Beryozovo gyvsidabrio tranzitą per saulę.\n\nEkspedicijos metu jis užfiksavo daugybę ornitologinių, botaninių, zoologinių, geografinių ir kitų mokslinių pastabų.\n\n","Izaokas Niutonas (gimė - 1643 m. sausio 4 d. Linkolšyre, mirė – 1727 m. kovo 31 d. Kensingtone) – anglų fizikas, matematikas, astronomas.\n\n1668 m. jis suprojektavo ir faktiškai sukonstravo pirmąjį atspindintį teleskopą — tokio tipo teleskopai naudojami ir šiandien.\n\n Niutono svarbiausias įnašas į matematikos mokslą buvo integralinio skaičiavimo atradimas, kurį jis padarė, būdamas dvidešimt trejų metų.\n\n 1687 m. jis išleido savo didįjį veikalą „Natūralios filosofijos matematiniai principai”, kuriame išdėstė gravitacijos ir judėjimo dėsnius.\n\nNiutonas išrado Niutono skalę: apibūdino „nulinę šilumos temperatūrą“ kaip tirpstantį sniegą ir „33 laipsnius šilumos“ kaip verdantį vandenį.\n\nŠis žmogus suformulavo pagrindinius mechanikos dėsnius, atrado baltos šviesos skaidymo dėsnį ir sukūrė korpuskulinę šviesos teoriją.","René Antoinas Ferchaultas de Réaumuras (gimė - 1683 m. vasario 28 d. , mirė – 1757 m. spalio 17 d.) – prancūzų entomologas, rašytojas.\n\nRéaumuras sukūrė kupolinę krosnį, kuri yra vis dar ekonomiškiausias ir dažniausiai naudojamas pilkojo geležies lydymo procesas.\n\nJis išrado Réumumuro termometrą ir pažymėjo temperatūros skalę: nulio laipsniu - užšalimo tašką ir aštuoniasdešimt laipsniais - virimo tašką.\n\nJo pastangos atnešė daug naujų pramonės šakų į Prancūziją, todėl apie dvylika kartų jis tapo Prancūzijos mokslų akademijos direktoriumi.\n\n1734 m. Réumumuris paskelbė pirmąjį savo leidinį. Nors jis buvo ir nebaigtas, tai buvo svarbus pasiekimas entomologijos istorijoje.\n\nJis ištyrė cheminę porceliano sudėtį ir 1740 m. sukūrė savo formulę vadinamajam Réumumuro porcelianui.","\n\nOle Christensenas Romeris (gimė - 1644 m. rugsėjo 25 d. Orhuse, mirė – 1710 m. rugsėjo 19 d. Kopenhagoje) – danų astronomas.\n\nJis 1676 m. pirmasis pasaulyje išmatavo šviesos greitį.\n\nRomeris turi temperatūros skalę pavadinta jo vardu, nes jis ją atrado 1701 m. .\n\nFarenheito skalės išradėjas, daug išmoko naudodamasis jo darbais ir didindamas dalinį keturiais kartais, taip gaudamas Farenheito skalę.\n\n1672 m. Romeris kartu su Pikardu grįžo į Prancūziją ir pradėjo dirbti karališkoje observatorijoje Paryžiuje.\n\nVėliau Romeris tapo antruoju Kopenhagos policijos viršininku ir padėjo kontroliuoti neturtingus.\n\n"]
#___________________________________________________________________________________________
#Sekama, jei pasikeičia temperatūrų tipai, siunčiamos komandos į funkciją.
variable.trace("w",keitimas1)
variable1.trace("w",keitimas1)
#___________________________________________________________________________________________
#Padaromas pradinis temperatūrų atradėjų informacijos langas, šiuo atveju jis yra mokslininko Celsijaus informacija.
photo1=PhotoImage(file=C[0])
photo1=photo1.zoom(dydis1)
photo1=photo1.subsample(dydis)
nuotrauka1=Label(b,image=photo1,bd=5, highlightthickness=0, relief=RIDGE)
nuotrauka1.pack(side="right",padx=10,pady=10)
af=Label(b,font=("Times",sriftas1,"italic"),bg="#F6F6F6",justify=RIGHT,text=B[0])
af.pack(side=RIGHT,anchor="e",padx=10)
#___________________________________________________________________________________________
#Cikle išdėliojami mygtukai su funkcijomis
A=["Andersas Celsijus (°C)","Viljamas Tomsonas-Kelvinas (K)","Gabrielis Danielis Farenheitas (°F)","Wiliamas Johnas Macquornas Rankine (°Ra)","Josephas-Nicolas Delislis (°De)","Izaokas Niutonas (°N)","René Antoinas Ferchaultas de Réaumuras (°Re)","Ole Christensenas Romeris (°Rø)"]
for x in range(8):
    Button(b,text=A[x],font=f,width=40,command=partial(keiciasi, x)).pack(padx=15+atimam*10,pady=5+3*atimam,anchor="w")
#___________________________________________________________________________________________
#___________________________________________________________________________________________
class DevNull:
    def write(self, msg):
        pass
sys.stderr = DevNull()
mainloop()

