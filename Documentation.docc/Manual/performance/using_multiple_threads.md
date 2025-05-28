<!-- Remove this line to publish to docs.xogot.com -->
# Using multiple threads

## Threads

Threads allow simultaneous execution of code. It allows off-loading work
from the main thread.

Godot supports threads and provides many handy functions to use them.

> Note: If using other languages (C#, C++), it may be easier to use the
> threading classes they support.
>

> Warning:
>
> Before using a built-in class in a thread, read <doc:thread_safe_apis>
> first to check whether it can be safely used in a thread.
>

## Creating a Thread

To create a thread, use the following code:

Your function will, then, run in a separate thread until it returns.
Even if the function has returned already, the thread must collect it, so call
[Thread.wait_to_finish()](https://docs.godotengine.org/en/stable/classes/class_thread_method_wait_to_finish.html#class-thread_method_wait_to_finish), which will
wait until the thread is done (if not done yet), then properly dispose of it.

> Warning:
>
> Creating threads is a slow operation, especially on Windows. To avoid
> unnecessary performance overhead, make sure to create threads before heavy
> processing is needed instead of creating threads just-in-time.
>
> For example, if you need multiple threads during gameplay, you can create
> threads while the level is loading and only actually start processing with
> them later on.
>
> Additionally, locking and unlocking of mutexes can also be an expensive
> operation. Locking should be done carefully; avoid locking too often (or for
> too long).
>

## Mutexes

Accessing objects or data from multiple threads is not always supported (if you
do it, it will cause unexpected behaviors or crashes). Read the
<doc:thread_safe_apis> documentation to understand which engine APIs
support multiple thread access.

When processing your own data or calling your own functions, as a rule, try to
avoid accessing the same data directly from different threads. You may run into
synchronization problems, as the data is not always updated between CPU cores
when modified. Always use a [Mutex](https://docs.godotengine.org/en/stable/classes/class_mutex.html#class-mutex) when accessing
a piece of data from different threads.

When calling [Mutex.lock()](https://docs.godotengine.org/en/stable/classes/class_mutex_method_lock.html#class-mutex_method_lock), a thread ensures that
all other threads will be blocked (put on suspended state) if they try to lock
the same mutex. When the mutex is unlocked by calling
[Mutex.unlock()](https://docs.godotengine.org/en/stable/classes/class_mutex_method_unlock.html#class-mutex_method_unlock), the other threads will be
allowed to proceed with the lock (but only one at a time).

Here is an example of using a Mutex:

## Semaphores

Sometimes you want your thread to work "on demand". In other words, tell it
when to work and let it suspend when it isn't doing anything.
For this, [Semaphores](https://docs.godotengine.org/en/stable/classes/class_semaphore.html#class-semaphore) are used. The function
[Semaphore.wait()](https://docs.godotengine.org/en/stable/classes/class_semaphore_method_wait.html#class-semaphore_method_wait) is used in the thread to
suspend it until some data arrives.

The main thread, instead, uses
[Semaphore.post()](https://docs.godotengine.org/en/stable/classes/class_semaphore_method_post.html#class-semaphore_method_post) to signal that data is
ready to be processed: