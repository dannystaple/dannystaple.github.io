"""Unit tests for prepare missing images"""
import os
import pytest

from _missing_images.prepare_missing_images import post_line_to_list_of_local_image_links, \
    post_line_to_list_of_browseimg_links, filter_substitution_image_links, make_gallery_name_from_post_name, \
    get_gallery_path, make_gallery_index


@pytest.mark.parametrize("line, expected", [
        ("---", []),
        ("layout: stuff", []),
        ("text", []),
        ('<img src="test_link" alt="foo" />', ["test_link"]),
        ('Stuff <img src="test2_link" alt="foo" /> more stuff', ["test2_link"]),
        ('Stuff <img alt="hello" src="test3_link" /> <img src="test4_link" />', ["test3_link", "test4_link"]),
        ('![](test5_link)',  ["test5_link"]),
        ('![some alt](test6_link)',  ["test6_link"]),
        ('Stuff ![](test7_link) more stuff', ["test7_link"]),
        ('Stuff ![](test8_link) ![](test9_link)', ["test8_link", "test9_link"]),
        ('![should exclude this remote link](http://remote_link/test10', []),
        ('<img src="http://some_other/test11">', []),
        ('<img src="test12_link&thumb=1" alt="foo" />', ["test12_link"]),
        ('Stuff ![](test13_link&thumb=1)', ["test13_link"])
])
def test_map_post_lines_to_lists_of_local_image_links(line, expected):
    """Given a line, it should convert each case to a list of local links"""
    assert post_line_to_list_of_local_image_links(line) == expected


@pytest.mark.parametrize("line, expected", [
    ("---", []),
    ("text", []),
    ('<img src="an image link">', []),
    ('<a href="http://some.where/not_interesting">Meh</a>', []),
    ('<a href="browseimage386">blah</a>', ['browseimage386']),
    ('<a title="foo" href="browseimage386">blah</a> stuff', ['browseimage386']),
    ('stuff <a href="browseimage386">blah</a> stuff', ['browseimage386']),
    ('stuff <a href="browseimage386">blah</a> stuff <a href="browseimage395">meh</a>', ['browseimage386', 'browseimage395']),
    ('<a href="browse_something_else">b</a>', []),
    ('[hello](browseimage395)', ['browseimage395'])
])
def test_map_post_lines_list_of_browseimg_links(line, expected):
    """Given a line, it should convert each case into a list of browseimg links"""
    assert post_line_to_list_of_browseimg_links(line) == expected


@pytest.mark.parametrize("links, expected", [
    (['image1', '{{ blah}}/image5'], ['image1']),
])
def test_filter_sub_image_links(links, expected):
    """Ensure links with expansion rules are filtered"""
    assert filter_substitution_image_links(links) == expected


@pytest.mark.parametrize("post_name, gallery_name", [
    ("2003-my-post-stuff.md", "2003-my-post-stuff")
])
def test_make_gallery_name_from_post_name(post_name, gallery_name):
    assert make_gallery_name_from_post_name(post_name) == gallery_name


import yaml

@pytest.mark.parametrize("post_name, image_list, expected_output_path, expected_contact_sheet", [
    ("2003-my-post-stuff.md", ["img1", "img2", "foo.jpg", "bar.jpg"], "galleries/2003-my-post-stuff/index.md",
     """---
    title: 2003-my-post-stuff
    layout: gen-gallery
    gallery:
        - img1
        - img2
        - foo.jpg
        - bar.jpg
    """)
])
def test_make_gallery_should_make_contact_sheet(post_name, image_list, expected_output_path, expected_contact_sheet):
    """Given a post name with list of images - alt, src, dest link:
    Create a gallery which has:
        * folder in galleries path
        * Images
        * Image thumbs
        * Contact sheet - use a template from the picasa output
        * Image pages - a the template from the picasa output
    """
    gallery_name = make_gallery_name_from_post_name(post_name)
    gallery_path = get_gallery_path(gallery_name)
    output_path = os.path.join(gallery_path, "index.md")
    output_data = make_gallery_index(gallery_name, image_list)

    assert output_path == expected_output_path
    assert yaml.load(output_data.split("---")[1]) == yaml.load(expected_contact_sheet.split("---")[1])

