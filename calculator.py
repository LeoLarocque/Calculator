import math
import numpy
import time
units = "units"
def sideA():
    pTHypLForA = float(input("Enter length of hypotenuse.\n"))
    pTBL = float(input("Enter length of side B.\n"))
    try:
        pTAA = math.sqrt((pTHypLForA ** 2) - (pTBL ** 2))
        print("The length of side A is " + str(pTAA) + " " + units + ".")
    except:
        print("The hypotenus has to be the longest length.")
        sideA()
def sideB():
    pTHypLForB = float(input("Enter length of hypotenuse.\n"))
    pTAL = float(input("Enter length of side A.\n"))
    try:
        pTAB = math.sqrt((pTHypLForB ** 2) - (pTAL ** 2))
        print("The length of side B is " + str(pTAB) + " " + units + ".")
    except:
        print("The hypotenus has to be the longest length.")
        sideB()
def perimiterF():
    wPShape = input("Enter what 2D shape you are using.\n1. Sqaure\n2. Rectangle\n3. Circle\n")
    pShape = wPShape.lower()
    if pShape == "square" or pShape == "1":
        squareSLForP = float(input("Enter side length of square.\n"))
        print("The perimeter of the square is " + str(squareSLForP * 4) + " " + units + ".")
    elif pShape == "rectangle" or pShape == "2":
        rectWForP = float(input("Enter width of rectangle.\n"))
        rectLForP = float(input("Enter length of rectanlge.\n"))
        print("The perimeter of the rectangle is " + str((rectWForP * 2) + (rectLForP * 2)) + " " + units + ".")
    elif pShape == "circle" or pShape == "3":
        cRForC = float(input("Enter raduis of circle.\n"))
        print("The perimeter of the circle is " + str(2 * (math.pi * cRForC)) + " " + units + ".")
def areaF():
    wAShape = input("Enter the shape you want to find the area of.\n1. Square\n2. Rectangle\n3. Circle\n4. Triangle\n")
    aShape = wAShape.lower()
    if aShape == "square" or aShape == "1":
        squareSLForA = float(input("Enter side length of square.\n"))
        print("The area of the square is " + str(squareSLForA * 2) + " " + units + "^2.")
    elif aShape == "rectangle" or aShape == "2":
        rectWForA = float(input("Enter width of rectangle.\n"))
        rectLForA = float(input("Enter length of rectangle.\n"))
        print("The area of the rectangle is " + str(rectWForA * rectLForA) + " " + units + "^2.")
    elif aShape == "circle" or aShape == "3":
        circleRForA = float(input("Enter radius of circle\n"))
        print("The area of the circle is " + str((circleRForA ** 2) * math.pi) + " " + units + "^2.")
    elif aShape == "triangle" or aShape == "4":
        triangleBForA = float(input("Enter side length of triangle (NOT HYPOTENUSE).\n"))
        triangleHForA = float(input("Enter height of traingle (NOT SLANT HEIGHT).\n"))
        print("The area of the traingle is " + str((triangleBForA * triangleHForA) / 2) + " " + units + "^2.")
def surfaceareaF():
    print("This function is unavialable right now.")
def volumeF():
    print("This will calculate the volume of different objects.")
    print("Print what object you would like to use.")
    wPrism = input("1. Rectangle\n2. cube\n3. SBPyramid (Square Based Pyramid)\n4. Cone\n5. Sphere\n6. Cylinder\n")
    prism = wPrism.lower()
    if prism == "rectangle" or prism == "1":
        rL = float(input("Enter rectangle length.\n"))
        rW = float(input("Enter rectangle width.\n"))
        rH = float(input("Enter rectangle height.\n"))
        print("The volume of the rectanlge is " + str(rL * rW * rH) + units + "^3.")
    elif prism == "cube" or prism == "2":
        cAD = float(input("Enter Cube side Length.\n"))
        print("The volume of the cube is " + str(cAD ** 3) + " " + units + "^3.")
    elif prism == "sbpyramid" or prism == "3" or prism == "pyramid":
        sBPB = float(input("Enter SBPyramid base side length.\n"))
        sBPH = float(input("Enter SBPyramid height, (NOT SLANT HEIGHT).\n"))
        print("The volume is " + str(((sBPB ** 2) * sBPH) / 3) + " " + units + "^3.")
    elif prism == "cone" or prism == "4":
        cR = float(input("Enter radius of cone.\n"))
        cH = float(input("Enter height of cone.\n"))
        print("The volume of the cone is " + str((math.pi * (cR ** 2) * cH) / 3) + " " + units + "^3.")
    elif prism == "sphere" or prism == "5":
        sR = float(input("Enter radius of sphere.\n"))
        print("The volume of the sphere is " + str((math.pi * (sR ** 3)) * 4 / 3) + " " + units + "^3.")
    elif prism == "cylinder" or prism == "6":
        cylR = float(input("Enter radius of cylinder.\n"))
        cylH = float(input("Enter heigh of cylinder.\n"))
        print("The volume of the cylinder is " + str(math.pi * (cylR ** 2) * cylH) + " " + units + "^3.")
