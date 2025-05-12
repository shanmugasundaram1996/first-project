

import pandas as pd
import streamlit as st
import numpy as np
import mysql.connector
import matplotlib.pyplot as plt 

#command for mysql connector
mydb=mysql.connector.connect(
    host="localhost",
    user="root",
    password="root",
    autocommit=True
  )
mycursor=mydb.cursor(buffered=True)
# white; /* Solid white background */


# st.markdown(
#       f"""
#       <style>
#       .stSidebar  {{
#         background-color:  #008000; /* Solid green background */
        
#         background-size: cover;
#       }}
#       </style>
#       """,
#       unsafe_allow_html=True
# )



#set home page with titles of other pages
st.sidebar.title('HOME')
page=st.sidebar.radio("Getpage",["Project Info","View Table","CRUD operations","sql Quary & Visualization","Learner sql Query",
                                    "Get Your Food"])
import base64



# st.markdown(
#     """
#     <style>
#     .st.App {
#         background: url("https://img.freepik.com/free-photo/green-texture_1160-721.jpg?semt=ais_hybrid&w=740")
#     }
#    .sidebar .sidebar-content {
#         background: url("https://img.freepik.com/free-photo/green-texture_1160-721.jpg?semt=ais_hybrid&w=740")
#     }
#     </style>
#     """,
#     unsafe_allow_html=True
# )
#page 1 is selected
if page=="Project Info":
    bg_image_url = "https://mcdn.wallpapersafari.com/medium/28/77/xmW4D8.jpg"

    st.markdown(
      f"""
      <style>
      .stApp {{
        color: black; /* Text color */
        background-image: url("{bg_image_url}");
        background-size: cover;
      }}
      </style>
      """,
      unsafe_allow_html=True
)
    st.write("")
    st.markdown(
    """
    <style>
    .header {
        color: black; /* Text color */
        background-color: white; /* Solid white background */
        padding: 40px;
        text-align: center;
        font-size: 40px;
        font-weight: bold;
        border-radius: 100px;
    }
    </style>
    <div class="header">FOOD WASTE MANAGEMENT</div>
    """,
    unsafe_allow_html=True
)
    
    #put one image 
    st.write("")
    st.image("C:/Users/shanm/OneDrive/Desktop/Food-waste.jpg")
    
    # give a intro to the website
    st.write(""" Food waste management involves strategies and practices to reduce,
              reuse, and recycle food waste. It addresses the environmental, economic, 
             and social impacts of food waste, such as greenhouse gas emissions, resource wastage,
              and food insecurity. Effective management includes reducing food waste at
              the source, redistributing surplus food to those in need, and converting
              waste into compost or energy.
             A food waste management app is a digital platform designed to tackle food waste issues. 
             These apps help individuals, households, and businesses monitor and reduce food waste.  """)
    #add a brief details about the tables
    st.subheader("providers table")
    st.write("""  Stores details about food providers like restaurants, grocery stores, or individuals donating surplus food.""")
    st.subheader("receivers table")
    st.write(""" Contains information about receivers who can claim surplus food, such as charities or individuals in need.""")
    st.subheader("food listings table")
    st.write("""Manages information about the available food items for donation, including details about quantity,
                       expiry date, and location.""")
    st.subheader("claims table")
    st.write("""Tracks the claiming process, linking food items with receivers and updating the claim status.""")
    

    # brief about why this website
    mycursor.execute("use food_waste_management ")
    st.write("""This system facilitates smooth interaction between providers and receivers.
               Tracks food availability, expiry dates, and claims in real time.It empowers food waste reduction and timely
              redistribution to those in need
                """)
    #st.image("C:/Users/shanm/Downloads/imagefood.png")

elif page=="View Table":
    st.markdown(
    """
    <style>
    .header {
        color: black; /* Text color */
        background-color:  #008000; /* Solid green background */
        padding: 40px;
        text-align: center;
        font-size: 40px;
        font-weight: bold;
        border-radius: 100px;
    }
    </style>
    <div class="header">SAVE FOOD SAVE LIVE</div>
    """,
    unsafe_allow_html=True
)
    
    st.write('')
    st.image("C:/Users/shanm/OneDrive/Desktop/say_no_to_food_waste.png")
    st.image("C:/Users/shanm/OneDrive/Desktop/aim_of_the_project.png")
    st.subheader("Database Tables")
    #use command for to use database 
    mycursor.execute("use food_waste_management ")
   
    #sql query to see entire datas in table
    Table_Name=st.selectbox("Select Tables",["providers","receivers","food_listings","claims","Volunteer"])
    mycursor.execute(f"select * from {Table_Name}")
    results = mycursor.fetchall()
    columns = [desc[0] for desc in mycursor.description]
    c = pd.DataFrame(results, columns=columns)
    st.write(c)


