import matplotlib.pyplot as plt
import numpy as np
import pandas as pd


def plot(title):
    with open('/tmp/rl_log.txt', 'r') as f:
        x = f.readlines()

    x = [(e.strip()) for e in x]
    x = x[1:]
    x = np.asarray([float(e) for e in x])
    x = pd.Series(x).rolling(100, min_periods=10).mean()
    plt.plot(x)
    plt.xlabel('Iterations')
    plt.ylabel('Average Reward per Iteration')
    plt.title(title)
    plt.tight_layout()
    plt.show()
    print("Completed")
