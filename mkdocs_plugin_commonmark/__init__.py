from mkdocs.plugins import BasePlugin
from mkdocs.structure.pages import Page, _RelativePathExtension

from mkdocs.structure.toc import get_toc
from .mistletoe_interop import MarkdownInterop, ETreeRenderer, DocumentLazy, mistletoe_span_tokens
from mistletoe.block_token import _token_types as _block_token_types
from mistletoe.span_token import HTMLSpan

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
    preprocessed = md._run_preprocessors(self.markdown)

    picked_st = [
        'EscapeSequence',
        # 'Strikethrough',  # mistletoe issue #86, PR #87
        'AutoLink',
        'CoreTokens',
        'InlineCode',
        'LineBreak',
        'RawText',
    ]

    my_inline_token_types = [mistletoe_span_tokens[x] for x in picked_st]

    # these are added by renderer when initializing, we
    # are replacing them later, so we have to insert them
    # by ourselves.
    # not knowing how to handle this better

    my_inline_token_types.insert(0, HTMLSpan)

    with ETreeRenderer() as r:
        docl = DocumentLazy(
            preprocessed,
            _block_token_types,
            my_inline_token_types,
            root_tag=md.doc_tag)

        docl.run_block()
        docl.run_maketree()

        doc = r.render(docl).getroot()
    self.content = md._convert_from_elem(doc)
    self.toc = get_toc(getattr(md, 'toc_tokens', []))

# Page.render = render

class CommonMark(BasePlugin):
    original_render = None

    def on_pre_build(self, config, **kwargs):
        if not self.original_render:
            self.original_render = Page.render
        Page.render = render

    def on_post_build(self, config, **kwargs):
        Page.render = self.original_render
