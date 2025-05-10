
#------------------MO-IT148 Homework: IoT Data Simulation_A3101_NIEVA OSIAS JR--------------------#

# This script generates a synthetic and Random only dataset for IoT healthcare data with sensors.
import pandas as pd                         # This will be used to create DataFrames and save data        
import numpy as np                          # This will be used to generate random numbers      
from datetime import datetime, timedelta    # This will be used to generate timestamps
import random                               # This will be used to generate random values     

# Your 50 provided Filipino full names
provided_names = [
    "Albert Pablo", "Fergus Laurente", "Daniel Guzman", "Elton Rico", "Arvin dela Cruz", "Ernie Sotto",
    "Jacob Vasquez", "Jerome Gregorio", "Christian Guillermo", "Genkei Javier", "Christian Reyes",
    "Jaime Nicolas", "Ryan Fajardo", "Crisanto Pangilinan", "Nathan Malinao", "Xavier Andaya", "Calix Blanco",
    "Harlem de Los Santos", "Dranreb Manuel", "Wilfred dela Rosa", "Benjamin Alarcon", "Arellano Punzalan",
    "Melchor Catalan", "Jalen Conde", "Kylen Villareal", "Johnny Espino", "John Paul Cuizon", "Rodrigo Baguio",
    "Joshua Delos Reyes", "Alvin Narciso", "Ryan Musa", "Jonas Corpuz", "Danilo Prado", "John Carlo Pimentel",
    "John Mark Asuncion", "Juan Cruz", "Jaime Ballesteros", "Lancel Cano", "Calgary Molina", "Arvin Arcilla",
    "Aaron Benitez", "Ash Bondoc", "Cedric Fernando", "Fraley Manansala", "John Rey Castro", "Juan Tenorio",
    "Shawn Domingo", "James Samson", "Vince Perez", "Cyler Cordova"
]
# The provided names are a mix of first and last names, so we will split them into first and last names
# SOURCE: https://www.namesnerd.com/people/filipino-name-generator/ (Accessed on 2025-05-09 by Osias Nieva Jr)
# Splitting the names into first and last names
# Random name pool for variability
filipino_first_names = [
    "Jose", "Maria", "Juan", "Ana", "Antonio", "Luz", "Pedro", "Carmen", "Ramon", "Teresa",
    "Carlos", "Rosa", "Andres", "Elena", "Miguel", "Isabel", "Ricardo", "Leticia", "Manuel", "Dolores",
    "Roberto", "Ligaya", "Eduardo", "Consuelo", "Fernando", "Virginia", "Jesus", "Estrella", "Jorge", "Adela"
]

filipino_last_names = [
    "Reyes", "Cruz", "Dela Cruz", "Santos", "Garcia", "Mendoza", "Torres", "Gonzales", "Ramos", "Lopez",
    "Rodriguez", "Morales", "Aquino", "Castro", "Villanueva", "Domingo", "Marquez", "Navarro", "Aguilar", "Salazar",
    "Delos Santos", "Silva", "Soriano", "Velasco", "Bautista", "Padilla", "Alvarez", "Ocampo", "Pascual", "Flores"
]

num_records = 500       # Records to generate = (number_records)input 
data = []               # List to hold the generated records

for _ in range(num_records):
    birth_date = datetime.now() - timedelta(days=random.randint(18*365, 90*365))  # Age between 18 and 90
    age = (datetime.now() - birth_date).days // 365

    # 40% chance to use one of the provided names, 60% chance to generate a new one
    if random.random() < 0.4:
        full_name = random.choice(provided_names)                                                   # Randomly selected from the provided names 
    else:
        full_name = f"{random.choice(filipino_first_names)} {random.choice(filipino_last_names)}"   # Randomly generated name

    record = {
        "timestamp": datetime.now() - timedelta(minutes=np.random.randint(0, 1440)),    # Random timestamp within the last 24 hours
        "patient_id": f"PID{random.randint(1000, 9999)}",                               # Random patient ID % of which 40% are from the provided names the other 60% are random
        "name": full_name,                                                              # Full name from the provided list or generated     
        "birth_date": birth_date.strftime("%Y-%m-%d"),                                  # Birth date in YYYY-MM-DD format        
        "age": age,                                                                     # Age in years     
        "heart_rate": np.random.randint(60, 100),                                       # Random heart rate in bpm from wearables
        "blood_pressure_systolic": np.random.randint(110, 140),                         # Random systolic blood pressure in mmHg from Huawei watch wearables
        "blood_pressure_diastolic": np.random.randint(70, 90),                          # Random diastolic blood pressure in mmHg from Huawei watch wearables
        "oxygen_level": np.random.randint(95, 100),                                     # Random oxygen level in SpO2 % from wearables      
        "body_temp_celsius": round(np.random.uniform(36.0, 37.5), 1),                   # Random body temperature in °C from wearables
        "activity_level": np.random.choice(["low", "medium", "high"]),                  # Random activity level from wearables  
        "steps_count": np.random.randint(100, 10000),                                   # Random steps count from pedometer
        "sleep_hours": round(np.random.uniform(4.0, 9.0), 1),                           # Random sleep duration in hours
        "sleep_quality": np.random.choice(["poor", "fair", "good", "excellent"]),       # Random sleep quality
        "location": np.random.choice(["ward", "ICU", "ER", "room 101", "recovery"]),    # Random location in the hospital
        "ecg_status": np.random.choice(["normal", "abnormal"])                          # Random ECG status from ECG patch    
    }
    data.append(record)                                     # Collecting data and appending to the list         

# This area convert to DataFrame and save
df = pd.DataFrame(data)                                     # Creating DataFrame from the list
df.to_csv("iot_healthcare_data.csv", index=False)           # Saving to CSV
df.to_json("iot_healthcare_data.json", orient="records")    # Saving to JSON

# this was designed to display the first few records of the DataFrame
# and some basic statistics about the data
# This area is for displaying the first few records and some basic statistics
print("First few records of the DataFrame:")
print("--------------------------------------------------")
print(df.head())                                            # Displaying the first few records to verify the data
print(df.info())                                            # Displaying the DataFrame information
print(df.describe())                                        # Displaying the DataFrame description
print(df.isnull().sum())                                   # Checking for missing values
print(df.duplicated().sum())                               # Checking for duplicate records
print(df["age"].value_counts())                            # Displaying the age distribution
print(df["heart_rate"].value_counts())                     # Displaying the heart rate distribution
print(df["blood_pressure_systolic"].value_counts())       # Displaying the systolic blood pressure distribution
print(df["blood_pressure_diastolic"].value_counts())      # Displaying the diastolic blood pressure distribution
print(df["oxygen_level"].value_counts())                  # Displaying the oxygen level distribution
print(df["body_temp_celsius"].value_counts())            # Displaying the body temperature distribution
print(df["activity_level"].value_counts())               # Displaying the activity level distribution
print(df["steps_count"].value_counts())                 # Displaying the steps count distribution
print(df["sleep_hours"].value_counts())                # Displaying the sleep hours distribution
print(df["sleep_quality"].value_counts())              # Displaying the sleep quality distribution
print(df["location"].value_counts())                   # Displaying the location distribution
print(df["ecg_status"].value_counts())                # Displaying the ECG status distribution    
print("--------------------------------------------------")  


