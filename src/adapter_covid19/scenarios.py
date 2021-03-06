from adapter_covid19.enums import Region, BackToWork

from adapter_covid19.data_structures import Scenario, ModelParams

__all__ = (
    "BASIC_MODEL_PARAMS",
    "BASIC_SCENARIO",
    "BASIC_NO_FURLOUGH_SCENARIO",
    "BASIC_NO_CORP_SUPPORT_SCENARIO",
    "BASIC_NO_FURLOUGH_NO_CORP_SUPPORT_SCENARIO",
    "BASIC_NO_LOCKDOWN_SCENARIO",
    "BASIC_SLOW_UNLOCK_SCENARIO",
    "BASIC_SLOW_UNLOCK_GREEDY_SCENARIO",
    "BASIC_SLOW_UNLOCK_CONSTRAINED_SCENARIO",
    "TEST_SCENARIO",
    "SCENARIOS",
)

"""
========
Timeline
========

The lockdown in the UK started on 23 March 2020. The strict lockdown ended on 10 May 2020 (inclusive). 
Convention for all scenarios below is that the start time (time 0) is 10 days prior to the start of the
lockdown, i.e., 13 March 2020. (When this convention is changed it should be changed for all scenarios 
consistently.)

Key events on the timeline are

* 13 March - Time 00 - Start of Simulation
* 23 March - Time 10 
    - Start of Lockdown (inclusive)
    - Start of `CCFF <https://www.bankofengland.co.uk/news/2020/march/the-covid-corporate-financing-facility>`_. 
* 31 March - Time 18 - Last day of Q1
* 1 April - Time 19 - First day of Q2
* 11 May - Time 59 - End of Lockdown (exclusive)
* 30 June - Time 109 - Last day of Q2
* 1 July - Time 110 - First day of Q3
* 30 September - Time 201 - Last day of Q3


=========
Scenarios
=========

* basic - Lockdown with a hard stop at 11 May, furloughing from the beginning of lockdown until the end of the 
  simulation, interventions to support corporates (CCFF, loan guarantees, new govt spending)
* slow_unlock - As basic, but with gradual easing of lockdown (sending back 10% of remaining workforce 
  every 10 days)
* slow_unlock_greedy - As slow_unlock, but send back workers in order of productivity.
* slow_unlock_constrained - As slow_unlock, but prioritizing to send back workers in sectors which are 
  supply-constrained first
* no_furlough - As basic, but without furloughing
* no_corp_support - As basic, but without corporate support
* no_furlough_no_corp_support - As basic, but without either furloughing or corporate support
* no_lockdown - No lockdown and no other interventions
* test - Testing scenario running for just 5 days.


=======================
Institutional Forecasts
=======================

Collecting some key figures from third party publications for reference.

BoE Monetary Policy Report May 2020
-----------------------------------

https://www.bankofengland.co.uk/-/media/boe/files/monetary-policy-report/2020/may/monetary-policy-report-may-2020
 
Key figures in "illustrative scenario": 

* GDP
    * Annual 2020: -14%
    * Q1: -3%
    * Q2: -25%
* Consumption 
    * Household consumption (in March-April): -30%
    * Sales (Q2): -40% to -45%
    * Business Investment (Q2): -40% to -50%

"""


SPREAD_MODEL_PARAMS = {
    "quarantine_household_on_positive": 1,
    "quarantine_household_on_symptoms": 1,
    "self_quarantine_fraction": 0.8,
}


BASIC_MODEL_PARAMS = ModelParams(
    economics_params={},
    gdp_params={},
    personal_params={
        "default_th": 300,
        "max_earning_furloughed": 30_000,
        "alpha": 5,
        "beta": 20,
    },
    corporate_params={"beta": 1.4, "large_cap_cash_surplus_months": 18,},
)

# Basic Scenario
# - Lockdown with a hard stop at 11 May
# - furloughing from the beginning of lockdown until the end of the simulation
# - interventions to support corporates (CCFF, loan guarantees, new govt spending)

