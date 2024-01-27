from data_source import DataSource
from content_type import ContentType
Telegram_Daily_Car_Prices_DS = DataSource(name='khodroo_rooz',
                                          source_type='Telegram_Channel',
                                          source_id='@khodroo_rooz',
                                          source_desc="""Telegram Channel with almost always one message per day 
                                          containing daily new car prices gathered from car dealers and sellers""",
                                          url='t.me/khodroo_rooz')
DS = Telegram_Daily_Car_Prices_DS

ct = ContentType(name='whole_text_of_all_messages', data_format='text',
                 # file_ext='.txt'
                 )
