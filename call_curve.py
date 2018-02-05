from scipy.stats import norm
from math import *
import matplotlib.animation as animation
import matplotlib.pyplot as plt
import numpy as np

"""
# The Black Scholes Formula
# Call_or_Put - This is set to 'call' for call option, anything else for put
# S - Stock price
# K - Strike price
# T - Time to maturity
# r - Riskfree interest rate
# d - Dividend yield
# v - Volatility
"""

def BlackScholes(Call_or_Put,S,K,T,r,d,v):
    d1 = (log(float(S)/K)+((r-d)+v*v/2.)*T)/(v*sqrt(T))
    d2 = d1-v*sqrt(T)
    if Call_or_Put=='call':
        return S*exp(-d*T)*norm.cdf(d1)-K*exp(-r*T)*norm.cdf(d2)
    else:
        return K*exp(-r*T)*norm.cdf(-d2)-S*exp(-d*T)*norm.cdf(-d1)


maturity = 0
S = np.linspace(80,120,200)
p1 = []
p2 = []
p3 = []
for i in S:
    p1.append(BlackScholes('call', i, 100, 0.005, 0.06, 0, 0.4))
for i in S:
    p2.append(BlackScholes('call', i, 100, 0.105, 0.06, 0, 0.4))
for i in S:
    p3.append(BlackScholes('call', i, 100, 0.055, 0.06, 0, 0.4))

p1=plt.plot( S , p1 ,color='blue')
p2=plt.plot( S , p2 ,color='yellow')
p2=plt.plot( S , p3 ,color='green')
plt.xlabel("underlying")
plt.ylabel("payoffs")
plt.title("Call")
plt.legend(["strike price (K)=0,005", "K=0.105", "K=0.055"])
plt.show()