BASIC_SCENARIO = Scenario(
    lockdown_start_time=10,
    lockdown_end_time=59,
    furlough_start_time=10,
    furlough_end_time=202,
    simulation_end_time=202,
    new_spending_day=10,
    ccff_day=10,
    loan_guarantee_day=10,
    model_params=BASIC_MODEL_PARAMS,
    spread_model_time_factor=1.0,
    fear_factor_coef_lockdown=0.3,
    fear_factor_coef_ill=4.0,
    fear_factor_coef_dead=1000.0,
    spread_model_params=SPREAD_MODEL_PARAMS,
)

# Basic No Furlough Scenario
# - Lockdown
# - No Furlough
# - Corporate Support

BASIC_NO_FURLOUGH_SCENARIO = Scenario(
    lockdown_start_time=10,
    lockdown_end_time=59,
    furlough_start_time=10000,
    furlough_end_time=10000,
    simulation_end_time=202,
    new_spending_day=10,
    ccff_day=10,
    loan_guarantee_day=10,
    model_params=BASIC_MODEL_PARAMS,
    spread_model_time_factor=1.0,
    fear_factor_coef_lockdown=0.3,
    fear_factor_coef_ill=4.0,
    fear_factor_coef_dead=1000.0,
    spread_model_params=SPREAD_MODEL_PARAMS,
)

# Basic No Corp Support Scenario
# - Lockdown
# - Furlough
# - No Corporate Support

BASIC_NO_CORP_SUPPORT_SCENARIO = Scenario(
    lockdown_start_time=10,
    lockdown_end_time=59,
    furlough_start_time=10,
    furlough_end_time=202,
    simulation_end_time=202,
    new_spending_day=10000,
    ccff_day=10000,
    loan_guarantee_day=10000,
    model_params=BASIC_MODEL_PARAMS,
    spread_model_time_factor=1.0,
    fear_factor_coef_lockdown=0.3,
    fear_factor_coef_ill=4.0,
    fear_factor_coef_dead=1000.0,
    spread_model_params=SPREAD_MODEL_PARAMS,
)

# Basic No Furlough No Corp Support Scenario
# - Lockdown
# - No Furlough
# - No Corporate Support

BASIC_NO_FURLOUGH_NO_CORP_SUPPORT_SCENARIO = Scenario(
    lockdown_start_time=10,
    lockdown_end_time=59,
    furlough_start_time=10000,
    furlough_end_time=10000,
    simulation_end_time=202,
    new_spending_day=10000,
    ccff_day=10000,
    loan_guarantee_day=10000,
    model_params=BASIC_MODEL_PARAMS,
    spread_model_time_factor=1.0,
    fear_factor_coef_lockdown=0.3,
    fear_factor_coef_ill=4.0,
    fear_factor_coef_dead=1000.0,
    spread_model_params=SPREAD_MODEL_PARAMS,
)

# Basic No Lockdown Scenario
# - No lockdown
# - No other interventions

BASIC_NO_LOCKDOWN_SCENARIO = Scenario(
    lockdown_start_time=10000,
    lockdown_end_time=10000,
    furlough_start_time=10000,
    furlough_end_time=10000,
    simulation_end_time=202,
    new_spending_day=10000,
    ccff_day=10000,
    loan_guarantee_day=10000,
    model_params=BASIC_MODEL_PARAMS,
    spread_model_time_factor=1.0,
    fear_factor_coef_lockdown=0.3,
    fear_factor_coef_ill=4.0,
    fear_factor_coef_dead=1000.0,
    spread_model_params=SPREAD_MODEL_PARAMS,
)

# Basic Scenario (aligned with actual interventions)
# * Lockdown
# * Furlough
# * Corporate Support
# * Slow release of lockdown
# * Naively send people back to work (sending back 10% of remaining workforce every 10 days)

