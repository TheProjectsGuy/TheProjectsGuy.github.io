# TheProjectsGuy Welcomes You

My personal webpage available at [theprojectsguy.github.io](https://theprojectsguy.github.io/), built using the [al-folio](https://github.com/alshedivat/al-folio) theme. The original readme is in [README.original.md](./README.original.md).

## Table of Contents

- [TheProjectsGuy Welcomes You](#theprojectsguy-welcomes-you)
    - [Table of Contents](#table-of-contents)
    - [Setup](#setup)
    - [References](#references)

## Setup

Steps to create this website (first build)

1. Fork the [al-folio](https://github.com/alshedivat/al-folio) theme as `TheProjectsGuy.github.io`.
2. Setup Jekyll using [these instructions](https://jekyllrb.com/docs/installation/)
3. Clone and see the webpage on local system. This is same as [step 4 and beyond from here](https://jekyllrb.com/docs/)

    ```bash
    git clone https://github.com/TheProjectsGuy/TheProjectsGuy.github.io.git
    cd TheProjectsGuy.github.io
    # Recompile and check results at localhost:4000
    bundle install
    bundle exec jekll serve
    ```

4. Set up the GitHub build pipeline
    1. In `_config.yml`, set the following

        ```yml
        url: https://TheProjectsGuy.github.io # the base hostname & protocol for your site
        baseurl: # the subpath of your site, e.g. /blog/
        ```

    2. Recompile the site and check the results (on local system). Push the changes to the repository (the page may not build yet)
    3. On GitHub, set the `Settings` > `Pages` > `Branch` to `gh-pages`
    4. Push some new changes (or wait for the site to rebuild)
5. Set up the branch and this file

    ```bash
    cd TheProjectsGuy.github.io
    git checkout -b main
    git checkout -b archive
    mv ./README.md ./README.original.md
    touch README.md
    git add --all
    git commit -m "Added separate README"
    git push origin -u main
    ```

6. Change default branch to `main` and delete the `master` branch (local and github). Keep `archive` as a local backup branch (do not deploy its build)

    Whenever you want to debug the original website, check the `archive` build

    ```bash
    git checkout archive
    bundle exec jekll serve
    ```

    Optionally, push `archive` to GitHub and add a read-only [branch protection rule](https://docs.github.com/en/repositories/configuring-branches-and-merges-in-your-repository/defining-the-mergeability-of-pull-requests/about-protected-branches). You may also delete `master` in remote and local repository.

## References

- [jekyll on ruby](https://jekyllrb.com/)
    - [Ruby 101](https://jekyllrb.com/docs/ruby-101/)
- [GitHub pages](https://pages.github.com/)
- [Liquid Documentation](https://shopify.github.io/liquid/)
- Template: [alshedivat.github.io/al-folio/](https://alshedivat.github.io/al-folio/)

[![Developer TheProjectsGuy][dev-shield]][dev-profile-link]

[dev-shield]: https://img.shields.io/badge/Developer-TheProjectsGuy-blue
[dev-profile-link]: https://github.com/TheProjectsGuy
