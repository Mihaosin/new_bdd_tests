from selenium.webdriver.common.by import By
from model.group import Group


class GroupHelper:

    def __init__(self, app):
        # этот конструктор получает в качестве внешнего параметра ссылку на объект класса Application
        # и сохраняет ее в свойство с именем app
        self.app = app

    def create(self, group):
        wd = self.app.wd
        # начало создания новой группы
        self.open_groups_page()
        wd.find_element(by=By.NAME, value="new").click()
        self.fill_group_form(group)
        # завершение создания группы
        wd.find_element(by=By.NAME, value="submit").click()
        # self.return_to_groups_page()
        self.group_cache = None

    def fill_group_form(self, group):
        # заполнение атрибутов группы
        wd = self.app.wd
        self.change_field_value("group_name", group.name)
        self.change_field_value("group_header", group.header)
        self.change_field_value("group_footer", group.footer)

    def change_field_value(self, field_name, text):
        wd = self.app.wd
        if text is not None:
            wd.find_element(by=By.NAME, value=field_name).click()
            wd.find_element(by=By.NAME, value=field_name).clear()
            wd.find_element(by=By.NAME, value=field_name).send_keys(text)

    def edit_first(self, group):
        self.edit_by_index(0, group)

    def edit_by_index(self, index, group):
        wd = self.app.wd
        self.open_groups_page()
        self.select_group_by_index(index)
        wd.find_element(by=By.NAME, value="edit").click()
        self.fill_group_form(group)
        # нажать на кнопку подтвердить изменения
        wd.find_element(by=By.NAME, value="update").click()
        # self.return_to_groups_page()
        self.group_cache = None

    def edit_by_id(self, group):
        wd = self.app.wd
        self.open_groups_page()
        self.select_group_by_id(group.id)
        wd.find_element(by=By.NAME, value="edit").click()
        self.fill_group_form(group)
        # нажать на кнопку подтвердить изменения
        wd.find_element(by=By.NAME, value="update").click()
        # self.return_to_groups_page()
        self.group_cache = None

    def delete_first(self, index):
        self.delete_by_index(0)

    def delete_by_index(self, index):
        wd = self.app.wd
        self.open_groups_page()
        self.select_group_by_index(index)
        # нажать на кнопуку "удалить группу"
        wd.find_element(by=By.NAME, value="delete").click()
        # self.return_to_groups_page()
        self.group_cache = None

    def delete_by_id(self, id):
        wd = self.app.wd
        self.open_groups_page()
        self.select_group_by_id(id)
        # нажать на кнопуку "удалить группу"
        wd.find_element(by=By.NAME, value="delete").click()
        # self.return_to_groups_page()
        self.group_cache = None

    # выбрать группу по заданному индексу (чек-бокс)
    def select_group_by_index(self, index):
        wd = self.app.wd
        wd.find_elements(by=By.NAME, value="selected[]")[index].click()

    # выбрать группу по заданному id
    def select_group_by_id(self, id):
        wd = self.app.wd
        wd.find_element(by=By.CSS_SELECTOR, value="input[value='%s']" % id).click()

    def open_groups_page(self):
        wd = self.app.wd
        if not (wd.current_url.endswith("/group.php") and len(wd.find_elements(by=By.NAME, value="new")) > 0):
            # переход на страницу "Группы"
            wd.find_element(by=By.LINK_TEXT, value="groups").click()

    # def return_to_groups_page(self):
        # wd = self.app.wd
        # возврат на страницу "Группы"
        # wd.find_element(by=By.LINK_TEXT, value="groups").click()

    def count(self):
        wd = self.app.wd
        self.open_groups_page()
        return len(wd.find_elements(by=By.NAME, value="selected[]"))

    group_cache = None

    def get_group_list(self):
        if self.group_cache is None:
            wd = self.app.wd
            self.open_groups_page()
            self.group_cache = []
            # for element in wd.find_elements_by_css_selector("span.group"):
            for element in wd.find_elements(by=By.CSS_SELECTOR, value="span.group"):
                text = element.text
                id = element.find_element(by=By.NAME, value="selected[]").get_attribute("value")
                self.group_cache.append(Group(name=text, id=id))
        return list(self.group_cache)

    def erase_groups(self):
        wd = self.app.wd
        self.open_groups_page()
        check_boxes = wd.find_elements(by=By.NAME, value="selected[]")
        for i in range(0, len(check_boxes)):
            check_boxes[i].click()
        wd.find_element(by=By.NAME, value="delete").click()
