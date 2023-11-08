# Dirmagic Python module

# This is a simple python module that contains a class for working with paths intuitively
The module contains a class `Path` which contains various functionalities for working with paths. It leverages python `magic` or `dunder`methods to make working with paths more intuitive and make the syntax minimal. The does the following:

* Get the home directory.
<pre>
    The class Path contains a static method , <span><code>Path.home</code><span> that returns the home directory.
    <pre><code>
        from dirmagic import Path
        home_directory=Path.home()
    </code></pre>
</pre>
