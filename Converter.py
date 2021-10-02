import time

def Time_Convert():
   def Mill_to_Sec():
        Time = int(input("Please enter the amount of Milliseconds you wish to convert: "))
        Seconds = Time / 1000
        print("That is " + str(Seconds) + " Seconds")
        Retry()

   def Sec_to_Mill():
        Time = int(input("Enter the amount of Seconds you wish to convert: "))
        Mill = Time * 1000
        print("That is " + str(Mill) + " Milliseconds")
        Retry()

   def Sec_to_Min():
        Time = int(input("Please enter the amount of seconds you wish to convert: "))
        Minutes = Time / 60
        print("That is " + str(Minutes) + " Minutes")
        Retry()

   def Min_to_Sec():
        Time = int(input("Please enter the amount of Minutes you wish to convert: "))
        Seconds = Time * 60
        print("That is " + str(Seconds) + " Seconds")
        Retry()

   def Min_to_Hour():
        Time = int(input("Please enter the amount of minutes you wish to convert: "))
        Hours = Time / 60
        print("That is " + str(Hours) + " Hours")
        Retry()

   def Hour_to_Min():
        Time = int(input("Please enter the amount of Hours you wish to convert: "))
        Minutes = Time * 60
        print("That is " + str(Minutes) + " Minutes")
        Retry()

   def Hour_to_Day():
        Time = int(input("Please enter the amount of hours you wish to convert: "))
        Days = Time / 24
        print("That is " + str(Days) + " Days")
        Retry()

   def Day_to_Hour():
        Time = int(input("Please enter the amount of Days you want to convert: "))
        Hours = Time * 24
        print("That is " + str(Hours) + " Hours")
        Retry()

   def Day_to_Year():
        Time = int(input("Please enter the amount of days you wish to convert: "))
        Years = Time / 365
        print("That is " + str(Years) + " Years")
        Retry()

   def Year_to_Day():
        Time = int(input("Please enter the amount of Years you wish to convert: "))
        Days = Time * 365
        print("That is " + str(Days) + " Days")
        Retry()

   def Retry():
        Retry = input("Would you like to convert again or go to menu: ")
        if Retry == "Again":
            Menu()
        elif Retry == "Menu":
            Main_Menu()
        else:
            print("Goodbye have a nice day")
            time.sleep(4)

   def Menu():
        Option = input("What would you like to convert" + "\n Milliseconds to Seconds (MS)" +"\n Seconds to Milliseconds (SMi)" + "\n Minutes to Seconds (MSe)" + "\n Hours to Minutes (HM)" + "\n Days to Hours (DH)" +"\n Years to Days (YD)" + "\n Seconds to Minutes (SM)" + "\n Minutes to Hour (MH)" + "\n Hours to Days (HD)" + "\n Days to Years (DY)" + "\n Which abbreviation do you choose: ")
        if Option == "MS":
            Mill_to_Sec()
        elif Option == "SMi":
            Sec_to_Mill()
        elif Option == "SM":
            Sec_to_Min()
        elif Option == "MSe":
            Min_to_Sec()
        elif Option == "MH":
            Min_to_Hour()
        elif Option == "HM":
            Hour_to_Min()
        elif Option == "HD":
            Hour_to_Day()
        elif Option == "DH":
            Day_to_Hour()
        elif Option == "DY":
            Day_to_Year()
        elif Option == "YD":
            Year_to_Day()
        else:
            print("That is currently not supported")
            time.sleep(4)
   Menu()

def Weight_Convert():

    def Gram_to_Ounce():
        Gram = int(input("How many grams are you converting: "))
        Ounce = Gram / 28.35
        print("That is aproximatley " + str(Ounce) + " Ounces")
        Retry()

    def Gram_to_Pound():
        Gram = int(input("How many grams are you converting: "))
        Pounds = Gram / 454
        print("That is aproximatly " + str(Pounds) + " Pounds")
        Retry()

    def Ounce_to_Gram():
        Ounce = int(input("How many ounces are you converting: "))
        Gram = Ounce * 28.35
        print("That is aproximatley " + str(Gram) + " Grams")
        Retry()

    def Ounce_to_Pound():
        Ounce = int(input("How many ounces are you converting: "))
        Pound = Ounce / 16
        print("That is " + str(Pound) + " Pounds")
        Retry()

    def Pound_to_Ounce():
        Pound = int(input("How many pounds are you coverting: "))
        Ounce = Pound * 16
        print("That is " + str(Ounce) + " Ounces")
        Retry()

    def Pound_to_Gram():
        Pound = int(input("How many pounds are you converting: "))
        Gram = Pound * 454
        print("That is aproximatly " + str(Gram) + " Grams")
        Retry()

    def Retry():
        Option = input("Would you like to convert again or go to menu: ")
        if Option == "Again":
            Menu()
        elif Option == "Menu":
            Main_Menu()

    def Menu():
        Option = input("What would you like to convert: " + "\n Grams to Ounce (GO)" + "\n Ounce to Grams (OG)" + "\n Ounce to Pound (OP)" + "\n Pound to Ounce (PO)" + "\n Pound to Grams (PG)" + "\n Grams to Pound (GP)" + "\n Which abrivition do you choose: ")
        if Option == "GO":
            Gram_to_Ounce()
        elif Option == "OG":
            Ounce_to_Gram()
        elif Option == "OP":
            Ounce_to_Pound()
        elif Option == "PO":
            Pound_to_Ounce()
        elif Option == "GP":
            Gram_to_Pound()
        elif Option == "PG":
            Pound_to_Gram()#
        else:
            print("That is not supported")
            time.sleep(4)

    Menu()

