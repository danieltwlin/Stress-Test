
import os

# Test CPU
os.system('sysbench --test=cpu --cpu-max-prime=2000 run')

# Test IO
os.system('sysbench --test=fileio --num-threads=20 --file-total-size=1G --file-test-mode=rndrw prepare')
os.system('sysbench --test=fileio --num-threads=20 --file-total-size=1G --file-test-mode=rndrw run')
os.system('sysbench --test=fileio --num-threads=20 --file-total-size=1G --file-test-mode=rndrw cleanup')

# Test Memory
os.system('sysbench --test=memory --memory-block-size=8K --memory-total-size=1G --memory-oper=read run')
os.system('sysbench --test=memory --memory-block-size=8K --memory-total-size=1G run ')
