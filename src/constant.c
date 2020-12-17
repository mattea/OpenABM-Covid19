/*
 * constant.c
 *
 *  Created on: 22 Mar 2020
 *      Author: hinchr
 */

#include "constant.h"

const int AGE_OCCUPATION_MAP[N_AGE_GROUPS] = {
	PRIMARY_NETWORK,
	SECONDARY_NETWORK,
	WORKING_NETWORK,
	WORKING_NETWORK,
	WORKING_NETWORK,
	WORKING_NETWORK,
	WORKING_NETWORK,
	RETIRED_NETWORK,
	ELDERLY_NETWORK	
};

const int NETWORK_TYPE_MAP[N_DEFAULT_OCCUPATION_NETWORKS] = {
	NETWORK_TYPE_CHILD,
	NETWORK_TYPE_CHILD,
	NETWORK_TYPE_ADULT,
	NETWORK_TYPE_ELDERLY,
	NETWORK_TYPE_ELDERLY
};

const int OCCUPATION_DEFAULT_MAP[N_DEFAULT_OCCUPATION_NETWORKS] = {
	OCCUPATION_PRIMARY_NETWORK,
	OCCUPATION_SECONDARY_NETWORK,
	OCCUPATION_WORKING_NETWORK,
	OCCUPATION_RETIRED_NETWORK,
	OCCUPATION_ELDERLY_NETWORK
};

const char* DEFAULT_NETWORKS_NAMES[N_DEFAULT_NETWORKS] = {
	"Household network (default)",
	"Occupation primary school network (default)",
	"Occupation secondary school network (default)",
	"Occupation working network (default)",
	"Occupation retired network (default)",
	"Occupation elderly network (default)",
	"Random network (default)"
};

const int AGE_TYPE_MAP[N_AGE_GROUPS] = {
	AGE_TYPE_CHILD,
	AGE_TYPE_CHILD,
	AGE_TYPE_ADULT,
	AGE_TYPE_ADULT,
	AGE_TYPE_ADULT,
	AGE_TYPE_ADULT,
	AGE_TYPE_ADULT,
	AGE_TYPE_ELDERLY,
	AGE_TYPE_ELDERLY
};

const char* AGE_TEXT_MAP[N_AGE_GROUPS] = {
	"0-9 years",
	"10-19 years",
	"20-29 years",
	"30-39 years",
	"40-49 years",
	"50-59 years",
	"60-69 years",
	"70-79 years",
	"80+ years"
};

const int EVENT_TYPE_TO_WARD_MAP[N_EVENT_TYPES] = {
	NOT_IN_HOSPITAL,
	NOT_IN_HOSPITAL,
	NOT_IN_HOSPITAL,
	NOT_IN_HOSPITAL,
	NOT_IN_HOSPITAL,
	NOT_IN_HOSPITAL,
	COVID_GENERAL,
	COVID_ICU,
	COVID_GENERAL,
	NOT_IN_HOSPITAL,
	NOT_IN_HOSPITAL,
	NOT_IN_HOSPITAL,
	NOT_IN_HOSPITAL,
	NOT_IN_HOSPITAL,
	NOT_IN_HOSPITAL,
	NOT_IN_HOSPITAL,
	NOT_IN_HOSPITAL,
	NOT_IN_HOSPITAL,
	NOT_IN_HOSPITAL,
	COVID_GENERAL,
	COVID_ICU,
	NOT_IN_HOSPITAL,
	NOT_IN_HOSPITAL,
};

const int NEWLY_INFECTED_STATES[N_NEWLY_INFECTED_STATES] = {
	PRESYMPTOMATIC,
	PRESYMPTOMATIC_MILD,
	ASYMPTOMATIC,
};

// Infectiousness buckets from greatest to least severity.
const int INFECTIOUSNESS_BUCKETS[N_INFECTIOUSNESS_BUCKETS] = {
	SYMPTOMATIC,
	SYMPTOMATIC_MILD,
	ASYMPTOMATIC,
};

gsl_rng * rng;