def Temp_Convert():

    def Cel_to_Fahr():
        Celsius = float(input("What is the tempertature in celsuis you wish to convert: "))
        Fahrenheit = float(Celsius * 1.8) + 32
        print("That is " + str(Fahrenheit) + "  Degrees Fahrenheit")
        Retry()

    def Cel_to_Kel():
        Celsius = float(input("What is the temperature in celsius you wish to convert: "))
        Kelvin = Celsius + 273.15
        print("That is " + str(Kelvin) + " Degrees Kelvin")
        Retry()

    def Fahr_to_Cel():
        Fahrenheit = float(input("What is the temperature in fahrenheit you wish to convert: "))
        Celsius = (Fahrenheit - 32) * 0.555555556
        print("That is aproximatly " + str(Celsius) + " Degrees Celsius")
        Retry()

    def Fahr_to_Kel():
        Fahrenheit = float(input("What is the temperature in fahrenheit you wish to convert: "))
        Kelvin = (Fahrenheit - 32) * 0.555555556 + 273.15
        print("That is aproximatly " + str(Kelvin) + " Degrees Kelvin")
        Retry()

    def Kel_to_Cel():
        Kelvin = float(input("What is the temperature in kelvin you wish to convert: "))
        Celsius = Kelvin * 273.15
        print("That is " + str(Celsius) + " Degrees Celsius")
        Retry()

    def Kel_to_Fahr():
        Kelvin = float(input("What is the temperature in kelvin you wish to convert: "))
        Fahrenheit = (Kelvin - 273.15) * 1.8 + 32
        print("That is " + str(Fahrenheit) + " Degrees Fahrenheit")
        Retry()

    def Retry():
        Again = input("Would you like to go again or go to menu?: ")
        if Again == "Again":
            Menu()
        elif Again == "Menu":
            Main_Menu()
        else:
            print("Goodbye")
            time.sleep(4)

    def Menu():
        Option = input("What would you like to convert" + "\n Celcius to Fahrenheit (CF)" + "\n Celsius to Kelvin (CK)" + "\n Fahrenheit to Celsius (FC)" + "\n Fahrenheit to Kelvin (FK)" + "\n Kelvin to Celsius (KC)" + "\n Kelvin to Fahrenheit (KF)" + "\n What abrivitaion do you choose: ")
        if Option == "CF":
            Cel_to_Fahr()
        elif Option == "CK":
            Cel_to_Kel()
        elif Option == "FC":
            Fahr_to_Cel()
        elif Option == "FK":
            Fahr_to_Kel()
        elif Option == "KC":
            Kel_to_Cel()
        elif Option == "KF":
            Kel_to_Fahr()
        else:
            print("That is not supported")
            time.sleep(4)

    Menu()

