import os
import sys

toe_file = 'test.toe'
toe_env_var1 = 'VAR1'
toe_env_val1 = sys.argv[1]
toe_env_var2 = 'VAR2'
toe_env_val2 = sys.argv[2]

os.environ[toe_env_var1] = toe_env_val1
os.environ[toe_env_var2] = toe_env_val2

os.startfile(toe_file)

print("starting file {} with env val {} and {}".format(toe_file, toe_env_val1, toe_env_val2))