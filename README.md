# TheProjectsGuy Welcomes You

My personal webpage available at [theprojectsguy.github.io](https://theprojectsguy.github.io/), built using the [al-folio](https://github.com/alshedivat/al-folio) theme. The original readme is in [README.original.md](./README.original.md).

## Table of Contents

- [TheProjectsGuy Welcomes You](#theprojectsguy-welcomes-you)
    - [Table of Contents](#table-of-contents)
    - [Setup](#setup)
        - [Adding Social Integration](#adding-social-integration)
        - [Enabling mermaid diagrams](#enabling-mermaid-diagrams)
        - [Enabling Disqus](#enabling-disqus)
        - [Creating Pages](#creating-pages)
        - [Minor Additions](#minor-additions)
            - [Email Scrambler](#email-scrambler)
    - [Local Deployment](#local-deployment)
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
    bundle exec jekyll serve
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

### Adding Social Integration

1. Choose the profile logo from [fontawesome brands search](https://fontawesome.com/search?o=r&f=brands) (there are also [academicons](https://jpswalsh.github.io/academicons/), but we'll use fontawesome here). I'm choosing GoodReads `fa-goodreads` for this.
2. Go to the social media site and get the identifier for your profile in URL

    For example, on [goodreads](https://www.goodreads.com/), go to your profile link. Mine looks like this (either of the following)

    ```txt
    https://www.goodreads.com/user/show/127374683-avneesh
    https://www.goodreads.com/user/show/127374683
    ```

    My identifier is `127374683` (which, with the URL can give my profile)

3. Add the entry to [_config.yml](./_config.yml) file, under `Social integration`

    ```yml
    goodreads_id: 127374683 # Your goodreads URL ID
    ```

    Make sure the key `goodreads_id` is unique.

4. In [_includes/social.html](./_includes/social.html), at the desired place, add the following

    ```html
    {%- if site.goodreads_id -%}
    <a href="https://www.goodreads.com/user/show/{{ site.goodreads_id }}" title="GoodReads"><i class="fab fa-goodreads"></i></a>
    {% endif %}
    ```

    The `href` section requires the URL template. The `site` gets the contents of the YML file in the build.

5. Rebuild the site and refresh the browser

    ```bash
    # Recompile and check results at localhost:4000
    bundle install
    bundle exec jekyll serve
    ```

### Enabling mermaid diagrams

1. Install `nodejs` and `npm` from [here](https://linuxize.com/post/how-to-install-node-js-on-ubuntu-20-04/)

    ```bash
    sudo apt update
    sudo apt install nodejs npm
    ```

2. Set the permissions for `npm` to use paths in home. These are borrowed from [here](https://docs.npmjs.com/resolving-eacces-permissions-errors-when-installing-packages-globally)

    ```bash
    mkdir ~/.npm-global
    npm config set prefix '~/.npm-global'
    echo 'export NPM_CONFIG_PREFIX=~/.npm-global' >> ~/.zshrc
    echo 'export PATH=$PATH:${NPM_CONFIG_PREFIX}/bin' >> ~/.zshrc
    ```

    This will set the `~/.npm-global` folder as the library folder for npm.

3. Install the `mermaid.cli` package

    ```bash
    npm install -g mermaid.cli
    ```

4. Add the following code changes

    - In `Gemfile`, make sure the following are there in `group :jekyll_plugins`

        ```bash
        gem 'jekyll-diagrams'
        gem 'asciidoctor-diagram'
        ```

    - In `_config.yml`, the `plugins` should include `jekyll-diagrams`
    - There can also be a blank setting `jekyll-diagrams:` for the diagrams settings

5. Rebuild the site and test on local system

    ```bash
    bundle install
    bundle exec jekyll serve
    ```

### Enabling Disqus

By default, the `comments` blog page won't have comments rendered. Do the following

1. Go to https://disqus.com/ and create an account (click on `Get Started`)

    I'm using the Basic plan (free with ads) and the website name is `theprojectsguy` (this page's name)

2. When choosing platform for your site, choose `Universal Code` (at the bottom). You do not need to modify anything, the layout already includes code for disqus.
3. Set the `disqus_shortname` in `_config.yml` (you may have to uncomment it).
4. Rebuild the site

    ```bash
    bundle install
    bundle exec jekyll serve
    # Site on localhost:4000
    ```

5. Go to the template post with comments and you should now see the comments

### Creating Pages

Creating another page (under dropdown options). Assuming a gists page here.

1. Create page under `_pages/gists.md` with the following header

    ```md
    ---
    layout: page
    permalink: /gists/
    title: Gists
    description: Code snippets I have created to ease my developer life.
    ---
    ```

2. In `_pages/drapdown.md`, add the following to the `children`

    ```md
        - title: divider
        - title: Gists
        permalink: /gists/
    ```

3. Rebuild the site and the dropdown should contain the contents of the `gists.md` file.

### Minor Additions

Some minor additions to the webpage I got from others

#### Email Scrambler

In the [about.md](./_pages/about.md) page, add your email address under `profile > email` section (in header of page).

Thanks to [Jeff Donahue](http://jeffdonahue.com/) for the JavaScript starter code and Nikhil Varma Keetha's [Webpage](https://nik-v9.github.io/) for the initial idea and implementation.

## Local Deployment

For testing changes before pushing them. Run commands under this in the repository folder.

```bash
# Install packages (if the Gemfile has been changed)
bundle install
# Serve website on localhost:40000
bundle exec jekyll serve
```

## References

- [jekyll on ruby](https://jekyllrb.com/)
    - [Ruby 101](https://jekyllrb.com/docs/ruby-101/)
- [GitHub pages](https://pages.github.com/)
- [Liquid Documentation](https://shopify.github.io/liquid/)
- Template: [alshedivat.github.io/al-folio/](https://alshedivat.github.io/al-folio/)
- [Distill blogs](https://distill.pub/)
- [jekyll-diagrams](https://github.com/zhustec/jekyll-diagrams)
    - [mermaid](https://mermaid-js.github.io/mermaid/#/)
    - [mermaid.live](https://mermaid.live/) interactive online editor
- [disqus](https://disqus.com/)
    - [How to Install Disqus Manually Using the Universal Code](https://youtu.be/Dr6pSdeJgkA): But we won't have to do much of this

[![Developer TheProjectsGuy][dev-shield]][dev-profile-link]

[dev-shield]: https://img.shields.io/badge/Developer-TheProjectsGuy-blue
[dev-profile-link]: https://github.com/TheProjectsGuy
