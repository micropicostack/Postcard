# Postcard

## What is it?
Postcard is a simple package to send _html_ styled emails. It was created to send visually good emails about Jenkins builds. 

## Quick Start
Install the package with _pip_ from a local folder.
```
cd Postcard
pip install .
```
Then use the package...
```python
>>> from postcard import Postcard
>>> from postcard.mailer import Mailman
>>> my_postcard = Postcard('Hello', 'sender@python.py', ['recipient@python.py'])
>>> my_postcard.create('<h1>Hello</h1>', 'Hello')
>>> mailman = Mailman('smtp.python_host.py', 0)
>>> mailman.connect()
>>> mailman.deliver('sender@python.py', ['recipient@python.py'], my_postcard.package())
```


