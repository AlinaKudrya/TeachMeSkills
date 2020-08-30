my_lambda = (lambda **kwargs: {i * 2: kwargs[i] for i in kwargs})

d = my_lambda(bla=2, chocolate=5, apple=10)

print(d)
