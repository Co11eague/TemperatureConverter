from tkinter import *
from tkinter import messagebox


# Konvertuojama iš X mato į Y matą
def XIY(*_):
    # Tikrinama ar nėra įvestas tekstas
    try:
        variable4.get()
    except TclError:
        # Jei tekstas įvestas nustatome įvedima 0
        variable4.set(0.0)
        XIY()
        return
    variable4.set(float(variable4.get()))
    if variable.get() == variable1.get():
        variable3.set(round((variable4.get()), 2))
    # ___________________________________________________________________________________________
    # ___________________________________________________________________________________________
    elif variable.get() == "K" and variable1.get() == "°C":
        variable3.set(round((variable4.get()) - 273.15, 2))
    elif variable.get() == "°C" and variable1.get() == "K":
        variable3.set(round((variable4.get()) + 273.15, 2))
    # ___________________________________________________________________________________________
    # ___________________________________________________________________________________________
    elif variable.get() == "°C" and variable1.get() == "°F":
        variable3.set(round((variable4.get()) * 9 / 5 + 32, 2))
    elif variable.get() == "°F" and variable1.get() == "°C":
        variable3.set(round(((variable4.get()) - 32) * 5 / 9, 2))
    # ___________________________________________________________________________________________
    elif variable.get() == "K" and variable1.get() == "°F":
        variable3.set(round((variable4.get()) * 9 / 5 - 459.67, 2))
    elif variable.get() == "°F" and variable1.get() == "K":
        variable3.set(round(((variable4.get()) + 459.67) * 5 / 9, 2))
    # ___________________________________________________________________________________________
    # ___________________________________________________________________________________________
    elif variable.get() == "°C" and variable1.get() == "°Ra":
        variable3.set(round(((variable4.get()) + 273.15) * 9 / 5, 2))
    elif variable.get() == "°Ra" and variable1.get() == "°C":
        variable3.set(round(((variable4.get()) - 491.67) * 5 / 9, 2))
    # ___________________________________________________________________________________________
    elif variable.get() == "K" and variable1.get() == "°Ra":
        variable3.set(round((variable4.get()) * 9 / 5, 2))
    elif variable.get() == "°Ra" and variable1.get() == "K":
        variable3.set(round((variable4.get()) * 5 / 9, 2))
    # ___________________________________________________________________________________________
    elif variable.get() == "°F" and variable1.get() == "°Ra":
        variable3.set(round((variable4.get()) + 459.67, 2))
    elif variable.get() == "°Ra" and variable1.get() == "°F":
        variable3.set(round((variable4.get()) - 459.67, 2))
    # ___________________________________________________________________________________________
    # ___________________________________________________________________________________________
    elif variable.get() == "°C" and variable1.get() == "°De":
        variable3.set(round((100 - (variable4.get())) * 3 / 2, 2))
    elif variable.get() == "°De" and variable1.get() == "°C":
        variable3.set(round(100 - (variable4.get()) * 2 / 3, 2))
    # ___________________________________________________________________________________________
    elif variable.get() == "K" and variable1.get() == "°De":
        variable3.set(round((373.15 - (variable4.get())) * 1.5, 2))
    elif variable.get() == "°De" and variable1.get() == "K":
        variable3.set(round(373.15 - (variable4.get()) * 2 / 3, 2))
    # ___________________________________________________________________________________________
    elif variable.get() == "°F" and variable1.get() == "°De":
        variable3.set(round((212 - (variable4.get())) * 5 / 6, 2))
    elif variable.get() == "°De" and variable1.get() == "°F":
        variable3.set(round(212 - (variable4.get()) * 6 / 5, 2))
    # ___________________________________________________________________________________________
    elif variable.get() == "°Ra" and variable1.get() == "°De":
        variable3.set(round((671.67 - (variable4.get())) * 5 / 6, 2))
    elif variable.get() == "°De" and variable1.get() == "°Ra":
        variable3.set(round(671.67 - (variable4.get()) * 6 / 5, 2))
    # ___________________________________________________________________________________________
    # ___________________________________________________________________________________________
    elif variable.get() == "°C" and variable1.get() == "°N":
        variable3.set(round((variable4.get()) * 33 / 100, 2))
    elif variable.get() == "°N" and variable1.get() == "°C":
        variable3.set(round((variable4.get()) * 100 / 33, 2))
    # ___________________________________________________________________________________________
    elif variable.get() == "°F" and variable1.get() == "°N":
        variable3.set(round(((variable4.get()) - 32) * 11 / 60, 2))
    elif variable.get() == "°N" and variable1.get() == "°F":
        variable3.set(round((variable4.get()) * 60 / 11 + 32, 2))
    # ___________________________________________________________________________________________
    elif variable.get() == "°N" and variable1.get() == "K":
        variable3.set(round((variable4.get()) * 100 / 33 + 273.15, 2))
    elif variable.get() == "K" and variable1.get() == "°N":
        variable3.set(round(((variable4.get()) - 273.15) * 33 / 100, 2))
    # ___________________________________________________________________________________________
    elif variable.get() == "°N" and variable1.get() == "°Ra":
        variable3.set(round((variable4.get()) * 60 / 11 + 491.67, 2))
    elif variable.get() == "°Ra" and variable1.get() == "°N":
        variable3.set(round(((variable4.get()) - 491.67) * 11 / 60, 2))
    # ___________________________________________________________________________________________
    elif variable.get() == "°N" and variable1.get() == "°De":
        variable3.set(round((33 - (variable4.get())) * 50 / 11, 2))
    elif variable.get() == "°De" and variable1.get() == "°N":
        variable3.set(round(33 - (variable4.get()) * 11 / 50, 2))
    # ___________________________________________________________________________________________
    # ___________________________________________________________________________________________
    elif variable.get() == "°C" and variable1.get() == "°Re":
        variable3.set(round((variable4.get()) * 4 / 5, 2))
    elif variable.get() == "°Re" and variable1.get() == "°C":
        variable3.set(round((variable4.get()) * 5 / 4, 2))
    # ___________________________________________________________________________________________
    elif variable.get() == "°F" and variable1.get() == "°Re":
        variable3.set(round(((variable4.get()) - 32) * 4 / 9, 2))
    elif variable.get() == "°Re" and variable1.get() == "°F":
        variable3.set(round((variable4.get()) * 9 / 4 + 32, 2))
    # ___________________________________________________________________________________________
    elif variable.get() == "°Re" and variable1.get() == "K":
        variable3.set(round((variable4.get()) * 5 / 4 + 273.15, 2))
    elif variable.get() == "K" and variable1.get() == "°Re":
        variable3.set(round(((variable4.get()) - 273.15) * 4 / 5, 2))
    # ___________________________________________________________________________________________
    elif variable.get() == "°Ra" and variable1.get() == "°Re":
        variable3.set(round(((variable4.get()) - 491.67) * 4 / 9, 2))
    elif variable.get() == "°Re" and variable1.get() == "°Ra":
        variable3.set(round((variable4.get()) * 9 / 4 + 491.67, 2))
    # ___________________________________________________________________________________________
    elif variable.get() == "°Re" and variable1.get() == "°De":
        variable3.set(round((80 - (variable4.get())) * 15 / 8, 2))
    elif variable.get() == "°De" and variable1.get() == "°Re":
        variable3.set(round(80 - (variable4.get()) * 8 / 15, 2))
    # ___________________________________________________________________________________________
    elif variable.get() == "°N" and variable1.get() == "°Re":
        variable3.set(round((variable4.get()) * 80 / 33, 2))
    elif variable.get() == "°Re" and variable1.get() == "°N":
        variable3.set(round((variable4.get()) * 33 / 80, 2))
    # ___________________________________________________________________________________________
    # ___________________________________________________________________________________________

    elif variable.get() == "°C" and variable1.get() == "°Rø":
        variable3.set(round((variable4.get()) * 21 / 40 + 7.5, 2))
    elif variable.get() == "°Rø" and variable1.get() == "°C":
        variable3.set(round(((variable4.get()) - 7.5) * 40 / 21, 2))
    # ___________________________________________________________________________________________
    elif variable.get() == "°F" and variable1.get() == "°Rø":
        variable3.set(round(((variable4.get()) - 32) * 7 / 24 + 7.5, 2))
    elif variable.get() == "°Rø" and variable1.get() == "°F":
        variable3.set(round(((variable4.get()) - 7.5) * 24 / 7 + 32, 2))
    # ___________________________________________________________________________________________
    elif variable.get() == "°Rø" and variable1.get() == "K":
        variable3.set(round(((variable4.get()) - 7.5) * 40 / 21 + 273.15, 2))
    elif variable.get() == "K" and variable1.get() == "°Rø":
        variable3.set(round(((variable4.get()) - 273.15) * 21 / 40 + 7.5, 2))
    # ___________________________________________________________________________________________
    elif variable.get() == "°Ra" and variable1.get() == "°Rø":
        variable3.set(round(((variable4.get()) - 491.67) * 7 / 24 + 7.5, 2))
    elif variable.get() == "°Rø" and variable1.get() == "°Ra":
        variable3.set(round(((variable4.get()) - 7.5) * 24 / 7 + 491.67, 2))
    # ___________________________________________________________________________________________
    elif variable.get() == "°Rø" and variable1.get() == "°De":
        variable3.set(round((60 - (variable4.get())) * 20 / 7, 2))
    elif variable.get() == "°De" and variable1.get() == "°Rø":
        variable3.set(round(60 - (variable4.get()) * 7 / 20, 2))
    # ___________________________________________________________________________________________
    elif variable.get() == "°N" and variable1.get() == "°Rø":
        variable3.set(round((variable4.get()) * 35 / 22 + 7.5, 2))
    elif variable.get() == "°Rø" and variable1.get() == "°N":
        variable3.set(round(((variable4.get()) - 7.5) * 22 / 35, 2))
    # ___________________________________________________________________________________________
    elif variable.get() == "°Rø" and variable1.get() == "°Re":
        variable3.set(round(((variable4.get()) - 7.5) * 32 / 21, 2))
    elif variable.get() == "°Re" and variable1.get() == "°Rø":
        variable3.set(round((variable4.get()) * 21 / 32 + 7.5, 2))


