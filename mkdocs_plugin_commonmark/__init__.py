from mkdocs.plugins import BasePlugin
from mkdocs.structure.pages import Page, _RelativePathExtension

from mkdocs.structure.toc import get_toc
from .mistletoe_interop import MarkdownInterop
import html


def render(self, config, files):
    """
    Convert the Markdown source file to HTML as per the config.
    """

    extensions = [
        _RelativePathExtension(self.file, files)
    ] + config['markdown_extensions']

    md = MarkdownInterop(
        extensions=extensions,
        extension_configs=config['mdx_configs'] or {}
    )

    self.content = md.convert(self.markdown)
    toct = getattr(md, 'toc_tokens', [])
    def unescapetoken(token):
        token["name"] = html.unescape(token["name"])
        token["children"] = map(unescapetoken, token["children"])
        return token
    self.toc = get_toc(map(unescapetoken, toct))

# Page.render = render

class CommonMark(BasePlugin):
    original_render = None

    def on_pre_build(self, config, **kwargs):
        if not self.original_render:
            self.original_render = Page.render
        Page.render = render

    def on_post_build(self, config, **kwargs):
        Page.render = self.original_render
