# coding: utf-8

# ==============================================================================
# 主要是用于生成机柜图
# ==============================================================================


from django.utils.html import format_html, mark_safe
from cabinet_structure.utils.algorithm import cabinet_algorithm
from cabinet_structure.utils.tools import MultipleIter


class HTMLRenderTemplate(object):
    """
    各种需要生成机柜的脚手架组件如(机柜\导轨)
    """

    @property
    def cabinet_structure_template(self):
        structure = "<table class='table cabinets'><tbody><tr>{0}</tr></tbody></table>"
        return structure

    @property
    def cabinet_structure_rows_template(self):
        """
        一排机柜架构组件
        :return:
        """
        cabinet_structure_rows_template = "<tr>{0}</tr>"
        return cabinet_structure_rows_template

    @property
    def single_cabinet_template(self):
        """
        单个机柜组件
        :return:
        """
        cabinet_cells_template = """
                            <td style="background-image:url('/static/cabinetmaps/img/idc-rack-42u.gif')" bgcolor="#eeeeee" width="200">
                            <table class='cabinet-{0}' cellpadding="1" cellspacing="0" align="center" id='A{0}'>
                            <tbody><tr><td class="rack" align="center" valign="bottom">
                            <font class="rack-title"><p>A{0}</p></font></td>
                            </tr>{1}</tbody>
                            </table></td>
                              """
        return cabinet_cells_template

    @property
    def lead_rail_rows_template(self):
        """
        导轨组件
        :return:
        """
        rack_structure_template = """
        <tr><td class='rack' align='center' valign='bottom' id='{0}'></td></tr>
        """
        return rack_structure_template


class RackStructureFactory(object):
    """
    就是一个生成整个机柜图的工厂类呗. This is it!!~
    parameter1: cabinet_num (最大机柜数)
    parameter2: lead_rail_num(需要生成的导轨数)
    """

    def __init__(self, cabinet_num, lead_rail_num):
        self.cabinet_num = cabinet_num
        self.lead_rail_num = lead_rail_num
        self.structure_template = HTMLRenderTemplate()
        self.result_list = []

    def create(self):
        create_rack_structure = RackStructure()
        return create_rack_structure.get_cabinet(self.cabinet_num, self.lead_rail_num)


class CabinetStructureFactory(RackStructureFactory):
    def create(self):
        rack = super(CabinetStructureFactory, self).create()
        all_structure = format_html(
            self.structure_template.cabinet_structure_template,
            rack)
        return mark_safe(all_structure)


class RackStructure(object):
    """
    构建机柜的架构图,主要是计算导轨数和机柜的个数
    """

    def get_lead_rail(self, lead_rail_num, lead_rail_rows_template):
        lead_rail = LeadRail()
        return lead_rail.create_lead_rail_nums(lead_rail_num, lead_rail_rows_template)

    def get_cabinet(self, cabinet_num, lead_rail_num):
        cabinet = Cabinet(cabinet_num, lead_rail_num)
        return cabinet.get_cabinet_rows_structure()


class LeadRail(object):
    def create_lead_rail_nums(self, lead_rail_num, lead_rail_rows_template):
        """
        其实很简单通过获取用户提供最大导轨数和脚手架模版,来生成有多少个导轨数
        """
        structure_list = [lead_rail_rows_template.format(str(i + 1)) for i in range(lead_rail_num)]
        return ''.join(structure_list)


class Cabinet(RackStructureFactory):
    def __init__(self, cabinet_num, lead_rail_num):
        super(Cabinet, self).__init__(cabinet_num, lead_rail_num)

    def create_cabinet_cells(self, cabinet_num, offset=None):
        leadrail = LeadRail()
        structure_list = []
        for i in xrange(cabinet_num, offset):
            structure_list.append(
                format_html(self.structure_template.single_cabinet_template, str(i + 1),
                            mark_safe(leadrail.create_lead_rail_nums(
                                self.lead_rail_num,
                                self.structure_template.lead_rail_rows_template
                            ))))

        return ''.join(structure_list)

    def get_cabinet_rows_structure(self):
        """
        核心方法,通过已知的导轨数和最大机柜数,动态计算出整个机柜的具体位置.
        具体计算公式和算法都在cabinet_algorithm这个闭包中
        :return:
        """
        cabinet_algorithm(
            iter_func=MultipleIter(),
            create_cabinet_cells_func=self.create_cabinet_cells,
            cabinet_num=self.cabinet_num,
            result_list=self.result_list,
            structure_template=self.structure_template
        )
        return mark_safe(''.join(self.result_list))


if __name__ == "__main__":
    rack_structure = RackStructureFactory(
        cabinet_num=7,
        lead_rail_num=2
    )
    print rack_structure.create()
