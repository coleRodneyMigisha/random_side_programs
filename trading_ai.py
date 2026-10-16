import pandas as pd
import numpy as np
import tensorflow as tf

# Load historical data (replace 'stock_data.csv' with your actual file)
data = pd.read_csv('stock_data.csv')

# Preprocess data (normalize price)
data['Normalized_Price'] = (data['Price'] - data['Price'].min()) / (data['Price'].max() - data['Price'].min())

# Create training and testing sets (80/20 split)
train_size = int(len(data) * 0.8)
train_data, test_data = data[:train_size], data[train_size:]

# Prepare data for training (assuming 'Price' is the target variable)
train_X = train_data.drop('Normalized_Price', axis=1).values
train_y = train_data['Normalized_Price'].values.reshape(-1, 1) 
test_X = test_data.drop('Normalized_Price', axis=1).values
test_y = test_data['Normalized_Price'].values.reshape(-1, 1)

# Define the model architecture (LSTM)
model = tf.keras.Sequential([
    tf.keras.layers.LSTM(50, return_sequences=True, input_shape=(train_X.shape[1], 1)),
    tf.keras.layers.LSTM(50),
    tf.keras.layers.Dense(1)
])

# Compile the model
model.compile(optimizer='adam', loss='mean_squared_error')

# Train the model
model.fit(train_X, train_y, epochs=10, batch_size=32)

# Make predictions
predictions = model.predict(test_X)

# Denormalize predictions
predictions = predictions * (data['Price'].max() - data['Price'].min()) + data['Price'].min()

# Evaluate model performance (example: calculate Mean Absolute Error)
from sklearn.metrics import mean_absolute_error
mae = mean_absolute_error(test_y, predictions)
print(f"Mean Absolute Error: {mae}")

# **Important Notes:**

# 1. Replace 'stock_data.csv' and 'Price' with your actual data and target column.
# 2. This is a basic example. Consider:
#    - More complex models (e.g., GRU, transformers)
#    - Feature engineering (e.g., moving averages, technical indicators)
#    - Hyperparameter tuning
#    - Backtesting on historical data
# 3. **This code does NOT include trading execution.** You'll need to integrate with a trading platform's API for that.
# 4. **This is a simplified example for educational purposes.** Real-world trading involves significant risk.

# **Disclaimer:** This code is for illustrative purposes only and does not constitute financial advice.