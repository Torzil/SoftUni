pool_volume = int(input())
pipe_1_flow_rate = int(input())
pipe_2_flow_rate = int(input())
worker_absent_time = float(input())

pipe_1_filled_amount = pipe_1_flow_rate * worker_absent_time
pipe_2_filled_amount = pipe_2_flow_rate * worker_absent_time

pool_filled_amount = pipe_1_filled_amount + pipe_2_filled_amount
pool_filled_percentage = pool_filled_amount / pool_volume * 100

pipe_1_filled_portion = (pipe_1_filled_amount / pool_filled_amount) * 100
pipe_2_filled_portion = (pipe_2_filled_amount / pool_filled_amount) * 100

overflow = pool_filled_amount - pool_volume

if pool_volume >= pool_filled_amount:
    print(f"The pool is {pool_filled_percentage:.2f}% full.\
 Pipe 1: {pipe_1_filled_portion:.2f}%. Pipe 2: {pipe_2_filled_portion:.2f}%.")
elif pool_volume < pool_filled_amount:
    print(f"For {worker_absent_time:.2f}\
 hours the pool overflows with {overflow:.2f} liters.")