elif page=="CRUD operations":
    st.markdown(
    """
    <style>
    .header {
        color: black; /* Text color */
        background-color:  #008000; /* Solid green background */
        padding: 40px;
        text-align: center;
        font-size: 40px;
        font-weight: bold;
        border-radius: 100px;
    }
    </style>
    <div class="header">CRUD operations</div>
    """,
    unsafe_allow_html=True
)
    #use select box command to select any one of the crud operations
    Functions=st.selectbox("",["Create","Insert","Read","update","Delete"])
    if Functions=="Create":
        #create function limited by creating one table called volunteer without any values
        #don't give permission to create table by any one
        st.subheader("Create Volunteer Tables")
        st.selectbox("Table Name",["Volunteer"])
        # use form format 
        form = st.form(key='creation of new table')
        
        name = form.text_input("Name*")
        city = form.text_input("City*")
        contact = form.text_input("Contact*")
        submit_button = form.form_submit_button(label='Create table')
        if submit_button:
            
             mycursor.execute("use food_waste_management ")
             mycursor.execute("""create table if not exists Volunteer(
                 volunteer_id int primary key,
                 V_name varchar(255) not null,
                 V_city varchar(100) not null,
                 Alloted_provider text unique,
                 V_contact varchar(50) not null
             )""")
             st.success("Table created!")
             mycursor.execute(f"select * from Volunteer")
             results = mycursor.fetchall()
             columns = [desc[0] for desc in mycursor.description]
             d = pd.DataFrame(results, columns=columns)
             st.write(d)
    if Functions=="Insert":
        Table_Name=st.selectbox("Select Tables",["providers","receivers","food_listings","claims","Volunteer"])
        # based on the selection form will created with column name
        if Table_Name=="providers":
            # use form to get values for respective table
            form = st.form(key='insert new datas in {Table_Name}')
            P_ID=form.text_input("P_id*")
            name = form.text_input("Name*")
            Type=form.text_input("Type*")
            Address=form.text_input("Address*")
            City = form.text_input("City*")
            Contact = form.text_input("Contact*")
            # submit button conformation for inserting new values
            submit_button = form.form_submit_button(label='update table')
            if submit_button:
              mycursor.execute("use food_waste_management ")
              mycursor.execute(f"""insert into {Table_Name} (
                               providers_id,name,type,address,city,contact) values ({P_ID},"{name}","{Type}","{Address}","{City}","{Contact}")""")
              # success message for values inserting
              st.success("Values inserted!")
        # next table is selected for value insertion 
        # same procedure repeated for each table selection
        if Table_Name=="receivers":
             # use form to get values for respective table
            form = st.form(key='insert new datas in {Table_Name}')
            R_ID=form.text_input("R_id*")
            name = form.text_input("Name*")
            Type=form.text_input("Type*")
            
            City = form.text_input("City*")
            Contact = form.text_input("Contact*")
            submit_button = form.form_submit_button(label='update table')
            if submit_button:
              # sql query to insert values in respective table
              mycursor.execute("use food_waste_management ")
              mycursor.execute(f"""insert into {Table_Name} (
                               Receiver_id,name,type,city,contact) values ({R_ID},"{name}","{Type}","{City}","{Contact}")""")
              # success message for values inserting
              st.success("Values inserted!")
        if Table_Name=="food_listings":
            #this form get entry for all columns
            form = st.form(key='insert new datas in {Table_Name}')
            Food_id=form.text_input("Food_id*")
            Food_name= form.text_input("Food_name*")
            Quantity=form.text_input("Quantity*")
            Ex_Date=form.text_input("Ex_Date*")
            providers_ID=form.text_input("providers_ID*")
            Provider_Type=form.text_input("Provider_Type*")
            Location=form.text_input("Location*")
            Food_Type = form.text_input("Food_Type*")
            Meal_Type = form.text_input("Meal_Type*")
            # submit button conformation for inserting new values
            submit_button = form.form_submit_button(label='update table')
            if submit_button: 
               # sql query to insert values in respective table
              mycursor.execute("use food_waste_management ")
              query = """INSERT INTO food_listings (
                    Food_id, Food_name, Quantity, Ex_Date, providers_ID, Provider_Type, Location, Food_Type, Meal_Type) 
                    VALUES (%s, %s, %s, STR_TO_DATE(%s, '%m/%d/%Y'), %s, %s, %s, %s, %s)"""

              values = (Food_id, Food_name, Quantity, Ex_Date, providers_ID, Provider_Type, Location, Food_Type, Meal_Type)
              mycursor.execute("use food_waste_management ")
              mycursor.execute(query, values)

              st.success("Values inserted!")

        if Table_Name=="claims":
               form = st.form(key='insert new datas in {Table_Name}')
               Claim_ID=form.text_input("Claim_ID*")
               Food_ID= form.text_input("Food_ID*")
               Receiver_ID=form.text_input("Receiver_ID*")
               Status= form.text_input("Status*")
               Timestamp = form.text_input("Timestamp*")
               submit_button = form.form_submit_button(label='update table')
               if submit_button:
                   # sql query to insert values in respective table
                  mycursor.execute("use food_waste_management ")
                  mycursor.execute(f"""insert into {Table_Name} (
                               Claim_ID,Food_ID,Receiver_ID,Status,Timestamp) values 
                                   ({Claim_ID},{Food_ID},{Receiver_ID},"{Status}",{Timestamp})""")
                  st.success("Values inserted!")

        if Table_Name=="Volunteer":
               form = st.form(key='insert new datas in {Table_Name}')
               volunteer_id=form.text_input("Volunteer_ID*")
               name = form.text_input("Name*")
               City_name = form.text_input("City*")
               Contact = form.text_input("Contact*")
               submit_button = form.form_submit_button(label='update table')
               if submit_button:
                  # 1st find out data for alloted provider column
                  mycursor.execute("use food_waste_management ")
                  # based on volunteer city provider details alloted for volunteer 
                  # and provider detail inserted in to alloted column in volunteer table
                  mycursor.execute(f"select Name from providers where City='{City_name}' ")
                  results = mycursor.fetchone()
                  name_provider =results
                  Alloted=(name_provider if name_provider  else "null"  )
                  # insert data into the volunteer table
                  mycursor.execute("use food_waste_management ")
                  mycursor.execute(f"""insert into {Table_Name} (
                               volunteer_id,V_name,V_city,V_contact,Alloted_provider) values 
                                   ({volunteer_id},"{name}","{City_name}","{Contact}","{Alloted}")""")
                  st.success("Values inserted!")
            # Read function only to read all values in selected table 
    if Functions=="Read":
        Table_Name=st.selectbox("Select Tables",["providers","receivers","food_listings","claims","Volunteer"])
        mycursor.execute("use food_waste_management ")
        mycursor.execute(f"select * from {Table_Name}")
        results = mycursor.fetchall()
        columns = [desc[0] for desc in mycursor.description]
        table_values= pd.DataFrame(results, columns=columns)
        st.write(table_values)

  #write query for  table updating 
    
    if Functions=="update":
        Table_Name=st.selectbox("Select Tables",["providers","receivers","food_listings","claims","Volunteer"])
        if Table_Name=="providers":
            mycursor.execute("use food_waste_management ")
            mycursor.execute("select providers_id from providers")
            results = mycursor.fetchall()
            
            providers_table_values= pd.DataFrame(results, columns=["providers_id"]) 
            providers_table_values_sorted_ids = providers_table_values["providers_id"].sort_values().tolist()

            with st.form("update_providers_table_values"):

               id=st.selectbox("Select id",providers_table_values_sorted_ids)
           
               submit_button = st.form_submit_button(label='Ok')     
            st.write("fill the all column")
            form = st.form(key='update new datas in {Table_Name}')
            
            name = form.text_input("Name*")
            Type=form.text_input("Type*")
            address=form.text_input("address*")
            City = form.text_input("City*")
            Contact = form.text_input("Contact*")
            submit_button = form.form_submit_button(label='update table')
            if submit_button:
              # sql query to insert values in respective table
              mycursor.execute("use food_waste_management ")
              mycursor.execute(f"""update {Table_Name} set 
                               name="{name}",type="{Type}",address="{address}",city="{City}",contact="{Contact}" where providers_id="{id}"   """) 
              st.success("Values updated!")      

        elif Table_Name=="receivers": 
 
            
            mycursor.execute("use food_waste_management ")
            mycursor.execute("select Receiver_id from receivers")
            results = mycursor.fetchall()
            
            Receiver_table_values= pd.DataFrame(results, columns=["Receiver_id"]) 
            Receiver_table_values_sorted_ids = Receiver_table_values["Receiver_id"].sort_values().tolist()

            with st.form("update_receivers_table_values"):

               id=st.selectbox("Select id",Receiver_table_values_sorted_ids )
           
               submit_button = st.form_submit_button(label='Ok')
            st.write("fill the all column")
            form = st.form(key='update new datas in {Table_Name}')
            
            name = form.text_input("Name*")
            Type=form.text_input("Type*")
            
            City = form.text_input("City*")
            Contact = form.text_input("Contact*")
            submit_button = form.form_submit_button(label='update table')
            if submit_button:
              # sql query to insert values in respective table
              mycursor.execute("use food_waste_management ")
              mycursor.execute(f"""update {Table_Name} set 
                               name="{name}",type="{Type}",city="{City}",contact="{Contact}" where Receiver_id="{id}"   """)
              # success message for values inserting
              st.success("Values updated!")
        

        elif Table_Name=="food_listings": 
            mycursor.execute("use food_waste_management ")
            mycursor.execute("select Food_id from food_listings")
            results = mycursor.fetchall()
            
            food_listings_table_values= pd.DataFrame(results, columns=["Food_id"]) 
            food_listings_table_values_sorted_ids = food_listings_table_values["Food_id"].sort_values().tolist()

            with st.form("update food_listings_table_values"):

               id=st.selectbox("Select id",food_listings_table_values_sorted_ids)
           
               submit_button = st.form_submit_button(label='Ok')   
            st.write("fill the all column")
            form = st.form(key='update new datas in {Table_Name}')
            
            Food_name= form.text_input("Food_name*")
            Quantity=form.text_input("Quantity*")
            Ex_Date=form.text_input("Ex_Date*")
            providers_ID=form.text_input("providers_ID*")
            Provider_Type=form.text_input("Provider_Type*")
            Location=form.text_input("Location*")
            Food_Type = form.text_input("Food_Type*")
            Meal_Type = form.text_input("Meal_Type*")
            # submit button conformation for inserting new values
            submit_button = form.form_submit_button(label='update table')
            if submit_button: 
               # sql query to insert values in respective table
              mycursor.execute("use food_waste_management ")
              mycursor.execute(f"""update {Table_Name} set
                                Food_name="{Food_name}", Quantity="{Quantity}", Ex_Date="{Ex_Date}", providers_ID="{providers_ID}",
                                Provider_Type="{Provider_Type}", Location="{Location}", Food_Type="{Food_Type}", Meal_Type="{Meal_Type}"
                                where Food_id="{id}"              """)

              

              st.success("Values updated!") 


        elif Table_Name=="claims":
            mycursor.execute("use food_waste_management ")
            mycursor.execute("select Claim_ID from claims")
            results = mycursor.fetchall()
            
            claims_table_values= pd.DataFrame(results, columns=["Claim_ID"]) 
            claims_table_values_sorted_ids = claims_table_values["Claim_ID"].sort_values().tolist()

            with st.form("update claims_table_values"):

               id=st.selectbox("Select id",claims_table_values_sorted_ids)
           
               submit_button = st.form_submit_button(label='Ok')  
               st.write("fill the all column")  
            form = st.form(key='update new datas in {Table_Name}')
               
            Food_ID= form.text_input("Food_ID*")
            Receiver_ID=form.text_input("Receiver_ID*")
            Status= form.text_input("Status*")
            Timestamp = form.text_input("Timestamp*")
            submit_button = form.form_submit_button(label='update table')
            if submit_button:
                   # sql query to insert values in respective table
                  mycursor.execute("use food_waste_management ")
                  mycursor.execute(f"""update {Table_Name} set
                                  Food_ID="{Food_ID}",Receiver_ID="{Receiver_ID}",Status="{Status}",Timestamp="{Timestamp}"
                                  where Claim_ID="{id}"    """)
                  st.success("Values updated!")        

        elif Table_Name=="Volunteer":
            mycursor.execute("use food_waste_management ")
            mycursor.execute("select volunteer_id from Volunteer")
            results = mycursor.fetchall()
            
            Volunteer_table_values= pd.DataFrame(results, columns=["volunteer_id"]) 
            Volunteer_table_values_sorted_ids = Volunteer_table_values["volunteer_id"].sort_values().tolist()

            with st.form("update Volunteer_table_values"):

               id=st.selectbox("Select id",Volunteer_table_values_sorted_ids)
           
               submit_button = st.form_submit_button(label='Ok')
               st.write("fill the all column")
            form = st.form(key='update new datas in {Table_Name}')
            
            name = form.text_input("Name*")
            City_name = form.text_input("City*")
            Contact = form.text_input("Contact*")
            submit_button = form.form_submit_button(label='update table')
            if submit_button:
                  # 1st find out data for alloted provider column
                  mycursor.execute("use food_waste_management ")
                  # based on volunteer city provider details alloted for volunteer 
                  # and provider detail inserted in to alloted column in volunteer table
                  mycursor.execute(f"select Name from providers where City='{City_name}' ")
                  results = mycursor.fetchall()
                  name_provider = pd.DataFrame(results, columns=["Name"])
                  Alloted=name_provider["Name"]
                  # insert data into the volunteer table
                  mycursor.execute("use food_waste_management ")
                  mycursor.execute(f"""update {Table_Name} set
                                   V_name="{name}",V_city="{City_name}",V_contact="{Contact}",Alloted_provider="{Alloted}"
                                   where volunteer_id="{id}"   """)
                  st.success("Values updated!")            


    if Functions=="Delete":
        Table_Name=st.selectbox("Select Tables",["providers","receivers","food_listings","claims","Volunteer"])
        if Table_Name=="providers":
            mycursor.execute("use food_waste_management ")
            mycursor.execute("select providers_id from providers")
            results = mycursor.fetchall()
            
            providers_table_values= pd.DataFrame(results, columns=["providers_id"]) 
            providers_table_values_sorted_ids = providers_table_values["providers_id"].sort_values().tolist()

            with st.form("delete_providers_table_values"):

               id=st.selectbox("Select id",providers_table_values_sorted_ids)
           
               submit_button = st.form_submit_button(label='Ok')
            if submit_button:
                mycursor.execute("use food_waste_management ")
                mycursor.execute(f"DELETE FROM providers WHERE providers_id=%s",(id,))
                st.success("Values Deleted!")

        if Table_Name=="receivers":
            mycursor.execute("use food_waste_management ")
            mycursor.execute("select Receiver_id from receivers")
            results = mycursor.fetchall()
            
            Receiver_table_values= pd.DataFrame(results, columns=["Receiver_id"]) 
            Receiver_table_values_sorted_ids = Receiver_table_values["Receiver_id"].sort_values().tolist()

            with st.form("delete receivers_table_values"):

               id=st.selectbox("Select id",Receiver_table_values_sorted_ids )
           
               submit_button = st.form_submit_button(label='Ok')
            if submit_button:
                mycursor.execute("use food_waste_management ")
                mycursor.execute(f"DELETE FROM receivers WHERE Receiver_id=%s",(id,))
                st.success("Values Deleted!")

        if Table_Name=="food_listings":
            mycursor.execute("use food_waste_management ")
            mycursor.execute("select Food_id from food_listings")
            results = mycursor.fetchall()
            
            food_listings_table_values= pd.DataFrame(results, columns=["Food_id"]) 
            food_listings_table_values_sorted_ids = food_listings_table_values["Food_id"].sort_values().tolist()

            with st.form("delete food_listings_table_values"):

               id=st.selectbox("Select id",food_listings_table_values_sorted_ids)
           
               submit_button = st.form_submit_button(label='Ok')
            if submit_button:
                mycursor.execute("use food_waste_management ")
                mycursor.execute(f"DELETE FROM food_listings WHERE Food_id=%s",(id,))
                st.success("Values Deleted!")

        if Table_Name=="claims":
            mycursor.execute("use food_waste_management ")
            mycursor.execute("select Claim_ID from claims")
            results = mycursor.fetchall()
            
            claims_table_values= pd.DataFrame(results, columns=["Claim_ID"]) 
            claims_table_values_sorted_ids = claims_table_values["Claim_ID"].sort_values().tolist()

            with st.form("delete claims_table_values"):

               id=st.selectbox("Select id",claims_table_values_sorted_ids)
           
               submit_button = st.form_submit_button(label='Ok')
            if submit_button:
                mycursor.execute("use food_waste_management ")
                mycursor.execute(f"DELETE FROM claims WHERE Claim_ID=%s",(id,))
                st.success("Values Deleted!")

        if Table_Name=="Volunteer":
            mycursor.execute("use food_waste_management ")
            mycursor.execute("select volunteer_id from Volunteer")
            results = mycursor.fetchall()
            
            Volunteer_table_values= pd.DataFrame(results, columns=["volunteer_id"]) 
            Volunteer_table_values_sorted_ids = Volunteer_table_values["volunteer_id"].sort_values().tolist()

            with st.form("delete Volunteer_table_values"):

               id=st.selectbox("Select id",Volunteer_table_values_sorted_ids)
           
               submit_button = st.form_submit_button(label='Ok')
            if submit_button:
                mycursor.execute("use food_waste_management ")
                mycursor.execute(f"DELETE FROM Volunteer WHERE volunteer_id=%s",(id,))
                st.success("Values Deleted!")


