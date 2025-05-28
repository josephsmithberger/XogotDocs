<!-- Remove this line to publish to docs.xogot.com -->
# Random number generation

Many games rely on randomness to implement core game mechanics. This page
guides you through common types of randomness and how to implement them in
Godot.

After giving you a brief overview of useful functions that generate random
numbers, you will learn how to get random elements from arrays, dictionaries,
and how to use a noise generator in GDScript. Lastly, we'll take a look at
cryptographically secure random number generation and how it differs from
typical random number generation.

> Note:
>
> Computers cannot generate "true" random numbers. Instead, they rely on
> pseudorandom number generators
> (PRNGs).
>
> Godot internally uses the PCG Family
> of pseudorandom number generators.
>

## Global scope versus RandomNumberGenerator class

Godot exposes two ways to generate random numbers: via global scope methods or
using the [RandomNumberGenerator](https://docs.godotengine.org/en/stable/classes/class_randomnumbergenerator.html#class-randomnumbergenerator) class.

Global scope methods are easier to set up, but they don't offer as much control.

RandomNumberGenerator requires more code to use, but allows creating
multiple instances, each with their own seed and state.

This tutorial uses global scope methods, except when the method only exists in
the RandomNumberGenerator class.

## The randomize() method

> Note:
>
> Since Godot 4.0, the random seed is automatically set to a random value when
> the project starts. This means you don't need to call randomize() in
> _ready() anymore to ensure that results are random across project runs.
> However, you can still use randomize() if you want to use a specific
> seed number, or generate it using a different method.
>

In global scope, you can find a [randomize()](https://docs.godotengine.org/en/stable/classes/class_@globalscope_method_randomize.html#class-@globalscope_method_randomize) method. **This method should be called only
once when your project starts to initialize the random seed.** Calling it
multiple times is unnecessary and may impact performance negatively.

Putting it in your main scene script's _ready() method is a good choice:

You can also set a fixed random seed instead using [seed()](https://docs.godotengine.org/en/stable/classes/class_@globalscope_method_seed.html#class-@globalscope_method_seed). Doing so will give you deterministic results
across runs:

When using the RandomNumberGenerator class, you should call randomize() on
the instance since it has its own seed:

## Getting a random number

Let's look at some of the most commonly used functions and methods to generate
random numbers in Godot.

The function [randi()](https://docs.godotengine.org/en/stable/classes/class_@globalscope_method_randi.html#class-@globalscope_method_randi) returns a random
number between 0 and 2^32 - 1. Since the maximum value is huge, you most
likely want to use the modulo operator (%) to bound the result between 0 and
the denominator:

[randf()](https://docs.godotengine.org/en/stable/classes/class_@globalscope_method_randf.html#class-@globalscope_method_randf) returns a random floating-point
number between 0 and 1. This is useful to implement a
<doc:random_number_generation#Weighted-Random-Probability> system, among
other things.

[randfn()](https://docs.godotengine.org/en/stable/classes/class_@globalscope_method_randfn.html#class-@globalscope_method_randfn) returns a random
floating-point number following a normal distribution. This means the returned
value is more likely to be around the mean (0.0 by default),
varying by the deviation (1.0 by default):

[randf_range()](https://docs.godotengine.org/en/stable/classes/class_@globalscope_method_randf_range.html#class-@globalscope_method_randf_range) takes two arguments
from and to, and returns a random floating-point number between from
and to:

[randi_range()](https://docs.godotengine.org/en/stable/classes/class_@globalscope_method_randi_range.html#class-@globalscope_method_randi_range) takes two arguments from
and to, and returns a random integer between from and to:

## Get a random array element

We can use random integer generation to get a random element from an array,
or use the [Array.pick_random](https://docs.godotengine.org/en/stable/classes/class_array_method_pick_random.html#class-array_method_pick_random) method
to do it for us:

To prevent the same fruit from being picked more than once in a row, we can add
more logic to the above method. In this case, we can't use
[Array.pick_random](https://docs.godotengine.org/en/stable/classes/class_array_method_pick_random.html#class-array_method_pick_random) since it lacks a way to
prevent repetition:

This approach can be useful to make random number generation feel less
repetitive. Still, it doesn't prevent results from "ping-ponging" between a
limited set of values. To prevent this, use the <doc:random_number_generation#Shuffle-Bags> pattern instead.

## Get a random dictionary value

We can apply similar logic from arrays to dictionaries as well:

## Weighted random probability

The [randf()](https://docs.godotengine.org/en/stable/classes/class_@globalscope_method_randf.html#class-@globalscope_method_randf) method returns a
floating-point number between 0.0 and 1.0. We can use this to create a
"weighted" probability where different outcomes have different likelihoods:

You can also get a weighted random index using the
[rand_weighted()](https://docs.godotengine.org/en/stable/classes/class_randomnumbergenerator_method_rand_weighted.html#class-randomnumbergenerator_method_rand_weighted) method
on a RandomNumberGenerator instance. This returns a random integer
between 0 and the size of the array that is passed as a parameter. Each value in the
array is a floating-point number that represents the relative likelihood that it
will be returned as an index. A higher value means the value is more likely to be
returned as an index, while a value of 0 means it will never be returned as an index.

For example, if [0.5, 1, 1, 2] is passed as a parameter, then the method is twice
as likely to return 3 (the index of the value 2) and twice as unlikely to return
0 (the index of the value 0.5) compared to the indices 1 and 2.

Since the returned value matches the array's size, it can be used as an index to
get a value from another array as follows:

## "Better" randomness using shuffle bags

Taking the same example as above, we would like to pick fruits at random.
However, relying on random number generation every time a fruit is selected can
lead to a less uniform distribution. If the player is lucky (or unlucky), they
could get the same fruit three or more times in a row.

You can accomplish this using the shuffle bag pattern. It works by removing an
element from the array after choosing it. After multiple selections, the array
ends up empty. When that happens, you reinitialize it to its default value:

When running the above code, there is a chance to get the same fruit twice in a
row. Once we picked a fruit, it will no longer be a possible return value unless
the array is now empty. When the array is empty, we reset it back to its default
value, making it possible to have the same fruit again, but only once.

## Random noise

The random number generation shown above can show its limits when you need a
value that slowly changes depending on the input. The input can be a position,
time, or anything else.

To achieve this, you can use random noise functions. Noise functions are
especially popular in procedural generation to generate realistic-looking
terrain. Godot provides [fastnoiselite](https://docs.godotengine.org/en/stable/classes/class_fastnoiselite.html#class-fastnoiselite) for this, which supports
1D, 2D and 3D noise. Here's an example with 1D noise:

## Cryptographically secure pseudorandom number generation

So far, the approaches mentioned above are **not** suitable for
cryptographically secure pseudorandom number generation (CSPRNG). This is fine
for games, but this is not sufficient for scenarios where encryption,
authentication or signing is involved.

Godot offers a [Crypto](https://docs.godotengine.org/en/stable/classes/class_crypto.html#class-crypto) class for this. This class can perform
asymmetric key encryption/decryption, signing/verification, while also
generating cryptographically secure random bytes, RSA keys, HMAC digests, and
self-signed [X509Certificate](https://docs.godotengine.org/en/stable/classes/class_x509certificate.html#class-x509certificate)s.

The downside of :abbr:`CSPRNG (Cryptographically secure pseudorandom number generation)`
is that it's much slower than standard pseudorandom number generation. Its API
is also less convenient to use. As a result,
:abbr:`CSPRNG (Cryptographically secure pseudorandom number generation)`
should be avoided for gameplay elements.

Example of using the Crypto class to generate 2 random integers between 0
and 2^32 - 1 (inclusive):

```
var crypto := Crypto.new()
# Request as many bytes as you need, but try to minimize the amount
# of separate requests to improve performance.
# Each 32-bit integer requires 4 bytes, so we request 8 bytes.
var byte_array := crypto.generate_random_bytes(8)

# Use the ``decode_u32()`` method from PackedByteArray to decode a 32-bit unsigned integer
# from the beginning of `byte_array`. This method doesn't modify `byte_array`.
var random_int_1 := byte_array.decode_u32(0)
# Do the same as above, but with an offset of 4 bytes since we've already decoded
# the first 4 bytes previously.
var random_int_2 := byte_array.decode_u32(4)

prints("Random integers:", random_int_1, random_int_2)
```

> Seealso:
>
> See [PackedByteArray](https://docs.godotengine.org/en/stable/classes/class_packedbytearray.html#class-packedbytearray)'s documentation for other methods you can
> use to decode the generated bytes into various types of data, such as
> integers or floats.