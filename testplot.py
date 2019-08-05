import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
def main():
    a=pd.read_csv("pss.csv")
    b=a["passed"]
    c=a["year"]
    print(b)
    plt.bar(c,b)
    plt.show()
    print(b)
if __name__=="__main__":
    main()