# Lint as: python3
"""Write county-specific parameters to county param file.
"""

import argparse
import itertools
import os

import numpy as np
import pandas as pd

def relative_path(filename: str) -> str:
    return os.path.join(os.path.dirname(__file__), filename)

parser = argparse.ArgumentParser(description="Generate county-specific parameters.")
parser.add_argument("--households_file", type=str, default=relative_path("../data/us-wa/wa_county_household_demographics_unscaled.csv"))
parser.add_argument("--output_params", type=str, default=relative_path("../data/us-wa/wa_county_parameters.csv"))
parser.add_argument("--output_households", type=str, default=relative_path("../data/us-wa/wa_county_household_demographics.csv"))

mobility_glm = [
    0.75361365, 0.6374258 , 0.6428742 , 0.64921296, 0.60837924, 0.59091055,
    0.6060355 , 0.67852694, 0.6129618 , 0.59461975, 0.60351306, 0.5986241 ,
    0.55482554, 0.48379263, 0.52284586, 0.5322181 , 0.4024645 , 0.381558  ,
    0.35036892, 0.34796682, 0.33947754, 0.3039799 , 0.29132232, 0.2507367 ,
    0.23450202, 0.20214951, 0.19372977, 0.19963208, 0.20852974, 0.20649046,
    0.2116164 , 0.2338841 , 0.21048251, 0.21023414, 0.21970361, 0.22019151,
    0.23410365, 0.22833323, 0.24152744, 0.23744714, 0.22881821, 0.24924383,
    0.20666292, 0.23937468, 0.24112837, 0.27063692, 0.26280558, 0.24523005,
    0.2555329 , 0.28259674, 0.27242604, 0.24968484, 0.24156943, 0.24783975,
    0.24462762, 0.2677685 , 0.29527706, 0.2754246 , 0.283517  , 0.28918535,
    0.28506503, 0.30099154, 0.2898438 , 0.33117008, 0.31593233, 0.34081346,
    0.30844223, 0.3297223 , 0.34095806, 0.44255745, 0.48620218, 0.31680763,
    0.30441892, 0.32293928, 0.31023166, 0.32210174, 0.333077  , 0.3767953 ,
    0.3338426 , 0.32884768, 0.32880855, 0.33669367, 0.35611898, 0.42755556,
    0.45756695, 0.24450314, 0.3671865 , 0.38228118, 0.38106483, 0.37331998,
    0.36172482, 0.44219512, 0.4206638 , 0.37929162, 0.41454402, 0.40553275,
    0.39841703, 0.4735672 , 0.49633804, 0.4081716 , 0.3711566 , 0.41258532,
    0.4129976 , 0.40091518, 0.4718228 , 0.54787153, 0.40769994, 0.41683897,
    0.4442321 , 0.46114036, 0.46782702, 0.5382079 , 0.61714375, 0.4668944 ,
    0.44194606, 0.4513628 , 0.47649282, 0.44980568, 0.51716125, 0.59390694,
    0.4631154 , 0.45829624, 0.50276434, 0.55138934, 0.4743529 , 0.43839782,
    0.60986537, 0.47248834, 0.43795305, 0.45862004, 0.44935322, 0.4606248 ]