# ___________________________________________________________________________________________
# ___________________________________________________________________________________________
# Konvertuojama iš Y mato į X matą
def YIX(*_):
    # Identiskas tikrinimas dėl klaidų
    try:
        variable3.get()
    except TclError:
        variable3.set(0.0)
        YIX()
        return
    variable3.set(float(variable3.get()))
    if variable.get() == "K" and variable1.get() == "°C":
        variable4.set(round((variable3.get()) + 273.15, 2))
    elif variable.get() == "°C" and variable1.get() == "K":
        variable4.set(round((variable3.get()) - 273.15, 2))
    # ___________________________________________________________________________________________
    # ___________________________________________________________________________________________
    elif variable.get() == variable1.get():
        variable4.set(round((variable3.get()), 2))
    elif variable.get() == "°C" and variable1.get() == "°F":
        variable4.set(round(((variable3.get()) - 32) * 5 / 9, 2))
    elif variable.get() == "°F" and variable1.get() == "°C":
        variable4.set(round((variable3.get()) * 9 / 5 + 32, 2))
    # ___________________________________________________________________________________________
    elif variable.get() == "K" and variable1.get() == "°F":
        variable4.set(round(((variable3.get()) + 459.67) * 5 / 9, 2))
    elif variable.get() == "°F" and variable1.get() == "K":
        variable4.set(round((variable3.get()) * 9 / 5 - 459.67, 2))
    # ___________________________________________________________________________________________
    # ___________________________________________________________________________________________
    elif variable.get() == "°C" and variable1.get() == "°Ra":
        variable4.set(round(((variable3.get()) - 491.67) * 5 / 9, 2))
    elif variable.get() == "°Ra" and variable1.get() == "°C":
        variable4.set(round(((variable3.get()) + 273.15) * 9 / 5, 2))
    # ___________________________________________________________________________________________
    elif variable.get() == "K" and variable1.get() == "°Ra":
        variable4.set(round((variable3.get()) * 5 / 9, 2))
    elif variable.get() == "°Ra" and variable1.get() == "K":
        variable4.set(round((variable3.get()) * 9 / 5, 2))
    # ___________________________________________________________________________________________
    elif variable.get() == "°F" and variable1.get() == "°Ra":
        variable4.set(round((variable3.get()) - 459.67, 2))
    elif variable.get() == "°Ra" and variable1.get() == "°F":
        variable4.set(round((variable3.get()) + 459.67, 2))
    # ___________________________________________________________________________________________
    # ___________________________________________________________________________________________
    elif variable.get() == "°C" and variable1.get() == "°De":
        variable4.set(round(100 - (variable3.get()) * 2 / 3, 2))
    elif variable.get() == "°De" and variable1.get() == "°C":
        variable4.set(round((100 - (variable3.get())) * 3 / 2, 2))
    # ___________________________________________________________________________________________
    elif variable.get() == "K" and variable1.get() == "°De":
        variable4.set(round(373.15 - (variable3.get()) * 2 / 3, 2))
    elif variable.get() == "°De" and variable1.get() == "K":
        variable4.set(round((373.15 - (variable3.get())) * 1.5, 2))
    # ___________________________________________________________________________________________
    elif variable.get() == "°F" and variable1.get() == "°De":
        variable4.set(round(212 - (variable3.get()) * 6 / 5, 2))
    elif variable.get() == "°De" and variable1.get() == "°F":
        variable4.set(round((212 - (variable3.get())) * 5 / 6, 2))
    # ___________________________________________________________________________________________
    elif variable.get() == "°Ra" and variable1.get() == "°De":
        variable4.set(round(671.67 - (variable3.get()) * 6 / 5, 2))
    elif variable.get() == "°De" and variable1.get() == "°Ra":
        variable4.set(round((671.67 - (variable3.get())) * 5 / 6, 2))
    # ___________________________________________________________________________________________
    # ___________________________________________________________________________________________
    elif variable.get() == "°N" and variable1.get() == "°C":
        variable4.set(round((variable3.get()) * 33 / 100, 2))
    elif variable.get() == "°C" and variable1.get() == "°N":
        variable4.set(round((variable3.get()) * 100 / 33, 2))
    # ___________________________________________________________________________________________
    elif variable.get() == "°N" and variable1.get() == "°F":
        variable4.set(round(((variable3.get()) - 32) * 11 / 60, 2))
    elif variable.get() == "°F" and variable1.get() == "°N":
        variable4.set(round((variable3.get()) * 60 / 11 + 32, 2))
    # ___________________________________________________________________________________________
    elif variable.get() == "°N" and variable1.get() == "K":
        variable4.set(round(((variable3.get()) - 273.15) * 33 / 100, 2))
    elif variable.get() == "K" and variable1.get() == "°N":
        variable4.set(round((variable3.get()) * 100 / 33 + 273.15, 2))
    # ___________________________________________________________________________________________
    elif variable.get() == "°N" and variable1.get() == "°Ra":
        variable4.set(round(((variable3.get()) - 491.67) * 11 / 60, 2))
    elif variable.get() == "°Ra" and variable1.get() == "°N":
        variable4.set(round((variable3.get()) * 60 / 11 + 491.67, 2))
    # ___________________________________________________________________________________________
    elif variable.get() == "°N" and variable1.get() == "°De":
        variable4.set(round(33 - (variable3.get()) * 11 / 50, 2))
    elif variable.get() == "°De" and variable1.get() == "°N":
        variable4.set(round((33 - (variable3.get())) * 50 / 11, 2))
    # ___________________________________________________________________________________________
    # ___________________________________________________________________________________________
    elif variable.get() == "°C" and variable1.get() == "°Re":
        variable4.set(round((variable3.get()) * 5 / 4, 2))
    elif variable.get() == "°Re" and variable1.get() == "°C":
        variable4.set(round((variable3.get()) * 4 / 5, 2))
    # ___________________________________________________________________________________________
    elif variable.get() == "°F" and variable1.get() == "°Re":
        variable4.set(round((variable3.get()) * 9 / 4 + 32, 2))
    elif variable.get() == "°Re" and variable1.get() == "°F":
        variable4.set(round(((variable3.get()) - 32) * 4 / 9, 2))
    # ___________________________________________________________________________________________
    elif variable.get() == "°Re" and variable1.get() == "K":
        variable4.set(round(((variable3.get()) - 273.15) * 4 / 5, 2))
    elif variable.get() == "K" and variable1.get() == "°Re":
        variable4.set(round((variable3.get()) * 5 / 4 + 273.15, 2))
    # __________________________________________________________________________________________
    elif variable.get() == "°Ra" and variable1.get() == "°Re":
        variable4.set(round((variable3.get()) * 9 / 4 + 491.67, 2))
    elif variable.get() == "°Re" and variable1.get() == "°Ra":
        variable4.set(round(((variable3.get()) - 491.67) * 4 / 9, 2))
    # ___________________________________________________________________________________________
    elif variable.get() == "°Re" and variable1.get() == "°De":
        variable4.set(round(80 - (variable3.get()) * 8 / 15, 2))
    elif variable.get() == "°De" and variable1.get() == "°Re":
        variable4.set(round((80 - (variable3.get())) * 15 / 8, 2))
    # ___________________________________________________________________________________________
    elif variable.get() == "°N" and variable1.get() == "°Re":
        variable4.set(round((variable3.get()) * 33 / 80, 2))
    elif variable.get() == "°Re" and variable1.get() == "°N":
        variable4.set(round((variable3.get()) * 80 / 33, 2))
    # ___________________________________________________________________________________________
    # ___________________________________________________________________________________________

    elif variable.get() == "°C" and variable1.get() == "°Rø":
        variable4.set(round(((variable3.get()) - 7.5) * 40 / 21, 2))
    elif variable.get() == "°Rø" and variable1.get() == "°C":
        variable4.set(round((variable3.get()) * 21 / 40 + 7.5, 2))
    # ___________________________________________________________________________________________
    elif variable.get() == "°F" and variable1.get() == "°Rø":
        variable4.set(round(((variable3.get()) - 7.5) * 24 / 7 + 32, 2))
    elif variable.get() == "°Rø" and variable1.get() == "°F":
        variable4.set(round(((variable3.get()) - 32) * 7 / 24 + 7.5, 2))
    # ___________________________________________________________________________________________
    elif variable.get() == "°Rø" and variable1.get() == "K":
        variable4.set(round(((variable3.get()) - 273.15) * 21 / 40 + 7.5, 2))
    elif variable.get() == "K" and variable1.get() == "°Rø":
        variable4.set(round(((variable3.get()) - 7.5) * 40 / 21 + 273.15, 2))
    # ___________________________________________________________________________________________
    elif variable.get() == "°Ra" and variable1.get() == "°Rø":
        variable4.set(round(((variable3.get()) - 7.5) * 24 / 7 + 491.67, 2))
    elif variable.get() == "°Rø" and variable1.get() == "°Ra":
        variable4.set(round(((variable3.get()) - 491.67) * 7 / 24 + 7.5, 2))
    # ___________________________________________________________________________________________
    elif variable.get() == "°Rø" and variable1.get() == "°De":
        variable4.set(round(60 - (variable3.get()) * 7 / 20, 2))
    elif variable.get() == "°De" and variable1.get() == "°Rø":
        variable4.set(round((60 - (variable3.get())) * 20 / 7, 2))
    # ___________________________________________________________________________________________
    elif variable.get() == "°N" and variable1.get() == "°Rø":
        variable4.set(round(((variable3.get()) - 7.5) * 22 / 35, 2))
    elif variable.get() == "°Rø" and variable1.get() == "°N":
        variable4.set(round((variable3.get()) * 35 / 22 + 7.5, 2))
    # ___________________________________________________________________________________________
    elif variable.get() == "°Rø" and variable1.get() == "°Re":
        variable4.set(round((variable3.get()) * 21 / 32 + 7.5, 2))
    elif variable.get() == "°Re" and variable1.get() == "°Rø":
        variable4.set(round(((variable3.get()) - 7.5) * 32 / 21, 2))


