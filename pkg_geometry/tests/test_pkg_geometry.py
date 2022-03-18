from pkg_geometry import __version__
from pkg_geometry.geometry import facequadri

def test_version():
    assert __version__ == '0.0.1'

def test_perimetre():
    fig_geo=facequadri(2,3,4)
    per=fig_geo.perimetre()
    assert per==18