changepoint_rate = [
    1.        , 1.        , 1.        , 1.        , 1.        ,
    1.        , 1.        , 1.        , 1.        , 1.        ,
    1.        , 1.        , 1.        , 1.        , 1.        ,
    1.        , 1.        , 1.        , 1.        , 1.        ,
    1.        , 1.        , 1.        , 1.        , 1.        ,
    1.        , 1.        , 1.        , 1.        , 1.        ,
    1.        , 1.        , 1.        , 1.        , 1.        ,
    1.        , 1.        , 1.        , 1.        , 0.99999994,
    0.99999976, 0.9999981 , 0.99998915, 0.99989426, 0.9993038 ,
    0.9968595 , 0.9869055 , 0.9583875 , 0.92156726, 0.8832767 ,
    0.8543031 , 0.8308939 , 0.81462353, 0.7999654 , 0.7872288 ,
    0.7766864 , 0.76803565, 0.76088834, 0.75616527, 0.75068736,
    0.74641025, 0.74349767, 0.740088  , 0.7383175 , 0.7367529 ,
    0.7356839 , 0.7350616 , 0.73431563, 0.7335588 , 0.73329717,
    0.7330837 , 0.7330729 , 0.7328347 , 0.73260194, 0.732494  ,
    0.7324209 , 0.7323586 , 0.73230326, 0.73216546, 0.73211575,
    0.7319937 , 0.7319734 , 0.73181605, 0.7317901 , 0.7317885 ,
    0.7317885 , 0.7317885 , 0.7317885 , 0.7317885 , 0.7317885 ,
    0.7317885 , 0.7317885 , 0.7317885 , 0.7317885 , 0.7317885 ,
    0.7317054 , 0.7317054 , 0.7317054 , 0.7317054 , 0.7316194 ,
    0.7316194 , 0.7316036 , 0.731565  , 0.73153794, 0.73153794,
    0.73153794, 0.73153794, 0.73153794, 0.73153794, 0.73153794,
    0.73153794, 0.73153794, 0.7315259 , 0.7313702 , 0.7313702 ,
    0.73118675, 0.73109984, 0.73109984, 0.73109984, 0.7310293 ,
    0.73098   , 0.7308445 , 0.7306876 , 0.73050874, 0.7304316 ,
    0.7303984 , 0.7302203 , 0.73017645, 0.73017645, 0.7301605 ,
    0.7300091 , 0.7300091 ]

all_params_sq8 = [{
    "county_fips": 53033, # King
    "n_total": 2252782,
    "n_seed_infection": 30,
    "infectious_rate": 5.02,
    "seeding_date_delta": 25,
    "lockdown_scalars": mobility_glm,
    "changepoint_scalars": changepoint_rate,
},{
    "county_fips": 53061, # Snohomish
    "n_total": 822083,
    "n_seed_infection": 30,
    "infectious_rate": 5.18,
    "seeding_date_delta": 18,
    "lockdown_scalars": mobility_glm,
    "changepoint_scalars": changepoint_rate,
},{
    "county_fips": 53053, # Pierce
    "n_total": 904980,
    "n_seed_infection": 30,
    "infectious_rate": 5.22,
    "seeding_date_delta": 14,
    "lockdown_scalars": mobility_glm,
    "changepoint_scalars": changepoint_rate,
},
]

all_params_sq2 = [{
    "county_fips": 53033, # King
    "n_total": 2252782,
    "n_seed_infection": 30,
    "infectious_rate": 4.00,
    "seeding_date_delta": 27,
    "lockdown_scalars": mobility_glm,
    "changepoint_scalars": changepoint_rate,
},{
    "county_fips": 53061, # Snohomish
    "n_total": 822083,
    "n_seed_infection": 30,
    "infectious_rate": 4.12,
    "seeding_date_delta": 20,
    "lockdown_scalars": mobility_glm,
    "changepoint_scalars": changepoint_rate,
},{
    "county_fips": 53053, # Pierce
    "n_total": 904980,
    "n_seed_infection": 30,
    "infectious_rate": 4.12,
    "seeding_date_delta": 14,
    "lockdown_scalars": mobility_glm,
    "changepoint_scalars": changepoint_rate,
},
]

all_params = all_params_sq8

HOUSEHOLD_SIZES=[f"household_size_{i}" for i in  range(1,7)]
AGE_BUCKETS=[f"{l}_{h}" for l, h in zip(range(0, 80, 10), range(9, 80, 10))] + ["80"]

def stringify(l):
  return ",".join((f"{x}" for x in l))

def process_scalars(scalars):
  l_rescaled = [s / scalars[0] for s in scalars]
  #l_rescaled.append(pd.Series(scalars).rolling(7,1).mean().to_list()[-1])
  return stringify(l_rescaled)

