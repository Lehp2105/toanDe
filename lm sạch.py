import pandas as pd

# Load the CSV file
file_path = 'D:/python/toàn/ThongTinHangTonKho_Chinh.csv'  # Update this path to your file location
data = pd.read_csv(file_path)

def clean_data(df):
    # Drop duplicates and assign the result back to df
    df = df.drop_duplicates()
    
    # Fill missing values in 'Current_Stock' with the median, and assign back to the column
    if df['Current_Stock'].isnull().sum() > 0:
        df['Current_Stock'] = df['Current_Stock'].fillna(df['Current_Stock'].median())
    
    # Reset the index and assign back to df
    df = df.reset_index(drop=True)
    
    return df

# Clean the data
cleaned_data = clean_data(data)

# Save the cleaned data to a new CSV file
cleaned_file_path = 'D:/python/toàn/cleaned_file.csv'  # Update this path to save the cleaned file
cleaned_data.to_csv(cleaned_file_path, index=False)
