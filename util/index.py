import os
import re
import pathlib
from util import consts

REGEX_MARKDOWN_HEADER = re.compile(r'(#+) ?(.+)\n?')
REGEX_TAG_START = re.compile(r'<!--ts-->', re.IGNORECASE)
REGEX_TAG_END = re.compile(r'<!--te-->', re.IGNORECASE)


def is_markdown_file(file_path):
    return pathlib.Path(file_path).suffix.lower() == consts.EXTENSION


def get_filenames(path, selector_lambda=None):
    # By default we select everything
    if selector_lambda is None:
        def selector_lambda(path): return True

    files = []
    for root, directories, filenames in os.walk(path):
        for filename in filenames:
            if selector_lambda(filename):
                files.append(os.path.join(root, filename))

    return files


def get_link_tag(header, link_tags_found):
    result = ''
    for c in header.lower():
        if c.isalnum():
            result += c
        elif c == ' ' or c == '-':
            result += '-'
        # else it's punctuation so we drop it.

    if result not in link_tags_found:
        link_tags_found[result] = 0
    else:
        link_tags_found[result] += 1
        result += '-' + str(link_tags_found[result])

    return '(#' + result + ')'


def generate_toc_lines(file_lines):
    toc = []
    link_tags_found = {}

    for line in file_lines:
        match = REGEX_MARKDOWN_HEADER.match(line)
        if match:
            # add spaces based on sub-level, add [Header], then figure out what
            # the git link is for that header and add it
            toc_entry = '    ' * (len(match.group(1)) - 1) + '- [' + match.group(
                2) + ']' + get_link_tag(match.group(2), link_tags_found)
            toc.append(toc_entry + '\n')

    return toc


def main(path):
    md_files = get_filenames(path, is_markdown_file)

    for file in md_files:
        lines = []
        with open(file, 'r') as file_handle:
            lines = file_handle.readlines()

        toc_lines = generate_toc_lines(lines)

        with open(file, 'w') as write_handle:
            for line in toc_lines:
                write_handle.write(line)