def household_sizes(households):
  pops = households.groupby("county_fips").sum()
  pops = pops.rename(columns=lambda l: l.replace("a_","population_"))
  pops["n_total"] = pops.sum(axis=1)

  house_sizes = households.set_index("county_fips").sum(axis=1).apply(lambda x: x if x <= 6 else 6)
  houses_df = pd.DataFrame(house_sizes, columns=["sizes"])
  houses_df["ones"] = 1
  house_counts = houses_df.pivot_table(index=houses_df.index,columns="sizes",aggfunc='count')['ones'].rename(columns=lambda l:f"household_size_{l}")
  house_counts.columns.name = None
  if 'household_size_0' in house_counts.columns:
    house_counts.drop('household_size_0', axis=1, inplace=True)
  return pops.join(house_counts)

def ssd(a, b):
  return sum((a-b)**2)
def hpdx(sample):
  return np.histogram(sample.sum(axis=1), bins=[1,2,3,4,5,6,1000])[0] / len(sample)
def apdx(sample):
  return sample.sum(axis=0)  / sample.sum()
def calc_err(hh, house_dist, age_dist):
  pop_pref = 2
  age_p = apdx(hh)
  house_p = hpdx(hh)
  return  ssd(house_p, house_dist) + ssd(age_p, age_dist) * pop_pref

def rejection_sample(panel, tot, house_dist=None, age_dist=None, batch_size=4, rs = np.random.RandomState(42)): 
  initial_acceptance_factor = 1e-5
  rejection_mult = 1.0001
  acceptable_mult = 0.99
  max_allowable_error = 1e-5

  if house_dist is None:
    house_dist = hpdx(panel)
  if age_dist is None:
    age_dist = apdx(panel)

  sample = panel[rs.choice(panel.shape[0], size=batch_size),:]
  #hh = np.concatenate((panel, sample), axis=0)
  hh = sample
  last_error = calc_err(hh, house_dist, age_dist)
  error = last_error
  acceptance = last_error * initial_acceptance_factor
  while hh.sum() < tot:
    sample = panel[rs.choice(panel.shape[0], size=batch_size),:]
    nhh = np.concatenate((hh, sample), axis=0)
    error = calc_err(nhh, house_dist, age_dist)
    if (error < last_error + acceptance):
      hh = nhh
      acceptance *= acceptable_mult
      last_error = min(error, last_error)
    else:
      acceptance *= rejection_mult
  if error > max_allowable_error:
    raise RuntimeError("Rejection sampling failed to converge.")
  return hh, last_error, error

def upsample(panel, tot, rs = np.random.RandomState(42)): 
  rem = tot - panel.sum()
  samples = [panel]
  for idx in rs.permutation(panel.shape[0]):
    if rem <= 0:
      break
    sample = panel[idx:idx+1,:]
    rem -= sample.sum()
    samples.append(sample)
  return np.concatenate(samples)

def hh_resample(households_file, all_params):
  households = pd.read_csv(households_file, skipinitialspace=True, comment="#")
  age_columns=[f"a_{a}" for a in AGE_BUCKETS]
  new_households = []
  for p in all_params:
    #nhh = rejection_sample(households[households.county_fips == p["county_fips"]][age_columns].values, p["n_total"])
    nhh = upsample(households[households.county_fips == p["county_fips"]][age_columns].values, p["n_total"])
    nhh = pd.DataFrame(nhh, columns=age_columns)
    nhh["county_fips"] = p["county_fips"]
    new_households.append(nhh)
  return pd.concat(new_households)

def main(args):
  for p in all_params:
    p["lockdown_scalars"] = process_scalars(p["lockdown_scalars"])
    p["changepoint_scalars"] = process_scalars(p["changepoint_scalars"])
  hhdf = hh_resample(args.households_file, all_params)
  hhdf.to_csv(args.output_households)
  pd.DataFrame(all_params).drop(columns="n_total").set_index("county_fips").join(household_sizes(hhdf), how="right").to_csv(args.output_params)

if __name__ == '__main__':
  main(parser.parse_args())
