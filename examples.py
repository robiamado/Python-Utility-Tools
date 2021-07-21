##############
# EXAMPLES
##############

# CLOCKS

# 30fps clock 10Hz flip flop
from plc_main import * # download python logical components here: https://github.com/robiamado/Logical-Components
ff = JKNANDff()
c1 = clock(30)
def check_update_flip_flop():
    ff(False,False,lambda: time.sleep(0.1))
    print(ff.j,ff.k,ff.q)
#c1(check_update_flip_flop)

# DISCRETE RANGES & RUN

# 30fps sin wave without run
def sin_wave(fps):
    for x in discrete_range(0, 2*math.pi, 100):
        print(math.sin(x))
        time.sleep(1/fps)
#sin_wave(30)

# 30fps sin wave with run
#run(30, lambda x: print(math.sin(x)), discrete_range(0, 2*math.pi, 100))

# run a multiple variables function on discretized ranges
interval_1 = discrete_range(0, 1, 10)
interval_2 = discrete_range(0, 10, 10)
#run(5, lambda x,y: print(x+y), interval_1, interval_2)
