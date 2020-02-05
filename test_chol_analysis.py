
import pytest

def test_HDLanalysis():
# naming convention test_ and name of function being tested
	from chol_analysis import HDLanalysis
	answer = HDLanalysis(80)
	expected = "Normal"
	assert answer == expected

def test_HDLanalysis_bl():
# naming convention test_ and name of function being tested
	from chol_analysis import HDLanalysis
	answer = HDLanalysis(40)
	expected = "Borderline Low"
	assert answer == expected


def test_LDLanalysis():
	from chol_analysis import LDLanalysis
	answer = LDLanalysis(165)
	expected = "High"
	assert answer == expected