def pythagoreanF():
    whatSTQ = input("Enter what side of the triangle you would like to find.\n1. Hypotenuse\n2. Side A\n3. Side B\n")
    whatST = whatSTQ.lower()
    if whatST == "hypotenuse" or whatST == "c" or whatST == "1":
        aSLT = float(input('Enter side "A" of Triangle.\n'))
        bSLT = float(input('Enter side "B" of Triangle.\n'))
        pTPAH = (aSLT ** 2) + (bSLT ** 2)
        print("The length of the hypotenuse is " + str(math.sqrt(pTPAH)) + " " + units + ".")
    elif whatST == "side a" or whatST == "a" or whatST == "2":
        sideA()
    elif whatST == "side b" or whatST == "b" or whatST == "3":
        sideB()
def gcfLcmF():
    num1 = int(input("Enter your first number. "))
    num2 = int(input("Enter your second number. "))
    gcf = math.gcd(num1, num2)
    lcm = numpy.lcm(num1, num2)
    print("The GCF is " + str(gcf))
    print("The LCM is " + str(lcm))
def speedFunction():
    speedUnit = input("Enter what speed you would like to convert. m/s to km/h, km/h to m/s, km/h to miles/h: ")
    if speedUnit == "1":
        mPerSToKmPerH = float(input("Enter m/s: "))
        mPerSToKmPerHAnswer = mPerSToKmPerH * 3.6
        print(str(mPerSToKmPerHAnswer) + "km/h")          
    elif speedUnit == "2":
        KmPerHToMPerS = float(input("Enter km/h: "))
        KmPerHToMPerSAnswer = KmPerHToMPerS * 3.6
        print(str(KmPerHToMPerSAnswer) + "m/s")
def lengthFunction():  
    whatDaHeck = input("Enter what units you would like to convert. \n 1. Km to Miles\n 2. Miles to Km\n 3. Cm to In\n 4. In to Cm ")
    whatDaHeckStr = str(whatDaHeck)
    if whatDaHeckStr == "1":
        kmToMiles = float(input("Enter km: "))
        kmToMilesAnswer = kmToMiles / 1.60934
        print(str(kmToMilesAnswer) + "miles")
    elif whatDaHeckStr == "2":
        milesToKm = float(input("Enter miles: "))
        milesToKmAnswer = milesToKm * 1.60934
        print(str(MilesToKmAnswer) + "km") 
    elif whatDaHeckStr == "3":
        cmToIn = float(input("Enter cm: "))
        cmToInAnswer = cmToIn / 2.54
        print(str(cmToInAnswer) + "in")    
    elif whatDaHeckStr == "4":
        InToCm = float(input("Enter in: "))
        InToCmAnswer = InToCm * 2.54
        print(str(InToCmAnswer) + "cm")
while 1 == 1:
    print("This programm calculates a number of different things including Perimeter, Area, Surface Area, Volume, and Pythagorean's Theorem of different objects.\n")
    """wUnits = input("What unit would you like to use. Example: cm.\n")
    units = wUnits.lower()"""
    wObjUse = input("Enter what you would like to use.\n1. Perimeter\n2. Area\n3. Surface Area\n4. Volume\n5. Pythagorean Theorem\n6. LCM / GCF\n7. Converter\n")
    wUse = wObjUse.lower()
    if wUse == "perimeter" or wUse == "1":
        perimiterF()
    elif wUse == "area" or wUse == "2":
        areaF()
    elif wUse == "surface area" or wUse == "3":
        surfaceareaF()
    elif wUse == "volume" or wUse == "4":
        volumeF()
    elif wUse == "pythagorean theorem" or wUse == "5":
        pythagoreanF()
    elif wUse == "6":
        gcfLcmF()
    elif wUse == "7":
        types = input("Would you like to convert speed or length? ")
        typesStr = str(types)
        if typesStr == "speed":
            speedFunction()
        elif typesStr == "length":
            lengthFunction()
    elif wUse == "exit":
        print("Goodbye!")
        break

            
