
import pytest



@pytest.mark.parametrize("input, output, expected", [
    (10, 'Normal', True), 
    (40, 'Borderline', True),
    (165, 'High', True),
    (100, 'Low', False),
])


def test_HDLanalysis(input, output, expected):
# naming convention test_ and name of function being tested
	from chol_analysis.py import HDLanalysis
	answer = HDLanalysis(input)
	expected = "Normal"
	assert answer == expected

def test_HDLanalysis_bl(input, output, expected):
# naming convention test_ and name of function being tested
	from chol_analysis.py import HDLanalysis
	answer = HDLanalysis(input)
	expected = "Borderline Low"
	assert answer == expected


def test_LDLanalysis(input, output, expected):
	from chol_analysis.py import LDLanalysis
	answer = LDLanalysis(input)
	expected = "High"
	assert answer == expected