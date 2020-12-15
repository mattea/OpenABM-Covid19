# Lint as: python3
import itertools
import pandas as pd

def enumerate_sims():
  """Generats all simulations with standard iteration parameters."""
  default_adoption_rates = [0, 0.15, 0.3, 0.45, 0.6, 0.75]

  adoption_sweep = [(f"en_{rate:0.2f}", {
      "app_turned_on": 1,
      "app_population_fraction": rate,
  }) for rate in default_adoption_rates]

  trace_frac = [(f"en_{rate:0.2f}_trace_frac_{en_tf}", {
      "app_turned_on": 1,
      "app_population_fraction": rate,
      "traceable_interaction_fraction": en_tf,
  }) for rate, en_tf in itertools.product([0.15, 0.3, 0.45, 0.6, 0.75],
                                          [0.2, 0.4, 0.6, 0.8, 0.9, 1])]

  social_distancing = [(f"en_{rate:0.2f}_social_dist_{dist:0.1f}", {
      "app_turned_on": 1,
      "app_population_fraction": rate,
      "predicted_relative_transmission_occupation": dist,
      "predicted_relative_transmission_random": dist,
  }) for rate, dist in itertools.product(default_adoption_rates,
                                         [0.4, 0.6, 0.8, 1])]

  adherence = [(f"en_{rate:0.2f}_self_quarantine_{dist:0.1f}", {
      "app_turned_on": 1,
      "app_population_fraction": rate,
      "predicted_self_quarantine_fraction": dist,
  }) for rate, dist in itertools.product(default_adoption_rates,
                                         [0.2, 0.4, 0.6, 0.8])]

  priority_testing = [(f"en_{rate:0.2f}_prio_wait_{delay}_cnt_{dist}", {
      "app_turned_on": 1,
      "app_population_fraction": rate,
      "predicted_test_order_wait_priority": 0,
      "predicted_test_result_wait": 3,
      "predicted_test_result_wait_priority": delay,
      "priority_test_contacts_0_9": dist,
      "priority_test_contacts_10_19": dist,
      "priority_test_contacts_20_29": dist,
      "priority_test_contacts_30_39": dist,
      "priority_test_contacts_40_49": dist,
      "priority_test_contacts_50_59": dist,
      "priority_test_contacts_60_69": dist,
      "priority_test_contacts_70_79": dist,
      "priority_test_contacts_80": dist,
  }) for rate, dist, delay in itertools.product(default_adoption_rates,
                                         [0,10,20,30,40,50,1000000],
                                         [0,1])]

  test_wait = [(f"en_{rate:0.2f}_test_delay_{delay}", {
      "app_turned_on": 1,
      "app_population_fraction": rate,
      "predicted_test_result_wait": delay,
  }) for rate, delay in itertools.product(default_adoption_rates,
                                          [0, 1, 2, 4, 6, 8, 10])]

  manual_tracing_delay = [(f"en_{rate:0.2f}_man_trace_delay_{delay}", {
      "app_turned_on": 1,
      "manual_trace_on": 1,
      "app_population_fraction": rate,
      "manual_trace_delay": delay,
  }) for rate, delay in itertools.product(default_adoption_rates,
                                          [0, 1, 2, 4])]

  manual_tracing_nwork_locked = [
      (f"en_{rate:0.2f}_locked_man_trace_numwork_{nwork}", {
          "app_turned_on": 1,
          "manual_trace_on": 1,
          "app_population_fraction": rate,
          "predicted_lockdown_occupation_multiplier_working_network": 0.482698,
          "predicted_lockdown_random_network_multiplier": 0.482698,
          "manual_trace_n_workers_per_100k": nwork,
      }) for rate, nwork in itertools.product(default_adoption_rates,
                                              [0, 4.7, 15, 30])
  ]

  manual_tracing_nwork = [(f"en_{rate:0.2f}_man_trace_numwork_{nwork}", {
      "app_turned_on": 1,
      "manual_trace_on": 1,
      "app_population_fraction": rate,
      "manual_trace_n_workers_per_100k": nwork,
  }) for rate, nwork in itertools.product(default_adoption_rates,
                                          [0, 4.7, 8.3, 15, 30])]

  school_manual_tracing_nwork = [
      (f"en_{rate:0.2f}_school_man_trace_numwork_{nwork}", {
          "app_turned_on": 1,
          "manual_trace_on": 1,
          "app_population_fraction": rate,
          "predicted_lockdown_occupation_multiplier_primary_network": 0.8,
          "predicted_lockdown_occupation_multiplier_secondary_network": 0.8,
          "manual_trace_n_workers_per_100k": nwork,
      }) for rate, nwork in itertools.product([0, 0.3], [0, 4.7, 8.3, 15, 30])
  ]

  exclude_app_manual_tracing_nwork = [
      (f"en_{rate:0.2f}_exclude_app_man_trace_numwork_{nwork}", {
          "app_turned_on": 1,
          "manual_trace_on": 1,
          "app_population_fraction": rate,
          "manual_trace_exclude_app_users": 1,
          "manual_trace_n_workers_per_100k": nwork,
      })
      for rate, nwork in itertools.product([0, 0.3, 0.6], [0, 4.7, 8.3, 15, 30])
  ]

  sims = []
  for sim_name, params in itertools.chain(adoption_sweep, social_distancing,
                                          trace_frac,
                                          test_wait,
                                          manual_tracing_nwork,
                                          manual_tracing_nwork_locked,
					  priority_testing):
    for idx in range(10):
      p = params.copy()
      p["rng_seed"] = idx * 10
      p["study_name"] = f"{sim_name}_{idx}"
      p["iteration"] = idx
      sims.append(p)

  return sims

def main():
  sims = enumerate_sims()
  pd.DataFrame(sims).to_csv("../data/us-wa/simulations.csv",index=False)

if __name__ == "__main__":
  main()
