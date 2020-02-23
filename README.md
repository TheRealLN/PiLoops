# PiLoops
An implementation of the loops described in the Numberphile video "Strings and Loops within Pi", as seen here:
https://www.youtube.com/watch?v=W20aT14t8Pw



## Example Output
```
1000000 digits of pi read in 0.003980398178100586 seconds.
169
 -> 40
 -> 70
 -> 96
 -> 180
 -> 3664
 -> 24717
 -> 15492
 -> 84198
 -> 65489
 -> 3725
 -> 16974
 -> 41702
 -> 3788
 -> 5757
 -> 1958
 -> 14609
 -> 62892
 -> 44745
 -> 9385
 -> 169
 ```

## Another Example of This Being Used
All index one numbers from 1 to 100000 that have a proper loop (using PI up to a million digits):
```python
print([i for i in range(int(1e6)) if pi_number_loop(pi_str, i, 1)[1] == 1])
```
Output:
```
[1, 19, 37, 40, 46, 70, 96, 169, 180, 1958, 3664, 3725, 3788, 5757, 9385, 14609, 15492, 16974, 24717, 41702, 44745, 62892, 65489, 84198]
```
