# mkdocs-plugin-commonmark

A plugin for mkdocs that swaps python-markdown for mistletoe to bring CommonMark support to mkdocs. Please note, this plugin monkey-patches mkdocs as there are not plugin hooks for changing the renderer.

The majority of the code to support this plugin comes from the development Andy Pan did to fork mkdocs to add commonmark support. This plugin eliminates the need for a fork, but given that is closely coupled to mkdoc internals, it may break on a subsequent mkdoc release. It has currently been tested with version 1.1.2 of mkdocs.

