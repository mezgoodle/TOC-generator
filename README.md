# TOC generator

[![Build Status](https://img.shields.io/badge/language-python-brightgreen?style=flat-square)](https://www.python.org/)

Hello everyone! This is the repository of TOC generator on Python.

> TOC = Table Of Contents

## Table of contents

- [TOC generator](#toc-generator)
- [Table of contents](#table-of-contents)
- [Motivation](#motivation)
- [Build status](#build-status)
- [Badges](#badges)
- [Code style](#code-style)
- [Screenshots](#screenshots)
- [Tech/framework used](#techframework-used)
- [Features](#features)
- [Code Example](#code-example)
- [Installation](#installation)
- [Fast usage](#fast-usage)
- [Tests](#tests)
- [Contribute](#contribute)
- [Credits](#credits)
- [License](#license)

## Motivation

When I improved my README files on GitHub, I learned about _Table of contents_. After reviewing several ways to create it, I have realized that it is either a package for _Node_ or _Python_, or a website on _JavaScript_. So I have decided to create myself generator. Also I wanted that everyone can use my generator, so I installed [_Flask_](https://flask.palletsprojects.com/) :bowtie:.

## Build status

Here you can see build status of [continuous integration](https://en.wikipedia.org/wiki/Continuous_integration):

[![Build Status](https://travis-ci.com/mezgoodle/TOC-generator.svg?branch=master)](https://travis-ci.com/mezgoodle/TOC-generator)

## Badges

[![Build Status](https://img.shields.io/badge/Platform-Flask-brightgreen?style=flat-square)](https://flask.palletsprojects.com/)

## Code style

I'm using [Codacy](https://www.codacy.com/) for automate my code quality.

[![Codacy Badge](https://app.codacy.com/project/badge/Grade/1e8f857fb7e34174b782365c596bd095)](https://www.codacy.com/manual/mezgoodle/TOC-generator?utm_source=github.com&amp;utm_medium=referral&amp;utm_content=mezgoodle/TOC-generator&amp;utm_campaign=Badge_Grade)
 
## Screenshots

- Main page, work with text

![Screenshot 1](https://raw.githubusercontent.com/mezgoodle/images/master/TOC-generator-1.png)

- Upload the files

![Screenshot 2](https://raw.githubusercontent.com/mezgoodle/images/master/TOC-generator-2.png)

## Tech/framework used

**Built with**

- [Flask](https://flask.palletsprojects.com/)
- [PyTest](https://docs.pytest.org/en/latest/)

## Features

On the website you can **create** TOC from _text_ or from _files_.

## Code Example

- generate TOC

```python
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
```

- upload and work with file

```python
@app.route('/file', methods=['GET', 'POST'])
def file():
    if request.method == 'GET':
        return redirect(url_for('index'))
    result, data = '', ''
    files = request.files.getlist('files')
    for file in files:
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            data += filename + consts.ENDING
            result += filename + consts.ENDING
            path = f'{consts.PATH}/{filename}'
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            with open(path, 'r') as file:
                data += file.read() + consts.ENDING
            main(consts.PATH)
            with open(path, 'r') as file:
                result += file.read() + consts.ENDING
            os.remove(path)
    return render_template(
        'index.html',
        rows=consts.ROWS,
        input=data,
        result=result)
```

## Installation

First install [Python](https://www.python.org/downloads/).

> If you don't have *pip*, [install](https://pip.pypa.io/en/stable/installing/) it.

Then type in terminal:

```bash
pip install -r requirements.txt
```

## Fast usage

Move to the project directory and type in terminal:

```bash
python app.py
```

Open in browser `http://127.0.0.1:5000/`

> or another port

## Tests

I do unit-testing with **pytest** and lint with **flake8**, so [here](https://travis-ci.com/mezgoodle/TOC-generator) you can see the result.

## Contribute

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change. Also look at the [CONTRIBUTING.md](https://github.com/mezgoodle/TOC-generator/blob/master/CONTRIBUTING.md).

## Credits

Videos, links that helped and inspired me to build this project: 

- [GitLab documentation](https://docs.gitlab.com/ee/user/markdown.html#header-ids-and-links)
- [Stackoverflow page](https://stackoverflow.com/questions/22520932/python-remove-all-non-alphabet-chars-from-string)
- [YouTube video](https://www.youtube.com/watch?v=6WruncSoCdI)
- [Bootstrap 5 documentation](https://v5.getbootstrap.com/docs/5.0)
- [Flask documentation](https://flask.palletsprojects.com/en/1.1.x/patterns/fileuploads/)

## License

MIT © [mezgoodle](https://github.com/mezgoodle)
