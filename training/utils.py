import matplotlib.pyplot as plt
import os

def save_plot(values, title, path):
    os.makedirs(os.path.dirname(path), exist_ok=True)  # 🔥 fix

    plt.figure()
    plt.plot(values)
    plt.title(title)
    plt.xlabel("Epoch")
    plt.ylabel(title)
    plt.savefig(path)
    plt.close()