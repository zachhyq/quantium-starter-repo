from contextvars import copy_context
from dash._callback_context import context_value
from dash._utils import AttributeDict
import pytest


# Import the names of callback functions you want to test
from app import app

@pytest.fixture
def app_server(dash_duo):
    """Start the Dash server and yield the dash_duo object."""
    dash_duo.start_server(app)
    return dash_duo

def test_for_header(app_server):
    header_text = "Visualising Sales across Time"
    app_server.wait_for_text_to_equal('h1',
                                      header_text,
                                      timeout=4)

def test_for_visualisation(app_server):
    graph_id = 'sales-graph'
    app_server.wait_for_element(f'#{graph_id}', timeout=4)

def test_region_picker(app_server):
    radio_id = 'region-radio'
    app_server.wait_for_element(f'#{radio_id}', timeout=4)
    print('all good')

