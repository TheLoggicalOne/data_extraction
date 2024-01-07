from bs4 import BeautifulSoup

import data_manager

html_data_path_html = data_manager.get_path(base_dir=data_manager.KHODROO_ROOZ_HTML_DIR_PATH,
                                            data_file_base_name=data_manager.HTML_DATA_FILE_BASE_NAME,
                                            data_file_name_ext='1_to_60.html')

html_data_path_txt = data_manager.get_path(base_dir=data_manager.KHODROO_ROOZ_HTML_DIR_PATH,
                                           data_file_base_name=data_manager.HTML_DATA_FILE_BASE_NAME,
                                           data_file_name_ext='1_to_60.txt')

with open(html_data_path_txt, 'r') as file:
    html_content = file.read()

# Write html data to html file
# html_content = "<html><body>...</body></html>"

formatted_content = BeautifulSoup(html_content, 'html.parser').prettify()

with open(html_data_path_html, "w") as file:
    file.write(formatted_content)

