import math

from nose.tools import eq_

from example.commons import Faker
from pyecharts import options as opts
from pyecharts.charts import Line3D


def test_line3d_base():
    data = []
    for t in range(0, 25000):
        _t = t / 1000
        x = (1 + 0.25 * math.cos(75 * _t)) * math.cos(_t)
        y = (1 + 0.25 * math.cos(75 * _t)) * math.sin(_t)
        z = _t + 2.0 * math.sin(75 * _t)
        data.append([x, y, z])
    c = (
        Line3D()
        .add(
            "",
            data,
            xaxis3d_opts=opts.Axis3DOpts(Faker.clock, type_="value"),
            yaxis3d_opts=opts.Axis3DOpts(Faker.week_en, type_="value"),
            grid3d_opts=opts.Grid3DOpts(width=100, height=100, depth=100),
        )
        .set_global_opts(
            visualmap_opts=opts.VisualMapOpts(
                max_=30, min_=0, range_color=Faker.visual_color
            )
        )
    )
    eq_(c.theme, "white")
    eq_(c.renderer, "canvas")
    c.render()
