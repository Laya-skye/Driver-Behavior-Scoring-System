import pandas as pd
import matplotlib.pyplot as plt

def calculate_driver_score(file_path):
    df = pd.read_csv(file_path)

    overspeed_count = (df['speed'] > 80).sum()
    harsh_brakes = (df['brake'] > 0.5).sum()
    sudden_accel = (df['acceleration'] > 0.5).sum()

    score = 100
    score -= overspeed_count * 3
    score -= harsh_brakes * 2
    score -= sudden_accel * 1.5
    score = max(score, 0)

    print(f"Driver Score: {score}/100")
    print(f"Overspeed Events: {overspeed_count}")
    print(f"Harsh Brakes: {harsh_brakes}")
    print(f"Sudden Acceleration Events: {sudden_accel}")

    plt.bar(['Overspeed', 'Harsh Brakes', 'Sudden Accel'], [overspeed_count,harsh_brakes,sudden_accel])
    plt.title("Risk Events Summary")
    plt.ylabel("Count")
    plt.savefig("driver_report.png")
    plt.show()

if __name__ == "__main__":
    calculate_driver_score("driver_data.csv")