elif page=="sql Quary & Visualization":
    st.markdown(
    """
    <style>
    .header {
        color: black; /* Text color */
        background-color:   #008000; /* Solid green background */
        padding: 40px;
        text-align: center;
        font-size: 40px;
        font-weight: bold;
        border-radius: 100px;
    }
    </style>
    <div class="header">sql Quary & Visualization</div>
    """,
    unsafe_allow_html=True
)
    st.subheader("Food Providers & Receivers")
    Query=st.selectbox("select_queries",["","How many food providers and receivers are there in each city?",
                                         "Which type of food provider (restaurant, grocery store, etc.) contributes the most food?",
                                         "What is the contact information of food providers in a specific city?",
                                         "Which receivers have claimed the most food?"])
    if Query=="How many food providers and receivers are there in each city?":
        mycursor.execute("use food_waste_management ")
        mycursor.execute("""select count(providers_id) as number_Of_providers_in_each_city,city from providers
                            group by city""")
        results = mycursor.fetchall()
           
        providers_count= pd.DataFrame(results, columns=["number_Of_providers_in_each_city","city"])
        st.write(providers_count) 

        mycursor.execute("""select count(Receiver_id) as number_Of_receivers_in_each_city,city from receivers
                            group by city""")
        results = mycursor.fetchall()
           
        receivers_count= pd.DataFrame(results, columns=["number_Of_receivers_in_each_city","city"])
        st.write(receivers_count) 
    
    if Query=="Which type of food provider (restaurant, grocery store, etc.) contributes the most food?":
      
        mycursor.execute("use food_waste_management ")
        mycursor.execute("""select count(Food_id) as totel_count_of_provider_type ,Provider_Type as type_of_food_provider from 
                         food_listings group by Provider_Type  order by totel_count_of_provider_type desc
                         limit 1  """)
        results = mycursor.fetchall()
           
        provider_type= pd.DataFrame(results, columns=["totel_count_of_provider_type","type_of_food_provider"])
        
        st.write(provider_type )
    if Query=="What is the contact information of food providers in a specific city?":
        mycursor.execute("use food_waste_management ")
        mycursor.execute("""select contact,city from providers
                            order by city""")
        results = mycursor.fetchall()
           
        contact_information= pd.DataFrame(results, columns=["contact","city"])
        st.write(contact_information) 

    if Query=="Which receivers have claimed the most food?":
        mycursor.execute("USE food_waste_management")
        mycursor.execute("""
        SELECT  R.Receiver_id,R.name,received_table.Status,received_table.number_of_times_food_received
        FROM receivers R 
        JOIN 
          (SELECT  Receiver_ID, COUNT(Claim_ID) AS number_of_times_food_received, Status FROM claims WHERE Status = 'Completed' 
            GROUP BY Receiver_ID, Status) AS received_table 
        ON 
          R.Receiver_id = received_table.Receiver_ID 
          order by number_of_times_food_received desc limit 1
        """)
        results = mycursor.fetchall()

        # Convert results to a DataFrame
        receivers_count = pd.DataFrame(results, columns=["Receiver_ID", "name", "Status","number_of_times_food_received"])
        st.write(receivers_count)

    st.subheader("Food Listings & Availability")
    Query_set2=st.selectbox("select_queries",["What is the total quantity of food available from all providers?",
                                           "Which city has the highest number of food listings?",
                                           "What are the most commonly available food types?"])
                                           
    if Query_set2=="What is the total quantity of food available from all providers?":
        mycursor.execute("USE food_waste_management")
        mycursor.execute("""select sum(Quantity) total_quantity from food_listings""")
        results = mycursor.fetchall()
        total_quantity = pd.DataFrame(results, columns=["total_quantity"])
        st.write(total_quantity)

    if Query_set2=="Which city has the highest number of food listings?":
        mycursor.execute("USE food_waste_management")
        mycursor.execute("""select f.Location from (select count(Food_id) as foodid,Location from food_listings group by Location
                         order by foodid desc limit 1 ) f""")
        results = mycursor.fetchall()
        total_ = pd.DataFrame(results, columns=["Location"])
        st.write(total_)
    if Query_set2=="What are the most commonly available food types?":
        mycursor.execute("USE food_waste_management")
        mycursor.execute("select Food_Type from food_listings group by Food_Type ")
        results = mycursor.fetchall()
        common_food_type = pd.DataFrame(results, columns=["Food_Type"])
        st.write(common_food_type )


    st.subheader("Claims & Distribution")
    Query_set2=st.selectbox("select_queries",["How many food claims have been made for each food item?",
                                              "Which provider has had the highest number of successful food claims?",
                                              "What percentage of food claims are completed vs. pending vs. canceled?"])
    if Query_set2=="How many food claims have been made for each food item?":
        mycursor.execute("USE food_waste_management")
        mycursor.execute("""select sum(N.number_of_claims) as NUMBR_OF_CLAIMS ,N.Food_name from (select count(C.Claim_ID) as number_of_claims,
                         F.Food_name,C.Food_ID from claims as C
                        join food_listings as F on C.Food_ID=F.Food_ID group by Food_ID
                         ) as N
                         group by N.Food_name
                         order by NUMBR_OF_CLAIMS desc """)
        results = mycursor.fetchall()
        food_claims = pd.DataFrame(results, columns=["NUMBR_OF_CLAIMS","Food_name"])
        st.write(food_claims)
        #subplot gives the food claims based on food name
        fig,ax=plt.subplots()
        ax.scatter(food_claims["NUMBR_OF_CLAIMS"],food_claims["Food_name"])
        st.pyplot(fig) 
    if Query_set2=="Which provider has had the highest number of successful food claims?":
            mycursor.execute("USE food_waste_management")
            mycursor.execute("""select P.providers_id,P.name,CC.count_of_successful_claims from providers P 
                             join (select F.providers_ID as p_id,count(F.providers_ID) count_of_successful_claims,C.Status 
                             from food_listings F 
                             join claims C 
                             on F.Food_id=C.Food_ID where C.Status="Completed"  
                             group by providers_ID
                             order by count_of_successful_claims desc limit 1
                             ) as CC
                             on P.providers_id=CC.p_id""")
            results = mycursor.fetchall()
            successful_claims = pd.DataFrame(results, columns=["providers_id","name","count_of_successful_claims"])
            st.write(successful_claims)
    if Query_set2=="What percentage of food claims are completed vs. pending vs. canceled?":  
            mycursor.execute("""SELECT Status,COUNT(Claim_ID) AS total_claims,
                             ROUND((COUNT(Claim_ID) * 100.0 / (SELECT COUNT(Claim_ID) FROM claims)), 2) AS percentage
                             FROM claims GROUP BY Status""")
            results = mycursor.fetchall()
            percentage = pd.DataFrame(results, columns=["Status","total_claims","percentage"])
            st.write(percentage)
            fig,ax=plt.subplots()
            ax.pie(percentage["percentage"], labels=percentage["Status"], autopct='%1.2f%%')
            st.pyplot(fig) 

    
    st.subheader("Analysis & Insights")
    Query_set3=st.selectbox("select_queries",["What is the average quantity of food claimed per receiver?",
                                              " Which meal type (breakfast, lunch, dinner, snacks) is claimed the most?",
                                              "What is the total quantity of food donated by each provider?"])
    if Query_set3=="What is the average quantity of food claimed per receiver?":
        mycursor.execute("USE food_waste_management")
        mycursor.execute("""select ROUND(count(Status)/count(distinct Food_ID)  ,2) as average
                          from claims where Status='Completed'
                           """)
        results = mycursor.fetchall()
        average= pd.DataFrame(results, columns=["average"])
        st.write(average)
        
    if Query_set3==" Which meal type (breakfast, lunch, dinner, snacks) is claimed the most?":
        mycursor.execute(""" select count(C.Claim_ID) as number_of_times_claimed, F.Meal_Type from claims C
                         join food_listings F on C.Food_ID=F.Food_id where C.Status='Completed'group by F.Meal_Type 
                         order by number_of_times_claimed desc """)
        results = mycursor.fetchall()
        claims= pd.DataFrame(results, columns=["number_of_times_claimed","Meal_Type"])
        st.write(claims)
        st.bar_chart(claims,x="Meal_Type",y="number_of_times_claimed",horizontal=False,width=1,height=None)
    if Query_set3=="What is the total quantity of food donated by each provider?":
         mycursor.execute(""" select F.providers_ID,count(C.Claim_ID) donated_quantity from food_listings F join claims C on F.Food_id=C.Food_ID 
                          where C.Status='Completed'
                          group by F.providers_ID
                          order by donated_quantity desc""")
         results = mycursor.fetchall()
         donated_quantity= pd.DataFrame(results, columns=["providers_ID","donated_quantity"])
         st.write(donated_quantity)

    Query_set4=st.selectbox("select_queries",["The most frequent food providers and their contributions?",
                                              "The highest demand locations based on food claims?"])
    if Query_set4=="The most frequent food providers and their contributions?":
         mycursor.execute("USE food_waste_management")
         mycursor.execute("""select F.providers_ID,P.name,count(F.Food_id) number_of_times_donated,sum(F.Quantity) total_quantity from food_listings F
                          join providers P
                          on F.providers_ID=P.providers_id
                          group by providers_ID
                          having count(F.Food_id)>2
                          order by total_quantity desc""" )
         results = mycursor.fetchall()
         most_frequent= pd.DataFrame(results, columns=["providers_ID","name","number_of_times_donated","total_quantity"])  #number_of_food_id  refers the how many times they are donated
         st.write(most_frequent)


    if Query_set4=="The highest demand locations based on food claims?":
        mycursor.execute("USE food_waste_management")
        mycursor.execute("""select R.city,count(C.Claim_ID) demands  from receivers R 
                        join  claims C 
                        on R.Receiver_id=C.Receiver_ID 
                        group by city 
                        order by demands desc 
                        """)   #WHERE C.Status = 'Completed'
        results = mycursor.fetchall()
        donated_quantity= pd.DataFrame(results, columns=["city","demands"])  
        st.write(donated_quantity)
        st.write("The highest demand locations based on successful food claims?")
        mycursor.execute("USE food_waste_management")
        mycursor.execute("""select R.city,count(C.Claim_ID) demands,Status  from receivers R 
                        join  claims C 
                        on R.Receiver_id=C.Receiver_ID 
                        WHERE C.Status = 'Completed'
                        group by city 
                        order by demands desc 
                        """)  
        results = mycursor.fetchall()
        donated_quantity= pd.DataFrame(results, columns=["city","demands","Status"])  
        st.write(donated_quantity)