# ___________________________________________________________________________________________
# Temperatūrų atradėju tekstai ir nuotraukos
def celsijus():
    global photo1
    af.config(
        text="Andersas Celsijus (gimė - 1701 m. lapkričio 27 d. Upsaloje, mirė – 1744 m. balandžio 25 d.) – švedų "
             "astronomas.\n\n 1742 m. sukūrė 100 laipsnių termometrą, kuris dabar naudojamas daugelyje pasaulio "
             "šalių.\n\n Vandens virimo temperatūrą jis pažymėjo 100 laipsnių, o ledo tirpimo temperatūrą 0 "
             "laipsnių.\n\n Celsijus dirbo Upsalos universiteto profesoriumi, nuo 1740 m. Upsalos observatorijos "
             "direktoriumi.\n\n Jis dalyvavo topografiniuose Laplandijos bei Peru tyrimuose, kurių rezultatai "
             "patvirtino Niutono hipotezę, kad Žemė plokštėja.\n\n Jis stengėsi, kad būtų įvestas Grigaliaus "
             "kalendorius. Be to jis pirmą kartą įrodė šiaurės pašvaistės ir magnetinio lauko ryšį.")
    photo1 = PhotoImage(file="Celsijus.gif")
    photo1 = photo1.zoom(dydis1)
    photo1 = photo1.subsample(dydis)
    nuotrauka1.config(image=photo1)


