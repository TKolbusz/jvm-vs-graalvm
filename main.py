import pandas as pd
import matplotlib.pyplot as plt

def compute_throughput(df):
    df['timeStamp'] = pd.to_datetime(df['timeStamp'], unit='ms')
    total_time = (df['timeStamp'].max() - df['timeStamp'].min()).seconds + 1  # +1 to avoid division by zero
    total_requests = len(df)
    return total_requests / total_time  # requests per second

# Read data from the three files
df1 = pd.read_csv('jvm-100.csv')
df2 = pd.read_csv('jvm-500.csv')
df3 = pd.read_csv('jvm-1000.csv')
df4 = pd.read_csv('graal-100.csv')
df5 = pd.read_csv('graal-500.csv')
df6 = pd.read_csv('graal-1000.csv')

# Compute throughputs
throughput1 = compute_throughput(df1)
throughput2 = compute_throughput(df2)
throughput3 = compute_throughput(df3)
throughput4 = compute_throughput(df4)
throughput5 = compute_throughput(df5)
throughput6 = compute_throughput(df6)

# Visualization
labels = [
    'jvm 100', 'jvm 500', 'jvm 1000',
    'graal 100', 'graal 500', 'graal 1000'
]
throughputs = [throughput1, throughput2, throughput3,throughput4,throughput5,throughput6]

plt.bar(labels, throughputs, color=['red', 'green', 'blue'], alpha=0.7)
plt.xlabel('Data File')
plt.ylabel('Throughput (requests per second)')
plt.title('Throughput Comparison')
plt.show()