def Speed_Convert():

   def MpS_to_MpH():
        Speed = float(input("Please enter the speed you wish to convert: "))
        MpH = Speed * 3600
        print("That is " + str(MpH) + " Meters per Hours")
        Retry()

   def MpS_to_KpS():
        Speed = float(input("Please enter the speed you wish to convert: "))
        KpS = Speed / 1000
        print("That is " + str(KpS) + " Kilometers per second")
        Retry()

   def MpS_to_KpH():
        Speed = float(input("Please enter the speed you wish to convert: "))
        KpH = Speed * 3.6
        print("That is " + str(KpH) + "Kilometers per Hour")
        Retry()

   def MpS_to_IpS():
        Speed = float(input("Please enter the speed you wish to convert: "))
        IpS = Speed *39.37
        print("That is " + str(IpS) + " Inches per Second")
        Retry()

   def MpS_to_IpH():
        Speed = float(input("Please enter the speed you wish to convert: "))
        IpH = Speed * 141732
        print("That is " + str(IpH) + " Inches per Hour")
        Retry()

   def MpS_to_FpS():
        Speed = float(input("Please enter the speed you wish to convert: "))
        FpS = Speed * 3.281
        print("That is " + str(FpS) + " Feet per Second")
        Retry()

   def MpS_to_FpH():
        Speed = float(input("Please enter the speed you wish to convert: "))
        FpH = Speed * 11811
        print("That is " + str(FpH) + " Feet per Hour")
        Retry()

   def MpS_to_MIpS():
        Speed = float(input("Please enter the speed you wish to convert: "))
        MIpS = Speed / 1609
        print("That is " + str(MIpS) + " Miles per Second")
        Retry()

   def MpS_to_MIpH():
        Speed = float(input("Please enter the speed you wish to convert: "))
        MIpH = Speed * 2.237
        print("That is " + str(MIpH) + " Miles per Hour")
        Retry()

   def MpS_to_Knots():
        Speed = float(input("Please enter the speed you wish to convert: "))
        Knots = Speed * 1.944
        print("That is " + str(Knots) + " Knots")
        Retry()

   def MpH_to_MpS():
        Speed = float(input("Please enter the speed you wish to convert: "))
        MpS = Speed / 3600
        print("That is " + str(MpS) + " Meters per Seconds")
        Retry()

   def MpH_to_KpS():
        Speed = float(input("Please enter the speed you wish to convert: "))
        KpS = Speed / 3.6e+6
        print("That is " + str(KpS) + " Kilometers per Second")
        Retry()

   def MpH_to_KpH():
        Speed = float(input("Please enter the speed you wish to convert: "))
        KpH = Speed / 1000
        print("That is " + str(KpH) + " Kilometers per Hour")
        Retry()

   def MpH_to_IpS():
        Speed = float(input("Please enter the speed you wish to convert: "))
        IpS = Speed / 91.44
        print("That is " + str(IpS) + " Inches per Second")
        Retry()

   def MpH_to_IpH():
        Speed = float(input("Please enter the speed you wish to convert: "))
        IpH = Speed * 39.37
        print("That is " + str(IpH) + " Inches per Hour")
        Retry()

   def MpH_to_FpS():
        Speed = float(input("Please enter the speed you wish to convert: "))
        FpS = Speed / 1097
        print("That is " + str(FpS) + "Feet per Second")
        Retry()

   def MpH_to_FpH():
        Speed = float(input("Please enter the speed you wish to convert: "))
        FpH = Speed * 3.281
        print("That is " + str(FpH) + " Feet per Hour")
        Retry()

   def MpH_to_MIpS():
        Speed = float(input("Please enter the speed you wish to convert: "))
        MIpS = Speed / 5.794e+6
        print("That is " + str(MIpS) + " Miles per Second")
        Retry()

   def MpH_to_MIpH():
        Speed = float(input("Please enter the speed you wish to convert: "))
        MIpH = Speed / 1609
        print("That is " + str(MIpH) + " Miles per Hour")
        Retry()

   def MpH_to_Knots():
        Speed = float(input("Please enter the speed you wish to convert: "))
        Knots = Speed / 1852
        print("That is " + str(Knots) + " Knots")
        Retry()

   def KpS_to_MpS():
        Speed = float(input("Please enter the speed you wish to convert: "))
        MpS = Speed * 1000
        print("That is " + str(MpS) + " Meters per Second")
        Retry()

   def KpS_to_MpH():
        Speed = float(input("Please enter the speed you wish to convert: "))
        MpH = Speed * 3600000
        print("That is " + str(MpH) + " Meters per Hour")
        Retry()

   def KpS_to_KpH():
        Speed = float(input("Please enter the speed you wish to convert: "))
        KpH = Speed * 3600
        print("That is " + str(KpH) + " Kilometers per Hour")
        Retry()

   def KpS_to_IpS():
        Speed = float(input("Please enter the speed you wish to convert: "))
        IpS = Speed * 39370
        print("That is " + str(IpS) + " Inches per Second")
        Retry()

   def KpS_to_IpH():
        Speed = float(input("Please enter the speed you wish to convert: "))
        IpH = Speed * 1.417e+8
        print("That is " + str(IpH) + " Inches per Hour")
        Retry()

   def KpS_to_FpS():
        Speed = float(input("Please enter the speed you wish to convert: "))
        FpS = Speed * 3281
        print("That is " + str(FpS) + " Feet per Second")
        Retry()

   def KpS_to_FpH():
        Speed = float(input("Please enter the speed you wish to convert: "))
        FpH = Speed * 1.181e+7
        print("That is " + str(FpH) + " Feet per Hour")
        Retry()

   def KpS_to_MIpS():
        Speed = float(input("Please enter the speed you wish to convert: "))
        MIpS = Speed / 1.609
        print("That is " + str(MIpS) + " Miles per Second")
        Retry()

   def KpS_to_MIpH():
        Speed = float(input("Please enter the speed you wish to convert: "))
        MIpH = Speed * 2237
        print("That is " + str(MIpH) + " Miles per Hour")
        Retry()

   def KpS_to_Knots():
        Speed = float(input("Please enter the speed you wish to convert: "))
        Knots = Speed * 1944
        print("That is " + str(Knots) + " Knots")
        Retry()

   def KpH_to_MpS():
        Speed = float(input("Please enter the speed you wish to convert: "))
        MpS = Speed / 3.6
        print("That is " + str(MpS) + " Meters per second")
        Retry()

   def KpH_to_MpH():
        Speed = float(input("Please enter the speed you wish to convert: "))
        MpH = Speed * 1000
        print("That is " + str(MpH) + " Meters per Hour")
        Retry()

   def KpH_to_KpS():
        Speed = float(input("Please enter the speed you wish to convert: "))
        KpS = Speed / 3600
        print("That is " + str(KpS) + " Kilometers per Second")
        Retry()

   def KpH_to_IpS():
        Speed = float(input("Please enter the speed you wish to convert: "))
        IpS = Speed * 10.936
        print("That is " + str(IpS) + " Inches per Second")
        Retry()

   def KpH_to_IpH():
        Speed = float(input("Please enter the speed you wish to convert: "))
        IpH = Speed * 39370
        print("That is " + str(IpH) + " Inches per Hour")
        Retry()

   def KpH_to_FpS():
        Speed = float(input("Please enter the speed you wish to convert: "))
        FpS = Speed / 1.097
        print("That is " + str(FpS) + " Feet per Second")
        Retry()

   def KpH_to_FpH():
        Speed = float(input("Please enter the speed you wish to convert: "))
        FpH = Speed * 3281
        print("That is " + str(FpH) + " Feet per Hour")
        Retry()

   def KpH_to_MIpS():
        Speed = float(input("Please enter the speed you wish to convert: "))
        MIpS = Speed / 5794
        print("That is " + str(MIpS) + " Miles per Second")
        Retry()

   def KpH_to_MIpH():
        Speed = float(input("Please enter the speed you wish to convert: "))
        MIpH = Speed / 1.609
        print("That is " + str(MIpH) + " Miles per Hour")
        Retry()

   def KpH_to_Knots():
        Speed = float(input("Please enter the speed you wish to convert: "))
        Knots = Speed / 1.852
        print("That is " + str(Knots) + " Knots")
        Retry()

   def IpS_to_MpS():
         Speed = float(input("Please enter the speed you wish to convert: "))
         MpS = Speed / 39.37
         print("That is " + str(MpS) + " Inches per Seconds")
         Retry()

   def IpS_to_MpH():
         Speed = float(input("Please enter the speed you wish to convert: "))
         MpH = Speed * 91.44
         print("That is " + str(MpH) + " Meters per Hour")
         Retry()

   def IpS_to_KpS():
         Speed = float(input("Please enter the speed you wish to convert: "))
         KpS = Speed / 39370
         print("That is " + str(KpS) + " Kilometers per second")
         Retry()

   def IpS_to_KpH():
         Speed = float(input("Please enter the speed you wish to convert: "))
         KpH = Speed / 10.936
         print("That is " + str(KpH) + " kilometers per Hour")
         Retry()

   def IpS_to_IpH():
         Speed = float(input("Please enter the speed you wish to convert: "))
         IpH = Speed * 3600
         print("That is " + str(IpH) + " Inches per Hour")
         Retry()

   def IpS_to_FpS():
         Speed = float(input("Please enter the speed you wish to convert: "))
         FpS = Speed / 12
         print("That is " + str(FpS) + " Feet per Second")
         Retry()

   def IpS_to_FpH():
         Speed = float(input("Please enter the speed you wish to convert: "))
         FpH = Speed * 300
         print("This is " + str(FpH) + " Feet per Hour")
         Retry()

   def IpS_to_MIpS():
         Speed = float(input("Please enter the speed you wish to convert: "))
         MIpS = Speed / 63360
         print("That is " + str(MIpS) + " Miles per Second")
         Retry()

   def IpS_to_MIpH():
         Speed = float(input("Please enter the speed you wish to convert: "))
         MIpH = Speed / 17.6
         print("That is " + str(MIpH) + " Miles per Hour")
         Retry()

   def IpS_to_Knots():
         Speed = float(input("Please enter the speed you wish to convert: "))
         Knots = Speed / 20.254
         print("That is " + str(Knots) + " Knots")

   def IpH_to_MpS():
         Speed = float(input("Please enter the speed you wish to convert: "))
         MpS = Speed / 141732
         print("That is " + str(MpS) + " Meters per second")
         Retry()

   def IpH_to_MpH():
         Speed = float(input("Please enter the speed you wish to convert: "))
         MpH = Speed / 39.37
         print("That is " + str(MpH) + " Meters per Hour")
         Retry()

   def IpH_to_KpS():
         Speed = float(input("Please enter the speed you wish to convert: "))
         KpS = Speed / 1.417e+8
         print("That is " + str(KpS) + " Kilometers per Seconds")
         Retry()

   def IpH_to_KpH():
         Speed = float(input("Please enter the speed you wish to convert: "))
         KpH = Speed / 39370
         print("That is " + str(KpH) + " Kilometers per Hour")
         Retry()

   def IpH_to_IpS():
         Speed = float(input("Please enter the speed you wish to convert: "))
         IpS = Speed / 3600
         print("That is " + str(IpS) + " Inches per second")
         Retry()

   def IpH_to_FpS():
         Speed = float(input("Please enter the speed you wish to convert: "))
         FpS = Speed / 43200
         print("That is " + str(FpS) + " Feet per second")
         Retry()

   def IpH_to_FpH():
         Speed = float(input("Please enter the speed you wish to convert: "))
         FpH = Speed / 12
         print("That is " + str(FpH) + " Feet per Hour")
         Retry()

   def IpH_to_MIpS():
         Speed = float(input("Please enter the speed you wish to convert: "))
         MIpS = Speed / 2.281e+8
         print("That is " + str(MIpS) + " Miles per second")
         Retry()

   def IpH_to_MIpH():
         Speed = float(input("Please enter the speed you wish to convert: "))
         MIpH = Speed / 63360
         print("That is " + str(MIpH) + " Miles per Hour")
         Retry()

   def IpH_to_Knots():
         Speed = float(input("Please enter the speed you wish to convert: "))
         Knots = Speed / 72913
         print("That is " + str(Knots) + " Knots")
         Retry()

   def FpS_to_MpS():
         Speed = float(input("Please enter the speed you wish to convert: "))
         MpS = Speed / 3.281
         print("That is " + str(MpS) + " Meters per Second")
         Retry()

   def FpS_to_MpH():
         Speed = float(input("Please enter the speed you wish to convert: "))
         MpH = Speed * 1097
         print("That is " + str(MpH) + " Meters per Hour")
         Retry()

   def FpS_to_KpS():
         Speed = float(input("Please enter the speed you wish to convert: "))
         KpS = Speed / 3281
         print("That is " + str(KpS) + " Kilometers per second")
         Retry()

   def FpS_to_KpH():
         Speed = float(input("Please enter the speed you wish to convert: "))
         KpH = Speed * 1.097
         print("That is " + str(KpH) + " Kilometers per Hour")
         Retry()

   def FpS_to_IpS():
         Speed = float(input("Please enter the speed you wish to convert: "))
         IpS = Speed * 12
         print("That is " + str(IpS) + " Inches per Second")
         Retry()

   def FpS_to_IpH():
         Speed = float(input("Please enter the speed you wish to convert: "))
         IpH = Speed * 43200
         print("That is " + str(IpH) + " Inches per Hour")
         Retry()

   def FpS_to_FpH():
         Speed = float(input("Please enter the speed you wish to convert: "))
         FpH = Speed * 3600
         print("That is " + str(FpH) + " Feet per Hour")
         Retry()

   def FpS_to_MIpS():
         Speed = float(input("Please enter the speed you wish to convert: "))
         MIpS = Speed / 5280
         print("That is " + str(MIpS) + " Miles per Second")
         Retry()

   def FpS_to_MIpH():
         Speed = float(input("Please enter the speed you wish to convert: "))
         MIpH = Speed / 1.467
         print("That is " + str(MIpH) + " Miles per Hour")
         Retry()

   def FpS_to_Knots():
         Speed = float(input("Please enter the speed you wish to convert: "))
         Knots = Speed / 1.688
         print("That is " + str(Knots) + " Knots")
         Retry()

   def FpH_to_MpS():
         Speed = float(input("Please enter the speed you wish to convert: "))
         MpS = Speed / 11811
         print("That is " + str(MpS) + " Meters per Second")
         Retry()

   def FpH_to_MpH():
         Speed = float(input("Please enter the speed you wish to convert: "))
         MpH = Speed / 3.281
         print("That is " + str(MpH) + " Meters per Hour")
         Retry()

   def FpH_to_KpS():
         Speed = float(input("Please enter the speed you wish to convert: "))
         KpS = Speed / 1.181e+7
         print("That is " + str(KpS) + " Kilometers per Second")
         Retry()

   def FpH_to_KpH():
         Speed = float(input("Please enter the speed you wish to convert: "))
         KpH = Speed / 3281
         print("That is " + str(KpH) + " Kilometers per Hour")
         Retry()

   def FpH_to_IpS():
         Speed = float(input("Please enter the speed you wish to convert: "))
         IpS = Speed / 300
         print("That is " + str(IpS) + " Inches per Second")
         Retry()

   def FpH_to_IpH():
         Speed = float(input("Please enter the speed you wish to convert: "))
         IpH = Speed * 12
         print("That is " + str(IpH) + " Inches per Hour")
         Retry()

   def FpH_to_FpS():
         Speed = float(input("Please enter the speed you wish to convert: "))
         FpS = Speed / 3600
         print("That is " + str(FpS) + " Feet per Second")
         Retry()

   def FpH_to_MIpS():
         Speed = float(input("Please enter the speed you wish to convert: "))
         MIpS = Speed / 1.901e+7
         print("That is " + str(MIpS) + "Miles per Second")
         Retry()

   def FpH_to_MIpH():
         Speed = float(input("Please enter the speed you wish to convert: "))
         MIpH = Speed / 5280
         print("That is " + str(MIpH) + " Miles per Hour")
         Retry()

   def FpH_to_Knots():
         Speed = float(input("Please enter the speed you wish to convert: "))
         Knots = Speed / 1.68780986
         print("That is " + str(Knots) + " Knots")
         Retry()

   def MIpS_to_MpS():
         Speed = float(input("Please enter the speed you wish to convert: "))
         MpS = Speed * 1609
         print("That is " + str(MpS) + " Meters per Second")
         Retry()

   def MIpS_to_MpH():
         Speed = float(input("Please enter the speed you wish to convert: "))
         MpH = Speed * 5.794e+6
         print("That is " + str(MpH) + " Meteres per Hour")
         Retry()

   def MIpS_to_KpS():
         Speed = float(input("Please enter the speed you wish to convert: "))
         KpS = Speed * 1.609
         print("That is " + str(KpS) + " Kilometers per Second")
         Retry()

   def MIpS_to_KpH():
         Speed = float(input("Please enter the speed you wish to convert: "))
         KpH = Speed * 5794
         print("That is " + str(KpH) + " Kilometers per Hour")
         Retry()

   def MIpS_to_IpS():
         Speed = float(input("Please enter the speed you wish to convert: "))
         IpS = Speed * 63360
         print("That is " + str(IpS) + " Inches per Second")
         Retry()

   def MIpS_to_IpH():
         Speed = float(input("Please enter the speed you wish to convert: "))
         IpH = Speed * 2.281e+8
         print("That is " + str(IpH) + " Inches per Hour")
         Retry()

   def MIpS_to_FpS():
         Speed = float(input("Please enter the speed you wish to convert: "))
         FpS = Speed * 5280
         print("That is " + str(FpS) + " Feet per Second")
         Retry()

   def MIpS_to_FpH():
         Speed = float(input("Please enter the speed you wish to convert: "))
         FpH = Speed * 1.901e+7
         print("That is " + str(FpH) + " Feet per Hour")
         Retry()

   def MIpS_to_MIpH():
         Speed = float(input("Please enter the speed you wish to convert: "))
         MIpH = Speed * 3600
         print("That is " + str(MIpH) + " Miles per Hour")
         Retry()

   def MIpS_to_Knots():
         Speed = float(input("Please enter the speed you wish to convert: "))
         Knots = Speed * 3128
         print("That is " + str(Knots) + " Knots")
         Retry()

   def MIpH_to_MpS():
         Speed = float(input("Please enter the speed you wish to convert: "))
         MpS = Speed / 2.237
         print("That is " + str(MpS) + " Meters per Second")
         Retry()

   def MIpH_to_MpH():
         Speed = float(input("Please enter the speed you wish to convert: "))
         MpH = Speed * 1609
         print("That is " + str(MpH) + " Meters per Hour")
         Retry()

   def MIpH_to_KpS():
         Speed = float(input("Please enter the speed you wish to convert: "))
         KpS = Speed / 2237
         print("That is " + str(KpS) + " Kilometers per Second")
         Retry()

   def MIpH_to_KpH():
         Speed = float(input("Please enter the speed you wish to convert: "))
         KpH = Speed * 1.609
         print("That is " + str(KpH) + " Kilometers per Hour")
         Retry()

   def MIpH_to_IpS():
         Speed = float(input("Please enter the speed you wish to convert: "))
         IpS = Speed * 17.6
         print("That is " + str(IpS) + " Inches per Second")
         Retry()

   def MIpH_to_IpH():
         Speed = float(input("Please enter the speed you wish to convert: "))
         IpH = Speed * 63360
         print("That is " + str(IpH) + " Inches per Hour")
         Retry()

   def MIpH_to_FpS():
         Speed = float(input("Please enter the speed you wish to convert: "))
         FpS = Speed * 1.467
         print("That is " + str(FpS) + " Feet per Second")
         Retry()

   def MIpH_to_FpH():
         Speed = float(input("Please enter the speed you wish to convert: "))
         FpH = Speed * 5280
         print("That is " + str(FpH) + " Feet per Hour")
         Retry()

   def MIpH_to_MIpS():
         Speed = float(input("Please enter the speed you wish to convert: "))
         MIpS = Speed / 3600
         print("That is " + str(MIpS) + " Miles per Second")
         Retry()

   def MIpH_to_Knots():
         Speed = float(input("Please enter the speed you wish to convert: "))
         Knots = Speed / 1.151
         print("That is " + str(Knots) + " Knots")
         Retry()

   def Knots_to_MpS():
         Speed = float(input("Please enter the speed you wish to convert: "))
         MpS = Speed / 1.944
         print("That is " + str(MpS) + " Meters per Second")
         Retry()

   def Knots_to_MpH():
         Speed = float(input("Please enter the speed you wish to convert: "))
         MpH = Speed * 1852
         print("That is " + str(MpH) + " Meters per Hour")
         Retry()

   def Knots_to_KpS():
         Speed = float(input("Please enter the speed you wish to convert: "))
         KpS = Speed / 1944
         print("That is " + str(KpS) + " Kilometers per Second")
         Retry()

   def Knots_to_KpH():
         Speed = float(input("Please enter the speed you wish to convert: "))
         KpH = Speed * 1.852
         print("That is " + str(KpH) + " Kilometers per Hour")
         Retry()

   def Knots_to_IpS():
         Speed = float(input("Please enter the speed you wish to convert: "))
         IpS = Speed * 20.254
         print("That is " + str(IpS) + " Inches per Second")
         Retry()

   def Knots_to_IpH():
         Speed = float(input("Please enter the speed you wish to convert: "))
         IpH = Speed * 72913
         print("That is " + str(IpH) + " Inches per Hour")
         Retry()

   def Knots_to_FpS():
         Speed = float(input("Please enter the speed you wish to convert: "))
         FpS = Speed * 1.688
         print("That is " + str(FpS) + " Feet per Second")
         Retry()

   def Knots_to_FpH():
         Speed = float(input("Please enter the speed you wish to convert: "))
         FpH = Speed * 6076
         print("That is " + str(FpH) + " Feet per Hour")
         Retry()

   def Knots_to_MIpS():
         Speed = float(input("Please enter the speed you wish to convert: "))
         MIpS = Speed / 3128
         print("That is " + str(MIpS) + " Miles per Second")
         Retry()

   def Knots_to_MIpH():
         Speed = float(input("Please enter the speed you wish to convert: "))
         MIpH = Speed * 1.151
         print("That is " + str(MIpH) + " Miles per Hour")
         Retry()


   def Retry():
        Again = input("Would you like to go again or go to menu?: ")
        if Again == "Again":
            Menu()
        elif Again == "Menu":
            Main_Menu()
        else:
            print("Goodbye")
            time.sleep(4)

   def Menu():
      Option = input("Which do you choose: \n Meters per Second to Meters per Hour (mps/mph) \n Meters per Second to Kilometers per Second (mps/kps) \n Meters per Second to Kilometers per Hour (mps/kph) \n Meters per Second to Inches per Second (mps/ips) \n Meters per Second to Inches per Hour (mps/iph) \n Meters per Second to Feet per Second (mps/fps) \n Meters per Second to Feet per Hour (mps/fph) \n Meters per Second to Miles per Second (mps/mips) \n Meters per Second to Miles per Hour (mps/miph) \n Meters per Second to Knots (mps/k) \n Meters per Hour to Meters per Second (mph/mps) \n Meters per Hour to Kilometers per Second (mph/kps) \n Meters per Hour to Kilometers per Hours (mph/kph) \n Meters per Hour to Inches per Second (mph/ips) \n Meters per Hour to Inches per Hour (mph/iph) \n Meters per Hour to Feet per Second (mph/fps) \n Meters per Hour to Feet per Hour (mph/fph) \n Meters per Hour to Miles per Second (mph/mips) \n Meters per Hour to Miles per Hour (mph/miph) \n Meters per Hour to Knots (mph/k) \n Kilometers per Second to Meters per Second (kps/mps) \n Kilometers per Second to Meters per Hour (kps/mph) \n Kilometers per Second to Kilometers per Hour (kps/kph) \n Kilometers per Second to Inches per Second (kps/ips) \n Kilometers per Second to Inches per Hour (kps/iph) \n Kilometers per Second to Feet per Second (kps/fps) \n Kilometers per Second to Feet per Hour (kps/fph) \n Kilometers per Second to Miles per Second (kps/mips) \n Kilometers per Second to Miles per Hour (kps/miph) \n Kilometers per Second to Knots (kps/k) \n Kilometers per Hour to Meters per Second (kph/mps) \n Kilometers per Hour to Meters per Hour (kph/mph) \n Kilometers per Hour to Kilometers per Second (kph/kps) \n Kilometers per Hour to Inches per Second (kph/ips) \n Kilometers per Hour to Inches per Hour (kph/iph) \n Kilometers per Hour to Feet per Second (kph/fps) \n Kilometers per Hour to Feet per Hour (kph/fph) \n Kilometers per Hour to Miles per Second (kph/mips) \n Kilometers per Hour to Miles per Hour (kph/miph) \n Kilometers per Hour to Knots (kph/k) \n Inches per Second to Meters per Second (ips/mps) \n Inches per Second to Meters per Hour (ips/mph) \n Inches per Second to Kilometers per Second (ips/kps) \n Inches per Second to Kilometers per Hour (ips/kph) \n Inches per Second to Inches per Hour (ips/iph) \n Inches per Second to Feet per Second (ips/fps) \n Inches per Second to Feet per Hour (ips/fph) \n Inches per Second to Miles per Second (ips/mips) \n Inches per Second to Miles per Hour (ips/miph) \n Inches per Second to Knots (ips/k) \n Inches per Hour to Meters per Second (iph/mps) \n Inches per Hour to Meters per Hour (iph/mph) \n Inches per Hour to Kilometers per Second (iph/kps) \n Inches per Hour to Kilometers per Hour (iph/kph) \n Inches per Hour to Inches per Second (iph/ips) \n Inches per Hour to Feet per Second (iph/fps) \n Inches per Hour to Feet per Hour (iph/fph) \n Inches per Hour to Miles per Second (iph/mips) \n Inches per Hour to Miles per Hour (iph/miph) \n Inches per Hour to Knots (iph/k) \n Feet per Second to Meters per Second (fps/mps) \n Feet per Second to Meters per Hour (fps/mph) \n Feet per Second to Kilometers per Second (fps/kps) \n Feet per Second to Kilometers per Hour (fps/kph) \n Feet per Second to Inches per Second (fps/ips) \n Feet per Second to Inches per Hour (fps/iph) \n Feet per Second to Feet per Hour (fps/fph) \n Feet per Second to Miles per Second (fps/mips) \n Feet per Second to Miles per Hour (fps/miph) \n Feet per Second to Knots (fps/k) \n Feet per Hour to Meters per Second (fph/mps) \n Feet per Hour to Meters per Hour (fph/mph) \n Feet per Hour to Kilometers per Second (fph/kps) \n Feet per Hour to Kilometers per Hour (fph/kph) \n Feet per Hour to Inches per Second (fph/ips) \n Feet per Hour to Inches per Hour (fph/iph) \n Feet per Hour to Feet per Second (fph/fps) \n Feet per Hour to Miles per Second (fph/mips) \n Feet per Hour to Miles per Hour (fph/miph) \n Feet per Hour to Knots (fph/k) \n Miles per Second to Meters per Second (mips/mps) \n Miles per Second to Meters per Hour (mips/mph) \n Miles per Second to Kilometers per Second (mips/kps) \n Miles per Second to Kilometers per Hour (mips/kph) \n Miles per Second to Inches per Second (mips/ips) \n Miles per Second to Inches per Hour (mips/iph) \n Miles per Second to Feet per Second (mips/fps) \n Miles per Second to Feet per Hour (mips/fph) \n Miles per Second to Miles per Hour (mips/miph) \n Miles per Second to Knots (mips/k) \n Miles per Hour to Meters per Second (miph/mps) \n Miles per Hour to Meter per Hour (miph/mph) \n Miles per Hour to Kilometers per Second (miph/kps) \n Miles per Hour to Kilometers per Hour (miph/kph) \n Miles per Hour to Inches per Second (miph/ips) \n Miles per Hour to Inches per Hour (miph/iph) \n Miles per Hour to Feet per Second (miph/fps) \n Miles per Hour to Feet per Hour (miph/fph) \n Miles per Hour to Miles per Second (miph/mips) \n Miles per Hour to Knots (miph/k) \n Knots to Meter per Second (k/mps) \n Knots to Meters per Hour (k/mph) \n Knots to Kilometers per Second (k/kps) \n Knots to Kilometers per Hour (k/kph) \n Knots to Inches per Second (k/ips) \n Knots to Inches per Hour (k/iph) \n Knots to Feet per Second (k/fps) \n Knots to Feet per Hour (k/fph) \n Knots to Miles per Second (k/mips) \n Knots to Miles per Hour (k/miph)\n What do you choose: ")
      if Option == "mps/mph":
         MpS_to_MpH()
      elif Option == "mps/kps":
         MpS_to_KpS()
      elif Option == "mps/kph":
         MpS_to_KpH()
      elif Option == "mps/ips":
         MpS_to_IpS()
      elif Option == "mps/iph":
         MpS_to_IpH()
      elif Option == "mps/fps":
         MpS_to_FpS()
      elif Option == "mps/fph":
         MpS_to_FpH()
      elif Option == "mps/mips":
         MpS_to_MIpS()
      elif Option == "mps/miph":
         MpS_to_MIpH()
      elif Option == "mps/k":
         MpS_to_Knots()
      elif Option == "mph/mps":
         MpH_to_MpS()
      elif Option == "mph/kps":
         MpH_to_KpS()
      elif Option == "mph/kph":
         MpH_to_KpH()
      elif Option == "mph/ips":
         MpH_to_IpS()
      elif Option == "mph/iph":
         MpH_to_IpH()
      elif Option == "mph/fps":
         MpH_to_FpS()
      elif Option == "mph/fph":
         MpH_to_FpH()
      elif Option == "mph/mips":
         MpH_to_MIpS()
      elif Option == "mph/miph":
         MpH_to_MIpH()
      elif Option == "mph/k":
         MpH_to_Knots()
      elif Option == "kps/mps":
         KpS_to_MpS()
      elif Option == "kps/mph":
         KpS_to_MpH()
      elif Option == "kps/kph":
         KpS_to_KpH()
      elif Option == "kps/ips":
         KpS_to_IpS()
      elif Option == "kps/iph":
         KpS_to_IpH()
      elif Option == "kps/fps":
         KpS_to_FpS()
      elif Option == "kps/fph":
         KpS_to_FpH()
      elif Option == "kps/mips":
         KpS_to_MIpS()
      elif Option == "kps/miph":
         KpS_to_MIpH()
      elif Option == "kps/k":
         KpS_to_Knots()
      elif Option == "kph/mps":
         KpH_to_MpS()
      elif Option == "kph/mph":
         KpH_to_MpH()
      elif Option == "kph/kps":
         KpH_to_KpS()
      elif Option == "kph/ips":
         KpH_to_IpS()
      elif Option == "kph/iph":
         KpH_to_IpH()
      elif Option == "kph/fps":
         KpH_to_FpS()
      elif Option == "kph/fph":
         KpH_to_FpH()
      elif Option == "kph/mips":
         KpH_to_MIpS()
      elif Option == "kph/miph":
         KpH_to_MIpH()
      elif Option == "kph/k":
         KpH_to_Knots()
      elif Option == "ips/mps":
         IpS_to_MpS()
      elif Option == "ips/mph":
         IpS_to_MpH()
      elif Option == "ips/kps":
         IpS_to_KpS()
      elif Option == "ips/kph":
         IpS_to_KpH()
      elif Option == "ips/iph":
         IpS_to_IpH()
      elif Option == "ips/fps":
         IpS_to_FpS()
      elif Option == "ips/fph":
         IpS_to_FpH()
      elif Option == "ips/mips":
         IpS_to_MIpS()
      elif Option == "ips/miph":
         IpS_to_MIpH()
      elif Option == "ips/k":
         IpS_to_Knots()
      elif Option == "iph/mps":
         IpH_to_MpS()
      elif Option == "iph/mph":
         IpH_to_MpH()
      elif Option == "iph/kps":
         IpH_to_KpS()
      elif Option == "iph/kph":
         IpH_to_KpH()
      elif Option == "iph/ips":
         IpH_to_IpS()
      elif Option == "iph/fps":
         IpH_to_FpS()
      elif Option == "iph/fph":
         IpH_to_FpH()
      elif Option == "iph/mips":
         IpH_to_MIpS()
      elif Option == "iph/miph":
         IpH_to_MIpH()
      elif Option == "iph/k":
         IpH_to_Knots()
      elif Option == "fps/mps":
         FpS_to_MpS()
      elif Option == "fps/mph":
         FpS_to_MpH()
      elif Option == "fps/kps":
         FpS_to_KpS()
      elif Option == "fps/kph":
         FpS_to_KpH()
      elif Option == "fps/ips":
         FpS_to_IpS()
      elif Option == "fps/iph":
         FpS_to_IpH()
      elif Option == "fps/fph":
         FpS_to_FpH()
      elif Option == "fps/mips":
         FpS_to_MIpS()
      elif Option == "fps/miph":
         FpS_to_MIpH()
      elif Option == "fps/k":
         FpS_to_Knots()
      elif Option == "fph/mps":
         FpH_to_MpS()
      elif Option == "fph/mph":
         FpH_to_MpH()
      elif Option == "fph/kps":
         FpH_to_KpS()
      elif Option == "fph/kph":
         FpH_to_KpH()
      elif Option == "fph/ips":
         FpH_to_IpS()
      elif Option == "fph/iph":
         FpH_to_IpH()
      elif Option == "fph/fps":
         FpH_to_FpS()
      elif Option == "fph/mips":
         FpH_to_MIpS()
      elif Option == "fph/miph":
         FpH_to_MIpH()
      elif Option == "fph/k":
         FpH_to_Knots()
      elif Option == "mips/mps":
         MIpS_to_MpS()
      elif Option == "mips/mph":
         MIpS_to_MpH()
      elif Option == "mips/kps":
         MIpS_to_KpS()
      elif Option == "mips/kph":
         MIpS_to_KpH()
      elif Option == "mips/ips":
         MIpS_to_IpS()
      elif Option == "mips/iph":
         MIpS_to_IpH()
      elif Option == "mips/fps":
         MIpS_to_FpS()
      elif Option == "mips/fph":
         MIpS_to_FpH()
      elif Option == "mips/miph":
         MIpS_to_MIpH()
      elif Option == "mips/k":
         MIpS_to_Knots()
      elif Option == "miph/mps":
         MIpH_to_MpS()
      elif Option == "miph/mph":
         MIpH_to_MpH()
      elif Option == "miph/kps":
         MIpH_to_KpS()
      elif Option == "miph/kph":
         MIpH_to_KpH()
      elif Option == "miph/ips":
         MIpH_to_IpS()
      elif Option == "miph/iph":
         MIpH_to_IpH()
      elif Option == "miph/fps":
         MIpH_to_FpS()
      elif Option == "miph/fph":
         MIpH_to_FpH()
      elif Option == "miph/mips":
         MIpH_to_MIpS()
      elif Option == "miph/k":
         MIpH_to_Knots()
      elif Option == "k/mps":
         Knots_to_MpS()
      elif Option == "k/mph":
         Knots_to_MpH()
      elif Option == "k/kps":
         Knots_to_KpS()
      elif Option == "k/kph":
         Knots_to_KpH()
      elif Option == "k/ips":
         Knots_to_IpS()
      elif Option == "k/iph":
         Knots_to_IpH()
      elif Option == "k/fps":
         Knots_to_FpS()
      elif Option == "k/fph":
         Knots_to_FpH()
      elif Option == "k/mips":
         Knots_to_MIpS()
      elif Option == "k/miph":
         Knots_to_MIpH()
      else:
         print("Thats is not supported")
         time.sleep(4)
   Menu()

