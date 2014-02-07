---
created: 2005-12-17 17:53:27
description: Review of bitweaver
tags: [forum, cms, blog, wiki, software, php]
title: Review of bitweaver
layout: post
---
{% include JB/setup %}
As much as it is my job to get the scoop on robots, or build robots and find content for orionrobots, it is also my responsibility to actually maintain the site, and make top level decisions about the future of how the content is stored and accessed.

# History

I will start with a little history - OrionRobots has been through a few CMS (Content Management System) tools in the last 4 years. It started life as a basic AMP (Apache MySQL PHP) database of articles of my own, and was turned into a site based on Slashcode (which I found a little too heavy), then PHPSlash which I eventually realised was not quite the required format. I then found Zope, which ran using Python- very expandable, but extremely heavyweight, and at that time, its wiki component was very unreliable and not being maintained very much. I finally settled, and have stayed for around 2 years now on Tikiwiki.

# Tikiwiki

Tikiwiki is fully featured. It is stable, well developed and easily styled. Although it is rough around the edges, I do have my migration script I created then for getting my zope content into tiki.

It has a few problems, it is not the fastest tool, though notably faster than Zope. It still has issues with modularity, and expansion - though the very active community (of which I am part and am working on a few mods of my own) are working to improve it a great deal. I find the galleries and file galleries useful, and the addition of subgalleries was great, but a more directory like structure (which Zope did have) might be useful. Tiki is undergoing quite rapid development and feels very right for what I do.

# Bitweaver

This week, I came across something new, and decided to evaluate it for testing - Bitweaver. Bitweaver actually started life as "TikiPro", a fork of Tikiwiki. It is far more modular, and fell out with the tiki maintainer over the use of PhpBB. In my evaluation - I notice it is much faster than tiki because of fewer database hits and optimized code. It only loads or installs the required modules.

So I made sure my test server was up to spec, met all the requirements (since I run a couple of tiki test sites, it was pretty much there already), downloaded Bitweaver1.1, and installed it. I will freely admit, since it is closely related to tikiwiki, and since I am very comfortable with tikiwiki - I compared it most closely with tiki.

Bitweavers installation was very shiny and easy, although, since installation is a rare operation, and I am very comfortable installing tikiwiki, I don't consider it that important. Once installed, and clicking around the sample data from the installation - the speed difference between this and tiki running on the same box was quite notable. It is definitely nippier. The only thing that has not undergone a speedup is the search system, which is quite slow, clunky and a little unreliable - a problem shared by the tiki search - and the reason I pair up with a google sitesearch bar.

What really strikes me is most definitely the "packages". Packages give a nice way to integrate new behaviour into a site, including taking pristine code from other AMP applications and making minimal changes to integrate them. You could (for example) probably take Squirrelmail, and integrate it the site - wrapping the user logins and making a few style changes, while keeping most of the core functionality close enough that merging new versions of squirrelmail wouldn't be too onerous.

Some of the existing packages are very nice as well. The "liberty" package - a component in the default distribution, integrates and standardises some content much closer than tikiwiki does. The "nexus" menu system seems interesting too.

The wikibooks (which directly rival tiki structures) allow multiple content types. It still suffers from tiki's problems creating PDF's which tend not to keep wiki formatting, but show the markup behind it. As well as greater content flexibility (drawing on "liberty" probably) it is also a little nicer in terms of usability here.

However, It has fallen behind in many respects - it does not offer the internationalised wiki pages that tiki has. It lacks spellchecking - a small feature that is actually quite important when trying to present good and accurate content.

Its developer documentation, and general documentation tends to be a lot more complete than tikiwiki's. Though I still couldn't always find what I was looking for.

Unfortunately - their use to integrate phpBB at the expense of tikiforums strikes me as a bad choice. Tikiwiki forums integrate well with the rest of a tiki site, as do much of the tikiwiki components. So maybe - someone will come out with a package that integrates tikiwiki forums, or a phpBB plugin to "tikiwikify" it a bit more. Of course, I know there are those who will prefer phpBB - so having the choice would be fantastic. I don't have the time myself to integrate tikiforums back into a bitweaver package though.

Also on my test installation, some operations, including a simple search produced many warnings - which were visible on the rendered page, and I (I reported the bug) also experienced a "white page of death". It just seems a little less stable and together than tikiwiki. This doesn't quite feel "enterprise ready" in the same way tiki has served me.

# Summary

In summary, Bitweaver has huge potential, but it needs a little more time - I will probably come back and take a look again in about 6 months, and see where it has gone. Some of the features seen in bitweaver may also be backported in tikiwiki. I am staying with Tikiwiki for now.

