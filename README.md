This is a simple demo for command line usage
```
[xiaocwan@dhcp test_robotframework]$ pybot -V resource-test.py   test.txt
==============================================================================
Test :: This suite cover all testxxx related cases                            
==============================================================================
case1 - scenario xxx and xxx                                          | PASS |
------------------------------------------------------------------------------
Test :: This suite cover all testxxx related cases                    | PASS |
1 critical test, 1 passed, 0 failed
1 test total, 1 passed, 0 failed
==============================================================================
Output:  /home/xiaocwan/test_robotframework/output.xml
Log:     /home/xiaocwan/test_robotframework/log.html
Report:  /home/xiaocwan/test_robotframework/report.html
```


By default the -L (debug level) is INFO, the print and return from lib func are printed to log.html
