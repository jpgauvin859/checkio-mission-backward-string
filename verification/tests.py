"""
TESTS is a dict with all of your tests.
Keys for this will be the categories' names.
Each test is a dict with
    "input" -- input data for a user function
    "answer" -- your right answer
    "explanation" -- not necessarily a key, it's used for an additional info in animation.
"""


TESTS = {
    "Basics": [
        {
            "input": ['val'],
            "answer": 'lav',
        },
        {
            "input": [''],
            "answer": '',
        },
        {
            "input": ['ohho'],
            "answer": 'ohho',
        },
        {
            "input": ['123456789'],
            "answer": '987654321',
        },
    ],
    "Extra": [
        
        {
            "input": ['aa'],
            "answer": 'aa',
        },
        {
            "input": ['1,2,3,4'],
            "answer": '4,3,2,1',
        },
        {
            "input": ['Welcome to CheckiO'],
            "answer": 'OikcehC ot emocleW',
        },
    ]
}
