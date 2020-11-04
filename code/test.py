#!/usr/bin/python2.7
rf = {
        **{i**2: 0 for i in range(45)},
            **{i**3: 0 for i in range(13)}
}
print(rf)