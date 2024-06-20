# Gaussian module

Probability distribution classes based on an exercise from Udacity's
Python for AI course.

## Probability distributions completed so far

* gaussian

## Factoids

* will eventually incorporate this work into grscheller.boring-math
* using Python 3.12.3 instead of the Python 3.10.13 used by Udacity
  * Udacity just upgraded the Python they use from 3.6.3 in June 2024
  * 3.6.3 was version of Python out when PyTorch was released in 2016
* using `__future__` statement to import annotations
  * for use by Python std library typing module 
  * annotations targeted for Python 3.13.X

## Testing

The testing suite is in the GitHub clone, it is not installed with the
package.

To kick off all tests,

```
   $ pytest tests/`
```

So that the test data is found, run the tests from the root of the clone
of the GitHub repo.

## Documentation

See: [grscheller-courses-distributions](https://grscheller.github.io/courses-distributions)

## License Summary

Apache v2.0 License

See [LICENSE](LICENSE) for license details
and [NOTICE](NOTICE) for copyright details.