def kelvinas():
    global photo1
    af.config(
        text="Viljamas Tomsonas-Kelvinas (gimė – 1824 m. birželio 26 d. Belfaste, mirė – 1907 m. gruodžio 17 d. "
             "Largse) - anglų fizikas.\n\nPadėjo suformuluoti Antrąjį termodinamikos dėsnį. 1848 m. sudarė "
             "absoliutinę temperatūros skalę.\n\n Plėtojo elektromagn. virpesių teoriją, sudarė kontūro virpesių "
             "periodo ir kontūro talpos bei induktyvumo sąryšio formulę.\n\n Apskaičiavo molekulių matmenis pagal "
             "skysčio plėvelės paviršinę energiją.\n\n 1870 m. nustatė sočiųjų garų tamprumo priklausomybę nuo "
             "skysčio paviršiaus formos.\n\n 1881 m. Tomsonas įėjo į komisiją, kuri sudarė pirmąją suderintą elektros "
             "vienetų sistemą.")
    photo1 = PhotoImage(file="kelvinas.gif")
    photo1 = photo1.zoom(dydis1)
    photo1 = photo1.subsample(dydis)
    nuotrauka1.config(image=photo1)


def farenheitas():
    global photo1
    af.config(
        text="Gabrielis Danielis Farenheitas (gimė - 1686 m. gegužės 24 d. Gdanske, mirė - 1736 m. rugsėjo 16 d. "
             "Hagoje) – vokiečių fizikas ir inžinierius.\n\nFarenheitas pagamino šiuolaikinės formos termometrą, "
             "naudojantį alkoholį, o vėliau termometrams panaudojo gyvsidabrį.\n\n Jis sudarė Farenheito skalę, "
             "kuri buvo plačiai naudojama Europoje iki Celsijaus skalės įvedimo.\n\n Farenheito skalėje 0 °F yra "
             "vandens užšalimo temperatūra, 32 °F - ledo tirpimo taškas, o 98 °F – sveiko žmogaus kūno "
             "temperatūra.\n\n Jo pavarde buvo pavadintas ir temperatūros matavimo vienetas – Farenheito "
             "laipsnis.\n\n Buvo įrengęs dirbtuves, kuriose gaminti termometrai, areometrai, barometrai. ")
    photo1 = PhotoImage(file="farenheitas.gif")
    photo1 = photo1.zoom(dydis1)
    photo1 = photo1.subsample(dydis)
    nuotrauka1.config(image=photo1)


