"""Script to find missing images on jekyll orionrobots site."""
from contextlib import closing
import os
import re
import itertools
import shutil
import urllib2


def post_line_to_list_of_local_image_links(line):
    """Convert a line to a list of image links"""
    normal_img = '<img .*?src="([^"]*?)(?:&thumb=1)?".*?>'
    md_img = '!\[[^\]]*\]\(([^)]*?)(?:&thumb=1)?\)'
    exp = re.compile(normal_img + "|" + md_img)
    results = itertools.chain(*re.findall(exp, line))

    return [item for item in results if item and not item.startswith("http")]


def post_line_to_list_of_browseimg_links(line):
    link_re = '<a .*?href="(browseimage[^"]*)".*?>'
    md_link = '\[[^\]]*\]\(([^)]*)\)'
    exp = re.compile(link_re + "|" + md_link)
    results = itertools.chain(*re.findall(exp, line))

    return [item for item in results if item]


def filter_substitution_image_links(links):
    """Remove any links that use a jekyll template rule - they won't be remote"""
    return [link for link in links if '{' not in link]


def post_to_list_of_image_and_browselinks(post_lines):
    browseimage_links = []
    image_links = []
    [(browseimage_links.extend(post_line_to_list_of_browseimg_links(line)),
     image_links.extend(post_line_to_list_of_local_image_links(line)))
     for line in post_lines]
    image_links = filter_substitution_image_links(image_links)
    image_links = [link for link in image_links if not os.path.exists(link)]
    return browseimage_links, image_links


def make_gallery_name_from_post_name(post_name):
    return post_name.replace(".md", '')


def get_gallery_path(gallery_name, config={'gallery_dir': 'galleries'}):
    """Get a gallery path"""
    return os.path.join(config['gallery_dir'], gallery_name)


def make_gallery_index(gallery_name, image_list):
    """Return index data for image_list"""
    gallery_data = [
        '---', 'title: %s ' % gallery_name, 'layout: gen-gallery',
        'gallery:',
    ]
    _ = [gallery_data.append('  - ' + image_link) for image_link in image_list]
    return "\n".join(gallery_data)


def copy_images(gallery_path, image_list):
    """Copy all the images in the list to the path"""
    for image_link in image_list:



def make_gallery(post_name, image_list, config={'gallery_dir': 'galleries'}):
    """make a gallery with a list of images"""
    gallery_name = make_gallery_name_from_post_name(post_name)
    gallery_path = get_gallery_path(gallery_name)
    output_path = os.path.join(gallery_path, "index.md")
    with open(output_path, "w") as fd:
        fd.write(make_gallery_index(gallery_name, image_list))

    copy_images(gallery_path, image_list)
    #make_thumbs
    #make_image_pages





#map: post -> image and browse links for each
    #map: post lines -> lists of local (no protocol) image links for each line
    #reduce: lists of image links in each line -> list of image links (chain)
    #map: post lines -> lists of browseimg links in each line
    #reduce: lists of links in each line -> list of links (chain)
#reduce: filter out image links with substitutions (these won't be remote)
#reduce: filtered image links -> those not in local dir - path.exists
#map: post name -> gallery name
#process: make gallery for each post
#process: download image+ thumb for each image link
#map: image links to gallery links
#map: browse links to gallery links


def fix_post(post_name):
    """Find and fix missing images/galleries on a post"""
    #find the image links
    with open("_posts" + post_name) as fd:
        image_links, browse_links = post_to_list_of_image_and_browselinks(fd)
    gallery_name = make_gallery_name_from_post_name(post_name)
    gallery_path = os.path.join("../galleries", gallery_name)
    try:
        os.makedirs(os.path.join(gallery_path, "images"))
    except OSError as err:
        if err.errno != 17:
            raise

    for image in image_links:
        #download image to it (both normal and thumb)
        with open(os.path.join(gallery_path, image), "wb") as output:
            with closing(urllib2.urlopen("http://orionrobots.co.uk/%s" % image)) as original:
                output.write(original.read())
        with open(os.path.join(gallery_path, "thm_" + image), "wb") as output:
            with closing(urllib2.urlopen("http://orionrobots.co.uk/%s" % image)) as original:
                output.write(original.read())

        #Log that the link to X in the post will now need to be a link to Y.
    #if there are browseimage links
        #make gallery thumb page.
    #For each browseimaqe link
        #Match with an image link
        #prepare list
        #log link change
    #For each in list
        #make gallery front end for it with
            #First/last/prev/next/thumbs/blog post


def main():
    for post_path in os.listdir("_posts"):
        fix_post("_posts/" + post_path)


if __name__ == "__main__":
    main()
