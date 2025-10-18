import unittest
import pandas
from src.core.implementations.sample_run import SampleDF

class TestSampleDF_scenario_working(unittest.TestCase):
    def setUp(self):
        dic = {
            'a': [1,2,3,5],
            'b': [1,2,3,5],
            'c': [1,2,3,5]
        }
        self.data = pandas.DataFrame(dic)
    
    def tearDown(self):
        pass
    
    @unittest.skip('work in progress')
    def test_sample(self):
        sample = SampleDF(df=self.data, pct=0.99, only_sample=True)
        df = sample.sample_dtype()
        