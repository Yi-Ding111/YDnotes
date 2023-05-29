# UnitTest

A testcase is created by subclassing [`unittest.TestCase`](https://docs.python.org/3/library/unittest.html#unittest.TestCase)

```python
import unittest

class testclass(unittess.TestCase):
  def setUp(self):
    pass
  def test_work(self):
    pass
  def tearDown(self):
    pass
  
 if __name__=="__main__":
  
```

The [`setUp()`](https://docs.python.org/3/library/unittest.html#unittest.TestCase.setUp) and [`tearDown()`](https://docs.python.org/3/library/unittest.html#unittest.TestCase.tearDown) methods allow you to define instructions that will be executed before and after each test method. They are covered in more detail in the section [Organizing test code](https://docs.python.org/3/library/unittest.html#organizing-tests).