elif page=="Learner sql Query":
    st.markdown(
    """
    <style>
    .header {
        color: black; /* Text color */
        background-color:   #008000; /* Solid green background */
        padding: 40px;
        text-align: center;
        font-size: 40px;
        font-weight: bold;
        border-radius: 100px;
    }
    </style>
    <div class="header">Learner sql Query</div>
    """,
    unsafe_allow_html=True
)
    st.subheader("Analysis & Insights")
    Query_set1=st.selectbox("select_queries",["Which city has the total quantity of food listings?",
                                               "How many providers and receivers are in a same city?",
                                               "What is the expiration period for cancelled claims from the time of cancellation?",
                                               "list of expired food items that are still pending?"
                                               ])
    if Query_set1=="Which city has the total quantity of food listings?":
        mycursor.execute("USE food_waste_management")
        mycursor.execute("""select Location,sum(Quantity) total_quantity, COALESCE(R.Receiver_id, 'None') AS receiver_id
                        from food_listings F left join receivers R
                         on  F.location=R.city
                         group by F.Location,R.Receiver_id
                         order by total_quantity  desc """)
        results = mycursor.fetchall()
        highest_quantity= pd.DataFrame(results, columns=["Location","total_quantity","Receiver_id"])
        st.write(highest_quantity)


    elif Query_set1=="How many providers and receivers are in a same city?":
        mycursor.execute("USE food_waste_management")   
        mycursor.execute("""select PC.providers_id as Providers_id,RC.receivers_id as Receivers_id ,PC.city as City
                          from (select count(distinct P.providers_id) providers_id ,P.city as city from providers P 
                          join receivers R
                         on P.city=R.city
                         group by P.city,R.city
                         order by P.city desc) as PC
                         join(select count(distinct R.Receiver_id) receivers_id ,R.city as city from receivers R 
                          join providers P 
                         on P.city=R.city
                         group by P.city,R.city
                         order by R.city desc) as RC
                         on PC.city=RC.city""")
        results = mycursor.fetchall()
        providers_and_receivers= pd.DataFrame(results, columns=["Providers_id","Receivers_id","City"])
        st.write(providers_and_receivers)
        # matplot used to show  values range of both  Receivers_id and Providers_id
        
        fig,ax=plt.subplots()
        ax.scatter(providers_and_receivers["Receivers_id"],providers_and_receivers["Providers_id"])
        st.pyplot(fig) 
         # area chart shows providers and receivers count in same  city
        st.area_chart (providers_and_receivers,y=["Receivers_id"])  
        st.area_chart (providers_and_receivers,y=["Providers_id"])  

    elif Query_set1=="What is the expiration period for cancelled claims from the time of cancellation?":
        mycursor.execute("USE food_waste_management")   
        mycursor.execute("""select Timestamp, Ex_Date, DATEDIFF(Ex_Date,Timestamp) expires_with_in
                          from claims C
                         join food_listings F on C.Food_ID=F.Food_id 
                         where Status='Cancelled'
                         
                         order by expires_with_in """)
        results = mycursor.fetchall()
        datediff= pd.DataFrame(results, columns=["Timestamp","Ex_Date","expires_with_in"])
        st.write(datediff)

    elif Query_set1=="list of expired food items that are still pending?":
        mycursor.execute("USE food_waste_management")   
        mycursor.execute("""select C.Food_ID,F.Meal_Type,F.Food_Type,C.Timestamp, F.Ex_Date, DATEDIFF(F.Ex_Date,C.Timestamp) as days_to_expiry, 
                         case
                            when DATEDIFF(F.Ex_Date,C.Timestamp) <=0 then "expired"
                            else "not expired"
                         end as validity from claims C
                         join food_listings F on C.Food_ID=F.Food_id  where Status in ("Pending","Cancelled")
                         group by C.Food_ID,F.Meal_Type,F.Food_Type,C.Timestamp,F.Ex_Date,days_to_expiry,validity
                         """)
        results = mycursor.fetchall()
        valitity_table= pd.DataFrame(results, columns=["Food_ID","Meal_Type","Food_Type","Timestamp","Ex_Date","days_to_expiry","validity"])
        st.write(valitity_table)