def rankine():
    global photo1
    af.config(
        text="Wiliamas Johnas Macquornas Rankine (gimė - 1820 m. liepos 5 d. Edinburge, mirė - 1872 m. gruodžio 24 d. "
             "Glazge) - škotų inžinierius, fizikas.\n\nJis sukūrė Rankinės skalę, susiejusia su Kelvino temperatūros "
             "skale, tačiau Fahrenheito laipsniais, o ne Celsijaus laipsniais.\n\nRankine sukūrė išsamią garo "
             "variklio ir visų šilumos variklių teoriją.\n\nJis paskelbė kelis šimtus mokslo ir inžinerijos "
             "leidinių.\n\nJo inžinerijos mokslo ir praktikos vadovai buvo naudojami daugelį dešimtmečių po jų "
             "paskelbimo.\n\nJis buvo entuziastingas mėgėjiškas dainininkas, pianistas ir violončelininkas, "
             "kuris kūrė savo humoristines dainas.")
    photo1 = PhotoImage(file="rankine.gif")
    photo1 = photo1.zoom(dydis1)
    photo1 = photo1.subsample(dydis)
    nuotrauka1.config(image=photo1)


def delislis():
    global photo1
    af.config(
        text="\n\nJosephas-Nicolas Delislis (gimė - 1688 m. balandžio 4 d. Paryžiuje, mirė - 1768 m. rugsėjo 11 d. "
             "Paryžiuje) - prancūzų astronomas, kartografas.\n\n1712 m. Liuksemburgo rūmuose įsteigė observatoriją ir "
             "po trejų metų persikėlė į „Hotel de Taranne“.\n\n1725 m. jis buvo išrinktas karališkosios draugijos "
             "nariu ir 1749 m. - Švedijos karališkosios mokslų akademijos užsienio nariu.\n\n1732 m. Delislis sukūrė "
             "termometrą, kuriame gyvsidabris naudojamas kaip darbinis skystis.\n\n1740 m. Delislis vyko ekspedicija "
             "į Sibirą, siekiant stebėti Beryozovo gyvsidabrio tranzitą per saulę.\n\nEkspedicijos metu jis užfiksavo "
             "daugybę ornitologinių, botaninių, zoologinių, geografinių ir kitų mokslinių pastabų.\n\n")
    photo1 = PhotoImage(file="delislis.gif")
    photo1 = photo1.zoom(dydis1)
    photo1 = photo1.subsample(dydis)
    nuotrauka1.config(image=photo1)


