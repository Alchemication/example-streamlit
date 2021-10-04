"""Frameworks for running multiple Streamlit views (applications) as a single app.
"""
from dataclasses import dataclass
from typing import Callable, Optional

import streamlit as st


@dataclass
class View:
    title: str  # title of the app. Appears in the dropdown in the sidebar
    func: Callable  # the python function to render this app


class StreamlitMultiViewApp:
    """Framework for combining multiple streamlit views (apps)
    Usage:
        import foo
        import bar
        app = StreamlitMultiViewApp()
        app.add_view(View(title="Foo", func=foo.view))
        app.add_view(View(title="Bar", func=bar.view))
        app.run()
    """
    def __init__(self):
        self.views: list = []
        self.header: Optional[View] = None

    def add_header(self, view: View):
        self.header = view

    def add_view(self, view: View):
        self.views.append(view)

    def run(self):
        if len(self.views) == 0:
            raise ValueError("Please provide at least one view using add_view method")
        # draw header if available
        if self.header:
            st.title(self.header.title)
            self.header.func()
        # no need to draw a radio selection when we have only 1 view
        if len(self.views) == 1:
            view = self.views[0]
        else:
            view = st.sidebar.radio(
                'Select View:',
                self.views,
                format_func=lambda v: v.title)
        # draw content
        view.func()
