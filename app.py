import streamlit as st
import pandas as pd
import os
from io import BytesIO
import time

# page setup
st.set_page_config(page_title="Converter", layout="wide")
st.title("🔄Unit Converter")
st.write("This is a simple unit conversion app")

# Conversion select
x = st.selectbox("Pick one", ["Temperature", "Length", "Mass"])

if x == "Length":
     option1 = st.selectbox(
     'FROM:  select unit',
     ('foot', 'yard', 'inch', 'metre','kilometre', 'centimetre', 'millimetre'))

     option2 = st.selectbox(
     'TO:  select unit',
     ('foot', 'yard', 'inch', 'metre','kilometre','centimetre', 'millimetre'))
elif x == "Mass":
     option1 = st.selectbox(
     'FROM:  select unit',
     ('gram', 'kilogram', 'milligram', 'metric ton', 'litre', 'centilitre', 'millilitre'))

     option2 = st.selectbox(
     'TO:  select unit',
     ('gram', 'kilogram', 'milligram', 'metric ton',  'litre', 'centilitre', 'millilitre'))
     
elif x == "Temperature":
     option1 = st.selectbox(
          'From: select unit',
          ('Celcius','Farenheit','Kelvin'))
     option2 = st.selectbox(
          'From: select unit',
          ('celcius','farenheit','kelvin')
     )
    
# conversion 
num = st.number_input('Insert a number')
if option1 == 'inch' and option2 == 'centimetre':            #length
    result =num*2.54
elif option1 =='centimetre' and option2 =='inch':
    result=num/2.54
elif option1 =='millimetre' and option2 =='inch':
    result=num/25.4 
elif option1 =='inch' and option2 =='millimetre':
    result=num*25.4 
elif option1 =='inch' and option2 =='metre':
    result=num/39.3700787 
elif option1 =='metre' and option2 =='inch':
    result=num*39.3700787 
elif option1 =='inch' and option2 =='kilometre':
    result=num/39370.0787
elif option1 =='foot' and option2 =='yard':
    result=round(num/3)
elif option1 =='yard' and option2 =='foot':
    result=num*3
elif option1 =='yard' and option2 =='metre':
    result=num/1.0936133
elif option1 =='metre' and option2 =='yard':
    result=num*1.0936133
elif option1 =='yard' and option2 =='centimetre':
    result=num/91.44
elif option1 =='yard' and option2 =='millimetre':
    result=num*914.4
elif option1 =='millitre' and option2 =='yard':
    result=num/914.4
elif option1 =='yard' and option2 =='centimetre':
    result=num*91.44
elif option1 =='yard' and option2 =='kilometre':
    result=num/1093.6133
elif option1 =='kilometre' and option2 =='yard':
    result=num*1093.6133
elif option1 =='foot' and option2 =='metre':
    result=num/3.2808399
elif option1 =='metre' and option2 =='foot':
    result=num*3.2808399
elif option1 =='foot' and option2 =='inch':
    result=num*12
elif option1 =='foot' and option2 =='kilometre':
    result=num/3280.8399
elif option1 =='kilometre' and option2 =='foot':
    result=num*3280.8399 
elif option1 =='millimetre' and option2 =='foot':
    result=num/304.8
elif option1 =='foot' and option2 =='millimetre':
    result=num*304.8 
elif option1 =='centimetre' and option2 =='foot':
    result=num/30.48
elif option1 =='foot' and option2 =='centimetre':
    result=num*30.48
elif option1 =='inch' and option2 =='foot':
    result=num/12 
elif option1 =='centimetre' and option2 =='metre':
    result=num/100
elif option1 =='metre' and option2 =='centimetre':
    result=num*100
elif option1 =='millimetre' and option2 =='metre':
    result=num/1000
elif option1 =='metre' and option2 =='millimetre':
    result=num*1000
elif option1 =='kilometre' and option2 =='metre':
    result=num*1000
elif option1 =='metre' and option2 =='kilometre':
    result=num*1000
elif option1 =='centimetre' and option2 =='millimetre':
    result=num*10
elif option1 =='millimetre' and option2 =='centimetre':
    result=num/10
elif option1 =='kiloemetre' and option2 =='millimetre':
    result=num*1000000
elif option1 =='millimetre' and option2 =='kilometre':
    result=num/1000000
elif option1 =='kilometre' and option2 =='centimetre':
    result=num*100000
elif option1 =='centimetre' and option2 =='kilometre': 
    result=num/100000
elif option1 =='foot' and option2=='foot':
     result=num
elif option1 =='yard' and option2=='yard':
     result=num
elif option1 =='inch' and option2=='inch':
     result=num
elif option1 =='metre' and option2=='metre':
     result=num
elif option1 =='kilometre' and option2=='kilometre':
     result=num
elif option1 =='centimetre' and option2=='centimetre':
     result=num
elif option1 =='millimetre' and option2=='millimetre':
     result=num
elif option1 =='centimetre' and option2 =='kilometre':               #mass conversions
    result=num/100000
elif option1 =='gram' and option2 =='kilogram':         
    result=num/1000    
elif option1 =='kilogram' and option2 =='gram':
    result=num*1000
elif option1 =='gram' and option2 =='milligram':
    result=num*1000 
elif option1 =='milligram' and option2 =='gram':
    result=num/1000 
elif option1 =='kilogram' and option2 =='milligram':
    result=num*1000000
elif option1 =='milligram' and option2 =='kilogram':
    result=num/1000000
elif option1 =='metric ton' and option2 =='kilogram':
    result=num*1000
elif option1 =='kilogram' and option2 =='metric ton':
    result=num/1000
elif option1 =='gram' and option2 =='metric ton':
    result=num/1000000
elif option1 =='metric ton' and option2 =='gram':
    result=num*1000000    
elif option1 =='milligram' and option2 =='metric ton':
    result=num/1.0000E+9
elif option1 =='metric ton' and option2 =='milligram':
    result=num*1.0000E+9
elif option1 =='metric ton' and option2 =='centigram':
    result=num*100000000
elif option1 =='centigram' and option2 =='metric ton':
    result=num/100000000    
elif option1 =='gram' and option2 =='gram':
     result=num
elif option1 =='kilogram' and option2 =='kilogram':
     result=num
elif option1 =='milligram' and option2 =='milligram':
     result=num
elif option1 =='metric ton' and option2 =='metric ton':
     result=num
elif option1 =='litre' and option2 =='litre':
     result=num
elif option1 =='centilitre' and option2 =='centilitre':
     result=num
elif option1 =='millilitre' and option2 =='millilitre':
     result=num
     
elif option1 =='Kelvin' and option2 =='celcius':                    #temperature
     result=num-273.15
elif option1 =='Kelvin' and option2 =='farenheit':
     result=(num-273.15)*9/5 + 32
elif option1 =='Celcius' and option2 =='kelvin':
     result=num+273.15
elif option1 =='Celcius' and option2 =='farenheit':
     result=num*(9/5)+32
elif option1 =='Farenheit' and option2 =='kelvin':
     result=(num-32)*5/9+273.15
elif option1 =='Farenheit' and option2 =='celcius':
     result=(num-32)*5/9
elif option1 =='Kelvin' and option2=='kelvin':
     result=num
elif option1 =='Celsius' and option2=='celsius':
     result=num
elif option1 =='Farenheit' and option2=='farenheit':
     result=num

# st.button("convert")
if st.button("convert"):
     with st.spinner('Wait for it...'):
      time.sleep(.5)
     st.success(result)


