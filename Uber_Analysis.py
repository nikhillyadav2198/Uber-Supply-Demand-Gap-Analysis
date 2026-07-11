import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Load the dataset
df = pd.read_csv("Uber Request Data.csv")

# Display first 5 rows
print(df.head())

# Last 5 rows
print(df.tail())

# Dataset dimensions
print("Shape:", df.shape)

# Column names
print(df.columns)

# Dataset Information
print(df.info())

# Statistical Summary
print(df.describe(include="all"))

# Missing Values 
print(df.isnull().sum())

# Maximum Cancellation Status
print(df['Pickup point'].value_counts())
print(df['Status'].value_counts())

# Duplicate Values
print("Duplicate Records:", df.duplicated().sum())

# Convert Timestamp
df["Request timestamp"] = pd.to_datetime(
    df["Request timestamp"],
    format="%d-%m-%y %H:%M"
)

df["Drop timestamp"] = pd.to_datetime(
    df["Drop timestamp"],
    format="%d-%m-%y %H:%M",
    errors="coerce"
)

# Total Requests Hour
df['Request_hour'] = df['Request timestamp'].dt.hour

# Status Hour
hourly_status = pd.crosstab(df['Request_hour'], df['Status'])
print(hourly_status)

df["Hour"] = df["Request timestamp"].dt.hour
df["Day"] = df["Request timestamp"].dt.day_name()

print(df.head())

# Ride Status Distribution
status = df["Status"].value_counts()

plt.figure(figsize=(8,5))
status.plot(kind="bar")

plt.title("Ride Status Distribution")
plt.xlabel("Ride Status")
plt.ylabel("Number of Requests")
plt.xticks(rotation=0)

plt.show()

# Pickup Point Analysis
pickup = df["Pickup point"].value_counts()

plt.figure(figsize=(6,5))
pickup.plot(kind="bar")

plt.title("Requests by Pickup Point")
plt.xlabel("Pickup Point")
plt.ylabel("Requests")

plt.show()

# Hour Wise Requests
hourly = df["Hour"].value_counts().sort_index()

plt.figure(figsize=(10,5))
hourly.plot(kind="line", marker="o")

plt.title("Requests by Hour")
plt.xlabel("Hour")
plt.ylabel("Number of Requests")

plt.grid(True)
plt.show()

# Day Wise Requests
day = df["Day"].value_counts()

plt.figure(figsize=(8,5))
day.plot(kind="bar")

plt.title("Day-wise Ride Requests")
plt.xlabel("Day")
plt.ylabel("Requests")

plt.show()

# Pickup Point vs Status
pd.crosstab(df["Pickup point"], df["Status"])

# Completion Rate %
completed = (df["Status"] == "Trip Completed").sum()
total = len(df)

completion_rate = completed / total * 100

print(f"Completion Rate: {completion_rate:.2f}%")