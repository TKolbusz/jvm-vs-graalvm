import pandas as pd
import matplotlib.pyplot as plt
import sys

def analyze_throughput(file_path):
    # Read CSV data from file
    df = pd.read_csv(file_path)

    # Convert the 'timeStamp' column to a more readable format
    df['timeStamp'] = pd.to_datetime(df['timeStamp'], unit='ms')

    # Analyzing throughput
    total_time = (df['timeStamp'].max() - df['timeStamp'].min()).seconds + 1  # +1 to avoid division by zero
    total_requests = len(df)
    throughput = total_requests / total_time  # requests per second
    print(f"Throughput: {throughput:.2f} requests per second")

    # Drawing a histogram for elapsed time
    plt.figure(figsize=(12, 5))
    plt.subplot(1, 2, 1)
    plt.hist(df['elapsed'], bins=20, edgecolor='black', alpha=0.7)
    plt.title('Elapsed Time Distribution')
    plt.xlabel('Elapsed Time (ms)')
    plt.ylabel('Number of Requests')

    # Drawing a line plot to visualize throughput over time
    df.set_index('timeStamp', inplace=True)
    df['cum_count'] = range(1, len(df) + 1)
    plt.subplot(1, 2, 2)
    df['cum_count'].plot()
    plt.title('Cumulative Requests Over Time')
    plt.xlabel('Time')
    plt.ylabel('Number of Requests')
    plt.tight_layout()

    plt.show()

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script_name.py <csv_file_path>")
    else:
        analyze_throughput(sys.argv[1])