def Data_Convert():

   def Bits_to_Nibble():
      Size = float(input("Please enter the amount of Data you wish to convert"))
      Nibble = Size / 4
      print("That is " + str(Nibble) + " Nibbles")
      Retry()

   def Bits_to_Bytes():
      Size = float(input("Please enter the amount of Data you wish to convert"))
      Bytes = Size / 8
      print("That is " + str(Bytes) + " Bytes")
      Retry()

   def Bits_to_Kilobyte():
      Size = float(input("Please enter the amount of Data you wish to convert"))
      Kilobytes = Size / 8000
      print("That is " + str(Kilobytes) + " Kilobytes")
      Retry()

   def Bits_to_Megabyte():
      Size = float(input("Please enter the amount of Data you wish to convert"))
      Megabyte = Size / 8000000
      print("That is " + str(Megabyte) + " Megabytes")
      Retry()

   def Bits_to_Gigabyte():
      Size = float(input("Please enter the amount of Data you wish to convert"))
      Gigabyte = Size / 8.0000e+9
      print("That is " + str(Gigabyte) + " Gigabytes")
      Retry()

   def Bits_to_Terabyte():
      Size = float(input("Please enter the amount of Data you wish to convert"))
      Terabyte = Size / 8.0000e+12
      print("That is " + str(Terabyte) + " Terabytes")
      Retry()

   def Nibble_to_Bits():
      Size = float(input("Please enter the amount of Data you wish to convert"))
      Bits = Size * 4
      print("That is " + str(Bits) + " Bits")
      Retry()

   def Nibble_to_Bytes():
      Size = float(input("Please enter the amount of Data you wish to convert"))
      Bytes = Size / 2
      print("That is " + str(Bytes) + " Bytes")
      Retry()

   def Nibble_to_Kilobyte():
      Size = float(input("Please enter the amount of Data you wish to convert"))
      Kilobyte = Size / 2000
      print("That is " + str(Kilobyte) + " Kilobytes")
      Retry()

   def Nibble_to_Megabyte():
      Size = float(input("Please enter the amount of Data you wish to convert"))
      Megabyte = Size / 2000000
      print("That is " + str(Megabyte) + " Megabytes")
      Retry()

   def Nibble_to_Gigabyte():
      Size = float(input("Please enter the amount of Data you wish to convert"))
      Gigabyte = Size / 2.0000e+9
      print("That is " + str(Gigabyte) + " Gigabytes")
      Retry()

   def Nibble_to_Terabyte():
      Size = float(input("Please enter the amount of Data you wish to convert"))
      Terabyte = Size / 2.0000e+12
      print("That is " + str(Terabyte) + " Terabytes")
      Retry()

   def Byte_to_Bits():
      Size = float(input("Please enter the amount of Data you wish to convert"))
      Bits = Size * 8
      print("That is " + str(Bits) + " Bits")
      Retry()

   def Byte_to_Nibble():
      Size = float(input("Please enter the amount of Data you wish to convert"))
      Nibble = Size * 2
      print("That is " + str(Nibble) + " Nibbles")
      Retry()

   def Byte_to_Kilobyte():
      Size = float(input("Please enter the amount of Data you wish to convert"))
      Kilobyte = Size / 1000
      print("That is " + str(Kilobyte) + " Kilobytes")
      Retry()

   def Byte_to_Megabyte():
      Size = float(input("Please enter the amount of Data you wish to convert"))
      Megabyte = Size / 1000000
      print("That is " + str(Megabyte) + " Megabytes")
      Retry()

   def Byte_to_Gigabyte():
      Size = float(input("Please enter the amount of Data you wish to convert"))
      Gigabyte = Size / 1.0000e+9
      print("That is " + str(Gigabyte) + " Gigabytes")
      Retry()

   def Byte_to_Terabyte():
      Size = float(input("Please enter the amount of Data you wish to convert"))
      Terabyte = Size / 1.0000e+12
      print("That is " + str(Terabyte) + " Terabytes")
      Retry()

   def Kilobyte_to_Bit():
      Size = float(input("Please enter the amount of Data you wish to convert"))
      Bit = Size * 8000
      print("That is " + str(Bit) + " Bits")
      Retry()

   def Kilobyte_to_Byte():
        Size = float(input("Please enter the amount of Data you wish to convert"))
        Byte = Size * 1000
        print("That is " + str(Byte) + " Bytes")
        Retry()

   def Kilobyte_to_Megabyte():
        Size = float(input("Please enter the amount of Data you wish to convert"))
        Megabyte = Size / 1000
        print("That is " + str(Megabyte) + " Megabytes")
        Retry()

   def Kilobyte_to_Gigabyte():
        Size = float(input("Please enter the amount of Data you wish to convert"))
        Gigabyte = Size / 1e+6
        print("That is " + str(Gigabyte) + " Gigabytes")
        Retry()

   def Kilobyte_to_Terabyte():
        Size = float(input("Please enter the amount of Data you wish to convert"))
        Terabyte = Size / 1e+9
        print("That is " + str(Terabyte) + " Terabytes")
        Retry()

   def Megabyte_to_Bit():
        Size = float(input("Please enter the amount of Data you wish to convert"))
        Bit = Size * 8e+6
        print("That is " + str(Bit) + " Bits")
        Retry()

   def Megabyte_to_Byte():
        Size = float(input("Please enter the amount of Data you wish to convert"))
        Byte = Size * 1e+6
        print("That is " + str(Byte) + " Bytes")
        Retry()

   def Megabyte_to_Kilobyte():
        Size = float(input("Please enter the amount of Data you wish to convert"))
        Kilobyte = Size * 1000
        print("That is " + str(Kilobyte) + " Kilobytes")
        Retry()

   def Megabyte_to_Gigabyte():
        Size = float(input("Please enter the amount of Data you wish to convert"))
        Gigabyte = Size / 1000
        print("That is " + str(Gigabyte) + " Gigabytes")
        Retry()

   def Megabyte_to_Terabyte():
        Size = float(input("Please enter the amount of Data you wish to convert"))
        Terabyte = Size / 1e+6
        print("That is " + str(Terabyte) + " Terabytes")
        Retry()

   def Gigabyte_to_Bit():
        Size = float(input("Please enter the amount of Data you wish to convert"))
        Bit = Size * 8e+9
        print("That is " + str(Bit) + " Bits")
        Retry()

   def Gigabyte_to_Byte():
        Size = float(input("Please enter the amount of Data you wish to convert"))
        Byte = Size * 1e+9
        print("That is " + str(Byte) + " Bytes")
        Retry()

   def Gigabyte_to_Kilobyte():
        Size = float(input("Please enter the amount of Data you wish to convert"))
        Kilobyte = Size * 1e+6
        print("This is " + str(Kilobyte) + " Kilobytes")
        Retry()

   def Gigabyte_to_Megabyte():
        Size = float(input("Please enter the amount of Data you wish to convert"))
        Megabyte = Size * 1000
        print("That is " + str(Megabyte) + " Kilobytes")
        Retry()

   def Gigabyte_to_Terabyte():
        Size = float(input("Please enter the amount of Data you wish to convert"))
        Terabyte = Size / 1000 
        print("That is " + str(Terabyte) + " Terabyte")
        Retry()

   def Terabyte_to_Bit():
        Size = float(input("Please enter the amount of Data you wish to convert"))
        Bit = Size * 8e+12
        print("That is " + str(Bit) + " Bits")
        Retry()

   def Terabyte_to_Byte():
        Size = float(input("What is the amount of Data you wish to convert"))
        Byte = Size * 1e+12
        print("That is " + str(Byte) + " Bytes")
        Retry()

   def Terabyte_to_Kilobyte():
        Size = float(input("Please enter the amount of Data you wish to convert"))
        Kilobyte = Size * 1e+9
        print("That is " + str(Kilobyte) + " Kilobytes")
        Retry()

   def Terabyte_to_Megabyte():
        Size = float(input("Please enter the amount of Data you wish to convert"))
        Megabyte = Size * 1e+6
        print("That is " + str(Megabyte) + " Megabytes")
        Retry()

   def Terabyte_to_Gigabyte():
        Size = float(input("Please enter the amount of Data you wish to convert"))
        Gigabyte = Size * 1000 
        print("That is " + str(Gigabyte) + " Gigabytes")
        Retry()

   def Retry():
        Again = ("Would you like to go again or go to menu? ")
        if Again == "Again":
            Menu()
        elif Again == "Menu":
            Main_Menu()
        else:
            print("Goodbye")
            time.sleep(4)

   def Menu():
      Choice = input("What would you like to do: Bit to Nibble (BtN) \n Bit to Byte (BtBy) \n Bit to Kilobyte (BtK) \n Bit to Megabyte (BtM) \n Bit to Gigabyte (BtG) \n Bit to Terabyte (BtT)")

   Menu()
def Main_Menu():
    Choice = input("\n Time" + "\n Weight" + "\n Temperature" + "\n Speed" + "\n Data" + "\n What would you like to convert: ")
    if Choice == "Time":
        Time_Convert()
    elif Choice == "Weight":
        Weight_Convert()
    elif Choice == "Temperature":
        Temp_Convert()
    elif Choice == "Speed":
        Speed_Convert()
    elif Choice == "Data":
        Data_Convert()
    else:
        print("Goodbye")
        time.sleep(4)

def Menu():
    Choice = input("What would you like to choose:")

Main_Menu()
