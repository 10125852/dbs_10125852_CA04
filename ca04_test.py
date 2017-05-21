# -*- coding: utf-8 -*-
"""
CA04 - Test 
author: 10125852 InSun Ahn

"""

import unittest 

from ca04_process_changes import get_commits, read_file

class TestCommits(unittest.TestCase):
    ''' class for unittest of get_commits ''' 

    def setUp(self):
        self.data = read_file('changes_python.log')
    
    # Test to see if the total 5255 lines exist in data
    def test_number_of_lines(self):
        self.assertEqual(5255, len(self.data))
    
    # Test to see if the total 422 commit objects exist in commits list.       
    def test_number_of_commit_objects(self):
        commits = get_commits(self.data)
        self.assertEqual(422, len(commits))
    
    
    #Test to see if the details of first commit object are correct.
    '''
    Values should equal to the below:
    {'date': '2015-11-27 16:57:44 +0000 (Fri, 27 Nov 2015)', 
    'comment': 'Renamed folder to the correct name', 
    'author': 'Thomas', 'number_of__comment_lines': '1', 
    'revision': '1551925'}    
    '''
    def test_first_commit(self):
        commits = get_commits(self.data)
        self.assertEqual("Thomas", commits[0]["author"])
        self.assertEqual('2015-11-27 16:57:44 +0000 (Fri, 27 Nov 2015)', commits[0]["date"])
        self.assertEqual('1551925', commits[0]["revision"])
        self.assertEqual('1', commits[0]["number_of__comment_lines"])
        self.assertEqual('Renamed folder to the correct name', commits[0]["comment"])
       

if __name__ == '__main__':
    unittest.main()
    
        