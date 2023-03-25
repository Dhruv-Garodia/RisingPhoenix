import pandas as pd
import numpy as np
import random

# Load the data from the CSV file
data = pd.read_csv("data.csv")

# Split the data into training and testing sets
train_data = data.sample(frac=0.8, random_state=42)
test_data = data.drop(train_data.index)

# Define the federated learning function


def federated_learning(client_ratings):
    # Compute the average rating across all clients

    sum = 0
    for i in client_ratings:
        sum += pd.to_numeric(i)

    global_average = sum/len(client_ratings)

    # Print the global average rating
    print("Global average rating:", global_average)


# Generate random client IDs
client_ids = list(range(10))

# Simulate multiple clients by randomly splitting the training data
client_data = []
for client_id in client_ids:
    client_subset = train_data.sample(
        frac=0.1, random_state=random.randint(0, 100))
    client_data.append(client_subset)

# Train the model on each client's data
for i, client_subset in enumerate(client_data):
    # Extract the ratings for this client's products

    client_ratings = client_subset["rating"].values
    pd.to_numeric(client_ratings)

    # Call the federated learning function with this client's ratings
    federated_learning(client_ratings)
