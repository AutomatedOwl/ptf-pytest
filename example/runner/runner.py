import sys
sys.path.append('./example/example-tests')
from ptf_example_tests import PtfExampleTests

# Unittest Test Runner Class
class UnittestTestRunner(PtfExampleTests):

    def setUp(self):
      print('Setting-Up PTF Example Test Method')

    def runTest(self):
      # Unittest test runner method
      pass
