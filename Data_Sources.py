from data_source import DataSource


Telegram_Daily_Car_Prices = DataSource(name='khodroo_rooz',
                                       source_type='Telegram_Channel',
                                       source_id='@khodroo_rooz',
                                       source_desc="""Telegram Channel with almost always one message per day containing
                                       daily new car prices gathered from car dealers and sellers""",
                                       url='t.me/khodroo_rooz')


