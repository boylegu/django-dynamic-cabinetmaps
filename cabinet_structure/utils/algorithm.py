# coding:utf-8

# ==============================================================================
# 用于计算动态机柜的核心算法
# ==============================================================================


from itertools import imap

from django.utils.html import format_html, mark_safe

from cabinet_structure.settings import SettingsConfig


def cabinet_algorithm(iter_func, create_cabinet_cells_func, cabinet_num, result_list, structure_template):
    """
        '''
        algorithm: 如随机数为13
        设max_cabinet_rows_nums如果为6
        13－13%6=12            (1)
        12 // 6 = 2 (6 6 )   (2)
        13-12 ＝1              (3)
        so 最终得出 ( 6 6 1 )
        :param obj: 可迭代对象
        :param num: 随机数, 也是用来控制递归数
        :param count: 计算数
        :param r:
        :return:
        '''
    """
    cabinet_cells_num = cabinet_num
    cabinet_settings = SettingsConfig(cabinet_cells_num)
    max_cabinet_rows_nums = cabinet_settings.verify()

    def algorithm(value, cycles_count):
        result_counts_list = []
        is_y_multiple = 0
        for obj_num in iter_func:
            if obj_num < cabinet_cells_num:
                if cabinet_cells_num % max_cabinet_rows_nums == 0:
                    is_y_multiple += max_cabinet_rows_nums
                    result_list.append(
                        format_html(structure_template.cabinet_structure_rows_template,
                                    mark_safe(create_cabinet_cells_func(obj_num, is_y_multiple))))
                else:
                    is_y_multiple_result_num = value - value % max_cabinet_rows_nums  # 计算(1) 如果随机数为y的倍数
                    if cycles_count == is_y_multiple_result_num // max_cabinet_rows_nums:  # 计算(2)
                        cycles_count_generator = imap(lambda x: (x * max_cabinet_rows_nums), range(cycles_count))
                        rack_tag_num = 0  # 为了控制前端机柜编号是可以逐渐叠加
                        for cycles_num in cycles_count_generator:
                            rack_tag_num += max_cabinet_rows_nums
                            result_counts_list.append(rack_tag_num)
                            result_list.append(
                                format_html(structure_template.cabinet_structure_rows_template,
                                            mark_safe(create_cabinet_cells_func(cycles_num, rack_tag_num))))
                        result_list.append(
                            format_html(structure_template.cabinet_structure_rows_template,
                                        mark_safe(
                                            create_cabinet_cells_func(
                                                result_counts_list[-1],
                                                result_counts_list[-1] + (value - is_y_multiple_result_num)
                                            ))))
                        break
                    return algorithm(cabinet_cells_num, is_y_multiple_result_num // max_cabinet_rows_nums)

    return algorithm(value=cabinet_cells_num, cycles_count=0)

