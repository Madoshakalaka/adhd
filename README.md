# ADHD

**Intended for personal use**

**Requires properly configured redis server**


[![Build Status](https://travis-ci.org/Madoshakalaka/adhd.svg)](https://travis-ci.org/Madoshakalaka/adhd)
[![codecov](https://codecov.io/gh/Madoshakalaka/adhd/branch/master/graph/badge.svg)](https://codecov.io/gh/Madoshakalaka/adhd)
[![PyPI version](https://badge.fury.io/py/adhd.svg)](https://badge.fury.io/py/adhd)
[![PyPI pyversions](https://img.shields.io/pypi/pyversions/adhd.svg)](https://pypi.python.org/pypi/adhd/)


## Installation

`$ pip install adhd`

Run adhd at startup

`$ adhd startup`

## What Does It Do

<!--![some show case picture](https://raw.githubusercontent.com/Madoshakalaka/adhd/master/readme_assets/showcasePicture.png)-->

Keep myself highly focused on work



## How to Use

First, register any number of different devices by having the `adhd` running on it.

For example I have a Windows tablet and PC.

Now on any of the devices:

`$ adhd for 1h`

Then any operation on registered devices will be monitored for 1 hour.

Operation can include: Mouse movement, mouse clicks, and key presses.

During the hour, if an inactivity of 10 seconds is detected anytime. There will be alert messages popping up on the 
screen.

If an inactivity of 20 seconds is detected, e-mails will be automatically sent to ALL MY G-MAIL CONTACTS with the 
following content:

```
Matt is not concentrating on his work
```

To have an emergency stop (alien invasion or earthquakes or something)

`$ adhd cured --password shitishouldneverpauseadhd`

When the emergency is resolved

`$ adhd relapses`