if page=="Get Your Food":
 st.markdown(
    """
    <style>
    .header {
        color: black; /* Text color */
        background-color:  #008000; /* Solid green background */         
        padding: 40px;
        text-align: center;
        font-size: 40px;
        font-weight: bold;
        border-radius: 100px;
    }
    </style>
    <div class="header">Get Your Food</div>
    """,
    unsafe_allow_html=True
)
 mycursor.execute("USE food_waste_management")
 mycursor.execute("SELECT * FROM food_listings")
 results = mycursor.fetchall()
 columns = [desc[0] for desc in mycursor.description]
 food_listings_values = pd.DataFrame(results, columns=columns)

 st.write("Available food listings:")
 st.dataframe(food_listings_values)

 #select your receiver id

 mycursor.execute("select Receiver_id from receivers")
 results = mycursor.fetchall()
            
 Receiver_table_values= pd.DataFrame(results, columns=["Receiver_id"]) 
 Receiver_table_values_sorted_ids = Receiver_table_values["Receiver_id"].sort_values().tolist()
 with st.form("select_receiver_id"):

               id=st.selectbox("Select id",Receiver_table_values_sorted_ids )
           
               submit_button = st.form_submit_button(label='Ok')
 st.write("You don't have a Receiver id please update your details in to Receivers table ")

