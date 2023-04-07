import pandas as pd
import numpy as np
import math

chat_id = 975846018 # Ваш chat ID, не меняйте название переменной

def solution(x_success: int, 
             x_cnt: int, 
             y_success: int, 
             y_cnt: int) -> bool:
  
    p1 = x_success / x_cnt
    p2 = y_success / y_cnt
    
    S = math.sqrt((p1 * (1 - p1)) / x_cnt + (p2 * (1 - p2)) / y_cnt)
    
    z = (p2 - p1) / S
    
    alpha = 0.06
    z_crit = 1.88
    
    return abs(z) > z_crit
