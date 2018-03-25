import os, sys
parentddir = os.path.abspath(os.path.join(os.path.dirname(__file__), os.path.pardir))
sys.path.append(parentddir)

from unittest import TestLoader, TestSuite, TextTestRunner
from Tests.Test_ResetPassword import ResetPassword
from Tests.Test_AddNewUser import AddNewUser
import testtools as testtools


#this is good if you have multiple test cases.You write them below and everything works
if __name__ == "__main__":

    loader = TestLoader()
    suite = TestSuite((
        loader.loadTestsFromTestCase(ResetPassword),
        loader.loadTestsFromTestCase(AddNewUser)
        ))


#run test sequentially using simple TextTestRunner
    runner = TextTestRunner(verbosity=1)
    runner.run(suite)


# #run test parallel using concurrent_suite
    concurrent_suite = testtools.ConcurrentStreamTestSuite(lambda: ((case, None) for case in suite))
    concurrent_suite.run(testtools.StreamResult())