# coding:utf-8
from django.views.generic import TemplateView

from cabinet_structure.utils.handle import CabinetStructureFactory


class CabinetViews(TemplateView):
    """
     提供了几个对外的API:
     1. template_name : 指定被渲染的模版
     2. cabinet_cells : 最大机柜个数
     3. rack_rows     : 最大导轨数
     4. cabinet_context  : template context name
     """
    template_name = None
    cabinet_cells = None
    rack_rows = 42
    cabinet_context = 'cabinet_data'

    def get_context_data(self, **kwargs):
        cabinet_structure = CabinetStructureFactory(
            cabinet_num=self.cabinet_cells,
            lead_rail_num=self.rack_rows
        )
        context = super(CabinetViews, self).get_context_data()
        context[self.cabinet_context] = cabinet_structure.create()
        return context