def niutonas():
    global photo1
    af.config(
        text="Izaokas Niutonas (gimė - 1643 m. sausio 4 d. Linkolšyre, mirė – 1727 m. kovo 31 d. Kensingtone) – anglų "
             "fizikas, matematikas, astronomas.\n\n1668 m. jis suprojektavo ir faktiškai sukonstravo pirmąjį "
             "atspindintį teleskopą — tokio tipo teleskopai naudojami ir šiandien.\n\n Niutono svarbiausias įnašas į "
             "matematikos mokslą buvo integralinio skaičiavimo atradimas, kurį jis padarė, būdamas dvidešimt trejų "
             "metų.\n\n 1687 m. jis išleido savo didįjį veikalą „Natūralios filosofijos matematiniai principai”, "
             "kuriame išdėstė gravitacijos ir judėjimo dėsnius.\n\nNiutonas išrado Niutono skalę: apibūdino „nulinę "
             "šilumos temperatūrą“ kaip tirpstantį sniegą ir „33 laipsnius šilumos“ kaip verdantį vandenį.\n\nŠis "
             "žmogus suformulavo pagrindinius mechanikos dėsnius, atrado baltos šviesos skaidymo dėsnį ir sukūrė "
             "korpuskulinę šviesos teoriją.")
    photo1 = PhotoImage(file="niutonas.gif")
    photo1 = photo1.zoom(dydis1)
    photo1 = photo1.subsample(dydis)
    nuotrauka1.config(image=photo1)