# First selection form (Meal Type)
 with st.form("meal_selection_form"):
    selected_meal_type = st.selectbox("Select Meal Type", food_listings_values["Meal_Type"].unique())
    selected_food_type = st.selectbox("Select Food Type", food_listings_values["Food_Type"].unique())

    submit_button_1 = st.form_submit_button(label="Select Meal Type")
    
    if submit_button_1:
        selected_date = pd.to_datetime("today").strftime('%Y-%m-%d')

        #  Expired food items do not appear on the list.

        query = """SELECT * FROM food_listings 
                   WHERE Meal_Type = %s 
                   AND Food_Type = %s 
                   AND Ex_Date > %s"""

        values = (selected_meal_type, selected_food_type, selected_date)
        mycursor.execute(query, values)

        results = mycursor.fetchall()
        columns = [desc[0] for desc in mycursor.description]
        food_listings_values = pd.DataFrame(results, columns=columns)

        st.write("Filtered food listings:")
        st.dataframe(food_listings_values)

# Second selection form (Food ID)
 with st.form("food_selection"):
    selected_id = st.text_input("Enter Food ID from available food listings")

    submit_button = st.form_submit_button(label='Submit')

    if submit_button:
        # Convert selected_id to integer if needed
        try:
            selected_id = int(selected_id)
        except ValueError:
            st.error("Invalid Food ID. Please enter a valid food ID.")
        else:
            # Filter based on the selected ID
            selected_row1 = food_listings_values.loc[food_listings_values["Food_id"] == selected_id]

            if selected_row1.empty:
                st.warning("No matching food found. Check the Food ID.")
            else:
                st.write("Your selected food details:")
                st.dataframe(selected_row1)
 with st.form(key='You must get delivery volunteer details '):
   submit_button = st.form_submit_button(label='ok')
   if submit_button:

      mycursor.execute(f"""
      SELECT V_name, V_contact 
      FROM Volunteer  
      WHERE V_city = (SELECT Location FROM food_listings WHERE Food_id='{selected_id}')
      """)

      results = mycursor.fetchall()
      volunteer_details= pd.DataFrame(results, columns=["V_name","V_contact"])
      st.write("volunteer details")
      st.write(volunteer_details)
 #update in claims table 
      
      query = """
      INSERT INTO claims (Food_ID, Receiver_ID, Status, Timestamp) 
      VALUES (%s, %s, %s, CURRENT_TIMESTAMP)
      """
      mycursor.execute(query, (selected_id, id, "Pending"))


      st.success("your food details inserted into claims table!")
      st.write("Any one of the above volunteer will deliver your food")


      query = """
      UPDATE food_listings 
      SET Quantity = Quantity - 1 
      WHERE Food_id = %s
      """
      mycursor.execute(query, (selected_id,))

                


st.sidebar.markdown("[Hunger in US ](https://www.bread.org/hunger-explained/hunger-in-the-u-s/) ")
st.sidebar.markdown("[similar Website](https://www.feedingamerica.org/hunger-in-america)")
st.sidebar.markdown("[Food Scarcity’s Influence on Mental Health During the COVID-19 Pandemic in New York State]"
"(https://nyhealthfoundation.org/resource/food-scarcitys-influence-on-mental-health-during-the-covid-19-pandemic-in-new-york-state/)")
