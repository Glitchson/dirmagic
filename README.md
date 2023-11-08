# Dirmagic Python module

# This is a simple python module that contains a class for working with paths intuitively
<span class="kw" style="color: purple;"></span>
<span class="cls" style="color: orange;"></span>
<span class="fn" style="color: blue;" ></span>
<span class= "vr" style="color: red"></span>
<div style="border-radius: 10px; border-width: 1px; border-color: green;" class="code"></div>
The module contains a class `Path` which contains various functionalities for working with paths. It leverages python `magic` or `dunder`methods to make working with paths more intuitive and make the syntax minimal. The does the following:

* Get the home directory.
<p>
    The class Path contains a static method , <span><code>Path.home</code><span> that returns the home directory.
    <pre><python>
from dirmagic import Path
home_directory=Path.home()
</python>
    </pre>
</p>
