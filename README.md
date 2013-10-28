# AutoUpdateSourceHeader for Sublime Text plug-in

Sublime Text 2/3 plug-in.

Auto update source header.
* modified user name
* modified date
* copyright year

ex)
your name : Harurow / date : 2013-10-20

* before
```c
/**********
* modified by     : O.Takafumi.
* last modified   : 2011-04-19
* Copyright (c) 2011 XXXXXX.
***********/
```

* after
```c
/**********
* modified by     : Harurow
* last modified   : 2013-10-20
* Copyright (c) 2011-2013 XXXXXX.
***********/
```

## How to Install ##

With [Package Control](https://sublime.wbond.net/installation):

1. Run “Package Control: Install Package” command, find and install `AutoUpdateSourceHeader` plugin.

Manually:

1. Clone or [download](https://github.com/Harurow/sublime_autoupdatesourceheader/archive/master.zip) git repo into your packages folder (in ST, find Browse Packages... menu item to open this folder)

## Setting ##

You must set your name.

1. Run “[Preferences] - [Package Settings] - [AutoUpdateSourceHeader] - [Settings -User]”

2. set your name
{
	"my_name": **INPUT YOUR NAME**
}

## License
The MIT License (MIT)

Copyright (c) 2013 Motoharu Tsubaki.

Permission is hereby granted, free of charge, to any person obtaining a 
copy of this software and associated documentation files (the "Software"),
to deal in the Software without restriction, including without limitation
the rights to use, copy, modify, merge, publish, distribute, sublicense,
and/or sell copies of the Software, and to permit persons to whom the
Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in
all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING
FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER
DEALINGS IN THE SOFTWARE.

