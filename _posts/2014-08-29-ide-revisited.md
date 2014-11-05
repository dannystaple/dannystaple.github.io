---
layout: post
title: IDE For Jekyll revisited
tags: [computers, ide, jekyll, linux, programming]
---
After playing with the cloud 9 idea for a couple of days, I decided that I still really like Pycharm - aka intellij too much.

However, how could I get the linux Jekyll experience, without reinstalling the vm, so running the ide natively on Windows?

I decided to explore the remote editing/sync features of pycharm.

1. Ensure ssh is set up on the vm
2. In pycharm, set up the sync directory - click tools, deployment, configuration, then add one. 
3. Exclude the _site and .git folders from the upload. 
4. Click the upload button and fix any issues.
5. Set up the vm to automatically run jekyll -w in the destination directory.
6. Check you can see the output in a browser on the native machine.
7. Now enable the "auto upload" feature in Pycharm.

You will now be able to point your browser at the output from Jekyll, and as you modify the code in your IDE, it will automatically keep that up to date, albeit with a bit of lag.

# Improvements

I would like to make sure that the output from Jekyll is available locally - I can ssh in and see the nohup.out file, but it would be nice to integrate that more into pycharm.

Also - it would be great if the VM would automatically start jekyll, as I have a couple of Jekyll based sites, I can almost visualise a runner with a couple of named directories and port numbers, starting jekyll on all of them. Maybe something set up to run with initd so I only need to start the VM headlessly, and it will start functioning correctly.

A certain amount of this is moot when minor site tweaks can be made from github directly on a connected device, so I can stick with pycharm when at my laptop. Github has preview built in, and will directly render valid stuff.

