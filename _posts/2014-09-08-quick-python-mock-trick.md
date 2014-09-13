---
title: Trick for python mock side affects
tags: [python, mocking, testing, tdd]
layout: post
---
When using python, I test and use mocks, using the mock library.
I've occasionally had the need to return a value based upon the input parameters to  a mock.

I've done this before by building something and passing it into side_effect on the mock.

However, if you know that the test conditions mean your mocked functions behaviour could be mapped to a dictionary, try passing the dictionaries .get method as side_effect. With a single parameter as a key, this works brilliantly:

    my_mock = mock.Mock(side_effect={1: 'first', 2: 'second'}.get)
    assert my_mock(1) == 'first'

Dead easy little trick for simple mocks.

There may be a sneaky way to map call objects to responses in a dictionary too - I've not tried that yet.