def reaumoras():
    global photo1
    af.config(
        text="René Antoinas Ferchaultas de Réaumuras (gimė - 1683 m. vasario 28 d. , mirė – 1757 m. spalio 17 d.) – "
             "prancūzų entomologas, rašytojas.\n\nRéaumuras sukūrė kupolinę krosnį, kuri yra vis dar ekonomiškiausias "
             "ir dažniausiai naudojamas pilkojo geležies lydymo procesas.\n\nJis išrado Réumumuro termometrą ir "
             "pažymėjo temperatūros skalę: nulio laipsniu - užšalimo tašką ir aštuoniasdešimt laipsniais - virimo "
             "tašką.\n\nJo pastangos atnešė daug naujų pramonės šakų į Prancūziją, todėl apie dvylika kartų jis tapo "
             "Prancūzijos mokslų akademijos direktoriumi.\n\n1734 m. Réumumuris paskelbė pirmąjį savo leidinį. Nors "
             "jis buvo ir nebaigtas, tai buvo svarbus pasiekimas entomologijos istorijoje.\n\nJis ištyrė cheminę "
             "porceliano sudėtį ir 1740 m. sukūrė savo formulę vadinamajam Réumumuro porcelianui.")
    photo1 = PhotoImage(file="reumeris.gif")
    photo1 = photo1.zoom(dydis1)
    photo1 = photo1.subsample(dydis)
    nuotrauka1.config(image=photo1)


def romeris():
    global photo1
    af.config(
        text="\n\nOle Christensenas Romeris (gimė - 1644 m. rugsėjo 25 d. Orhuse, mirė – 1710 m. rugsėjo 19 d. "
             "Kopenhagoje) – danų astronomas.\n\nJis 1676 m. pirmasis pasaulyje išmatavo šviesos greitį.\n\nRomeris "
             "turi temperatūros skalę pavadinta jo vardu, nes jis ją atrado 1701 m. .\n\nFarenheito skalės išradėjas, "
             "daug išmoko naudodamasis jo darbais ir didindamas dalinį keturiais kartais, taip gaudamas Farenheito "
             "skalę.\n\n1672 m. Romeris kartu su Pikardu grįžo į Prancūziją ir pradėjo dirbti karališkoje "
             "observatorijoje Paryžiuje.\n\nVėliau Romeris tapo antruoju Kopenhagos policijos viršininku ir padėjo "
             "kontroliuoti neturtingus.\n\n")
    photo1 = PhotoImage(file="romeris.gif")
    photo1 = photo1.zoom(dydis1)
    photo1 = photo1.subsample(dydis)
    nuotrauka1.config(image=photo1)


# ___________________________________________________________________________________________
# Klausiama ar nori išeiti iš programos
def isejimas():
    ats = messagebox.askyesno("Išėjimas", "Ar norite išeiti iš šios programos?")
    if ats:
        pg.destroy()

    # ___________________________________________________________________________________________


# Nustatomi lango parametrai
pg = Tk()
plotis = pg.winfo_screenheight()
ilgis = pg.winfo_screenwidth()
pg.geometry("%dx%d" % (ilgis, plotis))
pg.config(background="#F6F6F6")
pg.resizable(False, False)
pg.attributes("-fullscreen", True)
# ___________________________________________________________________________________________
# Įdedamas lango išjungimo mygtukas
d = Button(pg, text="X", font=("Arial", "17", "bold"), bg="red", command=isejimas)
d.place(x=ilgis - 36, y=0)
# ___________________________________________________________________________________________
# Nustatomi šrifto dydis pagal rezoliuciją
if ilgis <= 1200 or plotis <= 700:
    sriftas = "6"
    sriftas1 = 7
    atimam = -1
    dydis = 2
    dydis1 = 1
elif 1200 < ilgis < 1600 or 700 < plotis <= 900:
    sriftas = "10"
    sriftas1 = 9
    atimam = -1
    dydis = 3
    dydis1 = 2
else:  # Panašiai su šia rezoliucija buvo daryta programa
    sriftas = "12"
    atimam = 0
    sriftas1 = 12
    dydis = 1
    dydis1 = 1
f = ("Times", sriftas, "bold")
# ___________________________________________________________________________________________
# Antraštė
Label(pg, text="Temperatūrų konvertavimas", bg="#F6F6F6", font=("Times", "25", "bold underline")).pack(pady=ilgis / 40)
# ___________________________________________________________________________________________
# Temperatūrų konvertavimo aparato rėmai ir atradėjų informacijos rėmai
a = Frame(pg, bd=5, relief=RIDGE, bg="#F6F6F6")
a.pack(pady=ilgis / 150)
b = LabelFrame(pg, labelanchor="n", text="Temperatūrų atradėjai", font=("Times", "25", "bold"), bd=5, relief=RIDGE,
               bg="#F6F6F6")
