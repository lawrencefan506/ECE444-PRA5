import requests
import time
import csv
import pandas as pd
import matplotlib.pyplot as plt

# URL of your deployed Flask app
url = "http://pra5-ece444-env.eba-d45w3adj.us-east-2.elasticbeanstalk.com/predict"

# Test cases
test_cases = {
    "real_news_1": "Poutine comes from Quebec",
    "real_news_2": "Montreal is a better city than Toronto",
    "fake_news_1": "The earth is flat",
    "fake_news_2": "COVID-19 is a hoax"
}

def send_request(text):
    data = {"text": text}
    start_time = time.time()  # Record start time
    response = requests.post(url, json=data)
    end_time = time.time()  # Record end time
    latency = end_time - start_time
    return latency, response.status_code

def run_performance_test():
    results = []
    for case, text in test_cases.items():
        print(f"Running test case: {case}")
        for i in range(25):  # 25 API calls * 4 test cases = 100 calls
            latency, status_code = send_request(text)
            if status_code == 200:
                results.append([case, latency])
                print(f"Call {i+1} for {case}: {latency:.5f} seconds")
            else:
                print(f"Failed request for {case} with status code {status_code}")
    
    # Write results to CSV file
    with open('latency_results.csv', 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(['Test Case', 'Latency (s)'])
        writer.writerows(results)

def plot_boxplot():
    # Read CSV into DataFrame
    df = pd.read_csv('latency_results.csv')
    
    # Create boxplot
    plt.figure(figsize=(10, 6))
    df.boxplot(by='Test Case', column=['Latency (s)'], grid=False, showfliers=False)
    plt.title('Latency Performance per Test Case')
    plt.suptitle('')
    plt.xlabel('Test Case')
    plt.ylabel('Latency (seconds)')
    
    # Save boxplot as an image
    plt.savefig('latency_boxplot.png')
    plt.show()

def calculate_average():
    # Calculate average latency for each test case
    df = pd.read_csv('latency_results.csv')
    avg_latencies = df.groupby('Test Case')['Latency (s)'].mean()
    print("\nAverage Latencies:")
    print(avg_latencies)

if __name__ == "__main__":
    run_performance_test()  # Run performance tests
    plot_boxplot()  # Generate boxplot
    calculate_average()  # Print average latencies
