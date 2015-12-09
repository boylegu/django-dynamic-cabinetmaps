import logging

from django.conf import settings

logger = logging.getLogger(__name__)


class VerifySettings(object):
    __settings_name__ = 'MAX_CABINET_ROWS_NUM'

    __error_msg_dict__ = {'no_attribute': ("MAX_CABINET_ROWS_NUM must be specified in "
                                           "your Django settings file"),
                          'no_int': ("MAX_CABINET_ROWS_NUM "
                                     "must be specified integer"),
                          'min_cells': ("cabinet_cells "
                                        "is bigger than MAX_CABINET_ROWS_NUM")}

    def __init__(self, cabinet_cells):
        self.cabinet_cells = cabinet_cells

    @property
    def settings_max_cabinet_num(self):
        return getattr(
            settings, self.__settings_name__, 6
        )

    def verify_cabinet_num_type(self):
        if not isinstance(self.settings_max_cabinet_num, int):
            log_msg = self.__error_msg_dict__['no_int']
            logger.info(log_msg)
            raise TypeError(log_msg)
        else:
            return self.settings_max_cabinet_num

    def verify_cabinet_cells_gt_max_cabinet_num(self):
        if self.cabinet_cells < self.settings_max_cabinet_num:
            raise TypeError(self.__error_msg_dict__['min_cells'])
        return self.verify_cabinet_num_type()


class SettingsConfig(VerifySettings):
    def verify(self):
        max_rows_num = super(SettingsConfig, self).verify_cabinet_cells_gt_max_cabinet_num()
        return max_rows_num
