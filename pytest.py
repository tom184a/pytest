#!/usr/bin/env python

class AssertionResult:
    def __init__(self, result, info):
        self.result = result
        self.info = info

    def getResult(self):
        return self.result

    def getInfo(self):
        return self.info

class TestResult:
    def __init__(self):
        self.assertion_results = []
        self.passed = True

    def add(self, assertionResult):
        if assertionResult.getResult() == False:
            self.passed = False
        self.assertion_results.append(assertionResult)

    def getResult(self):
        return self.passed

    def getAsserts(self):
        return self.assertion_results

    def getFailedAsserts(self):
        return [x for x in self.assertion_results if x.getResult() == False]

################################## ASSERT MACROS ##############################

class ASSERT_TRUE:
    def __init__(self, condition, info):
        if condition == True:
            ASSERT_TRUE.test_hook.add(AssertionResult(True, ''))
        else:
            ASSERT_TRUE.test_hook.add(AssertionResult(False, info))

class ASSERT_FALSE:
    def __init__(self, condition, info):
        if condition == False:
            ASSERT_FALSE.test_hook.add(AssertionResult(True, ''))
        else:
            ASSERT_FALSE.test_hook.add(AssertionResult(False, info))



class ASSERT_EQ:
    def __init__(self, var1, var2, info):
        if var1 == var2:
            ASSERT_EQ.test_hook.add(AssertionResult(True, ''))
        else:
            ASSERT_EQ.test_hook.add(AssertionResult(False, info))

###############################################################################

class TestSuite:
    def __init__(self):
        self.tests_list = []
        self.n_executed = 0
        self.n_passed = 0

    def addTest(self, description, code):
        self.tests_list.append((description, code))

    def run(self):
        print 'Running: %d tests' % (len(self.tests_list))
        # Testing
        for desc, code in self.tests_list:
            result = TestResult()
            self.assertsInit(result)
            code() # Testing ...
            print '...........................................'
            if result.getResult() == True:
                print '[OK]:', desc
            else:
                print '[FAIL]:', desc
                print 'details'
                for x in result.getFailedAsserts():
                    print x.getInfo()


        #------------------------------------------------

    def assertsInit(self, testHook):
        ASSERT_TRUE.test_hook = testHook
        ASSERT_FALSE.test_hook = testHook
        ASSERT_EQ.test_hook = testHook







def main():
    pass

if __name__ == '__main__':
    main()