BASIC_SLOW_UNLOCK_SCENARIO = Scenario(
    lockdown_start_time=10,
    lockdown_end_time=59,
    slow_unlock=True,
    back_to_work_strategy=BackToWork.naive,
    furlough_start_time=10,
    furlough_end_time=202,
    simulation_end_time=202,
    new_spending_day=10,
    ccff_day=10,
    loan_guarantee_day=10,
    model_params=BASIC_MODEL_PARAMS,
    spread_model_time_factor=1.0,
    fear_factor_coef_lockdown=0.3,
    fear_factor_coef_ill=4.0,
    fear_factor_coef_dead=1000.0,
    spread_model_params=SPREAD_MODEL_PARAMS,
)


# Basic Scenario (aligned with actual interventions)
# * Lockdown
# * Furlough
# * Corporate Support
# * Slow release of lockdown
# * Send people back to work in order of productivity

BASIC_SLOW_UNLOCK_GREEDY_SCENARIO = Scenario(
    lockdown_start_time=10,
    lockdown_end_time=59,
    slow_unlock=True,
    back_to_work_strategy=BackToWork.greedy,
    furlough_start_time=10,
    furlough_end_time=202,
    simulation_end_time=202,
    new_spending_day=10,
    ccff_day=10,
    loan_guarantee_day=10,
    model_params=BASIC_MODEL_PARAMS,
    spread_model_time_factor=1.0,
    fear_factor_coef_lockdown=0.3,
    fear_factor_coef_ill=4.0,
    fear_factor_coef_dead=1000.0,
    spread_model_params=SPREAD_MODEL_PARAMS,
)


# Basic Scenario (aligned with actual interventions)
# * Lockdown
# * Furlough
# * Corporate Support
# * Slow release of lockdown
# * Send people back to work taking into account supply/demand

BASIC_SLOW_UNLOCK_CONSTRAINED_SCENARIO = Scenario(
    lockdown_start_time=10,
    lockdown_end_time=59,
    slow_unlock=True,
    back_to_work_strategy=BackToWork.constrained,
    furlough_start_time=10,
    furlough_end_time=202,
    simulation_end_time=202,
    new_spending_day=10,
    ccff_day=10,
    loan_guarantee_day=10,
    model_params=BASIC_MODEL_PARAMS,
    spread_model_time_factor=1.0,
    fear_factor_coef_lockdown=0.3,
    fear_factor_coef_ill=4.0,
    fear_factor_coef_dead=1000.0,
    spread_model_params=SPREAD_MODEL_PARAMS,
)

TEST_SCENARIO = Scenario(
    lockdown_start_time=2,
    lockdown_end_time=5,
    furlough_start_time=2,
    furlough_end_time=5,
    simulation_end_time=20,
    slow_unlock=True,
    back_to_work_strategy=BackToWork.constrained,
    new_spending_day=2,
    ccff_day=2,
    loan_guarantee_day=2,
    model_params=BASIC_MODEL_PARAMS,
    spread_model_time_factor=1.0,
    fear_factor_coef_lockdown=0.3,
    fear_factor_coef_ill=4.0,
    fear_factor_coef_dead=1000.0,
    epidemic_active=False,
    ill_ratio={t: {r: 0 for r in Region} for t in range(203)},
    dead_ratio={t: {r: 0 for r in Region} for t in range(203)},
    quarantine_ratio={t: {r: 0 for r in Region} for t in range(203)},
    spread_model_params=SPREAD_MODEL_PARAMS,
)

SCENARIOS = {
    "basic": BASIC_SCENARIO,
    "slow_unlock": BASIC_SLOW_UNLOCK_SCENARIO,
    "slow_unlock_greedy": BASIC_SLOW_UNLOCK_GREEDY_SCENARIO,
    "slow_unlock_constrained": BASIC_SLOW_UNLOCK_CONSTRAINED_SCENARIO,
    "no_furlough": BASIC_NO_FURLOUGH_SCENARIO,
    "no_corp_support": BASIC_NO_CORP_SUPPORT_SCENARIO,
    "no_furlough_no_corp_support": BASIC_NO_FURLOUGH_NO_CORP_SUPPORT_SCENARIO,
    "no_lockdown": BASIC_NO_LOCKDOWN_SCENARIO,
    "test": TEST_SCENARIO,
}
