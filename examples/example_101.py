"""
Example 101
Get the baseline parameters, model, run for a few time steps and print the output

Created: 17 April 2020
Author: roberthinch
"""

import example_utils as utils
import pandas as pd

# gets the baseline parameters
params = utils.get_baseline_parameters()

# change to run on a small population (much quicker)
params.set_param( "n_total", 10000 )
params.set_param("n_seed_infection", 100)
params.set_param("lateral_flow_test_on_traced", 1)
params.set_param("lateral_flow_test_on_symptoms", 1)
params.set_param("lateral_flow_test_sensitivity", 0.95)
params.set_param("lateral_flow_test_specificity", 0.99)
params.set_param("lateral_flow_test_repeat_count", 7)
params.set_param("lateral_flow_test_order_wait", 1)
params.set_param("test_on_traced", 0)
params.set_param("test_on_symptoms", 0)
params.set_param("quarantine_on_traced", 1)
params.set_param("app_turn_on_time", 0)
params.set_param("app_turned_on", 1)

# get the simulation object
sim = utils.get_simulation( params )

# run the simulation for 10 days
sim.steps( 30 )

# print the basic output
timeseries = pd.DataFrame( sim.results )
print( timeseries )