b.pack(pady=ilgis / 150, anchor="n", padx=plotis / 50, fill=X, expand=True)
# ___________________________________________________________________________________________
# Sukūriamas pirmas temperatūros pasirinkimo meniu
variable = StringVar()
variable.set("°C")
w = OptionMenu(a, variable, "°C", "K", "°F", "°Ra", "°De", "°N", "°Re", "°Rø")
w.grid(row=0, column=1)
w.configure(width=3, justify=CENTER, highlightthickness=0)
# ___________________________________________________________________________________________
# Sukūriamas antras temperatūros pasirinkimo meniu
variable1 = StringVar()
variable1.set("°C")
g = OptionMenu(a, variable1, "°C", "K", "°F", "°Ra", "°De", "°N", "°Re", "°Rø")
g.grid(row=0, column=5, padx=15)
g.configure(width=3, justify=CENTER, highlightthickness=0)
# ___________________________________________________________________________________________
# Sukūriama pirma temperatūros įrašymo vieta
variable3 = DoubleVar()
wg = Spinbox(a, justify=CENTER, command=YIX, from_=-9999999999999999999999999, to=9999999999999999999999999,
             textvariable=variable3, increment=0.1, width=20, font="10", bg="#F6F6F6")
wg.grid(row=0, column=4)
# ___________________________________________________________________________________________
# Sukūriama antra temperatūros įrašymo vieta
variable4 = DoubleVar()
wgf = Spinbox(a, command=XIY, justify=CENTER, from_=-9999999999999999999999999, to=9999999999999999999999999,
              textvariable=variable4, increment=0.1, width=20, font="10", bg="#F6F6F6")
wgf.grid(row=0, column=0, padx=15)
# ___________________________________________________________________________________________
# Patalpinamos kovertavimo rodyklės
photo = PhotoImage(file="ezgif.com-gif-maker.gif")
photo = photo.subsample(3)
nuotrauka = Label(a, image=photo, bd=0, highlightthickness=0)
nuotrauka.grid(row=0, column=2, padx=15, pady=15)
# ___________________________________________________________________________________________
# Kai tarp įrašymo vietų kažkas atleidžia klavišą, yra išsiunčiama komanda į funkciją.
wg.bind("<KeyRelease>", YIX)
wgf.bind("<KeyRelease>", XIY)
# ___________________________________________________________________________________________
# Sekama, jei pasikeičia temperatūrų tipai, siunčiamos komandos į funkciją.
variable.trace("w", XIY)
variable1.trace("w", XIY)
# ___________________________________________________________________________________________
# Padaromas pradinis temperatūrų atradėjų informacijos langas, šiuo atveju jis yra moksl. Celsijaus informacija.
photo1 = PhotoImage(file="Celsijus.gif")
photo1 = photo1.zoom(dydis1)
photo1 = photo1.subsample(dydis)
nuotrauka1 = Label(b, image=photo1, bd=5, highlightthickness=0, relief=RIDGE)
nuotrauka1.pack(side="right", padx=10, pady=10)
af = Label(b, bg="#F6F6F6", font=("Times", sriftas1, "italic"), justify=RIGHT,
           text="Andersas Celsijus (gimė - 1701 m. lapkričio 27 d. Upsaloje, mirė – 1744 m. balandžio 25 d.) – švedų "
                "astronomas.\n\n 1742 m. sukūrė 100 laipsnių termometrą, kuris dabar naudojamas daugelyje pasaulio "
                "šalių.\n\n Vandens virimo temperatūrą jis pažymėjo 100 laipsnių, o ledo tirpimo temperatūrą 0 "
                "laipsnių.\n\n Celsijus dirbo Upsalos universiteto profesoriumi, nuo 1740 m. Upsalos observatorijos "
                "direktoriumi.\n\n Jis dalyvavo topografiniuose Laplandijos bei Peru tyrimuose, kurių rezultatai "
                "patvirtino Niutono hipotezę, kad Žemė plokštėja.\n\n Jis stengėsi, kad būtų įvestas Grigaliaus "
                "kalendorius. Be to jis pirmą kartą įrodė šiaurės pašvaistės ir magnetinio lauko ryšį.")
af.pack(side=RIGHT, anchor="e", padx=10)
# ___________________________________________________________________________________________
# Cikle išdėliojami mygtukai su funkcijomis
A = ["Andersas Celsijus (°C)", "Viljamas Tomsonas-Kelvinas (K)", "Gabrielis Danielis Farenheitas (°F)",
     "Wiliamas Johnas Macquornas Rankine (°Ra)", "Josephas-Nicolas Delislis (°De)", "Izaokas Niutonas (°N)",
     "René Antoinas Ferchaultas de Réaumuras (°Re)", "Ole Christensenas Romeris (°Rø)"]
B = [celsijus, kelvinas, farenheitas, rankine, delislis, niutonas, reaumoras, romeris]
for x in range(8):
    Button(b, text=A[x], font=f, width=40, command=B[x]).pack(padx=15 + atimam * 10, pady=5 + 3 * atimam, anchor="w")
mainloop()
