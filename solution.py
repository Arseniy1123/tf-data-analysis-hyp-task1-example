import pandas as pd
import numpy as np
import math
from scipy.stats import norm

chat_id = 975846018 # Ваш chat ID, не меняйте название переменной

def solution(x_success: int, 
             x_cnt: int, 
             y_success: int, 
             y_cnt: int) -> bool:
  
    p1 = x_success / x_cnt
    p2 = y_success / y_cnt
    
    p_pool = (x_success + y_success) / (x_cnt + y_cnt)
    se = math.sqrt(p_pool * (1 - p_pool) * (1 / x_cnt + 1 / y_cnt))
    
    z_score = (p2 - p1) / se
    p_value = 2 * (1 - norm.cdf(abs(z_score)))
    
    alpha = 0.06
    reject_null = p_value < alpha
    
    return reject_null
