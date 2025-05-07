import pandas as pd
import streamlit as st
import numpy as np
import mysql.connector
providers=pd.read_csv("C:/Users/shanm/Downloads/providers_data.csv")
receivers=pd.read_csv("C:/Users/shanm/Downloads/receivers_data.csv")
food_listings=pd.read_csv("C:/Users/shanm/Downloads/food_listings_data.csv")
claims=pd.read_csv("C:/Users/shanm/Downloads/claims_data.csv")
st.title("food waste management")
r=st.sidebar.radio("navigation " \
                   "goto",["project info","view table","CURD operations","sql quary&visualization","learner sql query",
                                 "user information"])
mydb=mysql.connector.connect(
    host="localhost",
    user="root",
    password="root",
    autocommit=True
  )
mycursor=mydb.cursor(buffered=True)


mycursor.execute("create database if not exists food_waste_management ")
df=pd.DataFrame(mycursor.execute('show databases'))
st.write(df)
mycursor.execute("use food_waste_management ")
mycursor.execute("""create table if not exists providers(
                 providers_id int primary key,
                 name varchar(255),
                 type varchar(100),
                 address text,
                 city varchar(100),
                 contact varchar(50)
) """)
data1=mycursor.execute("""create table if not exists receivers(      
                 Receiver_id int primary key,
                 name varchar(255),
                 type varchar(100),
                 city varchar(100),
                 contact varchar(50)
) """)
data2=mycursor.execute("""create table if not exists food_listings(  
                 Food_id int primary key,
                 Food_name varchar(100),
                 Quantity int,
                 Ex_Date date,                
                 providers_ID int,
                 Provider_Type varchar(100),
                 Location varchar(120),
                 Food_Type varchar(150),
                 Meal_Type varchar(50),
                 foreign key(providers_ID) references providers(providers_id)                 
) """)

data3=mycursor.execute("""create table if not exists claims(
                 Claim_ID int primary key auto_increment,
                 Food_ID int,                         
                 Receiver_ID int,
                 Status varchar(100),
                 Timestamp timestamp,
                 foreign key(Food_ID) references food_listings(Food_id),
                 foreign key(Receiver_ID) references receivers(Receiver_id)
)""")


# for index, row in providers.iterrows():
#     mycursor.execute("""
#         insert into providers (providers_id,name,type,address,city,contact)
#         values(%s,%s,%s,%s,%s,%s)
#     """, tuple(row))
# df4=pd.DataFrame(mycursor.execute("describe providers"))
# results = mycursor.fetchall(df4)
# st.write(results)

# for index, row in receivers.iterrows():
#     mycursor.execute("""
#         insert into receivers(Receiver_id,name,type,city,contact)
#         values(%s,%s,%s,%s,%s)
#     """, list(row))


# for index, row in food_listings.iterrows():
#     mycursor.execute("""
#         insert into food_listings (Food_id,Food_name,Quantity,Ex_Date,providers_ID,Provider_Type,Location,Food_Type,Meal_Type)
#         values(%s,%s,%s,STR_TO_DATE(%s,'%m/%d/%Y'),%s,%s,%s,%s,%s)
#     """, tuple(row))

for index, row in claims.iterrows():
    mycursor.execute("""
        insert into claims(Claim_ID,Food_ID,Receiver_ID,Status,Timestamp)
        values(%s,%s,%s,%s,STR_TO_DATE(%s,'%m/%d/%Y %H:%i'))
    """, tuple(row))
    st.write("ok")

