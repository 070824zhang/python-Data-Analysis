from pyecharts.charts import Line
from pyecharts.options import TitleOpts, ToolboxOpts, AxisOpts
#设置变量
line = Line()
#添加x轴数据
x_data = [2005,2006,2007,2008,2009,2010,2011,2012,2013,2014,2015,2016,2017,2018,2019,2020,2021,2022,2023,2024,2025]
line.add_xaxis([str(year) for year in x_data])
#添加y轴数据
yaxis_data1 = [1617,1584,1594,1608,1615,1592,1604,1635,1640,1687,1655,1786,1723,1523,1465,1200,1062,956,902,954,792]
line.add_yaxis("出生人口",yaxis_data1)

yaxis_data2 = [849,892,913,935,943,949,960,966,972,977,976,977,986,993,998,998,1014,1041,1110,1093,1131]
line.add_yaxis("死亡人口",yaxis_data2)

#设置全局配置
line.set_global_opts (
    title_opts=TitleOpts(title="中国2005-2025年出生人口与死亡人口变化趋势",pos_left='center'),    #设置标题
    toolbox_opts=ToolboxOpts(is_show=True),
    xaxis_opts=AxisOpts(
        type_="category",
        axislabel_opts={"interval":0,"rotate":45}
    )
)
#通过render方法，将代码转化为图像
line.render("中国人口变化趋势.html",width="1200px")
line.render("中国人口变化趋势.html")