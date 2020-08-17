# ptf-pytest
pytest implementation of PTF(Packet Test Framework https://github.com/p4lang/ptf/).
Allure report is integrated within the test example.


## Test examples run command:
```
sudo pytest ptf_runner.py --test-dir ./example/mytests/  --interface {yourInterface} 
```


## Allure command:
```
cp -rf reports/html/history reports/allure2/history && allure generate reports/allure2/ -o ./reports/html --clean && allure open ./reports/html
```


## Common:
```
rm -rf reports/allure2/*.json && rm -rf reports/allure2/history
sudo pytest ptf_runner.py --test-dir ./example/runner/   --interface 0@wlp2s0 --interface 1@lo

```
